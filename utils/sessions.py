from utils.redis import RedisClient
from django.conf import settings
from rest_framework import authentication, exceptions
import uuid


class SessionManager:
    def __init__(self, email):
        self.client = RedisClient
        self.email = email

    def generate_session_id(self):
        return str(uuid.uuid4())

    def generate_session_key(self):
        return f"JWT_SESSION:{self.email}"

    def create_session(self):
        session_id = self.generate_session_id()
        self.client.setValue(
            self.generate_session_key(),
            session_id,
            settings.TOKEN_EXPIRY
        )
        return session_id

    def validate_session(self, session_id):
        set_session_id = self.client.getValue(self.generate_session_key())
        if set_session_id != session_id:
            msg = 'Invalid session ID'
            raise exceptions.AuthenticationFailed(msg)

    def delete_session(self):
        return self.client.deleteValue(self.generate_session_key())
