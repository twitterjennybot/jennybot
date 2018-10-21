# coding: utf8
import tweepy
import random
import os



consumer_key = open("/root/secrets/consumer_key").read().rstrip('\n')
consumer_secret = open("/root/secrets/consumer_secret").read().rstrip('\n')
access_token = open("/root/secrets/access_token").read().rstrip('\n')
access_token_secret =open("/root/secrets/access_token_secret").read().rstrip('\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

listfollower = ""
listchat = []


for dirname, dirnames, filenames in os.walk("/root/imagechat"):
    for filename in filenames:
        listchat = listchat + [os.path.join(dirname, filename)]

imagedechat=  listchat[random.randint(0,len(filenames)-1)]

print imagedechat

list_follower=[]
for follower in tweepy.Cursor(api.followers).items():
    print follower.screen_name
    list_follower=list_follower+[follower]
    try:
        follower.follow()
    except:
        pass

elu_follower = random.choice(list_follower)

api.update_with_media( imagedechat, 'Coucou @{0} ! Voici une superbe image de #chat :'.format(elu_follower.screen_name))


