from django.urls import path
from .views import (
    AuthorizeRequestFromPingFed,
    ProtectedView,
)
app_name = 'pingfed'

urlpatterns = [
    # /pingfed/
    path("authorize/", AuthorizeRequestFromPingFed.as_view()),
    path("safe/", ProtectedView.as_view()),
]