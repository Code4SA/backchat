from django.db import models
from django.contrib.postgres.fields import JSONField


class Submission(models.Model):
    """ General submission from some website.
    """

    # Name of the project this submission is for
    project = models.CharField(max_length=100, null=False, blank=False)
    remote_ip = models.CharField(max_length=20, help_text="User's remote IP")
    user_agent = models.CharField(max_length=200, help_text="User's user agent string")
    data = JSONField(help_text='Raw submission from the user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
