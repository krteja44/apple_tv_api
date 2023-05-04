from django.urls import path
from .views import (
    AuthorizeRequestFromPingFed,
)
app_name = 'pingfed'

urlpatterns = [
    # /pingfed/
    path("authorize/", AuthorizeRequestFromPingFed.as_view()),
]