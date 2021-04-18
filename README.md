# discord-ultimateframedata-bot
Scrapes [Ultimate Frame Data](https://ultimateframedata.com/) for GIFs of character hitboxes. A Discord bot is required for this; you can make one at the [Discord Developer Portal](https://discord.com/developers/applications).

The bot prefix is `!` and can be activated by using one of the character aliases found in the `ssbu_chars` dictionary followed optionally by one of the move aliases found in the `moveset` dictionary. In short:
* `!mario jab` gives you Mario's jab.
* `!mario` gives you [Mario's page on Ultimate Frame Data](https://ultimateframedata.com/mario.php).

Some moves aren't meant to have images (like Trainer's down special). Some move commands won't show all versions of the move, because the name does not contain the keywords that are searched for (like Donkey Kong's aerial down special or Little Mac's KO punch). You can get around this if you know the name it goes by (you can show Mac's KO punch with `!mac punch` or `!mac k.o.`). 

This should hopefully be easy enough to reuse for other, larger projects if you wish.

## Dependencies
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), to scrape the web
* [aiohttp](https://pypi.org/project/aiohttp/), async http client
* [discord.py](https://pypi.org/project/discord.py/) - it's a discord bot
* A [Discord bot](https://discord.com/developers/applications) already set up and usable
* [mysqlclient](https://pypi.org/project/mysqlclient/), used to store the data scraped
* An SQL database, I'm using mariadb without issue

## Setup
Before running the bot, verify you have all of the dependencies installed. BS4, aiohttp, and mysqlclient are likely in many distro default repositories. Otherwise, you can install them with pip3. Create a file in the same directory as the bot called `my_keys.py`. In it, you should set two strings: `discord` should be your Discord API key, and `db_pass` should be the password to the database user you want to use. This user needs permission to create tables and alter the data inside. Then, edit [the connect line](https://github.com/EthanWeegee/discord-ultimateframedata-bot/blob/main/bot.py#L167) and insert your own credentials.

Before unleashing the bot into production, you must run `!ssbucache` to populate the database. This could take a while, but likely won't. For reference, it takes roughly one minute on my Pi 4B with an SSD. After that's done, you're all good! It should be working now.

When a new update to Ultimate releases, and after the Ultimate Frame Data website updates, you need to run this command again to update the database.
