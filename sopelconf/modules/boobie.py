# -*- coding: utf8 -*-
"""
boobie.py - Sopel boobie Module + more
"""

from sopel.module import commands, example
import requests
import urllib
import re
import random


BOOBS = [
  "(.)(.)",
  "(.) (.)",
  "( . Y . )",
  "( -  )(  - )",
  "( o  )(  o )",
  "(O Y O)",
  "( · )( · )",
  "( \u0E4F Y \u0E4F )", #  ( ๏ Y ๏ )
  "\uFF08\u3002 \u3145  \u3002\uFF09" # （。 ㅅ  。）
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
@example('.bigmoney')
def bigmoney(bot, trigger):
    """.bigmoney"""
    bot.say("`(_)_)=============D~~~$$$~~~`")
