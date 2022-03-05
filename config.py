# Set up Crown Bot

# All the required packages that you need to download are : discord, emoji
# To install run this command in your terminal
# pip install emoji discord

# When new feature is added make sure to do the setup again

# To get id of channel or message enable developer mode in discord

# Paste your token as string below
your_bot_token = ""

# Make 3 different channels and copy their id to the variables below (as int)

# First is main chat channel (the main text channel of your server)
# Paste the id below as int
main_chat_channel_id = 1

# Second is main db channel (channel which bot uses as general db)
# Paste the id below as int
main_db_channel_id = 1

# Third is warn db channel (channel where bot stores all data regarding warn feature)
# Paste the id below as int
warns_db_channel_id = 1

# Next set the variable below to True and run Main.py
# It will send all the required messages to set up dbs into previous channels
first_time_setup = False

# After running Main.py for few seconds terminate it and change variable first_time_setup to False

# Now copy ids of msgs sent into channels during first time setup

# main_db_channel messages

# In this channel should be 2 messages
# First is status text (defaul is Mount & Blade: Warband)

# Paste the id below (as int)
status_text_id = 1

#Second is type of status (default is Play)
status_type_id = 1


# warns_db_channel messages

# In this channel should be 1 message
# First and only message is how many warns db has (default is 0)

# Paste the id below (as int)
how_many_current_warns_id = 1

# Next is making an admin role and pasting the id below
# Users with admin role can use all the features of the bot

# Paste the id below (as int)
admin_role_id = 1

# After that just run Main.py and your bot should be working
# To get all the commands send 
# If you dont want to break the bot dont edit anything outside config.py and also dont send, edit or remove anything in the db channels
# Thanks for using Crown Bot

#67...
#68...
#69