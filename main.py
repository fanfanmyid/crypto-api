from optparse import Option
from fastapi import FastAPI
import crypto_module as cm
from typing import Optional
from pydantic import BaseModel

class CryptoDetail(BaseModel):
    symbol: str
    interval: str
    limit: str
    timeStart:Optional[str] = None
    timeEnd:Optional[str] = None

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getRealtimeData")
async def getData(symbol:str,interval:str,limit:str,timeStart:Optional[str]=None,timeEnd:Optional[str]=None):
    return cm.getDataCrypto(symbol,interval,limit,timeStart,timeEnd)