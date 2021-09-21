from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json,unicodedata

# import API tokens
from secrets import *

#Twitter script example to connect to the Tweets stream
# Returned:  selected data from json fields

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

            all_data = json.loads(data)
            # collect all desired data fields
            if 'text' in all_data:
                tweet = all_data["text"]
                created_at = all_data["created_at"]
                retweeted = all_data["retweeted"]
                username = all_data["user"]["screen_name"]
                user_tz = all_data["user"]["time_zone"]
                user_location = all_data["user"]["location"]
                user_coordinates = all_data["coordinates"]

                # if coordinates are not present store blank value
                # otherwise get the coordinates.coordinates value
                if user_coordinates is None:
                    final_coordinates = user_coordinates
                else:
                    final_coordinates = str(all_data["coordinates"]["coordinates"])

                """ MY SQL CODE 
                # inser values into the db
                cursor.execute(
                    "INSERT INTO tableName (created_at, username, tweet, coordinates, userTimeZone, userLocation, retweeted) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (created_at, username, tweet, final_coordinates, user_tz, user_location, retweeted))
                cnx.commit()
                """
                print((username, tweet, final_coordinates))

                return True
            else:
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
