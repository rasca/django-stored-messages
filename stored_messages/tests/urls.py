from django.urls import re_path, include

from stored_messages.tests.views import message_view, message_create, message_create_mixed


urlpatterns = [
    re_path(r'^consume$', message_view),
    re_path(r'^create$', message_create),
    re_path(r'^create_mixed$', message_create_mixed),
    re_path(r'^messages', include(('stored_messages.urls', 'stored_messages'), namespace='stored_messages'))
]
