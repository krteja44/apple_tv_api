from django.contrib.auth.models import User


#checks if username exists in db
def username_exists(email_id):
    if User.objects.filter(username= email_id).exists():
        return True
    return False

email_id = request_data['email_id'] #email_id is one of the attribute returned from pinged after get request
valid_user = username_exists(email_id)



# If True:
#   save session_id to backend DB and send it as payload to GUI, store in browser local db and navigate to internal home page
# If False: (user doesn't exist in DB)
#   Return message -> User Not Found to GUI and redirect to pingfed SSO URL.