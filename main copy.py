# clone this website and extract the data 
import requests,asyncio,telegram
from bs4 import BeautifulSoup


bot = telegram.Bot(token='6374275265:AAFg6AklVU5HMhP4oH4pcY-q7rPB167HZ-c')
channel_id = '-1002099409867'

# Function to send messages
async def send_message(message,i):
    await bot.send_message(chat_id=channel_id, text=message)
    print("Message sent : ",i)

url = "https://www.hamropatro.com/rashifal"
print("Fetching data from", url)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# extract the data
print("Extracting data")
rashifaldivs= soup.find_all("div", class_="item")

loop = asyncio.get_event_loop()

# loop through the data
print("Looping Trhough the data")
# receive the index and the div
for i,div in enumerate(rashifaldivs):
    rashi= div.find("h3").text
    raashifal= div.find("div", class_="desc").p.text.split(")")[1]
    # check contans or not 
    if "राशिफल जे जस्तो" in raashifal:
        raashifal=raashifal.split("राशिफल जे जस्तो")[0]
    message=f"{rashi}\n{raashifal}"
    loop.run_until_complete(send_message(message,i))
    
