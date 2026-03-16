from datetime import datetime
from models import AdvertisementResponse
from typing import Optional, List


_ads = {}
_next_id = 1

def create_ad(ad_data: dict) -> AdvertisementResponse:

    global _next_id
    now = datetime.utcnow()
    ad_dict = {
        "id": _next_id,
        "created_at": now,
        **ad_data
    }
    _ads[_next_id] = ad_dict
    _next_id += 1
    return AdvertisementResponse(**ad_dict)

def get_ad(ad_id: int) -> Optional[AdvertisementResponse]:

    ad_dict = _ads.get(ad_id)
    if ad_dict:
        return AdvertisementResponse(**ad_dict)
    return None

def update_ad(ad_id: int, update_data: dict) -> Optional[AdvertisementResponse]:

    ad_dict = _ads.get(ad_id)
    if not ad_dict:
        return None
    ad_dict.update(update_data)
    return AdvertisementResponse(**ad_dict)

def delete_ad(ad_id: int) -> bool:

    if ad_id in _ads:
        del _ads[ad_id]
        return True
    return False

def search_ads(filters: dict) -> List[AdvertisementResponse]:

    result = []
    for ad_dict in _ads.values():
        match = True
        for key, value in filters.items():
            if key not in ad_dict or ad_dict[key] != value:
                match = False
                break
        if match:
            result.append(AdvertisementResponse(**ad_dict))
    return result