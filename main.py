import discord
from blackJack import playerHand,dealerHand,findTotal,dealCard,findWinner,blackJackNumber,restartGame,generateCard,dealAll
from discord.ext import commands

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async  def on_ready():
    print("bot is ready")

#Creates how the Menu will look like
class Menu(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="hit",style=discord.ButtonStyle.grey)
    async def hit(self, interaction: discord.Interaction, button: discord.ui.Button):
        dealCard(playerHand)
        if findTotal(playerHand) == blackJackNumber:
            await interaction.response.send_message(f"The dealer had {dealerHand} for a total of {findTotal(dealerHand)} and you had {playerHand} for a total of {findTotal(playerHand)}. The winner is you")
            restartGame()
            self.stop()
        elif findTotal(playerHand) > blackJackNumber:
            await interaction.response.send_message(f"You busted with {findTotal(playerHand)}.The winner is the Dealer")
            restartGame()
            self.stop()
        else:
            await interaction.response.edit_message(content = f"The dealer has {dealerHand[0]} and ?,You have{playerHand} for a total of {findTotal(playerHand)}")

    @discord.ui.button(label="stand",style=discord.ButtonStyle.grey)
    async def stand(self, interaction: discord.Interaction, button: discord.ui.Button):
        if blackJackNumber - findTotal(dealerHand) > blackJackNumber - findTotal(playerHand):
            await interaction.response.send_message(f"The dealer had {dealerHand} for a total of {findTotal(dealerHand)} and you had {playerHand} for a total of {findTotal(playerHand)}. The winner is you")
        elif blackJackNumber - findTotal(dealerHand) < blackJackNumber - findTotal(playerHand):
            await interaction.response.send_message(f"The dealer had {dealerHand} for a total of {findTotal(dealerHand)} and you had {playerHand} for a total of {findTotal(playerHand)}. The winner is the dealer")
        restartGame()
        self.stop()


@bot.command()
async def bj(ctx):
    generateCard(4)
    dealAll()
    view = Menu()
    if findTotal(playerHand) == blackJackNumber:
        await ctx.reply(f"You got a black jack! You won!")
        restartGame()
    elif findTotal(dealerHand) == blackJackNumber:
        await ctx.reply(f"The dealer got a black jack! The Dealer won")
        restartGame()
    elif findTotal(dealerHand) > blackJackNumber:
        await ctx.reply(f"The dealer busted! You won.")
        restartGame()
    else:
        await ctx.reply(f"The dealer has {dealerHand[0]} and ?,"
                        f"You have{playerHand} for a total of {findTotal(playerHand)}", view=view)

bot.run("")#add your discord token
