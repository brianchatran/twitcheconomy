from pokinator import Pokinator
from .. import db
from datetime import timedelta
from sys import exit
from time import time
from yahoo_fin import stock_info as si
BOOT_TIME = time()
OWNER = "lwg94"

def help(bot, prefix, cmds):
    bot.send_message(f"Registered commands: "
        + ", ".join([f"{prefix}{cmd.callables[0]}" for cmd in sorted(cmds, key=lambda cmd: cmd.callables[0])]))


def about(bot, user ,*args):
    bot.send_message("This is a FAKE economy bot , there is no real money involved in this .Version 0.1 Developed by Brianchatran.")


def F(bot, prefix, *args):
    
    bot.send_message("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⢀⣠⣤⣤⣤⣿⣧⣀⣀⣀⣀⣀⣀⣀⣀⣤⡄⠀ ⢠⣾⡟⠋⠁⠀⠀⣸⠇⠈⣿⣿⡟⠉⠉⠉⠙⠻⣿⡀ ⢺⣿⡀⠀⠀⢀⡴⠋⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠙⠇ ⠈⠛⠿⠶⠚⠋⣀⣤⣤⣤⣿⣿⣇⣀⣀⣴⡆⠀⠀⠀ ⠀⠀⠀⠀⠠⡞⠋⠀⠀⠀⣿⣿⡏⠉⠛⠻⣿⡀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀")

    





def userinfo(bot, user, *args):
    coins = db.field("SELECT Coins FROM users WHERE UserID = ?",
        user["id"])
    
    bot.send_message(f"Name: {user['name']}. ID: {user['id']} . Coins: {coins:,}.")


def pat(bot, prefix, *args):
    bot.send_message("UWU")


def ElDub(bot, prefix, *args):
    bot.send_message("wha u want mate")

def poke(bot, prefix, *args):
    bot.send_message(Pokinator.generate())


def socials(bot, prefix, *args):
    bot.send_message("lwg94 on twitter ,KingJellalTV on LwG94")

def ad(bot, prefix, *args):
    bot.send_message("if you have amazon prime you can link it with twitch to get a free subscription that you can use on this channel, also consider following")


def hello(bot, user, *args):
    bot.send_message(f"Hey {user['name']}!")


def shutdown(bot, user, *args):
    if user["name"].lower() == OWNER or user["name"].lower() == "brianchatran":
        bot.send_message("Bravo Six, going dark .")
        db.commit()
        db.close()
        bot.disconnect()
        exit(0)

    else:
        bot.send_message("You can't do that.")



def slap(bot, user, *args):
    try:
        if "@" in args[0]:
                                            #slap test
            phrase=args[0].partition("@")[2]    
            bot.send_message(f"{user['name']} slapped @"+phrase+" oof")
        else:
            bot.send_message(f"you need to @ someone")
        
        
        
        
    except:
        bot.send_message("idk something went wrong")
    pass







#economy
def coins(bot, user, *args):                #the coin command 
    coins = db.field("SELECT Coins FROM users WHERE UserID = ?",
        user["id"])
    bot.send_message(f"{user['name']}, you have {coins:,} coins.")
    db.execute("UPDATE users SET Coins = 500 WHERE UserID = ?",user["id"])




    
def stockprice(bot, user, *args):
    try:                                    #really bad way of doing a switch on python pls don't judge is a test
        if args[0].lower() == "redcorp": 

            print("redcorp")
            redcorp(bot)
            
        elif args[0].lower() == "lwgcorp":
            lwgcorp(bot)
        
        elif args[0].lower() == "kjcorp":
            kjcorp(bot)

        else:
            bot.send_message(f"you have to enter an existing company name , to see the list of names use the <stocklist command")
    except:
        bot.send_message(f"you have to enter an existing company name , to see the list of names use the <stocklist command")
    pass
    
 


#stocks
def redcorp(bot):
    price=si.get_live_price('SKLZ')
    price= int(price)
    bot.send_message(f"price Redcorp:"+str(price)+" coins  a share")
    print(price)

def lwgcorp(bot):
    price=si.get_live_price('TWTR')
    price= int(price)
    bot.send_message(f"price LWGCorp:"+str(price)+" coins  a share")
    print(price)      

def kjcorp(bot):
    price=si.get_live_price('DBX')
    price= int(price)
    bot.send_message(f"price KJCorp:"+str(price)+" coins  a share")
    print(price)    


#portfolio
def portfolio(bot,user,*args):
    portfolio = db.field("SELECT Portfolio FROM users WHERE UserID = ?", user["id"])
    if portfolio == None: 
        bot.send_message(f"WOW SUCH EMPTY")
    else:     #if the stock is already in the portfolio is added to the quantity
        print(portfolio)
        portfolios=portfolio.split(",")
        print(user["name"])
        name= list()
        quantity=list()
        bprice=list()
        print(portfolio)
        allstocks=""
        for i in range(len(portfolios)):
                
            a=portfolios[i][portfolios[i].find(".")+1 : portfolios[i].find("(")]
            if a == "":
                print("nope")
            else:
                print(i)
                name.append(i)
                quantity.append(i)
                bprice.append(i)
                name[i]=portfolios[i][portfolios[i].find(".")+1 : portfolios[i].find("(")]
                quantity[i]=portfolios[i][portfolios[i].find("qu")+2 : portfolios[i].find("-")]
                bprice[i]=portfolios[i][portfolios[i].find("-")+3 : portfolios[i].find(")")]
                
                allstocks +="-"+name[i]+" "+quantity[i]+" share/s -bought at "+bprice[i]+" coins / / /"
                print ("name "+name[i]+",")
                print ("quantity : "+quantity[i])
                print ("Bought at Price : "+bprice[i])
        bot.send_message(user["name"]+"'s portfolio "+allstocks)
 

#buy stocks
def stockbuy(bot, user,*args):
    try:                                    #really bad way of doing a switch on python pls don't judge is a test
        if args[0].lower() == "redcorp": 
            buyredcorp(bot,user,*args)  

        elif args[0].lower() == "lwgcorp":
            buylwgcorp(bot,user,*args)

        elif args[0].lower() == "kjcorp":
            buykjcorp(bot,user,*args)

        else:
            bot.send_message(f"you have to enter an existing company name , to see the list of names use the <stocklist command")
    except Exception as e:
        print(e)
        bot.send_message(f"you have to enter an existing company name , to see the list of names use the <stocklist command")
    pass


#buy stocks functions
def buyredcorp(bot,user,*args):
    price=si.get_live_price('SKLZ')
    price= int(price)
    qu=int(float(args[1].replace(',', '.')))
    fprice=price*qu
    coins = db.field("SELECT Coins FROM users WHERE UserID = ?", user["id"])
    print (coins)
    print (fprice)
    if coins < fprice :
        bot.send_message(f"You don't have that much, the final price is "+str(fprice)+" coins and you have "+str(coins)+" coins.")


    else:
        db.execute("UPDATE users SET Coins = Coins - ? WHERE UserID = ?",fprice, user["id"])
        portfolio = db.field("SELECT Portfolio FROM users WHERE UserID = ?", user["id"])
        if portfolio == None: #if the stock is not in the portfolio is added 
                port=".RedCorp(qu"+str(qu)+"-co"+str(price)+"),"
                print(port)
                db.execute("UPDATE users SET Portfolio = ? WHERE UserID = ?",
                port, user["id"])
        else:     #if the stock is already in the portfolio is added to the quantity
            print(portfolio)
            portfolios=portfolio.split(",")
            print(user["name"])
            name= list()
            quantity=list()
            bprice=list()
            print(portfolio)
            for i in range(len(portfolios)):
                
                a=portfolios[i][portfolios[i].find(".")+1 : portfolios[i].find("(")]
                if a == "":
                    print("nope")
                else:
                    print(i)
                    name.append(i)
                    quantity.append(i)
                    bprice.append(i)
                    name[i]=portfolios[i][portfolios[i].find(".")+1 : portfolios[i].find("(")]
                    quantity[i]=portfolios[i][portfolios[i].find("qu")+2 : portfolios[i].find("-")]
                    bprice[i]=portfolios[i][portfolios[i].find("-")+3 : portfolios[i].find(")")]
                    print ("name "+name[i]+",")
                    print ("quantity : "+quantity[i])
                    print ("Bought at Price : "+bprice[i])
            if  "RedCorp" in name: #if stock is in the list is 
                index=name.index("RedCorp")
                change="RedCorp(qu"+str(quantity[index])+"-co"+str(bprice[index])+")"
                nqu=str(int(quantity[index])+int(qu))
                new="RedCorp(qu"+nqu+"-co"+str(price)+")"
                db.execute("UPDATE users SET Portfolio = REPLACE(Portfolio,?,?)  WHERE UserID = ?",
                change,new, user["id"])
                bot.send_message(f"You bought "+str(qu)+" shares of RedCorp at a total price of "+str(fprice)+" coins ("+str(price)+" coins a share).")

            else:
                port=portfolio+".RedCorp(qu"+str(qu)+"-co"+str(price)+"),"
                print(port)
                db.execute("UPDATE users SET Portfolio = ? WHERE UserID = ?",
                port, user["id"])
                bot.send_message(f"You bought "+str(qu)+" shares of RedCorp at a total price of "+str(fprice)+" coins ("+str(price)+" coins a share).")

def buylwgcorp(bot,user,*args):
    price=si.get_live_price('TWTR')
    price= int(price)
    qu=int(float(args[1].replace(',', '.')))
    fprice=price*qu
    coins = db.field("SELECT Coins FROM users WHERE UserID = ?", user["id"])
    print (coins)
    print (fprice)
    if coins < fprice :
        bot.send_message(f"You don't have that much, the final price is "+str(fprice)+" coins and you have "+str(coins)+" coins.")


    else:
        db.execute("UPDATE users SET Coins = Coins - ? WHERE UserID = ?",fprice, user["id"])
        portfolio = db.field("SELECT Portfolio FROM users WHERE UserID = ?", user["id"])
        if portfolio == None: #if the stock is not in the portfolio is added 
                port=".LWGCorp(qu"+str(qu)+"-co"+str(price)+"),"
                print(port)
                db.execute("UPDATE users SET Portfolio = ? WHERE UserID = ?",
                port, user["id"])
                bot.send_message(f"You bought "+str(qu)+" shares of LWGCorp at a total price of "+str(fprice)+" coins ("+str(price)+" coins a share).")
        else:     #if the stock is already in the portfolio is added to the quantity
            print(portfolio)
            portfolios=portfolio.split(",")
            print(user["name"])
            name= list()
            quantity=list()
            bprice=list()
            print(portfolio)
            for i in range(len(portfolios)):
                
                a=portfolios[i][portfolios[i].find(".")+1 : portfolios[i].find("(")]
                if a == "":
                    print("nope")
                else:
                    print(i)
                    name.append(i)
                    quantity.append(i)
                    bprice.append(i)
                    name[i]=portfolios[i][portfolios[i].find(".")+1 : portfolios[i].find("(")]
                    quantity[i]=portfolios[i][portfolios[i].find("qu")+2 : portfolios[i].find("-")]
                    bprice[i]=portfolios[i][portfolios[i].find("-")+3 : portfolios[i].find(")")]
                    print ("name "+name[i]+",")
                    print ("quantity : "+quantity[i])
                    print ("Bought at Price : "+bprice[i])
            if  "LWGCorp" in name: #if stock is in the list is 
                print("bye")
                index=name.index("LWGCorp")
                change="LWGCorp(qu"+str(quantity[index])+"-co"+str(bprice[index])+")"
                nqu=str(int(quantity[index])+int(qu))
                new="LWGCorp(qu"+nqu+"-co"+str(price)+")"
                db.execute("UPDATE users SET Portfolio = REPLACE(Portfolio,?,?)  WHERE UserID = ?",
                change,new, user["id"])
                bot.send_message(f"You bought "+str(qu)+" shares of LWGCorp at a total price of "+str(fprice)+" coins ("+str(price)+" coins a share).")

            else:
                
                port=portfolio+".LWGCorp(qu"+str(qu)+"-co"+str(price)+"),"
                print("port"+port)
                db.execute("UPDATE users SET Portfolio = ? WHERE UserID = ?",
                port, user["id"])
                bot.send_message(f"You bought "+str(qu)+" shares of LWGCorp at a total price of "+str(fprice)+" coins ("+str(price)+" coins a share).")
                
