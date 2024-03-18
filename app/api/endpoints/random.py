from fastapi import APIRouter, HTTPException, status

from app.api.schemas.card import Card
from app.db.crud import DBType, get_random_card

router = APIRouter()


@router.get("/")
def random_card(db: DBType) -> Card:
    card = get_random_card(db)

    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No cards found"
        )

    return card
