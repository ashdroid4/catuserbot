pip install nekos.py
import nekos

@bot.on(admin_cmd(pattern="neko ?(.*)"))
async def (nekos):
  print(nekos.cat())
