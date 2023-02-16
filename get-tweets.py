import configparser
import pandas as pd
import tweepy



config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = config['twitter']['CONSUMER_SECRET']
ACCESS_KEY = config['twitter']['ACCESS_KEY']
ACCESS_SECRET = config['twitter']['ACCESS_SECRET']


def twitter_OAuth(consumer_key,consumer_secret,access_key,access_secret):
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api = tweepy.API(auth)
    return api

api = twitter_OAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)


query = 'Your query'
max_items = 100
tweets = tweepy.Cursor(api.search_tweets, q = query ,tweet_mode = 'extended', lang = 'fa').items(max_items)
column = ['Date','User Name','Id','Tweets','Hashtags','likes', 'Retweets', 'Followers', 'Location','Joined']
data = []
for tw in tweets:
    data.append([tw.created_at,tw.user.screen_name ,tw.id, tw.full_text, tw.entities['hashtags'] ,tw.favorite_count, tw.retweet_count, tw.user.followers_count,tw.user.location ,tw.user.created_at])
    df = pd.DataFrame(data, columns = column)
    df = df.sort_values(by= ['likes'])
    df.to_csv('fil_name.csv', index=False, encoding='utf-8-sig')


