from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
import os, mimetypes

def download(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    try:
        file_wrapper = FileWrapper(file(file_path, 'rb'))
        file_mimetype = mimetypes.guess_type(file_path)
    except IOError:
        raise Http404('File not found: ' + file_name)

    response = HttpResponse(file_wrapper, content_type=file_mimetype)
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    return response