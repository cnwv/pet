from fastapi import (
    APIRouter,
)



router = APIRouter(tags=["Users"])


@router.get("")
async def get_users():
    return '200'


@router.post("")
async def create_user():
    return "200"
