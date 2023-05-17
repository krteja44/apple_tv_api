from rest_framework import views, status
from rest_framework.response import Response
from .utils import get_user_attributes
from utils.sessions import SessionManager
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
import jwt

# Create your views here.
class AuthorizeRequestFromPingFed(views.APIView):
    def post(self, request):
        ref = request.data.get("REF", None)
        if not ref:
            return Response("ref not provided", status=status.HTTP_400_BAD_REQUEST)
        jwt_token = self._generate_jwt_token('1231')
        # user_attributes = get_user_attributes(ref)
        return Response({"access_token": jwt_token}, status=status.HTTP_200_OK)

    def _generate_jwt_token(self, user_id):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)
        # create a session ID and save it in redis
        session_id = SessionManager(user_id).create_session()
        payload = {
            'id': user_id,
            'exp': int(dt.timestamp()),
            'sessionId':session_id,
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

class ProtectedView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({"safe_view": "This is a safe view"}, status=status.HTTP_200_OK)