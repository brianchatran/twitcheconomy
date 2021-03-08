from collections import defaultdict
from datetime import datetime, timedelta
from random import randint
from re import search
from time import time
import random


from . import db
from .cmds import games

welcomed = []
messages = defaultdict(int)


def process(bot, user, message):
    update_records(bot, user)

    if user["id"] not in welcomed and user["name"] != "LwG94" and user["name"] and "lwg94exe" and user["name"] != "brianchatran":
        if "bye" in message:
            print("no")
        else:
            welcome(bot, user)

    elif "bye" in message:
        say_goodbye(bot, user)

    # if user["id"] != "190089937"
    check_activity(bot, user)

    if message == "F" or message == "f":
        from time import sleep
        a="""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢻⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀   .     .::⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""
        b="""⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀   ⠀⠀     .::⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""
        c="""⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""
        bot.send_message(a)
        bot.send_message(b)
        bot.send_message(c)



    if (h := games.heist) is not None:
        if h.start_time <= time() and not h.running:
            games.run_heist(bot)
            print("start")

        elif h.end_time <= time() and h.running:
            games.end_heist(bot)
            print("end")
    
    if "GG" in message or "gg" in message:
        gg(bot,user)



'''
    if (match := search(r'cheer[0-9]+', message)) is not None:
        thank_for_cheer(bot, user, match)

    


def add_user(bot, user):
    db.execute("INSERT OR IGNORE INTO users (UserID, UserName) VALUES (?, ?)",
        user["id"], user["name"].lower())
'''

def update_records(bot, user):
    db.execute("INSERT OR IGNORE INTO users (UserID) VALUES (?)",
         user["id"],)
    
    db.execute("UPDATE users SET UserName= ?  WHERE UserID= ?",
        user["name"],user["id"])
    

    db.execute("UPDATE users SET MessagesSent= MessagesSent + 1 WHERE UserID= ?",
        user["id"])
    

    stamp = db.field("SELECT CoinLock FROM users WHERE UserID = ?",
        user["id"])
    
    if datetime.strptime(stamp,"%Y-%m-%d %H:%M:%S") < datetime.utcnow():
        coinlock = (datetime.utcnow()+timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")

        db.execute("UPDATE users SET Coins = Coins + ?, CoinLock = ? WHERE UserID = ?",
            randint(1, 5), coinlock, user["id"])


def welcome(bot, user):
    bot.send_message(f"Welcome to the stream {user['name']}!")
    welcomed.append(user["id"])

def gg(bot, user):
    bot.send_message(f"GG")




def say_goodbye(bot, user):
    bot.send_message(f"See ya later {user['name']}!")
    welcomed.remove(user["id"])


def check_activity(bot, user):
    messages[user["id"]] += 1

    if (count := messages[user["id"]]) % 20 == 0:
        bot.send_message(f"Thanks for being active in chat {user['name']} - you've sent {count:,} messages! Keep it up!")

'''
def thank_for_cheer(bot, user, match):
    bot.send_message(f"Thanks for the {match.group[5:]:,} bits {user['name']}! That's really appreciated!")
'''