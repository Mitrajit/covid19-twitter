import os
import covid19api
import tweepy
auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("SECRET_KEY"))
auth.set_access_token(os.getenv("ACCESS_TOKEN_KEY"), os.getenv("ACCESS_TOKEN_SECRET"))
print("OAuthHandler set")
api = tweepy.API(auth)
print("logged in as @"+api.me().screen_name)
flag = True
for tweet in api.user_timeline(count=5, include_rts = False, tweet_mode="extended"):
    if "COVID tracker bot" in tweet.full_text:
        if "".join(["Last update ",covid19api.last_update]) in tweet.full_text:
            flag = False
        else:
            api.destroy_status(tweet.id)

if flag:
    api.update_status("".join(["🦠 COVID tracker bot • India🤖\n","😷 Active cases: ",covid19api.active,"\n😄 Recovery rate: ",
    covid19api.recoverypercent,"\n😖 Fatality rate: ",covid19api.fatalitypercent,"\n💉 Vaccination rate: 💉",
    covid19api.vaccinateddose1percent," 💉💉",covid19api.vaccinateddose2percent,"\n📈 Today ",covid19api.today_inc if int(covid19api.today_inc) < 0 else "+"+
    covid19api.today_inc,"\n📈 Yesterday ",covid19api.yesterday_inc if int(covid19api.yesterday_inc)<0 else "+"
    +covid19api.yesterday_inc,"\nLast update ",covid19api.last_update,"\n#IndiaFightsCOVID19 #COVIDEmergency #CovidTracker"]))
    print("Tweeted")
else:
    print("Not tweeted, no new data")