from fastapi import APIRouter

from app.schemas import Card

router = APIRouter()


@router.get("/", response_model=Card)
def get_random_card():
    ...
