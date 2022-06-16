import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from core.config import get_settings

settings = get_settings()

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(
    cred,
    {
        "projectId": settings.PROJECT_ID,
    },
)

db = firestore.AsyncClient()
