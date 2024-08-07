from typing import Annotated

from fastapi import APIRouter, Cookie, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse

router = APIRouter(tags=["demo_cookie"])


@router.post("/cookie-and-object/")
def create_cookie_with_response_parameter(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}


@router.post("/return-response-directly/")
def create_cookie_directly():
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession1", value="fake-cookie-session-value2")
    return response


@router.get("/read_specific_cookie/")
async def read_item(fakesession: Annotated[str | None, Cookie()] = None):
    if fakesession is None:
        not_found_cookie = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cookie_not_found",
        )
        raise not_found_cookie
    return {"fakesession": fakesession}


@router.get("/read_all_cookie/")
async def get_items(request: Request):
    return request.cookies
