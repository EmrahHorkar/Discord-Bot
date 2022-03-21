from importlib import import_module
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession


TOKEN = ''


"""Döviz"""
url = "https://www.doviz.com/"

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

currencies = soup.find_all("span",{"class":"name"})
exchange_rates = soup.find_all("span", {"class": "value"})

a = []
for currency, exchange_rate in zip(currencies, exchange_rates):
    
    currency = currency.text
    exchange_rate = exchange_rate.text
    
    currency = currency.strip()
    currency = currency.replace("\n", "")

    exchange_rate = exchange_rate.strip()
    exchange_rate = exchange_rate.replace("\n", "")
    
    a.append([currency+"="+exchange_rate])


"""SONG"""
song_url = "https://www.vulture.com/article/best-songs-2022.html"

song_response = requests.get(song_url)

html_songcontent = song_response.content

soup = BeautifulSoup(html_songcontent, "html.parser")

songs  = soup.find_all("span",{"class":"text"})

list = []

for i in songs:
    i = i.text
    i = i.strip()
    list.append(i)




"""Movie"""
url1 = "https://www.imdb.com/chart/top/"
url2 = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
response = requests.get(url1)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

titles = soup.find_all("td",{"class":"titleColumn"})
ratings = soup.find_all("td",{"class":"ratingColumn imdbRating"})

response2 = requests.get(url2)
html_content2 = response2.content

soup2 = BeautifulSoup(html_content2,"html.parser")


b = []
for title,rating in zip(titles,ratings):
    title = title.text
    rating = rating.text
    
    
    title = title.strip()
    title = title.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    
    b.append([title,rating])



import discord

import random
import time




client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel}')



    if message.author == client.user:
        return
    

    if message.channel.name == 'general':
            if user_message.lower() == 'hey':
                await message.channel.send(f'Hii {username}!')
                return
            elif user_message.lower() == 'help':
                await message.channel.send('----Here is the commands------')
                await message.channel.send('exchange => instant exchange rates')
                await message.channel.send('movie => movie recommandation from IMBD top 250')
                await message.channel.send('quote => quote of the day')
                await message.channel.send('weather => instant weather')
                await message.channel.send('song => song recommandation')
                

                return
            elif user_message.lower() == 'see you later':
                await message.channel.send(f'See you {username}!')
                return
        
            elif user_message.lower() == 'hello':
                await message.channel.send(f' Hii {username}')
                return
            elif user_message.lower() == 'song':
                await message.channel.send(random.choice(list))
                return
            elif user_message.lower() == 'what you doing':
                await message.channel.send(f'Listening music {username} what about you?')
                return
            
            elif user_message.lower() == 'weather':
                s = HTMLSession()
                query = 'ankara'
                url = f'https://www.google.com/search?q=weather+{query}'
                r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'})
                temp = r.html.find('span#wob_tm', first = True).text
                c = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
                sit = r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text
                await message.channel.send(f'{query} {temp} {c} {sit}')
                return
            
            
            elif user_message.lower() == 'good night':
                await message.channel.send(f'Good night {username}!')
                return
            elif user_message.lower() == 'good morming':
                await message.channel.send(f'Good morning {username}!')
                return
            elif user_message.lower() == 'how are you':
                await message.channel.send(f'I am okay what about you {username}')
                return
            elif user_message.lower() == 'whats up':
                await message.channel.send(f'Not much {username} whats up with you?')
                return
            
            
            elif user_message.lower() == 'exchange':      
                await message.channel.send(f'Exchange rates =>  {a}')
                return
        
            elif user_message.lower() == 'movie':
                await message.channel.send(f'Imbd rank {random.choice(b)}')
                return
            
                
            elif user_message.lower() == 'quote':
                await message.channel.send(f' In the end, the whole of life becomes an act of letting go')
                return
            
    
            
            
            
        
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return
        
        

client.run(TOKEN)
