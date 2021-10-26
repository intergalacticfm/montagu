# -*- coding: utf8 -*-
"""
gfycat.py - Sopel gfy Module
"""

from sopel.module import commands, example
import requests
import time
import urllib
import random
import json


QUERY_ENDPOINT = 'https://api.gfycat.com/v1/gfycats/'
OAUTH_ENDPOINT = 'https://api.gfycat.com/v1/oauth/token'
ERROR_KEY = 'errorMessage'


class GfyCat(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.get_token()

    def query(self, query):
        self.check_token()

        r = requests.get(QUERY_ENDPOINT + 'search' + '?search_text={}'.format(query), headers=self.headers)
        response = r.json()

        return response

    def check_token(self):
        """
        Checks if Token is still valid and updates if it's not
        """
        if time.time() > self.expires_at:
            self.get_token()

    def get_token(self):
        """
        Gets the authorization token
        """

        payload = {'grant_type': 'client_credentials', 'client_id': self.client_id, 'client_secret': self.client_secret}
        r = requests.get(OAUTH_ENDPOINT, data=json.dumps(payload), headers={'content-type': 'application/json'})

        response = r.json()

        if r.status_code != 200 and not ERROR_KEY in response:
            raise GfycatClientError('Error fetching the OAUTH URL', r.status_code)
        elif ERROR_KEY in response:
            raise GfycatClientError(response[ERROR_KEY], r.status_code)

        self.token_type = response['token_type']
        self.access_token = response['access_token']
        self.expires_in = response['expires_in']
        self.expires_at = time.time() + self.expires_in - 5
        self.headers = {'content-type': 'application/json', 'Authorization': self.token_type + ' ' + self.access_token}


@commands('gfy')
@commands('gif')
@example('.gfy cat')
def giphy(bot, trigger):
    """.gfy cat"""
    API_ID = bot.config.apikeys.gfycat_id
    API_SECRET = bot.config.apikeys.gfycat_secret
    client = GfyCat(API_ID, API_SECRET)

    user_input = urllib.parse.quote_plus(trigger.group(2))

    result = client.query(user_input)
    gifs = result['gfycats']
    
    if len(gifs) > 0:
        rand_image = random.randint(0, len(gifs)-1)
        obj = gifs[rand_image]
        url = obj['gifUrl']

        bot.say(url)
    else:
        bot.say('No gif found. Blame the dog.')
