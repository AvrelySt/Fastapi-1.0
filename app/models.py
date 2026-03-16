from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AdvertisementBase(BaseModel):

    title: str = Field(..., min_length=1, max_length=200, description="Заголовок объявления")
    description: str = Field(..., max_length=1000, description="Описание")
    price: float = Field(..., gt=0, description="Цена (должна быть положительной)")
    author: str = Field(..., min_length=1, max_length=100, description="Автор")

class AdvertisementCreate(AdvertisementBase):

    pass  # достаточно унаследовать

class AdvertisementUpdate(BaseModel):

    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    price: Optional[float] = Field(None, gt=0)
    author: Optional[str] = Field(None, min_length=1, max_length=100)

class AdvertisementResponse(AdvertisementBase):

    id: int
    created_at: datetime

    class Config:
        orm_mode = True