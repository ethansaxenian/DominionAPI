from firebase_admin import firestore
from google.oauth2 import service_account

from core.config import get_settings

settings = get_settings()

credentials = service_account.Credentials.from_service_account_file(settings.GOOGLE_APPLICATION_CREDENTIALS)
db = firestore.AsyncClient(credentials=credentials)
