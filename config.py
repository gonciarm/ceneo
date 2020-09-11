import os, gspread

#Email configuration

gmailUser = os.environ.get('GMAIL_USER') #data stored in system user variable
gmailPassword = os.environ.get('GMAIL_PASSWORD') #data stored in system user variable

#Connection

url = 'https://www.ceneo.pl/' #ceneo.pl url
gc = gspread.service_account(filename='credentials.json') #google sheet api connection

#Google sheets ids
ceneoItemsSheetId = '1aMREIDS9dVw7NzfdyZ-nDVI_pDlM9GLwd4Oux9PNOBI' #id of google spreadsheet containing list of items to price check
ceneoDataSheetId = '1enz2-EtElFaP2MosxmRbjoF-6CbEmu-zaRniJtEErfc' #id of google spreadsheet in which data will be stored