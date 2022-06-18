from firebase_admin import firestore
from google.oauth2 import service_account

from core.config import get_settings

settings = get_settings()

credentials = service_account.Credentials.from_service_account_info(
    {
        "project_id": settings.FIRESTORE_PROJECT_ID,
        "private_key_id": settings.FIRESTORE_PRIVATE_KEY_ID,
        "private_key": settings.FIRESTORE_PRIVATE_KEY,
        "client_email": settings.FIRESTORE_CLIENT_EMAIL,
        "token_uri": settings.FIRESTORE_TOKEN_URI,
    }
)

firestore_db = firestore.AsyncClient(credentials=credentials)


def get_firestore_db():
    return firestore_db
