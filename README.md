Backchat
========

Backchat is a simple Django application for taking submissions
from a website via AJAX and saving them to a database.

To send a submission for PROJECT, use jQuery something like this:

    $.post("http://backchat.code4sa.org/submit/PROJECT/", {processData: false, data: JSON.stringify({foo: 2, bar: [2, 3]})});

License
-------

MIT License
