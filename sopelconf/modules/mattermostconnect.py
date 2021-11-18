from sopel.module import event, rule

@rule('.*')
@event('001')
def logon(bot, trigger):
    bot.say("login {} {} {} {}".format(bot.config.mattermost.server, bot.config.mattermost.team, bot.config.mattermost.username, bot.config.mattermost.password), "mattermost")

