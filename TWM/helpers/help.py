import discord

def get_help(bot):
    cogs_list = bot.cogs.keys()
    sorted_cogs_list = sorted(cogs_list, key=str.lower)
    filtered_cogs_list = []
    for n in sorted_cogs_list:
        if bot.get_cog(n).get_commands():
            filtered_cogs_list.append(n)
    cogs_message = "\n".join(filtered_cogs_list)
    return cogs_message

def get_commands(bot, cog):
    command_list = [c.name for c in cog.get_commands()]
    sorted_command_list = sorted(command_list, key=str.lower)
    command_message = "\n".join(sorted_command_list)
    return command_message

