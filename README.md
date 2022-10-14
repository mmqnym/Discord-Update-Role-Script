# Discord role update script

## Set up
- You have to go [here](https://discord.com/developers/applications) first to get the `token` of the bot,  and select `SERVER MEMBERS INTENT` in `Privileged Gateway Intents` and `bot`, `applications.commands` two `SCOPES`, also `Manage Roles` `PERMISSIONS`.
- Fill in your settings in `configs.json`, including the role ids you want to add and delete.
- Run script!

``` sh
cd <folder>
pip install -r requirements.txt
python app.py
```

## Commands

- /update roles
This command can update role(s) of the server members.

- /reload lists
This command reloads the lists of role(s) to update.

## LICENSE
[MIT](LICENSE)
