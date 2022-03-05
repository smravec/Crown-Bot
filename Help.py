import discord

main_chat_channel = None
main_db_channel = None
formated_message = None

# Commands
commands_help = [ ":crown: **All features of Crown Bot** :crown:",
f"**1** !status help - learn more about how to change status message of bot",
f"**2** !warns help - learn more about how to set and delete warns (only for admins)",
f"**3** !manage chat help - learn more about some functions for chat moderation (only for admins)"
]

status_commands_help = [ f"**1** !status text text_you_want_to_change_the_status_to - changes the status text",
f"**2** !status type type_of_the_activity - changes the type of status , replace type_of_the_activity with one of these (Play, Compete, Listen, Watch)"]


warn_commands_help = [ f"**1** !warn name warn_message - gives a warn to specified person",
f"**2** !warnlist name - displays all warnings for specified person",
f"**3** !delwarn name number - deletes the warn of person with specified number (you can get all the numbers by using warnlist command)"
]

manage_chat_commands_help = [f"**1** !delmessages number_how_many - deletes last x messages in channel this command is used"]