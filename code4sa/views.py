import json

from django.shortcuts import render
from django.http import HttpResponseBadRequest

from code4sa.models import Submission


def home(request):
    return render(request, 'index.html')


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
        client_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    else:
        client_ip = request.META.get('REMOTE_ADDR', '')

    details = {
        'project': project,
        'remote_ip': client_ip,
        'data': data,
    }

    print details

    sub = Submission(**details)
    sub.save()
