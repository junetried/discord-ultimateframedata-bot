# discord-ultimateframedata-bot
Scrapes [Ultimate Frame Data](https://ultimateframedata.com/) for GIFs of character hitboxes. A Discord bot is required for this; you can make one at the [Discord Developer Portal](https://discord.com/developers/applications).

The bot prefix is `!` and can be activated by using one of the character aliases found in the `ssbu_chars` dictionary followed optionally by one of the move aliases found in the `moveset` dictionary. In short:
* `!mario jab` gives you Mario's jab.
* `!mario` gives you [Mario's page on Ultimate Frame Data](https://ultimateframedata.com/mario.php).

Some moves aren't meant to have animated GIFs (like Trainer's down special). Some move commands won't show all versions of the move, because the name does not contain the keywords that are searched for. (like Donkey Kong's aerial down special or Little Mac's KO punch).

This should hopefully be easy enough to reuse for other, larger projects if you wish.
