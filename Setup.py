import discord

async def first_time_setup_func(main_db_channel, warns_db_channel):
    
    await main_db_channel.send("Mount & Blade: Warband")
    await main_db_channel.send("Play")
    await warns_db_channel.send("0")

    print("Function completed now change variable first_time_setup to False and terminate Main.py and continue with setup")
