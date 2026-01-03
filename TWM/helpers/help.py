import discord

def get_help(bot):
    cogs_list = bot.cogs.keys()
    sorted_cogs_list = sorted(cogs_list, key=str.lower)
    for n in sorted_cogs_list:
        if bot.get_cog(n).get_commands():
            filtered_cogs_list = filtered_cogs_list.append(n)
    cogs_message = "\n".join(filtered_cogs_list)
    return cogs_message