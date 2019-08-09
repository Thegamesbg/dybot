import discord
from discord import Message, Guild, Member
from discord.ext.commands import Bot
from typing import Optional, Set
from discord.ext import commands

import sys
import traceback
import asyncio

bot = Bot(command_prefix='!')
bot.remove_command('help')

server: Optional[Guild] = None

shiki: Optional[Member] = None

# bot status.

@bot.event
async def on_ready():
    global server
    server = bot.get_guild(448571905524498432)

    global shiki
    shiki = server.get_member(393839495859929089)

    await bot.change_presence(activity=discord.Game(name='with dy & shiki >_<'))
    print('e - nightclub BOT has started working!')

# welcome message

@bot.event
async def on_member_join(member):
    if(member.guild.id == 448571905524498432):
        channel = discord.utils.get(member.guild.channels, name="☆│lounge")
        channel2 = discord.utils.get(member.guild.channels, name="✵│welcome-rules")
        channel3 = discord.utils.get(member.guild.channels, name="∞│roles-menu")
        channel4 = discord.utils.get(member.guild.channels, name="✵│faq")
        await channel.send("Welcome {} to **e nightclub!** You’re the **{}** member. \n\n Make sure to read: {}  |  Roles: {}  |  For help:  {}.".format(member.mention, member.guild.member_count, channel2.mention, channel3.mention, channel4.mention))

# leave message

@bot.event
async def on_member_remove(member):
    if(member.guild.id == 448571905524498432):
        channel = discord.utils.get(member.guild.channels, name="✵│arrivals")
        await channel.send("**{}** has left the server. We now have **{}** members.".format(member.mention, member.guild.member_count))

@bot.event
async def on_message(message: Message):
    if(message.content == "!welcome" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Welcome to e- nightclub__  ⁺˳✧ ༚**", description="- We are so glad to have you join our server! By joining this server you agreed on our rules. \r\n\r\n - We have over 170+ roles, channels and some bots to play different games and much more! \r\n\r\n - Our channels are not aggressively moderated so feel free to join any conversation you like.", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/j6HHIdWsJFuPTPfNlW/giphy.gif")
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
    if(message.content == "!rules" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Server rules__ ⁺˳✧ ༚**", description="__``1``__ • Make sure to Follow **Discord TOS** and **Community Guidelines** (TOS:  ``https://discordapp.com/terms`` | Community Guidelines: ``https://discordapp.com/guidelines``). \r\n\r\n __``2``__ • Keep content in the appropriate channels. This includes only posting NSFW content in NSFW marked channels. \r\n\r\n __``3``__ • No Doxing / Do not leak someone's IP address / Do not share personal information of anyone. \r\n\r\n __``4``__ • Any type of serious harassment [Blackmailing, Hate speech, DM spamming members, etc..]. Will result in a ban. \r\n\r\n __``5``__ • No advertising (Including PM advertisement). \r\n\r\n __``6``__ • Do NOT tell people to kill themselves (even if it's a joke). \r\n\r\n __``7``__ • Do not impersonate other users. Impersonating our staff team or discord staff will result in a permanent ban. \r\n\r\n __``8``__ • Remember that this server is English only! Try to avoid using any other languages so everyone can understand each other and have fun. \r\n\r\n __``9``__ • Respect all staff and follow their instructions. Especially the owners ( dy & scopes ). \r\n\r\n __``10``__ • Do NOT set people up against each other or against STAFF. \r\n\r\n __``11``__ • Respect people's wishes considering revealing their age, face reveal etc. \r\n\r\n __``12``__ • Asking for nudes or for other information is ABSOLUTELY not accepted here and will result in a ban. \r\n\r\n **- Please contact <@495680416422821888> if you have any issues with Staff or the rules posted above.** \r\n\r\n **- Make sure to check <#567371465633169436> if you're new to discord or have any questions.** \r\n\r\n **- Thank you for joining e- nightclub! We hope you have a great stay here!**", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/ZXBS4ZfZKU1EbTXlL8/giphy.gif")
        embed3 = discord.Embed(title="**༚ ✧˳⁺ __Voice Chat rules__ ⁺˳✧ ༚**", description="__``1``__ • Don't ear rape other people with music or with your mic. \r\n\r\n __``2``__ • Do not spam music, let other people play their song. \r\n\r\n __``3``__ • Do not stop the music if there are still others in the voice channel. \r\n\r\n __``4``__ • Do not mic spam, yell or disturb others. \r\n\r\n __``5``__ • Do NOT be toxic or be racist.", color=0xFF93F0)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed1)
    if(message.content == "!faq" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="*__**FAQ**:__*", description="__**How can I level up?**__ \r\n\r\n To level up you have to be active in any channel in the server, avoid spamming. Spamming won't level you up. \r\n\r\n __**Is there a way to get picture perms/embed links?**__ \r\n\r\n Yes there is a way to get these perms, when you reach **level 10+** you'll be able to post pictures or links in <#491366183447298068>. \r\n\r\n __**Someone is advertising in my DMS what do I do?**__ \r\n\r\n Dm a staff member and they'll ban them as soon as possible. \r\n\r\n __**Staff is abusing his perms, what do I do?**__ \r\n\r\n Dm <@303564745565536256> or <@495680416422821888>. \r\n\r\n __**Is there a NSFW channel?**__ \r\n\r\n Yes there is, to get access to the NSFW + shitpost channels you have to get the NSFW role. (can be found in <#491368164370677781>). \r\n\r\n __**Do you guys do giveaways and events?**__ \r\n\r\n Yes we do events and giveaways sometimes. (get the events + giveaway roles in <#491368164370677781> so you don't miss our giveaways and events!) \r\n\r\n __**I want to become a Staff member for e - nightclub , how can I apply?**__ \r\n\r\n You can apply in <#566420979069222912> by typing **!apply** there! Please do not annoy the owners to get Mod/Admin. \r\n\r\n __**I want to apply for a Partner Manager, how can I do that?**__ \r\n\r\n Dm dy#0777. \r\n\r\n __**Where can I shoutout my instagram , snapchat, etc..?**__ \r\n\r\n You can send your snapcode in <#558992750612054036>, for instagram go to <#558992817532436521>.", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/kH73TzZ51Lz0ocgRJR/giphy.gif")
        embed3 = discord.Embed(title="", description="__**Can we be partners?**__ \r\n\r\n Sure! You can be partner with us by messaging dy#0777 or a Partner Manager. \r\n\r\n __**What can I do with the bot money?**__ \r\n\r\n You can bet, buy items, gamble and much more. \r\n\r\n __**How can I get access to <#558991846785679360> & <#558992153393496074> ?**__ \r\n\r\n To get access to one of these channels please make sure to read <#558991108915462164>. However we've got a channel without verification (can be found here <#558992392242331658>.) \r\n\r\n __**How can I play a song in music voice chat?**__ \r\n\r\n Go to <#559063589114216470> and type ``$play [song name or URL]`` │You can also use ``%play [song name or URL]``. \r\n\r\n __**I got banned for no reason, what do I do?**__ \r\n\r\n Simply DM one of the owners **dy#0777 or scopes#9333** and we'll unban you as soon as possible! \r\n\r\n __**Can I get a color?**__ \r\n\r\n Yes, you can pick a color form our colors menu. (check them here <#566212667837120522>). \r\n\r\n __**Someone leaked my pictures, IP, phone number. What do I do?**__ \r\n\r\n DM one of the Staff members and they'll ban them. \r\n\r\n __**Where can I find the server's leaderboard for levels?**__ \r\n\r\n You can find it here: https://mee6.xyz/leaderboard/448571905524498432 \r\n\r\n __**When was this server created?**__ \r\n\r\n created on 22 May 2018. \r\n\r\n __**Is this a dating server?**__ \r\n\r\n Nope, this is a chill server to talk to new people and make friends. However we're not going to do anything if you date here. This is not our business.", color=0xFF93F0)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed3)
    if(message.content == "!staff" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**__Staff Members:__**", description="☆ - Owners: dy <@495680416422821888> | scopes <@303564745565536256>. \r\n\r\n ☆ - Co Owners: Blitzzy <@322362178306965504> | Djimi <@322361798625853441> | Ave <@340478577906548737> | Ashton <@335445790808080385> | Blury <@315076865171783682> \r\n\r\n ☆ - Head Admins: N/A \r\n\r\n ☆ - Admins: Quenty <@243218955014111232> | Lil Akame <@464447422249304084> \r\n\r\n ☆ - Mods: Poppy <@454036738885681162> | Sammy <@541048817307353095>", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/Xy1debdAWrNLK3cnHk/giphy.gif")
        embed3 = discord.Embed(title="**__Perm invite links:__**", description="🔗 Perm invite link: https://discord.gg/UrbUgWH \r\n\r\n 🔗 You can also use this link: https://invite.gg/enightclub \r\n\r\n Last updated: 08/05   /2019", color=0xFF93F0)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed3)
    if(message.content == "!verification" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ Verification ⁺˳✧ ༚**", description="✧ - Post selfie in <#558991375681716256> with 'e- Nightclub and your discord username' on a piece of paper to get verified! \r\n\r\n ✧ - Verified role gives you access to <#558992153393496074> or <#558991846785679360> depends on your gender. \r\n\r\n ✧ - **NOTE:** You cannot use a photo that you took for another server. \r\n\r\n You can also Dm me or dm a staff member to role you verified if you don't want to post your face in <#604506916051484683>.", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        await message.channel.send(embed=embed1)

 
# dy  & shiki commands

  #  if "xxx" in message.content:
     #   await message.author.send("Hi")


  #  if len(message.mentions) > 0:
    #    if message.mentions[0].id == 393839495859929089:
     #       try:
     #           await message.author.send("Hey there, {}! \nPlease don't abusively mention the Devs without a reason. If you want to just talk to them, it's okay, but don't don it oftenly without a real reason. But while you're here... \n\n Are you looking for **cheap** and sometimes **free** __bot developing and hosting__? Our **custom bot**, <@593090256560193549> was made by the user you just pinged, <@393839495859929089>. \n\n If you're interesting in having a custom bot like this one, **DM <@393839495859929089>** and we'll talk about it there. \n\n > This automatic action was fired because you pinged either the Bot Coder role or <@393839495859929089>.".format(message.author.mention))
      #      except:
       #         print("worked fine with no errors at all *cough*")

    if shiki in message.mentions:
        await message.author.send(f"Hey there, {message.author.mention}! \nPlease don't abusively mention the Devs without a reason. If you want to just talk to them, it's okay, but don't don it oftenly without a real reason. But while you're here... \n\n Are you looking for **cheap** and sometimes **free** __bot developing and hosting__? Our **custom bot**, <@593090256560193549> was made by the user you just pinged, {shiki.mention}. \n\n If you're interesting in having a custom bot like this one, **DM {shiki.mention}** and we'll talk about it there. \n\n > This automatic action was fired because you pinged either the Bot Coder role or {shiki.mention}.")

    await bot.process_commands(message)

# - Fun commands:
@bot.command()
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar of {}".format(user))
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@avatar.error
async def avatar_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="While trying to execute the command '!avatar', I ran in an error. Description:", description="You didn't enter a valid user/user id. Try again.")
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Avatar of {}".format(ctx.message.author))
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def av(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar of {}".format(user))
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@av.error
async def av_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="While trying to execute the command '!av', I ran in an error. Description:", description="You didn't enter a valid user/user id. Try again.")
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Avatar of {}".format(ctx.message.author))
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Admin commands: 

@bot.command()
@commands.has_any_role("Co Owner ‧₊˚ ༄", "$ dy", "scopes", "Bot Coder")
async def lockdown(ctx):
	enightclubrole = discord.utils.get(ctx.message.guild.roles, name="@everyone")
	check = ctx.message.channel.overwrites_for(enightclubrole)
	if check.send_messages == False:
		await ctx.send(":warning: **e - nightclub** | **Lockdown** mode turned __off__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=True)
	elif check.send_messages == True:
		await ctx.send(":warning: **e - nightclub** | **Lockdown** mode turned __on__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=False)
	else:
		await ctx.send(":warning: **e - nightclub** | **Lockdown** mode turned __on__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=False)

@lockdown.error
async def lockdown_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send("{} sorry but this command is for owners, co-owners, and the developer only.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


@bot.command()
@commands.has_any_role("Admin ˚｡☆")
async def ban(ctx, user: discord.Member, *, reason: str = ""):
    if len(reason) == 0:
        await ctx.send("**{}** was __banned__ from **e - nightclub**.\n>> Banned by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got clapped justcuz**".format(user.mention, ctx.message.author.mention))
        try:
            await user.send("You've been banned from **e - nightclub**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
        except:
            await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
    else:
        await ctx.send("**{}** was __banned__ from **e - nightclub**.\n>> Banned by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
        try:
            await user.send("You've been banned from **e - nightclub**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
        except:
            await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
    await user.ban()

@ban.error    
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆")
async def unban(ctx, id: int, *, reason: str = ""):
	#print("I got the user!")
	#print("ID: " + id)
	user = await bot.fetch_user(id)
	if user is None:
		#print("I couldn't find this user!")
		await ctx.send(f"{ctx.message.author.mention}, this user doesn't exist.")
		return
	print("I fetched this user!")
	banEntry = await ctx.message.guild.fetch_ban(user)
	if banEntry is None:
		#print("This user is not banned!")
		await ctx.send(f"{ctx.message.author.mention}, are you sure this user is banned?")
	else:
		if banEntry.reason is None:
			#print("Going without a reason!")
			await ctx.send("**{}** was __unbanned__. \n"
							">> Unbanned by: **{}**\n"
							">> Reason: **who even puts reasons on unban lol**"
							.format(banEntry.user, ctx.message.author.mention))
		else:
			print("Going with a reason!")
			await ctx.send("**{}** was __unbanned__. \n"
							">> Unbanned by: **{}**\n"
							">> Reason: **{}**"
							.format(banEntry.user, ctx.message.author.mention, reason))
		#print("I unbanned the user!")
		await ctx.message.guild.unban(banEntry.user, reason="Ban reason goes here")
		
@unban.error    
async def unban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("{} look now, do i look like a magician? just give me the id of an user and i'll unban them \n example: ``!unban id how did this happen to begin with``".format(ctx.message.author.mention))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to unban? \n example: ``!unban id how did this happen to begin with``".format(ctx.message.author.mention))
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Mod ˚｡⋆")
async def kick(ctx, user: discord.Member, *, reason: str = ""):
    if len(reason) == 0:
        await ctx.send("**{}** was __kicked__ from **e - nightclub**.\n>> Kicked by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got slapped justcuz**".format(user.mention, ctx.message.author.mention))
        try:
            await user.send("You've been kicked from **e - nightclub**. You were kicked by **{}**, and you were kicked for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
        except:
            await ctx.send("I failed to DM {}, so I didn't inform them for their kick. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
    else:
        await ctx.send("**{}** was __kicked__ from **e - nightclub**.\n>> Kicked by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
        try:
            await user.send("You've been kicked from **e - nightclub**. You were kicked by **{}**, and you were kicked for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
        except:
            await ctx.send("I failed to DM {}, so I didn't inform them for their kick. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
    await user.kick()
 
@kick.error    
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("{} look now, do i look like a magician? just mention a user and i'll kick them \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to kick? \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Mod ˚｡⋆", "Chat Moderator")
async def mute(ctx, user: discord.Member, *, reason: str = ""):
    mutedrole = discord.utils.get(ctx.message.author.guild.roles, name="Muted")
    if len(reason) == 0:
        await ctx.send("**{}** was __muted__.\n>> Muted by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got slapped justcuz** \n**This mute won't be removed automatically. Someone has to manually remove it.**".format(user.mention, ctx.message.author.mention))
        try:
            await user.send("You've been muted in **e - nightclub**. You were muted by **{}**, and you were muted for **none (no reason was found)**.\n**This mute won't be removed automatically. Someone has to manually remove it.**\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
        except:
            await ctx.send("I failed to DM {}, so I didn't inform them for their mute. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
    else:
        await ctx.send("**{}** was __muted__.\n>> Muted by: **{}**\n>> Reason: **{}**\n**This mute won't be removed automatically. Someone has to manually remove it.**".format(user.mention, ctx.message.author.mention, reason))
        try:
            await user.send("You've been muted in **e - nightclub**. You were muted by **{}**, and you were muted for **{}**. \n**This mute won't be removed automatically. Someone has to manually remove it.**\n If you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author, reason))
        except:
            await ctx.send("I failed to DM {}, so I didn't inform them for their mute. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
    await user.add_roles(mutedrole)
 
@mute.error    
async def mute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("{} look now, do i look like a magician? just mention a user and i'll kick them \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to kick? \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ˚｡☆", "Mod ˚｡⋆", "Chat Moderator")
async def unmute(ctx, user: discord.Member, *, reason: str = ""):
    mutedrole = discord.utils.get(ctx.message.author.guild.roles, name="Muted")
    if len(reason) == 0:
        await ctx.send("**{}** was __unmuted__. \n>> Unmuted by: **{}**\n>> Reason: **who even puts reasons on unmute lol**".format(user.mention, ctx.message.author.mention))
    else:
        await ctx.send("**{}** was __unmuted__. \n>> Unmuted by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
    await user.remove_roles(mutedrole)

@unmute.error    
async def unmute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("{} look now, do i look like a magician? just mention a user and i'll unmute them \n example: ``!unmute @dy lol begged for unmute``".format(ctx.message.author.mention))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to unmute? \n example: ``!unmute @dy lol begged for unmute``".format(ctx.message.author.mention))
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)


# - BOT LOGIN

bot.run(os.environ.get("token"))
