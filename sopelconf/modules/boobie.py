# -*- coding: utf8 -*-
"""
boobie.py - Sopel boobie Module + more
"""

import random
from sopel.module import commands, example

BOOBS = [
    "(.)(.)",
    "(.) (.)",
    "( . Y . )",
    "( -  )(  - )",
    "( o  )(  o )",
    "(O Y O)",
    "( · )( · )",
    "( \u0E4F Y \u0E4F )",  # ( ๏ Y ๏ )
    "\uFF08\u3002 \u3145  \u3002\uFF09"  # （。 ㅅ  。）
]


@commands('boobs')
@commands('tits')
@commands('titties')
@commands('tieten')
@commands('moobs')
@commands('schloobs')
@commands('bewbs')
@commands('jopen')
@commands('kwarktassen')
@commands('tetten')
@commands('memmen')
@commands('postzakken')
@commands('meloenen')
@example('.boobs')
def boobie(bot, trigger):
    """.boobs"""
    bot.say(random.choice(BOOBS))


PENISES = [
    "8=====)",
    "8====)",
    "8===)",
    "8==)",
    "8=)",
    "8====D)",
    "8===D~~",
    "B=====b~",
    "8=϶",
    "°|°",
    "`(_)_)=============D~~~~~`"
]


@commands('penis')
@commands('piemel')
@commands('cock')
@commands('dick')
@commands('pik')
@commands('lul')
@commands('schlong')
@commands('pecker')
@commands('johnson')
@commands('vleeslasso')
@commands('kwarkkannon')
@commands('puddingbuks')
@commands('dong')
@example('.penis')
def penie(bot, trigger):
    """.penis"""
    bot.say(random.choice(PENISES))


VAGINAS = [
    "()",
    "(*)",
    "[]",
    "({})",
    "{()}",
    "[(`)]",
    "(())",
    "([*])",
    "{}",
    "{*}",
    "{#}",
    "(#)"
]


@commands('vagina')
@commands('vag')
@commands('pussy')
@commands('kut')
@commands('fanny')
@commands('vulva')
@commands('cunt')
@commands('poes')
@commands('poesie')
@commands('poenie')
@commands('flamoes')
@example('.vagina')
def vagie(bot, trigger):
    """.vagina"""
    bot.say(random.choice(VAGINAS))


ASSES = [
    "(  Y  )",
    "(   )(   )",
    "(  )(  )",
    "( Y )",
    "( : )",
    "OO",
    "oo"
]


@commands('ass')
@commands('butt')
@commands('booty')
@commands('bum')
@example('.ass')
def assie(bot, trigger):
    """.ass"""
    bot.say(random.choice(ASSES))


@commands('badum')
@example('.badum')
def badum(bot, trigger):
    """.ass"""
    bot.say('tsssssh!')


@commands('bigmoney')
@commands('jeffbezosrocket')
@example('.bigmoney')
def bigmoney(bot, trigger):
    """.bigmoney"""
    bot.say("`(_)_)=============D~~~$$$~~~`")

COFFEES = [
    ":coffee:",
    ":coffeebounce:",
    ":coffeemug:",
    ":partycoffee:",
    ":tea:"
]

@commands('bakkie')
@commands('coffee')
@commands('catpipi')
@commands('pleur')
@commands('geef')
@commands('koffie')
@example('.bakkie')
def bakkie(bot, trigger):
    """.bakkie"""
    bot.say(random.choice(COFFEES))

@commands('tea')
@commands('thee')
@example('.tea')
def tea(bot, trigger):
    """.tea"""
    bot.say(':tea:')

@commands('wine')
@commands('wijn')
@commands('vin')
@commands('vino')
@commands('tinto')
@example('.wine')
def wine(bot, trigger):
    """.wine"""
    bot.say(':wine_glass:')

@commands('hamburger')
@commands('hamburguesa')
@example('.hamburger')
def hamburger(bot, trigger):
    """.hamburger"""
    bot.say(':hamburger:')

@commands('bubbels')
@commands('champagne')
@example('.bubbels')
def bubbels(bot, trigger):
    """.bubbels"""
    bot.say(':clinking_glasses:')

@commands('beer')
@commands('bier')
@commands('cerveza')
@example('.beer')
def beer(bot, trigger):
    """.beer"""
    bot.say(':beer:')

@commands('biertjes')
@commands('beers')
@commands('cervezas')
@example('.beers')
def beers(bot, trigger):
    """.beers"""
    bot.say(':beers:')


