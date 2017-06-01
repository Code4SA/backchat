Backchat
========

Backchat is a simple Django application with a couple of roles:

 - taking submissions from a website via AJAX and saving them to a database.
 - proxying queries to select private datasets in our data portal so that the data is accessible but not publicly listed in the portal.

To send a submission for PROJECT, use jQuery something like this:

    $.post("http://backchat.code4sa.org/submit/PROJECT/", {processData: false, data: JSON.stringify({foo: 2, bar: [2, 3]})});

To query an exposed dataset, request a url similar to the Socrata query URL like http://backchat.code4sa.org/portalproxy/resource/aaaa-bbbb.json?$q=blue%20moon

Deployment
----------

Deploy using dokku

Set the following config variables:

    DJANGO_SECRET_KEY=...
    DATABASE_URL=...
    DJANGO_EMAIL_HOST_PASSWORD=...
    DJANGO_SECRET_KEY=...
    DJANGO_SEND_EMAILS=...
    NEW_RELIC_APP_NAME=Backchat
    NEW_RELIC_LICENSE_KEY=...

On an old dokku, copy the tls folder with the wildcard cert into the app folder and rebuild to configure TLS.

License
-------

MIT License
