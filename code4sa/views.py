import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse

from code4sa.models import Submission


def home(request):
    return render(request, 'index.html')


@csrf_exempt
def submit(request, project):
    """ Make a new submission for a project.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("POST only, I'm afraid.")

    if request.POST.get('data'):
        try:
            data = json.loads(request.POST.get('data'))
        except ValueError:
            return HttpResponseBadRequest('Invalid "data" value, it must be JSON.')

    if 'HTTP_X_FORWARDED_FOR' in request.META:
        remote_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    else:
        remote_ip = request.META.get('REMOTE_ADDR', '')

    details = {
        'project': project,
        'remote_ip': remote_ip,
        'data': data,
        'user_agent': request.META.get('HTTP_USER_AGENT')
    }

    Submission(**details).save()
    return HttpResponse('ok')
