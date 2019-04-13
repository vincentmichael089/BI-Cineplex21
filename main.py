from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as pyplot
import config

consumerKey = config.consumerKey
consumerSecret = config.consumerSecret
accessToken = config.accessToken
accessTokenSecret = config.accessTokenSecret

auth = tweepy.OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

def percent(part, total):
    return 100*float(part)/float(total)


