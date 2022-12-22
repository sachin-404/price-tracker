import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

# send a request to fetch HTML
response = requests.get('https://www.amazon.in/Sony-WH-1000XM5-Cancelling-Headphones-Connectivity/dp/B09XS7JWHH/ref=sr_1_2?crid=329PAFGZJT9F&keywords=sony%2B1000xm5&qid=1671654559&sprefix=sony%2B1000xm5%2Caps%2C264&sr=8-2&th=1', headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
soup.encode('utf-8')

# function to check if the price has dropped below 25,000
def check_price():
    title = soup.find(id= "productTitle").get_text()
    price = soup.find(class_ = "a-price-whole").get_text().replace(',', '').replace('.', '').strip()

    #converting the string amount to float
    converted_price = float(price[0:5])
    if(converted_price < 25000):
        send_mail()

# function to sends the email
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # enter your email id and password
    server.login('email_id', 'email_password')

    subject = 'Price Fell Down'
    body = """
    Price of the product you were looking for has fell down. Check it out before it's gone.
    Product link https://www.amazon.in/Sony-WH-1000XM5-Cancelling-Headphones-Connectivity/dp/B09XS7JWHH/ref=sr_1_2?crid=329PAFGZJT9F&keywords=sony%2B1000xm5&qid=1671654559&sprefix=sony%2B1000xm5%2Caps%2C264&sr=8-2&th=1
    """

    msg = f"Subject: {subject}\n\n{body}"
  
    server.sendmail(
        'sender_email',
        'reciever_email',
        msg
    )
    #print a message for confirmation
    print('Email has been sent')
    # quit the server
    server.quit()

#regularly check for prices using the loop
while(True):
  check_price()
  time.sleep(60) # this will repeat after every 60 seconds