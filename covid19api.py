# Thanks to covid19india for providing the data
import json, ssl, sys
import urllib.request, urllib.parse, urllib.error
import datetime

def fetch_data(url):
    ctx = ssl.create_default_context()
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    return data

try:
    js = json.loads(fetch_data("https://api.covid19india.org/states_daily.json"))
    states_daily = js['states_daily']
    today = states_daily[len(states_daily)-3]
    date = today["date"]
    today_inc = today["tt"]
    yesterday = states_daily[len(states_daily)-6]
    yesterday_inc = yesterday["tt"]
except:
    js = None
if not js or 'states_daily' not in js:
    print('==== Failure To Retrieve ====')
    sys.exit()

try:
    js = json.loads(fetch_data("https://api.covid19india.org/v4/data.json"))
    active = str(js['TT']['total']['confirmed']-js['TT']['total']['recovered']-js['TT']['total']['deceased']-js['TT']['total']['other'])
    recoverypercent = "{:.2f}%".format(round(js['TT']['total']['recovered']/js['TT']['total']['confirmed']*100,2))
    fatalitypercent = "{:.2f}%".format(round(js['TT']['total']['deceased']/js['TT']['total']['confirmed']*100,2))
    vaccinateddose1percent = "{:.2f}%".format(round(js['TT']['total']['vaccinated1']/js['TT']['meta']['population']*100,2))
    vaccinateddose2percent = "{:.2f}%".format(round(js['TT']['total']['vaccinated2']/js['TT']['meta']['population']*100,2))
    updatetime = datetime.datetime.strptime(js['TT']['meta']['last_updated'], "%Y-%m-%dT%H:%M:%S+05:30")
    last_update = updatetime.strftime('%b-%d-%y %I:%M%p')
except:
    js = None
if not js or 'TT' not in js:
    print('==== Failure To Retrieve ====')
    sys.exit()

print("Active:",active,"\nRecovery %",recoverypercent,"\nFarality",fatalitypercent,"\nVaccinated %",vaccinateddose1percent,vaccinateddose2percent)
print("Today",today_inc if int(today_inc) < 0 else "+"+today_inc)
print("Yesterday",yesterday_inc if int(yesterday_inc)<0 else "+"+yesterday_inc)
print("Last update",last_update)