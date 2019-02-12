# Jamiel Sheikh - jamiel@chainhaus.com

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd
import json
import io


### Scrape Etherscan.io, use BeautifulSoup document search
block_data = requests.get('https://etherscan.io/block/7200964')
block_document = BeautifulSoup(block_data.text,features='html.parser')
print(block_document.title)


### Eth prices - Pull Ether via CSV file scrape, load into pandas DataFrame
url = 'https://etherscan.io/chart/etherprice?output=csv'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
df = pd.read_table(io.StringIO(response.content.decode("utf-8")),sep=",")
df.dropna()
df = df.drop(df.columns[1], axis=1)
df['Date(UTC)'] = pd.to_datetime(df['Date(UTC)'],format = "%m/%d/%Y")
df.index = df['Date(UTC)']
df = df.drop(df.columns[0], axis=1)
plt.plot(df)
plt.show()





