import requests, re, smtplib, os, config
from bs4 import BeautifulSoup
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Email
def sendEmail(name, lowestPrice): #function attributes are: item name, and price
    sentFrom = config.gmailUser
    sentTo = [config.gmailUser]
    subject = f'Price allert: {name}!' #email subject
    body = f"Hey, price of: {name} has dropped.\nCurrent lowest price is now: {lowestPrice}.\nYour beloved scraper-bot." #email text
    msg = MIMEMultipart()
    msg['To'] = config.gmailUser
    msg['From'] = config.gmailUser
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    email_text = msg.as_string()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #mail server configuration
    server.ehlo()
    server.login(config.gmailUser, config.gmailPassword) #mail server login action
    server.sendmail(sentFrom, sentTo, email_text) #send mail action
    server.close() #mail server connection termination

def sheetConnector(id): #connect to google sheet
    googleSheet = config.gc.open_by_key(id)
    return googleSheet

ceneoItemsList = sheetConnector(config.ceneoItemsSheetId)
ceneoItemsData = sheetConnector(config.ceneoDataSheetId)

#main loop
for item in ceneoItemsList.sheet1.get_all_records(): #gets all fields from worksheet 1 of spreadsheet
    with requests.Session() as s:
        response = s.get(config.url + str(item['Ceneo_ID']), verify=False)  #sends get request to item url
    soup = BeautifulSoup(response.text, 'html.parser') #text version of response is parsed
    scriptText = soup.find_all('script') #search for specific text in the parsed response
    text = str(scriptText) #change to the string format
    lowestPrice = float(re.search(r'"lowPrice":.+\d', text).group().split(' ')[1]) #search for specific text pattern to get associated lowest price value
    if item['Target_Price'] == '':
        ceneoItemsData.sheet1.append_row([item['Item_Name'],lowestPrice, date.today().strftime('%Y-%m-%d')]) #check if target price was set
    elif lowestPrice <= float(item['Target_Price'].replace(',','.')): #condition checking if lowest price is <= desired price set in google spreadsheet
        sendEmail(item['Item_Name'], lowestPrice) #sendEmail function is triggered when condition was met
        ceneoItemsData.sheet1.append_row([item['Item_Name'],lowestPrice, date.today().strftime('%Y-%m-%d')]) #data saved in spreadsheet
    else:
        ceneoItemsData.sheet1.append_row([item['Item_Name'],lowestPrice, date.today().strftime('%Y-%m-%d')]) #data saved in spreadsheet
