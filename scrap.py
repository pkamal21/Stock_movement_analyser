from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
from threading import Thread
import smtplib
from twilio.rest import Client

quote_page = 'https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/summary/company-summary/GB00B7FC0762GBGBXSET1.html'

latest = 0
last = 0
f = 0
for i in range(10):
    time.sleep(10)
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('tr',attrs={'class':'even'})
    c = 1
    for td in table.find_all('td'):
        if c==2:
            latest = td.text
            latest = latest.replace(',','')
        c+=1
    if float(latest) > float(last):
        print("latest price",latest)
        f+=1
    else:
        print("last price :",last)
        f+=1
    last = latest
    
    if f >=2:
        # Your Account Sid and Auth Token from twilio.com/console
        account_sid = 'AC752d5a1157f11cb284c2c837f037a921'
        auth_token = ''
        client = Client(account_sid, auth_token)
        x = 'buy the share at:'
        message = client.messages.create(
                                    body=x+str(latest),
                                    from_='+18645684944',
                                    to='+917619589376'
                                )
        