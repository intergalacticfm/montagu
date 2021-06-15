from sopel.module import event, rule

@rule('.*')
@event('001')
def logon(bot, trigger):
    bot.say("login {} {}".format(bot.config.mattermost.username, bot.config.mattermost.password), "mattermost")

