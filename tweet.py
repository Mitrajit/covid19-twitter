import sys, os
# import encryptdecrypt38
import covid19api
try:
    import tweepy, geocoder, argparse
    from playsound import playsound
    from tabulate import tabulate
except ModuleNotFoundError :
    print("Libraries could not be imported\nUse \"pip install -r requirements.txt\"")
    sys.exit(0)
# def delete_tweet() :
#     tweet = api.user_timeline(count = 1)[0]
#     print("Are you sure you want to delete this tweet(Y/N):\n",tweet.text.lstrip())
#     confirm = input('')
#     if confirm =='Y' or confirm == 'y':
#         api.destroy_status(tweet.id)
#         playsound('delete-tweet.mp3')
#         print('Tweet is deleted')
#     else:
#         print('Tweet is not deleted')
# my_parser = argparse.ArgumentParser(description='List the content of a folder')
# my_parser.add_argument('tweet',
#                        metavar='tweet',
#                        type=str,
#                        action="append",
#                        nargs="*",
#                        help='tweet <The text you want to tweet>')
# my_parser.add_argument('-api',
#                        type=str,
#                        metavar=("<api key>", "<api secret>" , "<token key>","<token secret>"),
#                        action="store",
#                        help='gets the api keys and secrets',
#                        nargs=4)
# my_parser.add_argument('-tr',
#                        type=str,
#                        metavar=("place name or global"),
#                        action="store",
#                        help='gets the trending in the given place',
#                        nargs="*")
# my_parser.add_argument('-d',
#                        action="store_true",
#                        help='deletes the last tweet')
# args = my_parser.parse_args()
# if len(args.tweet[0])==0 and args.api is None and not args.d and args.tr is None:
#     my_parser.print_help()
#     sys.exit(0)
try :
    # if args.api is not None:
    #     encryptdecrypt38.encrypt([args.api[0],args.api[1],args.api[2],args.api[3]])
    #     print('API, tokens keys and secrets are saved')
    # cred=encryptdecrypt38.decrypt()
    auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("SECRET_KEY"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN_KEY"), os.getenv("ACCESS_TOKEN_SECRET"))
    print("OAuthHandler set")
    api = tweepy.API(auth)
    print("logged in as @"+api.me().screen_name)
except tweepy.error.TweepError as tp:
    print("Could not log in with the given credentials\n",tp)
    sys.exit(0)
# except IndexError:
#     my_parser.print_help()
#     sys.exit(0)
# elif len(args.tweet[0])!=0 :
#     api.update_status(status = " ".join(args.tweet[0]))
#     playsound('tweet-sfx.mp3')
#     print("Tweeted")

for tweet in api.user_timeline(count=2, include_rts = False):
    if "COVID tracker bot" in tweet.text:
        api.destroy_status(tweet.id)

api.update_status("".join(["🦠 COVID tracker bot 🤖\n","😷 Active cases: ",covid19api.active,"\n😄 Recovery rate: ",
covid19api.recoverypercent,"\n😖 Fatality rate: ",covid19api.fatalitypercent,"\n💉 Vaccination rate: ",
covid19api.vaccinatedpercent,"\n📈 Today ",covid19api.today_inc if int(covid19api.today_inc) < 0 else "+"+
covid19api.today_inc,"\n📈 Yesterday ",covid19api.yesterday_inc if int(covid19api.yesterday_inc)<0 else "+"
+covid19api.yesterday_inc,"\nLast update ",covid19api.last_update]))
