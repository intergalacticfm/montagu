import random

from sopel.module import commands, example

userMachines = {}

REELS = [
    [
        ":cherries:",
        ":peach:",
        ":7-11:",
        ":ironcross:",
        ":mc:",
        ":money_with_wings:",
        ":grapes:",
        ":reveal1:"
    ],
    [
        ":cherries:",
        ":peach:",
        ":7-11:",
        ":ironcross:",
        ":mc:",
        ":money_with_wings:",
        ":grapes:",
        ":reveal2:"
    ],
    [
        ":cherries:",
        ":peach:",
        ":7-11:",
        ":ironcross:",
        ":mc:",
        ":money_with_wings:",
        ":grapes:",
        ":reveal3:"
    ]
]


def register_hold(user_machine, hold):
    if user_machine['spinsLeft'] < 3:
        reel_index = int(hold[1])
        if reel_index < 4:
            user_machine['reels'].get(reel_index)['hold'] = True
            user_machine['holding'] = True


def spin_reel(user_machine, reel_index):
    reel = user_machine['reels'].get(reel_index)

    if not reel['hold']:
        reel['symbol'] = random.choice(REELS[reel_index - 1])


def winning(user_machine) -> bool:
    return user_machine['reels'].get(1)['symbol'] == user_machine['reels'].get(2)['symbol'] == \
           user_machine['reels'].get(3)['symbol'] or \
           (user_machine['reels'].get(1)['symbol'] == ':reveal1:' and user_machine['reels'].get(2)[
               'symbol'] == ':reveal2:' and user_machine['reels'].get(3)['symbol'] == ':reveal3:')


@commands('s')
@commands('S')
@commands('spin')
@commands('spinnit')
@commands('ד')
@example('.s')
def slots(bot, trigger):
    """.spro"""
    reply = ""
    user_machine = initialize_user_machine(trigger)
    if not trigger.group(2) and not user_machine['holding']:
        reset_spins(user_machine)

    if trigger.group(3):
        register_hold(user_machine, trigger.group(3))

    if trigger.group(4):
        register_hold(user_machine, trigger.group(4))

    if trigger.group(5):
        bot.reply("You can't hold more than two reels")
        return

    spin_reel(user_machine, 1)
    spin_reel(user_machine, 2)
    spin_reel(user_machine, 3)
    reply += ('%s%s - %s%s - %s%s' % (
        user_machine['reels'].get(1)['symbol'], '*' if user_machine['reels'].get(1)['hold'] else '',
        user_machine['reels'].get(2)['symbol'], '*' if user_machine['reels'].get(2)['hold'] else '',
        user_machine['reels'].get(3)['symbol'], '*' if user_machine['reels'].get(3)['hold'] else ''))

    if winning(user_machine):
        reset_spins(user_machine)
        reply += ' WIN WIN WIN'
    else:
        register_spin(user_machine)
        if user_machine['holding']:
            if user_machine['spinsLeft'] == 0:
                reply += ' nothing! Resetting holds'
                reset_spins(user_machine)
            else:
                reply += ' Holding! Spins left %s' % user_machine['spinsLeft']

    bot.reply(reply)


def initialize_user_machine(trigger):
    nick = trigger.nick
    userMachines[nick] = userMachines.get(nick, {"spinsLeft": 3,
                                                 "holding": False,
                                                 "reels": {1: {"hold": False, "symbol": ""},
                                                           2: {"hold": False, "symbol": ""},
                                                           3: {"hold": False, "symbol": ""}}})
    user_machine = userMachines[nick]
    return user_machine


def register_spin(user_machine) -> int:
    user_machine['spinsLeft'] -= 1
    return user_machine['spinsLeft']


def reset_spins(user_machine):
    user_machine['spinsLeft'] = 3

    if user_machine['holding']:
        user_machine['reels'].get(1)['hold'] = False
        user_machine['reels'].get(2)['hold'] = False
        user_machine['reels'].get(3)['hold'] = False
        user_machine['holding'] = False
