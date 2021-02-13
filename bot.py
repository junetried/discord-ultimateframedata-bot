#!/usr/bin/env python3
import my_keys
import discord, logging, requests, regex
from discord.ext import commands
from bs4 import BeautifulSoup

logging.basicConfig(format="%(asctime)-15s %(message)s")

bot = commands.Bot(command_prefix="!")

async def send_message(ctx, *args, **kwargs):
	try:
		await ctx.send(*args, **kwargs)
	except Exception as exception:
		logging.error("Error sending message: ", exc_info=exception)

@bot.event
async def on_ready():
	logging.info("Ready.")

class chars:
	mario = "Mario"
	dk = "Donkey Kong"
	link = "Link"
	samus = "Samus"
	darksamus = "Dark Samus"
	yoshi = "Yoshi"
	kirby = "Kirby"
	fox = "Fox"
	pikachu = "Pikachu"
	luigi = "Luigi"
	ness = "Ness"
	falcon = "Captain Falcon"
	jigglypuff = "Jigglypuff"
	peach = "Peach"
	bowser = "Bowser"
	iceclimbers = "Ice Climbers"
	sheik = "Sheik"
	zelda = "Zelda"
	drmario = "Dr. Mario"
	pichu = "Pichu"
	falco = "Falco"
	marth = "Marth"
	lucina = "Lucina"
	younglink = "Young Link"
	ganondorf = "Ganondorf"
	mewtwo = "Mewtwo"
	roy = "Roy"
	chrom = "Chrom"
	gameandwatch = "Mr. Game & Watch"
	metaknight = "Meta Knight"
	pit = "Pit"
	darkpit = "Dark Pit"
	zerosuitsamus = "Zero Suit Samus"
	wario = "Wario"
	snake = "Snake"
	ike = "Ike"
	charizard = "Pt. Charizard"
	ivysaur = "Pt. Ivysaur"
	squirtle = "Pt. Squirtle"
	diddykong = "Diddy Kong"
	lucas = "Lucas"
	sonic = "Sonic"
	kingdedede = "King Dedede"
	olimar = "Olimar"
	lucario = "Lucario"
	rob = "R.O.B."
	toonlink = "Toon Link"
	wolf = "Wolf"
	villager = "Villager"
	megaman = "Mega Man"
	wiifittrainer = "Wii Fit Trainer"
	rosalinaluma = "Rosalina & Luma"
	littlemac = "Little Mac"
	greninja = "Greninja"
	palutena = "Palutena"
	pacman = "Pac-Man"
	robin = "Robin"
	shulk = "Shulk"
	bowserjr = "Bowser Jr."
	duckhunt = "Duck Hunt"
	ryu = "Ryu"
	ken = "Ken"
	cloud = "Cloud"
	corrin = "Corrin"
	bayonetta = "Bayonetta"
	inkling = "Inkling"
	ridley = "Ridley"
	simon = "Simon"
	richter = "Richter"
	kingkrool = "King K. Rool"
	isabelle = "Isabelle"
	incineroar = "Incineroar"
	miibrawler = "Mii Brawler"
	miiswordfighter = "Mii Swordfighter"
	miigunner = "Mii Gunner"
	piranhaplant = "Piranha Plant"
	joker = "Joker"
	hero = "Hero"
	banjokazooie = "Banjo & Kazooie"
	terry = "Terry"
	byleth = "Byleth"
	minmin = "Min Min"
	steve = "Steve"
	sephiroth = "Sephiroth"

class moveset:
	# Normals
	jab = "Jab"
	ftilt = "Forward tilt"
	utilt = "Up tilt"
	dtilt = "Down tilt"
	dashattack = "Dash attack"
	# Smashes
	fsmash = "Forward smash"
	usmash = "Up smash"
	dsmash = "Down smash"
	# Specials
	neutralb = "Neutral B"
	sideb = "Side B"
	upb = "Up B"
	downb = "Down B"
	# Grab
	grab = "Grab"
	dashgrab = "Dash grab"
	pivotgrab = "Pivotgrab"
	pummel = "Pummel"
	fthrow = "Forward throw"
	bthrow = "Back throw"
	uthrow = "Up throw"
	dthrow = "Down throw"
	# Aerials
	nair = "Neutral air"
	fair = "Forward air"
	bair = "Back air"
	uair = "Up air"
	dair = "Down air"
	# Other
	ledgegrab = "Ledge grab"
	ledgehang = "Ledge hang"
	ledgeattack = "Edge attack"
	tripattack = "Floor attack (trip)"
	getupattackup = "Floor attack (back)"
	getupattackdown = "Floor attack (front)"

attributes = {"startup" : "**Startup:** $a frames", "totalframes" : "**Total Frames:** $a frames", "landinglag" : "**Landing Lag:** $a frames", "notes" : "**Notes:** $a", "basedamage" : "**Base Damage:** $a", "shieldlag" : "**Shield Lag:** $a frames", "shieldstun" : "**Shield Stun:** $a frames", "whichhitbox" : "**Which Hitbox:** $a", "advantage" : "**On Shield:** $a frames on shield", "activeframes" : "**Active Frames:** $a"}

ssbu_chars = {"mario" : chars.mario, "dk" : chars.dk, "donkeykong" : chars.dk, "link" : chars.link, "samus" : chars.samus, "darksamus" : chars.darksamus, "dsamus" : chars.darksamus, "damus" : chars.darksamus, "yoshi" : chars.yoshi, "kirby" : chars.kirby, "fox" : chars.fox, "pikachu" : chars.pikachu, "pika" : chars.pikachu, "luigi" : chars.luigi, "ness" : chars.ness, "falcon" : chars.falcon, "cptfalcon" : chars.falcon, "captainfalcon" : chars.falcon, "jigglypuff" : chars.jigglypuff, "puff" : chars.jigglypuff, "peach" : chars.peach, "bowser" : chars.bowser, "icies" : chars.iceclimbers, "iceclimbers" : chars.iceclimbers, "iceclimber" : chars.iceclimbers, "sheik" : chars.sheik, "zelda" : chars.zelda, "doc" : chars.drmario, "drmario" : chars.drmario, "pichu" : chars.pichu, "falco" : chars.falco, "marth" : chars.marth, "lucina" : chars.lucina, "younglink" : chars.younglink, "yink" : chars.younglink, "ylink" : chars.younglink, "yl" : chars.younglink, "ganondorf" : chars.ganondorf, "ganon" : chars.ganondorf, "mewtwo" : chars.mewtwo, "roy" : chars.roy, "chrom" : chars.chrom, "g&w" : chars.gameandwatch, "gameandwatch" : chars.gameandwatch, "mrgameandwatch" : chars.gameandwatch, "gnw" : chars.gameandwatch, "metaknight" : chars.metaknight, "mk" : chars.metaknight, "pit" : chars.pit, "darkpit" : chars.darkpit, "dpit" : chars.darkpit, "zerosuitsamus" : chars.zerosuitsamus, "zss" : chars.zerosuitsamus, "wario" : chars.wario, "snake" : chars.snake, "ike" : chars.ike, "charizard" : chars.charizard, "zard" : chars.charizard, "ivysaur" : chars.ivysaur, "ivy" : chars.ivysaur, "squirtle" : chars.squirtle, "diddykong" : chars.diddykong, "diddy" : chars.diddykong, "lucas" : chars.lucas, "sonic" : chars.sonic, "kingdedede" : chars.kingdedede, "dedede" : chars.kingdedede, "d3" : chars.kingdedede, "olimar" : chars.olimar, "alph" : chars.olimar, "lucario" : chars.lucario, "r.o.b." : chars.rob, "rob" : chars.rob, "toonlink" : chars.toonlink, "tlink" : chars.toonlink, "wolf" : chars.wolf, "villager" : chars.villager, "megaman" : chars.megaman, "wiifittrainer" : chars.wiifittrainer, "wiifit" : chars.wiifittrainer, "trainer" : chars.wiifittrainer, "rosalina&luma" : chars.rosalinaluma, "rosalinaandluma" : chars.rosalinaluma, "rosalinaluma" : chars.rosalinaluma, "rosalina" : chars.rosalinaluma, "rosa" : chars.rosalinaluma, "rosaluma" : chars.rosalinaluma, "littlemac" : chars.littlemac, "mac" : chars.littlemac, "greninja" : chars.greninja, "palutena" : chars.palutena, "palu" : chars.palutena, "pacman" : chars.pacman, "pac-man" : chars.pacman, "robin" : chars.robin, "shulk" : chars.shulk, "bowserjr" : chars.bowserjr, "duckhunt" : chars.duckhunt, "ryu" : chars.ryu, "ken" : chars.ken, "cloud" : chars.cloud, "corrin" : chars.corrin, "bayonetta" : chars.bayonetta, "bayo" : chars.bayonetta, "inkling" : chars.inkling, "ridley" : chars.ridley, "simon" : chars.simon, "richter" : chars.richter, "kingkrool" : chars.kingkrool, "krool" : chars.kingkrool, "isabelle" : chars.isabelle, "incineroar" : chars.incineroar, "incin" : chars.incineroar, "miibrawler" : chars.miibrawler, "brawler" : chars.miibrawler, "miiswordfighter" : chars.miiswordfighter, "swordfighter" : chars.miiswordfighter, "miigunner" : chars.miigunner, "gunner" : chars.miigunner, "piranhaplant" : chars.piranhaplant, "plant" : chars.piranhaplant, "joker" : chars.joker, "hero" : chars.hero, "banjo&kazooie" : chars.banjokazooie, "banjoandkazooie" : chars.banjokazooie, "banjo" : chars.banjokazooie, "terry" : chars.terry, "byleth" : chars.byleth, "minmin" : chars.minmin, "steve" : chars.steve, "sephiroth" : chars.sephiroth}
moveset = {"jab" : moveset.jab, "ftilt" : moveset.ftilt, "forwardtilt" : moveset.ftilt, "utilt" : moveset.utilt, "uptilt" : moveset.utilt, "dtilt" : moveset.dtilt, "downtilt" : moveset.dtilt, "dashattack" : moveset.dashattack, "fsmash" : moveset.fsmash, "forwardsmash" : moveset.fsmash, "usmash" : moveset.usmash, "upsmash" : moveset.usmash, "dsmash" : moveset.dsmash, "downsmash" : moveset.dsmash, "neutralb" : moveset.neutralb, "upb" : moveset.upb, "upspecial" : moveset.upb, "sideb" : moveset.sideb, "sidespecial" : moveset.sideb, "downb" : moveset.downb, "downspecial" : moveset.downb, "grab" : moveset.grab, "dashgrab" : moveset.dashgrab, "pivotgrab" : moveset.pivotgrab, "pummel" : moveset.pummel, "forwardthrow" : moveset.fthrow, "fthrow" : moveset.fthrow, "backthrow" : moveset.bthrow, "bthrow" : moveset.bthrow, "upthrow" : moveset.uthrow, "uthrow" : moveset.uthrow, "downthrow" : moveset.dthrow, "dthrow" : moveset.dthrow, "neutralair" : moveset.nair, "neutralaerial" : moveset.nair, "nair" : moveset.nair, "forwardair" : moveset.fair, "forwardaerial" : moveset.fair, "fair" : moveset.fair, "backair" : moveset.bair, "backaerial" : moveset.bair, "bair" : moveset.bair, "upair" : moveset.uair, "upaerial" : moveset.uair, "uair" : moveset.uair, "downair" : moveset.dair, "downaerial" : moveset.dair, "dair" : moveset.dair, "ledgegrab" : moveset.ledgegrab, "ledgehang" : moveset.ledgehang}
# These dicts are for aliases. For example, you can do !doc or !drmario, or !ftilt or !forwardtilt

@bot.command(aliases=list(ssbu_chars))
async def character_command(ctx, *args):
	#print(locals())
	arguments = locals()["args"][0].lower()
	char = ssbu_chars[ctx.invoked_with]
	if arguments in list(moveset):
		url = "https://ultimateframedata.com/" + char.replace(" ", "_").replace(".", "").replace("&", "and").replace("-", "_").lower() + ".php"
		page = requests.get(url)
		soup = BeautifulSoup(page.content, "html.parser")
		try: # If this fails, probably a weird move
			for x in soup.find_all("div", class_="movename", string=lambda y: y and moveset[arguments].title() in y): # Find all move containers
				for z in x.parent.find_all("a"): # Find the hitbox images
					if not z: # If this happens, the move likely has no animation, like with pokemon trainer switch
						await send_message(ctx, "I couldn't find that move's animation.\nFeel free to check for yourself: <" + url + ">")
						return
					image = "https://ultimateframedata.com/" + z["data-featherlight"].replace(" ", "%20")
					desc = "" # We will add to this variable and make it the description of the embed
					for a in ["startup", "totalframes", "landinglag", "notes", "basedamage", "shieldlag", "shieldstun", "whichhitbox", "advantage", "activeframes"]: # Find all these attributes of a move
						if not "--" in x.parent.find("div", class_=a).text.strip(): # If they don't exist, they are set as '--'
							desc = desc + "\n" + attributes[a].replace("$a", x.parent.find("div", class_=a).text.strip()) # Append this to the embed description, 'prettified' with the attributes dict
					
					await send_message(ctx, embed=discord.Embed(title=char + " " + x.parent.find("div", class_="movename").text.strip(), description=desc.strip(), url=image).set_image(url="\n" + image))
			return
		except TypeError:
			await send_message(ctx, "I couldn't find that move, it might be a special one.\nFeel free to check for yourself: <" + url + ">")
			return

@bot.command(name="framedata")
async def framedata_command(ctx):
	await send_message(ctx, "<https://ultimateframedata.com>")

bot.run(my_keys.discord)
