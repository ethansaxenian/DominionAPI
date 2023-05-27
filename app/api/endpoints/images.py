import deta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse

from app.db import DBType, get_drive, get_image_by_id

router = APIRouter()


@router.get("/{id}", response_class=StreamingResponse)
def get_image(id: str, db: DBType, drive: deta.Drive = Depends(get_drive)):
    image = get_image_by_id(db, drive, id)

    if image is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Image with id {id} not found",
        )

    return StreamingResponse(image.iter_chunks(1024), media_type="image/png")
