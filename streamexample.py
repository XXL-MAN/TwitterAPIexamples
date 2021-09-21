from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json,unicodedata

# import API tokens
from secrets import *

#Twitter script example to connect to the Tweets stream
# Returned:  FULL json on every tweet, whole data

"""
secrets.py file must handle the private keys given by Twitter 
secrets.py debe contener las claves API key generadas de una cuenta de TWITTER

-> https://developer.twitter.com/en/

access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"

"""

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):

        def normalize(text):
            return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')

        #data = normalize(json.load(data))
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter tweets from the words.
    stream.filter(track=['cybersecurity', 'ciberseguridad'])
