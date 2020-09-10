import requests, gspread, json, re
from bs4 import BeautifulSoup

#Configuration
url = 'https://www.ceneo.pl/' #ceneo.pl url
gc = gspread.service_account(filename='credentials.json') #google sheet api connection

ceneoItemsListId = '1aMREIDS9dVw7NzfdyZ-nDVI_pDlM9GLwd4Oux9PNOBI' #id of google spread sheet containing list of items to price check
ceneoItemsDataId = '1enz2-EtElFaP2MosxmRbjoF-6CbEmu-zaRniJtEErfc' #id of google spread sheet in which data will be stored
#Items which price you would like to check

def sheetConnector(id): #connect to google sheet
    googleSheet = gc.open_by_key(id)
    return googleSheet

ceneoItemsList = sheetConnector(ceneoItemsListId)
ceneoItemsData = sheetConnector(ceneoItemsDataId)
#main loop
for item in ceneoItemsList.sheet1.get_all_records():
    print(item['Ceneo_ID'])
    with requests.Session() as s:
        response = s.get(url + str(item['Ceneo_ID']), verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        scriptText = soup.find_all('script')
        data = str(scriptText)
        # m = re.search(r'"lowPrice":.+\d', data)
        # lowestPrice = m.group().split(' ')[1]
        lowestPrice = float(re.search(r'"lowPrice":.+\d', data).group().split(' ')[1])

    print(lowestPrice)
    
    # print(scriptText)
  
    # print(soup)
#print()

#response = requests.get('https://www.ceneo.pl/58983508',verify=False)

# with requests.Session() as s:
#     response = s.get('https://www.ceneo.pl/', verify=False)
    
# print(response.text)