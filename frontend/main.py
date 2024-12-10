from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


def get_from_mitm() -> str:
    """Queries the mitm server and expects to retrieve the flag string"""
    r = requests.post("http://backend/", json={"secret": "give!it!to!me"})
    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to query mitm")
    return r.json()["flag"]


@app.get("/")
def root():
    flag = get_from_mitm()
    return {"flag": flag}
