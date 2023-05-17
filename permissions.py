"""
Permissions file for apis
"""
from rest_framework import permissions


class CustomValidateUser(permissions.BasePermission):
    """
    Custom user validation
    """

    def has_permission(self, request, view):
        """
        Deny access if user is an AnonymousUser.
        """
        user = str(request.user)
        if user != "AnonymousUser":
            print("Access granted to {0} for {1}".format(user, view.get_view_name()))
            has_permission_value = True
        else:
            print("Access denied to {0} for {1}".format(user, view.get_view_name()))
            has_permission_value = False

        return has_permission_value
