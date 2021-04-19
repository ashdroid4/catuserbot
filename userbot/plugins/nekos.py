import nekos

@bot.on(admin_cmd(pattern="neko ?(.*)"))
async def cat(nekos):
  print(nekos.cat())
