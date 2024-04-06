from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.models.Response import CounterResponse
from src.models.utils import Counter

router = APIRouter(prefix="/counter")


@router.get("/", status_code=200, response_model=CounterResponse)
async def get_counter() -> JSONResponse:
    """Get the current count of requests.

    Returns
    -------
    JSONResponse
        A JSON response containing the current count of requests.
    """
    counter = Counter()
    counter.increment()
    response = CounterResponse(count=counter.get_count())
    return JSONResponse(content=response.model_dump())
