Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import dicord
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import dicord
ModuleNotFoundError: No module named 'dicord'
>>> import dicord
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import dicord
ModuleNotFoundError: No module named 'dicord'
>>> import discord
>>> from dicord.ext import commands
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    from dicord.ext import commands
ModuleNotFoundError: No module named 'dicord'
>>> import discord
>>> from discord.ext import commands
>>> 
>>> client = commands.Bot(command_prefix = '?')
>>> 
>>> @client.event
async def on_ready():
	print('Bot is ready.')

	
>>> client.run('NzA0Njg5OTUxNDA4OTE0NTMz.Xqgz3A.VU3fUuQ_KSjhyVFs2RnArnYsZyQ')
Bot is ready.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Traceback (most recent call last):
  File "C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py", line 10, in <module>
    @cliet.event
NameError: name 'cliet' is not defined
>>> 
= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.
Ignoring exception in command _8ball:
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 83, in wrapped
    ret = await coro(*args, **kwargs)
  File "C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py", line 17, in _8ball
    responses- ['As I see it, yes.'
NameError: name 'responses' is not defined

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\bot.py", line 892, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 797, in invoke
    await injected(*ctx.args, **ctx.kwargs)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 92, in wrapped
    raise CommandInvokeError(exc) from exc
discord.ext.commands.errors.CommandInvokeError: Command raised an exception: NameError: name 'responses' is not defined

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Traceback (most recent call last):
  File "C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py", line 12, in <module>
    async def kick(ctx, member : dicord.Member, *, reason=none):
NameError: name 'none' is not defined
>>> 
= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Traceback (most recent call last):
  File "C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py", line 12, in <module>
    async def kick(ctx, member : dicord.Member, *, reason=None):
NameError: name 'dicord' is not defined
>>> 
= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.
Ignoring exception in command kick:
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\bot.py", line 892, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 790, in invoke
    await self.prepare(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 751, in prepare
    await self._parse_arguments(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 670, in _parse_arguments
    transformed = await self.transform(ctx, param)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 516, in transform
    raise MissingRequiredArgument(param)
discord.ext.commands.errors.MissingRequiredArgument: member is a required argument that is missing.
Ignoring exception in command ban:
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\bot.py", line 892, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 790, in invoke
    await self.prepare(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 751, in prepare
    await self._parse_arguments(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 670, in _parse_arguments
    transformed = await self.transform(ctx, param)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 516, in transform
    raise MissingRequiredArgument(param)
discord.ext.commands.errors.MissingRequiredArgument: member is a required argument that is missing.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.
Ignoring exception in command None:
discord.ext.commands.errors.CommandNotFound: Command "bans" is not found
Ignoring exception in command unban:
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 83, in wrapped
    ret = await coro(*args, **kwargs)
  File "C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py", line 21, in unban
    member_name, member_discriminator = member.spli('#')
AttributeError: 'str' object has no attribute 'spli'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\bot.py", line 892, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 797, in invoke
    await injected(*ctx.args, **ctx.kwargs)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 92, in wrapped
    raise CommandInvokeError(exc) from exc
discord.ext.commands.errors.CommandInvokeError: Command raised an exception: AttributeError: 'str' object has no attribute 'spli'
Ignoring exception in command unban:
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 83, in wrapped
    ret = await coro(*args, **kwargs)
  File "C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py", line 21, in unban
    member_name, member_discriminator = member.spli('#')
AttributeError: 'str' object has no attribute 'spli'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\bot.py", line 892, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 797, in invoke
    await injected(*ctx.args, **ctx.kwargs)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 92, in wrapped
    raise CommandInvokeError(exc) from exc
discord.ext.commands.errors.CommandInvokeError: Command raised an exception: AttributeError: 'str' object has no attribute 'spli'

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.
Ignoring exception in command unban:
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 83, in wrapped
    ret = await coro(*args, **kwargs)
  File "C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py", line 26, in unban
    if (user.name, user.discriminator) -- (member_name, member_discriminator):
TypeError: bad operand type for unary -: 'tuple'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\bot.py", line 892, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 797, in invoke
    await injected(*ctx.args, **ctx.kwargs)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 92, in wrapped
    raise CommandInvokeError(exc) from exc
discord.ext.commands.errors.CommandInvokeError: Command raised an exception: TypeError: bad operand type for unary -: 'tuple'

= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.
Ignoring exception in command unban:
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\ext\commands\core.py", line 83, in wrapped
    ret = await coro(*args, **kwargs)
  File "C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py", line 26, in unban
    if (user.name, user.discriminator) -- (member_name, member_discriminator):
TypeError: bad operand type for unary -: 'tuple'

The above exception was the direct cause of the following exception:


= RESTART: C:/Users/Mayo.I/AppData/Local/Programs/Python/Python38-32/Activity bot.py
Bot is ready.
(member) has joined a server.

===== RESTART: C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py ====
Bot is ready.

===== RESTART: C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py ====
Bot is ready.

===== RESTART: C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py ====
Bot is ready.

===== RESTART: C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py ====
Bot is ready.

===== RESTART: C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py ====
Ignoring exception in on_ready
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\client.py", line 312, in _run_event
    await coro(*args, **kwargs)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py", line 8, in on_ready
    await client.change_presence(status=discord.Status.Online, activity=discord.Game('Monitoring activity'))
AttributeError: type object 'Status' has no attribute 'Online'

===== RESTART: C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py ====
Ignoring exception in on_ready
Traceback (most recent call last):
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\lib\site-packages\discord\client.py", line 312, in _run_event
    await coro(*args, **kwargs)
  File "C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py", line 8, in on_ready
    await client.change_presence(status=discord.Status.Idle, activity=discord.Game('Monitoring activity'))
AttributeError: type object 'Status' has no attribute 'Idle'

===== RESTART: C:\Users\Mayo.I\AppData\Local\Programs\Python\Python38-32\avc.py ====
Bot is ready.
