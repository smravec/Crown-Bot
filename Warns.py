import discord
from discord import channel

warns_db_channel = None
how_many_current_warns = None

# Warn help functions
async def format_warn_message(warn):

    name = warn[1].replace("!", "")
    warn_message = warn[2]

    if len(warn) > 3:
        for number_of_words in range(len(warn) - 3):
            warn_message = f"{warn_message} {warn[number_of_words + 3]}"

    warn = [name, warn_message]
    
    return warn


async def update_warns_counter(plus_or_minus , how_many_warns_msg):

    how_many_warns_int = int(how_many_warns_msg.content)

    if plus_or_minus == "plus":
        how_many_warns_int = how_many_warns_int + 1

    elif plus_or_minus == "minus":
        how_many_warns_int = how_many_warns_int - 1

    return how_many_warns_int


async def count_warns_of_person(person, count_or_display, msg_history, logs_channel):
    counter = 0

    # Counts all the warns person has
    for message in msg_history:
        message = message.content.split("---")
        if message[1] == person:
            counter += 1

    # Displays all warns of specific person
    if count_or_display == "display":
        await logs_channel.send(f"{person} has {counter} warns")
        counter1 = len(msg_history) - 1
        
        while counter1 > -1:
            message1  = msg_history[counter1].content.split("---")
            if message1[1] == person:
                await logs_channel.send(f"{message1[0]}. {message1[2]}")

            counter1 -= 1
    
    return counter

# Main warn Functions
async def save_warn_to_db(db_channel , how_many_current_warns_msg , logs_channel , warn):
    channel_history = await db_channel.history(limit = int(how_many_current_warns_msg.content)).flatten()
    count = await count_warns_of_person(warn[0], "count", channel_history, logs_channel) + 1
    
    await db_channel.send(f"{count}---{warn[0]}---{warn[1]}")
    await how_many_current_warns_msg.edit(content = await  update_warns_counter("plus" , how_many_current_warns_msg))           


async def delwarn(person, warn_num , how_many_current_warns_msg , db_channel):
    channel_history = await db_channel.history(limit = int(how_many_current_warns_msg.content)).flatten()
    await how_many_current_warns_msg.edit(content = await update_warns_counter("minus", how_many_current_warns_msg))

    for messages in channel_history:
        message = messages.content.split("---")
        
        if message[0] == warn_num and message[1] == person:
            deleted_message = await db_channel.fetch_message(messages.id)
            await deleted_message.delete()

        elif int(message[0]) > int(warn_num) and message[1] == person:
            msgs = await db_channel.fetch_message(messages.id)
            
            new_num = str(int(message[0]) - 1)
            
            message_to_be_edited = new_num + "---" + message[1] + "---" + message[2]
            await msgs.edit(content = message_to_be_edited)
