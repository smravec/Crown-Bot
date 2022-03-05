from asyncio import events
from asyncio.tasks import wait_for
import asyncio
from threading import main_thread
import discord
from discord import activity
from discord.ext.commands.errors import NoEntryPointError
from discord.utils import get
from emoji.core import demojize, emojize

from Warns import *
from Other import *
from Help import *
from Setup import *
from config import *

def Main_function():
    Bot_token = your_bot_token

    intents = discord.Intents.all()
    intents.members = True
    intents.messages = True

    client = discord.Client(intents = intents)

    @client.event
    async def on_message(message):
        formated_message = message.content.split(" ")
        
        if message.channel == main_chat_channel and message.author.bot != True:

            # ONLY FOR ADMINS
            # These commands can use only ppl with role admin
            # Can only be used in main chat channel
                
            # WARNS PART
            # Admins can add, remove or view all the warns of person
            if formated_message[0] == "!warn" and await check_role(message.author.roles, admin_role_id) :
                warn_formated = await format_warn_message(formated_message)
                await message.channel.send(f"warned {warn_formated[0]} {warn_formated[1]}")
                await save_warn_to_db(warns_db_channel, how_many_current_warns, message.channel, warn_formated)
                await refresh_variables("warn")

            elif formated_message[0] == "!warnlist":
                await count_warns_of_person(formated_message[1].replace("!", ""), "display", await fetch_history_of_channel(warns_db_channel, how_many_current_warns), message.channel)
                await refresh_variables("warn")

            elif formated_message[0] == "!delwarn" and await check_role(message.author.roles, admin_role_id) :
                await delwarn(formated_message[1].replace("!", ""), formated_message[2], how_many_current_warns, warns_db_channel)
                await refresh_variables("warn")
                await message.channel.send(f"warn deleted")

            # CHAT MANAGMENT PART
            # Admins can manage chat with this command, currently just delete last x messages function is available
            elif formated_message[0] == "!delmessages" and await check_role(message.author.roles, admin_role_id) :
                await del_messages(formated_message[1], message.channel)
                await message.channel.send(f"deleted {formated_message[1]} messages")

            # FOR REGULAR USERS PART
            # These commands can use anyone who is not bot user on the server
            # Can only be used in main chat channel
                
            # UI PART
            # All current bot functions with descriptions what they do
            elif message.content == f"!help":
                for msg in commands_help:
                    await message.channel.send(msg)
            
            elif message.content == f"!warns help":
                for msg in warn_commands_help:
                    await message.channel.send(msg)

            elif message.content == f"!status help":
                for msg in status_commands_help:
                    await message.channel.send(msg)

            elif message.content == f"!manage chat help":
                for msg in manage_chat_commands_help:
                    await message.channel.send(msg)
            
            # STATUS PART
            # Users can change bot status with this command
            elif formated_message[0] == "!status":

                if formated_message[1] == "text":
                    status_text_message = await format_status_message(formated_message)
                    await set_status( status_text_message[1], status_type.content)
                    await status_text.edit(content = status_text_message[1])
                    await refresh_variables("status")

                elif formated_message[1] == "type":
                    await set_status(status_text.content, formated_message[2])
                    await status_type.edit(content = formated_message[2])
                    await refresh_variables("status")

    @client.event
    async def on_ready():
        await get_channels()
        
        if first_time_setup == True:
            await first_time_setup_func(main_db_channel, warns_db_channel)
        
        else:
            await refresh_variables("all")
            await set_status(status_text.content, status_type.content)
            print("Crown Bot is online")

    # General Functions
    async def get_channels():
        global main_chat_channel, warns_db_channel, main_db_channel

        main_chat_channel = await client.fetch_channel(main_chat_channel_id)
        warns_db_channel = await client.fetch_channel(warns_db_channel_id)
        main_db_channel = await client.fetch_channel(main_db_channel_id)

    async def refresh_variables(which_variable_refreshing):
        global how_many_current_warns, status_text, status_type

        if which_variable_refreshing == "warn":
            how_many_current_warns = await warns_db_channel.fetch_message(how_many_current_warns_id)

        elif which_variable_refreshing == "status":
            status_text = await main_db_channel.fetch_message(status_text_id)
            status_type = await main_db_channel.fetch_message(status_type_id)

        else:
            how_many_current_warns = await warns_db_channel.fetch_message(how_many_current_warns_id)
            status_text = await main_db_channel.fetch_message(status_text_id)
            status_type = await main_db_channel.fetch_message(status_type_id)

    async def fetch_history_of_channel(channel, kolko_sprav):
        return await channel.history(limit = int(kolko_sprav.content)).flatten()

    # Status Functions
    async def set_status(status, status_type):

        if status_type == "Play":
            await client.change_presence(activity=discord.Game(name = status))

        elif status_type == "Listen":
            await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = status))

        elif status_type == "Watch":
            await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = status))

        elif status_type == "Compete":
            await client.change_presence(activity = discord.Activity(type = discord.ActivityType.competing, name = status))    

    client.run(Bot_token)

Main_function()