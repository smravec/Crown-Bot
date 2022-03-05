import discord

status_text = None
status_type = None

# Chat managment
async def del_messages(how_many_words_deleting, which_channel):
    await which_channel.purge(limit = int(how_many_words_deleting))

# Check if person has certain role
async def check_role(person_roles, desired_role):

    for role in person_roles:
        if desired_role == role.id:
            
            return True
    return False

# Status
# Format message for status command
async def format_status_message(status_msg):

    text_or_type = status_msg[1]
    status_message1 = ""

    for number_of_words in range(len(status_msg) - 2):
        status_message1 = f"{status_message1} {status_msg[number_of_words + 2]}"

    status = [text_or_type, status_message1]
    
    return status