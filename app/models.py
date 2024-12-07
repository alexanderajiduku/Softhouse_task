from pydantic import BaseModel, Field


class StockWinner(BaseModel):
    rank: int = Field(..., description="Ranking position (1-3)")
    name: str = Field(..., description="Stock code/name")
    percent: float = Field(..., description="Percentage change in value")
    latest: float = Field(..., description="Latest stock price")
