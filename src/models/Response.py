from pydantic import BaseModel


class CounterResponse(BaseModel):
    count: int


class DateResponse(BaseModel):
    date: str
