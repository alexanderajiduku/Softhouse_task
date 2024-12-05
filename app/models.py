from pydantic import BaseModel


class StockWinner(BaseModel):
    rank: int
    name: str
    percent: float
    latest: int
