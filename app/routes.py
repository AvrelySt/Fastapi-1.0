from fastapi import APIRouter, HTTPException, Query
from models import AdvertisementCreate, AdvertisementUpdate, AdvertisementResponse
from storage import create_ad, get_ad, update_ad, delete_ad, search_ads
from typing import List, Optional

router = APIRouter(prefix="/advertisement", tags=["advertisements"])

@router.post("/", response_model=AdvertisementResponse, status_code=201)
async def create_ad_endpoint(ad: AdvertisementCreate):

    new_ad = create_ad(ad.dict())
    return new_ad

@router.get("/{ad_id}", response_model=AdvertisementResponse)
async def get_ad_endpoint(ad_id: int):

    ad = get_ad(ad_id)
    if ad is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return ad

@router.patch("/{ad_id}", response_model=AdvertisementResponse)
async def update_ad_endpoint(ad_id: int, ad_update: AdvertisementUpdate):


    update_data = ad_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No data to update")
    updated_ad = update_ad(ad_id, update_data)
    if updated_ad is None:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return updated_ad

@router.delete("/{ad_id}", status_code=204)
async def delete_ad_endpoint(ad_id: int):

    deleted = delete_ad(ad_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Advertisement not found")


@router.get("/", response_model=List[AdvertisementResponse])
async def search_ad_endpoint(
    title: Optional[str] = Query(None, description="Фильтр по заголовку (точное совпадение)"),
    description: Optional[str] = Query(None, description="Фильтр по описанию"),
    price: Optional[float] = Query(None, gt=0, description="Фильтр по цене"),
    author: Optional[str] = Query(None, description="Фильтр по автору")
):

    filters = {k: v for k, v in locals().items() if v is not None}
    ads = search_ads(filters)
    return ads