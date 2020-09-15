import os, gspread

#Email configuration

gmailUser = os.environ.get('GMAIL_USER') #data stored in system user variable
gmailPassword = os.environ.get('GMAIL_PASSWORD') #data stored in system user variable

#Connection

url = 'https://www.ceneo.pl/' #ceneo.pl url
gc = gspread.service_account(filename='credentials.json') #google sheet api connection

#Google sheets ids
ceneoItemsSheetId = os.environ.get('CENEO_ITEMS_LIST') #id of google spreadsheet containing list of items to price check stored in system user variable
ceneoDataSheetId = os.environ.get('CENEO_DATA_SHEET') #id of google spreadsheet in which data will be stored stored in system user variable