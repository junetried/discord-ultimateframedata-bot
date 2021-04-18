#!/usr/bin/env python3
import my_keys # Your discord key and mysql password goes here
import aiohttp, discord, logging, re, MySQLdb
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
	pyra = "Pyra"
	mythra = "Mythra"

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
	floorattackup = "Floor attack (back)"
	floorattackdown = "Floor attack (front)"
	floorattackgeneric = "Floor attack" # lol
	rollforward = "Forward Roll"
	rollback = "Backward Roll"

attributes = {"hitbox" : "**Image Order:** {0}", "startup" : "**Startup:** {0} frames", "totalframes" : "**Total Frames:** {0} frames", "landinglag" : "**Landing Lag:** {0} frames", "notes" : "**Notes:** {0}", "basedamage" : "**Base Damage:** {0}", "shieldlag" : "**Shield Lag:** {0} frames", "shieldstun" : "**Shield Stun:** {0} frames", "whichhitbox" : "**Which Hitbox:** {0}", "advantage" : "**On Shield:** {0} frames on shield", "activeframes" : "**Active Frames:** {0}"}

ssbu_chars = {"mario" : chars.mario, "dk" : chars.dk, "donkeykong" : chars.dk, "link" : chars.link, "samus" : chars.samus, "darksamus" : chars.darksamus, "dsamus" : chars.darksamus, "damus" : chars.darksamus, "yoshi" : chars.yoshi, "kirby" : chars.kirby, "fox" : chars.fox, "pikachu" : chars.pikachu, "pika" : chars.pikachu, "luigi" : chars.luigi, "ness" : chars.ness, "falcon" : chars.falcon, "cptfalcon" : chars.falcon, "captainfalcon" : chars.falcon, "jigglypuff" : chars.jigglypuff, "puff" : chars.jigglypuff, "peach" : chars.peach, "bowser" : chars.bowser, "icies" : chars.iceclimbers, "iceclimbers" : chars.iceclimbers, "iceclimber" : chars.iceclimbers, "sheik" : chars.sheik, "zelda" : chars.zelda, "doc" : chars.drmario, "drmario" : chars.drmario, "pichu" : chars.pichu, "falco" : chars.falco, "marth" : chars.marth, "lucina" : chars.lucina, "younglink" : chars.younglink, "yink" : chars.younglink, "ylink" : chars.younglink, "yl" : chars.younglink, "ganondorf" : chars.ganondorf, "ganon" : chars.ganondorf, "mewtwo" : chars.mewtwo, "roy" : chars.roy, "chrom" : chars.chrom, "g&w" : chars.gameandwatch, "gameandwatch" : chars.gameandwatch, "mrgameandwatch" : chars.gameandwatch, "gnw" : chars.gameandwatch, "metaknight" : chars.metaknight, "mk" : chars.metaknight, "pit" : chars.pit, "darkpit" : chars.darkpit, "dpit" : chars.darkpit, "zerosuitsamus" : chars.zerosuitsamus, "zss" : chars.zerosuitsamus, "wario" : chars.wario, "snake" : chars.snake, "ike" : chars.ike, "charizard" : chars.charizard, "zard" : chars.charizard, "ivysaur" : chars.ivysaur, "ivy" : chars.ivysaur, "squirtle" : chars.squirtle, "diddykong" : chars.diddykong, "diddy" : chars.diddykong, "lucas" : chars.lucas, "sonic" : chars.sonic, "kingdedede" : chars.kingdedede, "dedede" : chars.kingdedede, "d3" : chars.kingdedede, "olimar" : chars.olimar, "alph" : chars.olimar, "lucario" : chars.lucario, "r.o.b." : chars.rob, "rob" : chars.rob, "toonlink" : chars.toonlink, "tlink" : chars.toonlink, "wolf" : chars.wolf, "villager" : chars.villager, "megaman" : chars.megaman, "wiifittrainer" : chars.wiifittrainer, "wiifit" : chars.wiifittrainer, "trainer" : chars.wiifittrainer, "rosalina&luma" : chars.rosalinaluma, "rosalinaandluma" : chars.rosalinaluma, "rosalinaluma" : chars.rosalinaluma, "rosalina" : chars.rosalinaluma, "rosa" : chars.rosalinaluma, "rosaluma" : chars.rosalinaluma, "littlemac" : chars.littlemac, "mac" : chars.littlemac, "greninja" : chars.greninja, "palutena" : chars.palutena, "palu" : chars.palutena, "pacman" : chars.pacman, "pac-man" : chars.pacman, "robin" : chars.robin, "shulk" : chars.shulk, "bowserjr" : chars.bowserjr, "duckhunt" : chars.duckhunt, "ryu" : chars.ryu, "ken" : chars.ken, "cloud" : chars.cloud, "corrin" : chars.corrin, "bayonetta" : chars.bayonetta, "bayo" : chars.bayonetta, "inkling" : chars.inkling, "ridley" : chars.ridley, "simon" : chars.simon, "richter" : chars.richter, "kingkrool" : chars.kingkrool, "krool" : chars.kingkrool, "isabelle" : chars.isabelle, "incineroar" : chars.incineroar, "incin" : chars.incineroar, "miibrawler" : chars.miibrawler, "brawler" : chars.miibrawler, "miiswordfighter" : chars.miiswordfighter, "swordfighter" : chars.miiswordfighter, "miigunner" : chars.miigunner, "gunner" : chars.miigunner, "piranhaplant" : chars.piranhaplant, "plant" : chars.piranhaplant, "joker" : chars.joker, "hero" : chars.hero, "banjo&kazooie" : chars.banjokazooie, "banjoandkazooie" : chars.banjokazooie, "banjo" : chars.banjokazooie, "terry" : chars.terry, "byleth" : chars.byleth, "minmin" : chars.minmin, "steve" : chars.steve, "sephiroth" : chars.sephiroth, "seph" : chars.sephiroth, "pyra" : chars.pyra, "mythra" : chars.mythra}
moveset = {"jab" : moveset.jab, "ftilt" : moveset.ftilt, "forwardtilt" : moveset.ftilt, "utilt" : moveset.utilt, "uptilt" : moveset.utilt, "dtilt" : moveset.dtilt, "downtilt" : moveset.dtilt, "dashattack" : moveset.dashattack, "fsmash" : moveset.fsmash, "forwardsmash" : moveset.fsmash, "usmash" : moveset.usmash, "upsmash" : moveset.usmash, "dsmash" : moveset.dsmash, "downsmash" : moveset.dsmash, "neutralb" : moveset.neutralb, "upb" : moveset.upb, "upspecial" : moveset.upb, "sideb" : moveset.sideb, "sidespecial" : moveset.sideb, "downb" : moveset.downb, "downspecial" : moveset.downb, "grab" : moveset.grab, "dashgrab" : moveset.dashgrab, "pivotgrab" : moveset.pivotgrab, "pummel" : moveset.pummel, "forwardthrow" : moveset.fthrow, "fthrow" : moveset.fthrow, "backthrow" : moveset.bthrow, "bthrow" : moveset.bthrow, "upthrow" : moveset.uthrow, "uthrow" : moveset.uthrow, "downthrow" : moveset.dthrow, "dthrow" : moveset.dthrow, "neutralair" : moveset.nair, "neutralaerial" : moveset.nair, "nair" : moveset.nair, "forwardair" : moveset.fair, "forwardaerial" : moveset.fair, "fair" : moveset.fair, "backair" : moveset.bair, "backaerial" : moveset.bair, "bair" : moveset.bair, "upair" : moveset.uair, "upaerial" : moveset.uair, "uair" : moveset.uair, "downair" : moveset.dair, "downaerial" : moveset.dair, "dair" : moveset.dair, "ledgegrab" : moveset.ledgegrab, "ledgehang" : moveset.ledgehang, "ledgeattack" : moveset.ledgeattack, "edgeattack" : moveset.ledgeattack, "getupattack" : moveset.ledgeattack, "tripattack" : moveset.tripattack, "floorattack" : moveset.floorattackgeneric, "rollforward" : moveset.rollforward, "froll" : moveset.rollforward, "rollf" : moveset.rollforward, "rollback" : moveset.rollback, "broll" : moveset.rollback, "rollb" : moveset.rollback}
# These dicts are for aliases. For example, you can do !doc or !drmario, with ftilt or forwardtilt

def fix_string(string): # Remove characters that aren't okay for mysql
	return string.strip().replace("--", "").replace("—", "-").encode(encoding="ascii", errors="replace").decode(encoding="ascii", errors="replace")
	# From what I can tell, yes, this is necessary. I'm sorry.
	# Shoutouts to Donkey Kong's UpB, which is listed as being active on ¯\_(ツ)_/¯
	# Also, many moves have attributes that aren't empty, but are listed as
	# '--', but we don't need to store those since they're empty.
	# You can remove that replace() and store them if you really want to
	# know that Kirby's ftilt has no landing lag

def get_db_connection(): # Return a mysql connection
	return MySQLdb.connect(host="myhost", db="mydb", user="myuser", passwd=my_keys.db_pass) 
						  # Replace with your own credentials!

# This command is meant to be run before the first time using
# the bot and after every game update. It everything from
# ultimateframedata.com and puts it in a mysql database. It 
# might take a while. It only takes about a minute for me on
# a Pi, so it can't be too bad
@bot.command(name="ssbucache")
async def ssbu_reload_command(ctx, *args):
	async with aiohttp.ClientSession() as session:
		db = get_db_connection()
		cursor = db.cursor()
		url = "https://ultimateframedata.com"
		async with session.get(url) as response:
			homepage = await response.text() # Get the home page
		homesoup = BeautifulSoup(homepage, "html.parser")
		# Iterate through all the characters in the game
		for x in homesoup.find_all("div", class_=re.compile("charactericon *")):
			if not x.a["title"] == "Stats": # We don't really want that page
				char = fix_string(x.a["href"]) # Character from the page name
				if char.startswith("/"):
					char = char[1:]
				if char.endswith(".php"):
					char = char[:len(char)-4]

				charpage = url + x.a["href"]
				async with session.get(charpage) as response:
					charpage = await response.text() # Get the character's page
				charsoup = BeautifulSoup(charpage, "html.parser")
				cursor.execute("CREATE OR REPLACE TABLE {0} (movename VARCHAR(96), hitboximg TEXT, PRIMARY KEY(movename));".format(char))
				# Iterate through character x's moveset
				for y in charsoup.find_all("div", class_="movecontainer"):
					moveset_dict = {} # This will contain all the attributes
					# Iterate through the move's attributes
					for z in y.children:
						try:
							if fix_string(z.text):
								moveset_dict["".join(z.attrs["class"])] = fix_string(z.text)
								cursor.execute("ALTER TABLE " + char + " ADD COLUMN IF NOT EXISTS ({0} TEXT)".format("".join(z.attrs["class"])))
						except (AttributeError, KeyError): # This didn't have text and/or class, ignore it
							pass
					if moveset_dict:
						cursor.execute("INSERT INTO " + char + " (" + ", ".join(moveset_dict.keys()) + ") VALUES %s;", [list(moveset_dict.values())])
						try:
							hitboximg = ""
							for i in y.find_all("a", class_="hitboximg"): # Iterate through the hitbox images,
							                                              # we want all of them for later. If
							                                              # we didn't iterate, we would only
							                                              # keep the first one.
								hitboximg += "{0}\n".format(i.attrs["data-featherlight"])
							cursor.execute("UPDATE " + char + " SET hitboximg = %s WHERE movename = %s", [hitboximg, moveset_dict["movename"]])
						except AttributeError: # This could happen if there is no image
								pass
		await send_message(ctx, "done") # We're still alive!
		cursor.close()

# The command for getting info from the database and
# using that in a discord embed. Aliases are the key
# words you can use to invoke it, so character names
# will work.
@bot.command(aliases=list(ssbu_chars))
async def character_command(ctx, *args):
	char = ctx.invoked_with.lower()
	prettychar = char.replace("_", " ").capitalize() # This is used if we don't have a pretty
	                                                 # name for the character. Will be used when
	                                                 # new characters are added, but before this
	                                                 # bot is updated to include their name
	arguments = ctx.message.content.split()
	arguments.pop(0)
	arguments = "".join(arguments).replace("%", "") # Replacing % because it's a wildcard to mysql
	if char in ssbu_chars: # If the character has an entry here, use it. It's a prettier name anyway
		prettychar = ssbu_chars[char]
		char = ssbu_chars[char].replace(" ", "_").replace(".", "").replace("&", "and").replace("-", "_").lower()
	if not arguments:
		await send_message(ctx, "<https://ultimateframedata.com/{0}.php>".format(char))
	db = get_db_connection()
	cursor = db.cursor()
	if arguments in moveset: # If what the user asked for matches the
	                         # moveset list, use that instead.
		query = "%{0}%".format(moveset[arguments])
	else:
		query = "%{0}%".format(arguments)
	cursor.execute("SELECT * FROM " + char + " WHERE movename LIKE %s", [query]) # This matches everything that contains what the user asked for.
	                                                                             # For example, '!mario a' matches every move with the letter 'a'
	                                                                             # anywhere in the movename.
	values = cursor.fetchall() # Everything the query returned
	cursor.execute("DESC {0};".format(char))
	columns = cursor.fetchall() # Now the column names

	for v in values: # Iterate through every match
		output = "" # Will be sent to Discord
		title = "move" # Embed title
		image_url = [] # Image link. If it turns out there is no image, this will remain empty
		for value, column in zip(v, columns): # Iterate through the move attributes
			if value:
				if not column[0] in ["movename", "hitboximg"]:
					if column[0] in attributes:
						output += "\n" + attributes[column[0]].format(value.replace("*", "\*"))
					else:
						output += "\n**{0}:** {1}".format(column[0], value.replace("*", "\*"))
				elif column[0] == "movename":
					title = "**{0}** - **{1}**".format(prettychar, value)
				elif column[0] == "hitboximg":
					for i in value.splitlines():
						image_url.append("https://ultimateframedata.com/" + i.replace(" ", "%20"))
		for i in image_url: # Some moves have multiple images but share the same attributes, so send them like that
			await send_message(ctx, embed=discord.Embed(title=title, description=output, url=i).set_image(url=i))
	cursor.close()

@bot.command(name="framedata")
async def framedata_command(ctx):
	await send_message(ctx, "<https://ultimateframedata.com>")

bot.run(my_keys.discord)
