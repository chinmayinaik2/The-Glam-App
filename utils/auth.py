import streamlit_authenticator as stauth

def login():
    credentials = {
        "usernames": {
            "admin": {
                "name": "Admin User",
                "password": "$2b$12$Q7fZzTFGu1TNTYZIno3KYO9Zg1b6Unk0Ow3tw0OQNPcIwbFhLo9Rm"
            }
        }
    }

    authenticator = stauth.Authenticate(
        credentials,
        "makeup_app",   # app name
        "abcdef",       # cookie key
        cookie_expiry_days=1
    )

    return authenticator
