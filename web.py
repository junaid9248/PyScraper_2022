from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd
import csv

# Creating the URL that we can parse through to BeautifulSoup
url = "https://www.amazon.in/SQL-All-One-Dummies-3ed/dp/8126534494/ref=sr_1_4?crid=2WVAB4O10MPY&keywords=sql&qid=1670776114&sprefix=sql%2Caps%2C772&sr=8-4"

# Assigning the user data to a dictionary
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

# Using an HTTP request to fetch the data from requested url with our system details
page = requests.get(url, headers=headers)

# Getting HTML from requested page
soup1 = BeautifulSoup(page.content, "html.parser")
# Cleaning for better visual representation
soup2 = BeautifulSoup(soup1.prettify())

# Now we get the title of the product we are going to track .strip() is used to eliminate all the whitespace
title = soup2.find(id='productTitle').get_text().strip()

# Getting the price of the book by passing it's id, taking only numerical part by giving range to extracted text and cleaning it up
price_paperback = soup2.find(id='price').get_text().strip()[1:]

# Making it a float, so we can do calculations on it
converted = float(price_paperback)

# Extracting rating from it, taking only numerical part
rating = soup2.find(class_='a-icon-alt').get_text().strip()[0:4] + "stars"

# Giving the date today (dd/ mm/ yy) and time (hour: minute: second) right now
date_today = datetime.date.today().strftime('%d:%m:%y')
time_today = datetime.date.today().strftime('%H: %M: %S')

# Collecting the variables in a list so we can use them in the csv file
data = [title, price_paperback, rating, date_today, time_today]

# newFile = pd.DataFrame([data], columns=['Name', 'price', 'rating', 'Date and Time'])

# This is a list to store the title of the various columns of the csv
header = ['Item name', 'Price', 'Ratings', 'Date', 'Time']

# Creating the csv file from the data and headers we have created. open() function is used
# 'w' is for creating the first row
csv_file = open('item.csv', 'w', newline='', encoding='UTF8')
with csv_file:
    write = csv.writer(csv_file)
    write.writerow(header)
    write.writerow(data)


df = pd.read_csv(r'C:\Users\ther3\projects\python\item.csv')
print(df)


# Appending new data to the initial set. 'a+' is the command we use
def check_price():
    with open('item.csv', 'a+', newline='', encoding='UTF8') as csv_file:
        write1 = csv.writer(csv_file)
        write1.writerow(data)



while True:
    check_price()
    df = pd.read_csv(r'C:\Users\ther3\projects\python\item.csv')
    print(df)
    time.sleep(5)


