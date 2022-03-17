from urllib.request import urlopen
import json
import pandas as pd
import pandas_ta as ta
import time
import datetime
import math

def getDataCrypto(symbol,interval,limit,timeStart,timeEnd):
    
    # store the URL in url as 
    # parameter for urlopen
    if((timeStart and timeEnd) is None):
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit
    else:
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit+"&startTime="+str(timeStart)+"&endTime="+str(timeEnd)
    
    response = urlopen(url)

    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
#     print(data_json)
    tm,op,hi,lo,cl = [],[],[],[],[]

    for x in range(len(data_json)):
    #     print(data_json[x][0])
        tm.append(data_json[x][0])
        op.append(data_json[x][1])
        hi.append(data_json[x][2])
        lo.append(data_json[x][3])
        cl.append(data_json[x][4])
    data = {"time": tm, "open":op,"high":hi,"low":lo,"close":cl}
    df = pd.DataFrame(data)
    
    json2data = json.loads(df.to_json(orient='records'))
    return {
        "status" : 200,
        "symbol" : symbol,
        "timeframe" : interval,
        "total_data" : limit,
        "source_data" : url,
        "data" : json2data
    }
    
def indicatorMa(symbol,interval,length,limit,timeStart,timeEnd):
    # store the URL in url as 
    # parameter for urlopen
    if((timeStart and timeEnd) is None):
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit
    else:
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit+"&startTime="+str(timeStart)+"&endTime="+str(timeEnd)
    
    response = urlopen(url)

    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
#     print(data_json)
    tm,op,hi,lo,cl = [],[],[],[],[]

    for x in range(len(data_json)):
    #     print(data_json[x][0])
        tm.append(data_json[x][0])
        op.append(data_json[x][1])
        hi.append(data_json[x][2])
        lo.append(data_json[x][3])
        cl.append(data_json[x][4])
    data = {"time": tm, "open":op,"high":hi,"low":lo,"close":cl}
    df = pd.DataFrame(data)
    sma = ta.sma(df['close'], length=int(length))
    df['sma'] = sma
    
    json2data = json.loads(df.to_json(orient='records'))
    return {
        "status" : 200,
        "symbol" : symbol,
        "timeframe" : interval,
        "total_data" : limit,
        "source_data" : url,
        "data" : json2data
    }
    
def indicatorRsi(symbol,interval,length,limit,timeStart,timeEnd):
    # store the URL in url as 
    # parameter for urlopen
    if((timeStart and timeEnd) is None):
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit
    else:
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit+"&startTime="+str(timeStart)+"&endTime="+str(timeEnd)
    
    response = urlopen(url)

    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
#     print(data_json)
    tm,op,hi,lo,cl = [],[],[],[],[]

    for x in range(len(data_json)):
    #     print(data_json[x][0])
        tm.append(data_json[x][0])
        op.append(data_json[x][1])
        hi.append(data_json[x][2])
        lo.append(data_json[x][3])
        cl.append(data_json[x][4])
    data = {"time": tm, "open":op,"high":hi,"low":lo,"close":cl}
    df = pd.DataFrame(data)
    rsi = ta.rsi(df['close'].astype(float), length=int(length))
    df['rsi'] = rsi
    
    json2data = json.loads(df.to_json(orient='records'))
    return {
        "status" : 200,
        "symbol" : symbol,
        "timeframe" : interval,
        "total_data" : limit,
        "source_data" : url,
        "data" : json2data
    }
    
def indicatorBB(symbol,interval,length,limit,timeStart,timeEnd):
    # store the URL in url as 
    # parameter for urlopen
    if((timeStart and timeEnd) is None):
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit
    else:
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit+"&startTime="+str(timeStart)+"&endTime="+str(timeEnd)
    
    response = urlopen(url)

    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
#     print(data_json)
    tm,op,hi,lo,cl = [],[],[],[],[]

    for x in range(len(data_json)):
    #     print(data_json[x][0])
        tm.append(data_json[x][0])
        op.append(data_json[x][1])
        hi.append(data_json[x][2])
        lo.append(data_json[x][3])
        cl.append(data_json[x][4])
    data = {"time": tm, "open":op,"high":hi,"low":lo,"close":cl}
    df = pd.DataFrame(data)
    bbands = ta.bbands(df['close'].astype(float), length = int(length))
    df['bbands_low'] = bbands["BBL_"+str(length)+"_2.0"]
    df['bbands_middle'] = bbands["BBM_"+str(length)+"_2.0"]
    df['bbands_upper'] = bbands["BBU_"+str(length)+"_2.0"]
    
    json2data = json.loads(df.to_json(orient='records'))
    return {
        "status" : 200,
        "symbol" : symbol,
        "timeframe" : interval,
        "total_data" : limit,
        "source_data" : url,
        "data" : json2data
    }
    
def indicatorAll(symbol,interval,limit,timeStart,timeEnd):
    # store the URL in url as 
    # parameter for urlopen
    length_ma = 10
    length_rsi = 10
    length_bb = 10
    if((timeStart and timeEnd) is None):
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit
    else:
        url = "https://api.binance.me/api/v3/klines?symbol="+str(symbol)+"&interval="+str(interval)+"&limit="+limit+"&startTime="+str(timeStart)+"&endTime="+str(timeEnd)
    
    response = urlopen(url)

    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
#     print(data_json)
    tm,op,hi,lo,cl = [],[],[],[],[]

    for x in range(len(data_json)):
    #     print(data_json[x][0])
        tm.append(data_json[x][0])
        op.append(data_json[x][1])
        hi.append(data_json[x][2])
        lo.append(data_json[x][3])
        cl.append(data_json[x][4])
    data = {"time": tm, "open":op,"high":hi,"low":lo,"close":cl}
    df = pd.DataFrame(data)
    
    sma = ta.sma(df['close'], length=int(length_ma))
    rsi = ta.rsi(df['close'].astype(float), length=int(length_rsi))
    bbands = ta.bbands(df['close'].astype(float), length = int(length_bb))
    
    
    df['sma'] = sma
    df['rsi'] = rsi
    df['bbands_low'] = bbands["BBL_"+str(length_bb)+"_2.0"]
    df['bbands_middle'] = bbands["BBM_"+str(length_bb)+"_2.0"]
    df['bbands_upper'] = bbands["BBU_"+str(length_bb)+"_2.0"]
    df = df.dropna()
    # df = df[['sma','rsi','bbands_low','bbands_middle','bbands_upper']].apply(str)
    
    json2data = json.loads(df.to_json(orient='records'))
    return {
        "status" : 200,
        "symbol" : symbol,
        "timeframe" : interval,
        "total_data" : limit,
        "source_data" : url,
        "data" : json2data
    }
    
# def getData(timeStart,timeEnd):
#     # store the URL in url as 
#     # parameter for urlopen
#     url = "https://api.binance.me/api/v3/klines?symbol=BTCBUSD&interval=1m&limit=1000&startTime="+str(timeStart)+"&endTime="+str(timeEnd)
#     # store the response of URL
#     response = urlopen(url)

#     # storing the JSON response 
#     # from url in data
#     data_json = json.loads(response.read())

#     # print the json response
# #     print(data_json)
#     tm,op,hi,lo,cl = [],[],[],[],[]

#     for x in range(len(data_json)):
#     #     print(data_json[x][0])
#         tm.append(data_json[x][0])
#         op.append(data_json[x][1])
#         hi.append(data_json[x][2])
#         lo.append(data_json[x][3])
#         cl.append(data_json[x][4])
#     data = {"time": tm, "open":op,"high":hi,"low":lo,"close":cl}
#     df = pd.DataFrame(data)
#     return df

# def timeFrameOne(startTime,loop,timeFrame,interval):
#     dfall = pd.DataFrame()
#     openTime = unixToUtc(startTime)
#     check_start = unixToUtc(startTime)
#     for x in range(loop):
#         openTime = openTime + datetime.timedelta(minutes = timeFrame)
#         closeTime = openTime + datetime.timedelta(hours = interval)
#         df = getData(utcToUnix(openTime),utcToUnix(closeTime))
# #         df = pd.concat(df)
# #         print(len(df))
#         dfall = dfall.append(df) 
# #         print(len(dfall))
#         print(openTime)
#         print(closeTime)
#         openTime = closeTime
#     print(len(dfall))
#     json2data = json.loads(dfall.to_json(orient='records'))
#     return {
#         "status" : 200,
#         "length" : len(dfall),
#         "datafrom" : check_start,
#         "data" : json2data
#     }

def utcToUnix(timeData):
    timeData = datetime.datetime.timestamp(timeData)*1000
    timeData = math.trunc(timeData)
#     print(timeData)
    return timeData

def unixToUtc(timeData):
    timeData = datetime.datetime.fromtimestamp(int(timeData)/1000)
    return timeData