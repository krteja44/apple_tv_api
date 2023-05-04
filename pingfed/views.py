from rest_framework import views, status
from rest_framework.response import Response
from .utils import get_user_attributes

# Create your views here.
class AuthorizeRequestFromPingFed(views.APIView):
    def post(self, request):
        ref = request.data.get("REF", None)
        if not ref:
            return Response("ref not provided", status=status.HTTP_400_BAD_REQUEST)
        user_attributes = get_user_attributes(ref)
        return Response({"record": user_attributes}, status=status.HTTP_200_OK)