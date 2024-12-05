from fastapi import FastAPI, HTTPException
from app.services import get_top_winners


app = FastAPI()


@app.get("/")
async def home():
    return "Server running ......"


@app.get("/winners")
async def winners():
    try:
        top_winners = get_top_winners()
        return {"winners": top_winners}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
