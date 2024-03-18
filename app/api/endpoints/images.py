from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse

from app.db.crud import DBType, DriveType, get_image_by_id

router = APIRouter()


@router.get("/{id}")
def get_image(id: str, db: DBType, drive: DriveType) -> StreamingResponse:
    image = get_image_by_id(db, drive, id)

    if image is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Image with id {id} not found",
        )

    return StreamingResponse(image.iter_chunks(1024), media_type="image/png")
