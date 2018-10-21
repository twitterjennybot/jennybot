# coding: utf8
import tweepy
import random
import os
import chardet
import pickle


consumer_key = open("/root/secrets/consumer_key").read().rstrip('\n')
consumer_secret = open("/root/secrets/consumer_secret").read().rstrip('\n')
access_token = open("/root/secrets/access_token").read().rstrip('\n')
access_token_secret =open("/root/secrets/access_token_secret").read().rstrip('\n')



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#user = api.me()
#print (user.name)

def getpoeme() :
        listpoeme=[]
        for dirname, dirnames, filenames in os.walk("/root/poetry/4lines.poemes/"):
                for filename in filenames:
                        listpoeme = listpoeme + [os.path.join(dirname, filename)]

        poeme =   random.choice (listpoeme)
        return open (poeme).read().decode("cp1252")


file_data_already_seen = "/root/data/sauvegarde.poeme.data"
infile = open(file_data_already_seen,'rb')
tweet_already_respond = pickle.load(infile)
infile.close()

print tweet_already_respond


for tweet in api.mentions_timeline():
    try:
	if not (tweet.id in tweet_already_respond) :
	        print tweet.id
        	api.update_status("@" + tweet.user.screen_name + " "+ getpoeme() + "\n\n\n#poesie #poeme",  tweet.id)
		tweet_already_respond = tweet_already_respond + [tweet.id]
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

outfile = open(file_data_already_seen,'wb')
pickle.dump(tweet_already_respond,outfile)
outfile.close()
