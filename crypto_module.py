from urllib.request import urlopen
import json
import pandas as pd

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