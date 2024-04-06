from datetime import datetime

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.models.Payload import PayloadDate
from src.models.Response import DateResponse
from src.models.utils import Counter

router = APIRouter(prefix="/date")


@router.post("/", status_code=200, response_model=DateResponse)
async def now_date(payload: PayloadDate) -> JSONResponse:
    """Get the current date and time.

    Parameters
    ----------
    payload : PayloadDate
        A boolean flag that indicates whether the response should include the time or not.

    Returns
    -------
    JSONResponse
        A JSON response containing the current date and time.
    """
    counter = Counter()
    current_datetime = datetime.now()
    payload = payload.dict()

    if payload["timestamp"]:
        response = DateResponse(date=current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        response = DateResponse(date=current_datetime.strftime("%Y-%d-%m"))

    counter.increment()
    return JSONResponse(content=response.model_dump())
