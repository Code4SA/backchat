import json
import re
import logging

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from code4sa.models import Submission
from code4sa.html2text import html2text


EMAIL_RE = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

log = logging.getLogger(__name__)


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


@csrf_exempt
def budget2016_notice(request):
    """ Send a response email after a budget 2016 submission.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("POST only, I'm afraid.")

    if request.POST.get('data'):
        try:
            data = json.loads(request.POST.get('data'))
        except ValueError:
            return HttpResponseBadRequest('Invalid "data" value, it must be JSON.')
    from_email = data.get('UserEmail', '').strip()
    # sanity check from_email
    if not from_email or not EMAIL_RE.match(from_email):
        from_email = "noreply@internationalbudget.org"

    html = data.get('EmailBody')
    # sanity check the body, it should have certain sentences
    if (html and 'National Assembly Standing Committee on Appropriations' in html
            and 'ranked the biggest increases' in html
            and 'Thank you for considering my submission' in html):

        recipient = "greg@code4sa.org" if settings.DEBUG else "daarends@parliament.gov.za"
        subject = "Public Feedback on the 2016 Budget"
        # plain text version
        message = html2text(html)

        # do it
        if settings.SEND_EMAILS:
            log.info("Sending email to %s from %s" % (recipient, from_email))
            send_mail(subject, message, from_email, [recipient], html_message=html)
    else:
        log.warn("Ignoring submission, it looks bad: %s" % data)

    return HttpResponse('ok')
