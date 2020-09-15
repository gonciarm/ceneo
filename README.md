Super simple to use and configure python ceneo scraper.

Functionalities:
- checks current lowest item price on ceneo.pl
- configuration is made via google sheets
- scraped data is collected in google sheets (no data base required)
- scraping can be scheduled by task scheduler
- included email notification if price of interesting items achieves certain level 

Requirements:
- python 3.6 or above
- python requests module
- python  beautifulsoup4 module
- python gspread module
- google account (gmail aswell)

Setup:
1) Create two google sheets: 
- 1 sheet containing  three columns in exact order: Ceneo_ID (text type), Item_Name (text type), Target_Price (number type), 
- 2 sheet containing  three column in exact order: Item_Name (text type), Price (number type), Date (date type)

2 Create new project in google developers console: https://console.developers.google.com.
3 Add two API interfaces to the project: Google Sheets API, Google Drive API.
4 Get service account credentials in json format (save it and add it to script folder with name changed to credentials.json)
5 Share the created sheets with appication bot email.
(check this tutorial that explains a lot of topics: https://www.youtube.com/watch?v=T1vqS1NL89E)
6 Create user variables in the system to store secret data like: email adress, email password, google sheets id.
(check this tutorial that explains how to create user variables in the system: https://www.youtube.com/watch?v=IolxqkL7cD8).
7 Configure the data you want to be scraped in 1 spread sheet (Ceneo_Id = number value after domain name on item page https://www.ceneo.pl/>>83359603<<, Target_Price = desired price also triggers email notification.
8 Adjust the script in config.py to met your expectations.
