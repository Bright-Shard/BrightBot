from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm a Discord bot. You can invite me to your server <a href='https://discord.com/api/oauth2/authorize?client_id=745433967486042133&permissions=8&scope=bot'>here!</a>"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()