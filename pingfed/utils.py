import requests
from django.conf import settings

def get_user_attributes(ref):
    pickup_location = settings.PINGFED_PICKUP_URL + ref
    headers = {
        "ping.uname": settings.PINGFED_USERNAME,
        "ping.pwd": settings.PINGFED_PASSWORD,
        "ping.instanceId": settings.PINGFED_INSTANCE
    }

    response = requests.get(pickup_location, headers=headers, verify=False).json()
    return response
