import random

from sopel.module import commands, example

userMachines = {}

stats = {
    "wins": 0,
    "jackpot": 0,
    "spins": 0
}

REELS = [
    [
        ":pa:",
        ":ifm:",
        ":mc:",
        ":cbs:",
        ":df:",
        ":tdm:",
        ":hotmix:",
        ":viewlexx:",
        ":reveal1:"
    ],
    [
        ":na:",
        ":ifm:",
        ":mc:",
        ":cbs:",
        ":df:",
        ":tdm:",
        ":hotmix:",
        ":viewlexx:",
        ":reveal2:"
    ],
    [
        ":ma:",
        ":ifm:",
        ":mc:",
        ":cbs:",
        ":df:",
        ":tdm:",
        ":hotmix:",
        ":viewlexx:",
        ":reveal3:"
    ]
]


def register_hold(user_machine, hold):
    if user_machine['spinsLeft'] < 4:
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
           special_win(user_machine, ':reveal1:', ':reveal2:', ':reveal3:') or \
           special_win(user_machine, ':pa:', ':na:', ':ma:') or \
           special_win(user_machine, ':pa:', ':na:', ':reveal3:') or \
           special_win(user_machine, ':viewlexx:', ':na:', ':mc:') or \
           special_win(user_machine, ':cbs:', ':df:', ':tdm:') or \
           special_win(user_machine, ':cbs:', ':tdm:', ':df:') or \
           special_win(user_machine, ':df:', ':tdm:', ':cbs:') or \
           special_win(user_machine, ':df:', ':cbs:', ':tdm:') or \
           special_win(user_machine, ':tdm:', ':cbs:', ':df:') or \
           special_win(user_machine, ':tdm:', ':df:', ':cbs:')


def special_win(user_machine, reel1_, reel2_, reel3_) -> bool:
    return (user_machine['reels'].get(1)['symbol'] == reel1_ and user_machine['reels'].get(2)[
        'symbol'] == reel2_ and user_machine['reels'].get(3)['symbol'] == reel3_)


@commands('s')
@commands('S')
@commands('spin')
@commands('spinnit')
@commands('ד')
@example('.s')
def slots(bot, trigger):
    """.s"""
    reply = ""
    user_machine = initialize_user_machine(trigger)
    if not trigger.group(2) and not user_machine['holding']:
        reset_spins(user_machine)

    if trigger.group(3):
        if trigger.group(3) == 'stats':
            bot.reply("Total of all Spins: {} Wins: {}".format(stats['spins'], stats['wins']))
            return
        if trigger.group(3) == 'jackpot':
            bot.reply("Jackpot is loaded with {}k".format(stats['jackpot']))
            return
        else:
            register_hold(user_machine, trigger.group(3))

    if trigger.group(4):
        register_hold(user_machine, trigger.group(4))

    if trigger.group(5):
        bot.reply("You can't hold more than two reels")
        return

    spin_reels(user_machine)

    reply += ('%s%s - %s%s - %s%s' % (
        user_machine['reels'].get(1)['symbol'], '*' if user_machine['reels'].get(1)['hold'] else '',
        user_machine['reels'].get(2)['symbol'], '*' if user_machine['reels'].get(2)['hold'] else '',
        user_machine['reels'].get(3)['symbol'], '*' if user_machine['reels'].get(3)['hold'] else ''))

    if winning(user_machine):
        stats['wins'] += 1
        reset_spins(user_machine)
        reply += ' WIN WIN WIN {} K'.format(stats['jackpot'])
        stats['jackpot'] = 0
    else:
        register_spin(user_machine)
        if user_machine['holding']:
            if user_machine['spinsLeft'] == 0:
                reply += ' nothing! Resetting holds'
                reset_spins(user_machine)
            else:
                reply += ' Holding! Spins left %s' % user_machine['spinsLeft']

    bot.reply(reply)


def spin_reels(user_machine):
    stats['spins'] += 1
    stats['jackpot'] += 1
    spin_reel(user_machine, 1)
    spin_reel(user_machine, 2)
    spin_reel(user_machine, 3)


def initialize_user_machine(trigger):
    nick = trigger.nick
    userMachines[nick] = userMachines.get(nick, {"spinsLeft": 4,
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
    user_machine['spinsLeft'] = 4

    if user_machine['holding']:
        user_machine['reels'].get(1)['hold'] = False
        user_machine['reels'].get(2)['hold'] = False
        user_machine['reels'].get(3)['hold'] = False
        user_machine['holding'] = False
