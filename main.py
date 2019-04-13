from textblob import textblob
import sys, tweepy
import matplotlib.pyplot as pyplot

consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""

auth = tweepy.OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

def percent(part, total):
    return 100*float(part)/float(total)


