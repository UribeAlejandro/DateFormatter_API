from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/", status_code=200)
async def root() -> JSONResponse:
    """Root endpoint for the API.

    Returns
    -------
    JSONResponse
        Welcome message.
    """
    return JSONResponse({"message": "Welcome to Date Formatter!"})
