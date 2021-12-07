import random
from sopel.module import commands, example

REEL = [
    ":cherries:",
    ":peach:",
    ":7-11:",
    ":ironcross:",
    ":ironcross:",
    ":ironcross:",
    ":ironcross:",
    ":ironcross:",
    ":mc:",
    ":money_with_wings:",
    ":tumbleweed:"

]

@commands('s')
@commands('D')
@commands('spin')
@commands('spinnit')
@commands('ד')
@example('.s')
def slots(bot, trigger):
    """.s"""
    bot.reply('%s - %s - %s' % (random.choice(REEL),random.choice(REEL),random.choice(REEL)))
