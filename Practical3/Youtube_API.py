import requests

API_KEY= " "
url = "https://www.googleapis.com/youtube/v3/search"

parameters={
    "part":"snippet",
    "q":"Artificial Intelligence",
    "type":"video",
    "maxResults":5,
    "key": API_KEY
}

response=requests.get(url,params=parameters)

data=response.json()

for video in data ["items"]:
    print("Title : ", video["snippet"]["title"])
    print("Channel : ", video["snippet"]["channelTitle"])
    print("VideoId : " , video["id"]["videoId"])
