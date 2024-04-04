from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/", status_code=200)
async def get_health() -> JSONResponse:
    """Health check endpoint.

    Returns
    -------
    JSONResponse
        Status of the API.
    """
    return JSONResponse({"status": "OK"})
