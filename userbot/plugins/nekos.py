import nekos

@bot.on(admin_cmd(pattern="nekos ?(.*)"))
async def cat(nekos):
  print(nekos.cat())
