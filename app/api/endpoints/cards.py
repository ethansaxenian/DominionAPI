from fastapi import APIRouter

from app.schemas import Card

router = APIRouter()


@router.get("/", response_model=list[Card])
def get_cards():
    ...


@router.get("/{id}", response_model=Card)
def get_card(id: int):
    ...
