from time import time

from . import misc, games


PREFIX = "<"

class Cmd(object):
	def __init__(self, callables, func, cooldown=0):
		self.callables = callables
		self.func = func
		self.cooldown = cooldown
		self.next_use = time()
'''
cmds = {
	"F":misc.F,
	"user":misc.userinfo,
	"pat":misc.pat,
	"ElDub":misc.ElDub,
	"poke":misc.poke,
	"socials":misc.socials,
	"ad":misc.ad,
	"vol":misc.vol,
	"rpg":misc.rpg,
	"hello":misc.hello	
}
'''
cmds = [
	#	misc
	Cmd(["hello", "hi", "hey"], misc.hello, cooldown=15),
	Cmd(["about"], misc.about),
	Cmd(["userinfo", "ui"], misc.userinfo),
	Cmd(["shutdown"], misc.shutdown),
	Cmd(["socials"], misc.socials),
	Cmd(["slap"], misc.slap),
	Cmd(["stockp","stock","stockprice"], misc.stockprice),
	Cmd(["stockb"], misc.stockbuy),
	Cmd(["port"], misc.portfolio),
	#   economy
	Cmd(["coins","money","bank","balance"],misc.coins),
	#   games
	Cmd(["coinflip", "flip"], games.coinflip, cooldown=30),
	Cmd(["coinflip t", "flip t","coinflip h", "flip h","coinflip tails","flip tails","coinflip heads","flip heads"], games.coinflip),
	Cmd(["heist"], games.start_heist, cooldown=60),
	Cmd(["join"], games.start_heist, cooldown=60)
	
]
def process(bot , user, message):
	if message.startswith(PREFIX):
		cmd=message.split(" ")[0][len(PREFIX):]
		args = message.split(" ")[1:]
		perform(bot, user, cmd, *args)

def perform(bot, user, call, *args):
	if call in ("help", "commands", "cmds"):
		misc.help(bot, PREFIX, cmds)
	
	else:
		for cmd in cmds:
			if call in cmd.callables:
				if time() > cmd.next_use:
					cmd.func(bot, user, *args)
					cmd.next_use = time() + cmd.cooldown

				else:
					bot.send_message(f"Cooldown still in effect. Try again in {cmd.next_use-time():,.0f} seconds.")

				return

		bot.send_message(f"{user['name']}, \"{call}\" isn't a registered command.")