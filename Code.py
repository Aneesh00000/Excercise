#Question 1: Use yfinance to Extract Stock Data
#Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is TSLA.

import yfinance as yf
import pandas as pd

# Create ticker object for Tesla stock
tesla_ticker = yf.Ticker("TSLA")

# Extract stock data and store in dataframe
tesla_data = tesla_ticker.history(period="max")

# Reset index and display first five rows
tesla_data.reset_index(inplace=True)
tesla_data.head()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 2: Use Webscraping to Extract Tesla Revenue Data
#Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named html_data.

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Download the webpage and store the response text in a variable named html_data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text

# Parse the html data using BeautifulSoup
soup = BeautifulSoup(html_data, "html.parser")

# Extract the table with Tesla Quarterly Revenue and store it into a dataframe named tesla_revenue
table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]
tesla_revenue = df[['Date', 'Revenue']]

# Remove the comma and dollar sign from the Revenue column
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")

# Remove any null or empty strings in the Revenue column
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Display the last 5 rows of the tesla_revenue dataframe
print(tesla_revenue.tail(5))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 3: Use yfinance to Extract Stock Data
#Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is GME.

import yfinance as yf

# Extract stock information for GameStop and save it in a dataframe named gme_data
ticker = "GME"
gme_data = yf.Ticker(ticker).history(period="max")

# Reset the index of the gme_data DataFrame
gme_data.reset_index(inplace=True)

# Display the first five rows of the gme_data dataframe
print(gme_data.head(5))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 4: Use Webscraping to Extract GME Revenue Data
#Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named `html_data`.

import requests
from bs4 import BeautifulSoup
import pandas as pd

# download webpage and save as html_data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data = requests.get(url).text

# parse HTML data using beautiful_soup
soup = BeautifulSoup(html_data, 'html.parser')

# find table with GameStop Quarterly Revenue data
table = soup.find('table', {'id': 'GameStop-revenue-Q'})

# convert table to dataframe
gme_revenue = pd.read_html(str(table))[0]

# remove commas and dollar signs from Revenue column
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace(',', '').str.replace('$', '').astype(float)

# remove any null or empty strings in Revenue column
gme_revenue = gme_revenue[gme_revenue['Revenue'].notna()]

# display last five rows of gme_revenue dataframe
print(gme_revenue.tail())
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Question 5: Plot Tesla Stock Graph
#Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph. The structure to call the make_graph function is make_graph(tesla_data, tesla_revenue, 'Tesla'). Note the graph will only show data upto June 2021.

import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock_name):
    fig, ax1 = plt.subplots()
    ax1.plot(stock_data['Date'], stock_data['Close'], color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Stock Price', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax2 = ax1.twinx()
    ax2.bar(revenue_data['Quarter'], revenue_data['Revenue'], color='red', alpha=0.3)
    ax2.set_ylabel('Revenue', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    plt.title(f'{stock_name} Stock Price vs Revenue')
    plt.show()

make_graph(tesla_data, tesla_revenue, 'Tesla')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 6: Plot GameStop Stock Graph
#Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the make_graph function is make_graph(gme_data, gme_revenue, 'GameStop'). Note the graph will only show data upto June 2021.

import matplotlib.pyplot as plt
from make_graph import make_graph

# Plot GameStop Stock Graph
make_graph(gme_data, gme_revenue, 'GameStop')

# Set the title of the graph
plt.title('GameStop Stock Data')

# Show the graph
plt.show()
