from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()


class FlagRequest(BaseModel):
    secret: str


@app.post("/")
def root(flag_req: FlagRequest):
    if flag_req.secret == "give!it!to!me":
        return {"flag": "for_your_eyes_only"}
    raise HTTPException(status_code=400, detail="invalid post request")
