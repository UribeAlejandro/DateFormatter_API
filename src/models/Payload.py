from pydantic import BaseModel


class PayloadDate(BaseModel):
    timestamp: bool
