import discord
from discord.ext import commands, tasks


class View(discord.ui.View):
    def __init__(self, Titre, Image, Taille, Prix, Url):
        super().__init__()
        
        # Ajoutez un bouton avec l'URL
        self.add_item(discord.ui.Button(label="🗒️Detalles", style=discord.ButtonStyle.url, url=Url))
        self.add_item(discord.ui.Button(label="🛒Comprar", style=discord.ButtonStyle.green, url=Url))

        


# Préfixe pour les commandes du bot
bot_prefix = "!"

# Intents permettant au bot de recevoir des événements comme les messages privés
intents = discord.Intents.default()
intents.messages = True

# Initialisation du bot avec le préfixe et les intents
bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user.name}")

    # Démarrer la tâche qui envoie un message toutes les secondes
    send_message.start()

@tasks.loop(seconds=11)  # Envoyer un message chaque seconde
async def send_message():
    # Récupérer l'objet salon (channel) où vous voulez envoyer le message
    channel_id = 1188464354027372605  # Remplacez par l'ID du salon
    channel = bot.get_channel(channel_id)
    
    if channel:
        with open("Tire_0.txt", "r") as f:
            Titre = f.read()
        with open("Image_0.txt", "r") as f:
            Image = f.read()
        with open("Taille_0.txt", "r") as f:
            Taille = f.read()
        with open("Prix_0.txt", "r") as f:
            Prix = f.read()
        with open("Url_0.txt", "r") as f:
            Url = f.read()
        with open("Seler_0.txt", "r") as f:
            Seller = f.read()
        
        
            
        image_url = Image

        view = View(Titre=Titre, Image=Image, Taille=Taille, Prix=Prix, Url=Url)
        button = discord.ui.Button(label="Clique")
        view.add_item(button)
        
        await channel.send(f">>> [{Titre}]({image_url}) 💸Precio :\n {Prix}€ \n 📏Talla :\n {Taille} \n 👤Vendedor :\n {Seller} \n \n ", view=view)
        


# Lancez le bot avec le token
bot.run("MTE4ODQ0NzYxMjM4MzI2ODkyNA.G0dzn8.YEC6DAFO9sdHMEF6Qcs-cmSmwE0KekEoix0jZ4")
