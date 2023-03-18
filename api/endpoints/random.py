from fastapi import APIRouter, HTTPException, status

from api.schemas import Card
from db import DBType, get_random_card

router = APIRouter()


@router.get("/", response_model=Card)
def random_card(db: DBType):
    card = get_random_card(db)

    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No cards found"
        )

    return card
