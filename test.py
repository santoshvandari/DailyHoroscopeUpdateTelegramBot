# get resuest on the api 

import requests
try:
    url = "https://nepalipatro.com.np/rashifal/getv5/type/dwmy?lang=en"
    response = requests.get(url)
    data= response.json()["np"][0]

    horoscopedata = {}
    horoscope=["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
    for i in horoscope:
        horoscopedata[i] = data[i]
    
    for i in horoscopedata:
        print(i,horoscopedata[i])
        
except Exception as e:
    print("Error : ",e)
    data = None