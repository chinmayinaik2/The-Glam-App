import streamlit_authenticator as stauth

def login():
    credentials = {
        "usernames": {
            "admin": {
                "email": "admin@example.com",
                "name": "Admin",
                "password": stauth.Hasher(["admin123"]).generate()[0]
            }
        }
    }
    authenticator = stauth.Authenticate(
        credentials,
        "makeup_app_cookie",
        "auth_key",
        cookie_expiry_days=30
    )
    return authenticator
