from fastapi import APIRouter, Depends, HTTPException

from app.schemas import Card
from core.config import Settings, get_settings
from db.init_db import db

router = APIRouter()


@router.get("/", response_model=list[Card])
async def get_cards(settings: Settings = Depends(get_settings)):
    docs = db.collection(settings.FIRESTORE_DOCUMENT_NAME).stream()
    return [doc.to_dict() async for doc in docs]


@router.get("/{id}", response_model=Card)
async def get_card(id: int, settings: Settings = Depends(get_settings)):
    doc = await db.collection(settings.FIRESTORE_DOCUMENT_NAME).document(str(id)).get()

    if doc.exists:
        return doc.to_dict()
    else:
        raise HTTPException(status_code=404, detail=f"Card with id {id} not found")
