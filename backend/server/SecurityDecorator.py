from flask import request
from google.auth.transport import requests
import google.oauth2.id_token
from server.bo.User import User

from server.Administration import Administration as Admin

"""Decorator zur Google Firebase-basierten Authentifizierung von Benutzern"""


def secured(function):
    firebase_request_adapter = requests.Request()

    def wrapper(*args, **kwargs):
        # Verify Firebase auth
        id_token = request.cookies.get("token")
        error_message = None
        claims = None
        objects = None

        if id_token is None:
            try:
                id_token = request.headers['Authorization'].split(' ').pop()
            except BaseException:
                id_token = None

        if id_token:
            try:
                claims = google.oauth2.id_token.verify_firebase_token(
                    id_token, firebase_request_adapter)
                if claims is not None:
                    google_user_id = claims.get("user_id")
                    email = claims.get("email")
                    fullname = claims.get("name").rsplit(maxsplit=1)  # last word of string is lastname
                    if not fullname:
                        fullname = ["N/A", "N/A"]
                    firstname = fullname[0]
                    lastname = fullname[1]

                    user = Admin.get_user_by_google_user_id(google_user_id)
                    if user is not None:
                        """Fall: Der Benutzer ist unserem System bereits bekannt."""
                        user.set_firstname(firstname)
                        user.set_lastname(lastname)
                        user.set_email(email)
                        Admin.save_user(user)
                    else:
                        """Fall: Der Benutzer war bislang noch nicht eingelogged. """
                        user = User()
                        user.set_firstname(firstname)
                        user.set_email(email)
                        user.set_google_user_id(google_user_id)
                        user = Admin.create_user(user)
                    if request.method == 'POST' or request.method == 'PUT':
                        kwargs['user'] = user
                    objects = function(*args, **kwargs)
                    return objects
                else:
                    return '', 401  # Unauthorized
            except ValueError as exc:
                # This will be raised if the token is expired or any other
                # verification checks fail.
                error_message = str(exc)
                return exc, 401  # UNAUTHORIZED !!!

        return '', 401  # UNAUTHORIZED !!!

    return wrapper
