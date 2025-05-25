import streamlit_authenticator as stauth

def login():
    credentials = {
        "usernames": {
            "admin": {
                "name": "Admin User",
                "password": "$2b$12$ynPZQnsX7E9oXhUcCwqjC.4eM/vZ57FYXE3bVwrvcDVPInN9/BrDi"
            }
        }
    }

    authenticator = stauth.Authenticate(
        credentials,
        "makeup_app",
        "abcdef",
        cookie_expiry_days=1
    )

    return authenticator
