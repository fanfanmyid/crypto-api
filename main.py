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

@app.get("/getData")
async def getData(symbol:str,interval:str,limit:str,timeStart:Optional[str]=None,timeEnd:Optional[str]=None):
    return cm.getDataCrypto(symbol,interval,limit,timeStart,timeEnd)

@app.get("/indicator/ma")
async def getData(symbol:str,interval:str,length:str,limit:str,timeStart:Optional[str]=None,timeEnd:Optional[str]=None):
    return cm.indicatorMa(symbol,interval,length,limit,timeStart,timeEnd)

@app.get("/indicator/rsi")
async def getData(symbol:str,interval:str,length:str,limit:str,timeStart:Optional[str]=None,timeEnd:Optional[str]=None):
    return cm.indicatorRsi(symbol,interval,length,limit,timeStart,timeEnd)

@app.get("/indicator/bbands")
async def getData(symbol:str,interval:str,length:str,limit:str,timeStart:Optional[str]=None,timeEnd:Optional[str]=None):
    return cm.indicatorBB(symbol,interval,length,limit,timeStart,timeEnd)

@app.get("/indicator/allForPersonal")
async def getData(symbol:str,interval:str,limit:str,timeStart:Optional[str]=None,timeEnd:Optional[str]=None):
    return cm.indicatorAll(symbol,interval,limit,timeStart,timeEnd)