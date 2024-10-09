# clone this website and extract the data 
import requests,asyncio,telegram,datetime,os
from dotenv import load_dotenv

load_dotenv()
apikey=os.getenv("BOTAPIKEY")
channel_id=os.getenv("CHATID")

# Create a Bot Object
bot = telegram.Bot(token=apikey)



# Function to send messages
async def send_message(message):
    chunk_size = 4096
    for i in range(0, len(message), chunk_size):
        await bot.send_message(chat_id=channel_id, text=message[i:i + chunk_size])
        print("Message sent")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    url = "https://nepalipatro.com.np/rashifal/getv5/type/dwmy?lang=en"
    response = requests.get(url)
    print("Data fetched")
    data= response.json()["np"][0]
    horoscopedata = {}
    horoscope=["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
    for i in horoscope:
        horoscopedata[i] = data[i]
    date = datetime.datetime.now().strftime("%A %d-%B %Y")
    message=f"Horoscope of {date}\n"
    for i in horoscopedata:
        message+=f"{i.title()}:\n{horoscopedata[i]}\n\n"
    print("Message created")
    loop.run_until_complete(send_message(message))
