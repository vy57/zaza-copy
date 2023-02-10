

def copyserver(token, new_server, prefix):
  import discord
  from discord.ext import commands
  import asyncio 
  
  client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)
  
  @client.command()
  async def copyserver(ctx):
    print("a")
    await ctx.message.delete()
    print(f"{ctx.guild.name} isimli sunucu kopyalanıyor...")
    server = await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
  
    for sunucu in client.guilds:
        if f'backup-{ctx.guild.name}' in sunucu.name:
            for kanal in sunucu.channels:
                await kanal.delete()
              
            for kategori in ctx.guild.categories:
                x = await sunucu.create_category(f"{kategori.name}")
              
                for kanall in kategori.channels:
                    if isinstance(kanall, discord.VoiceChannel):
                        await x.create_voice_channel(f"{kanall}")
                    if isinstance(kanall, discord.TextChannel):
                        await x.create_text_channel(f"{kanall}")
            await sunucu.edit(name=new_server)

    for role in ctx.guild.roles[::-1]:
      if role.name != "@everyone":
        await server.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
    print(f"{ctx.guild.name} isimili sunucu {new_server} isimli sunucuya kopyalandı")
  client.run(token, bot=False)