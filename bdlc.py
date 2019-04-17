import requests
import json

API_KEY = 'ZiG0VQseAh5yrWa7E3NWwkwi93Gb1FUk'

companyList = ['AAPL', 'AMZN', 'CLDR', 'CSCO', 'DBX', 'FB', 'GOOGL', 'HPQ', 'IBM', 'JNPR', 'MSFT', 'NFLX', 'NTAP',
               'ORCL', 'RHT', 'SNAP', 'SPOT', 'TSLA', 'TWTR', 'VMW']

'''
Import Company Profile
'''

# Import Header
print('Writing Companyprofile Header CSV')
url = 'https://api.unibit.ai/companyprofile/' + companyList[
    0] + '?size=10&datatype=json&AccessKey=' + API_KEY
r = requests.get(url).json()
with open("header.csv", "w") as file:
    for key in r:
        file.write(key + '\t')

# import Companyprofile CSV
print('Writing Companyprofile CSV')
with open("data.csv", "w") as file:
    for company in companyList:
        url = 'https://api.unibit.ai/companyprofile/' + company + '?size=10&datatype=json&AccessKey=' + API_KEY
        r = requests.get(url).json()
        file.write(r['ticker'] + '\t' + r['company_name'] + '\t' + r['industry'] + '\t' + r['website'] + '\t' + r[
            'company_decription'] + '\t' + r['company_leadership'] + '\t' + r['sector'] + '\t' + r['asset_type'] + '\n')

# import Companyprofile JSON
print('Writing Companyprofile JSON')
with open("unibit-ai-Companyprofile-20y-jq.json", "w") as file:
    for company in companyList:
        url = 'https://api.unibit.ai/companyprofile/' + company + '?size=10&datatype=json&AccessKey=' + API_KEY
        r = requests.get(url).json()
        json.dump(r, file)
        file.write('\n')

print('FINISHED IMPORT COMPANY PROFILE')

'''
Import Historical Stock Price
'''

# Import Header
print('Writing Historical Stock Price Header CSV')
url = 'https://api.unibit.ai/historicalstockprice/' + companyList[0] + 'range=20y&interval=1&datatype=json&AccessKey=' + API_KEY
r = requests.get(url).json()
with open("header.csv", "w") as file:
    for key in r:
        file.write(key + '\t')

# Import Historical Stock Price CSV
print('Writing Historical Stock Price CSV')
with open("historical.csv", "w") as file:
    for company in companyList:
        url = 'https://api.unibit.ai/historicalstockprice/' + company + '?range=20y&interval=1&datatype=json&AccessKey=' + API_KEY
        r = requests.get(url).json()
        file.write(r['ticker'] + '\t' + r['date'] + '\t' + r['open'] + '\t' + r['high'] + '\t' + r['low'] + '\t' + r[
            'close'] + '\t' + r['adj_close'] + '\t' + r['volume'] + '\n')

# import Historical Stock Price JSON
print('Writing Historical Stock Price JSON')
with open("historical.json", "w") as file:
    for company in companyList:
        url = 'https://api.unibit.ai/historicalstockprice/' + company + '?range=20y&interval=1&datatype=json&AccessKey=' + API_KEY
        r = requests.get(url).json()
        json.dump(r, file)
        file.write('\n')

print('FINISHED IMPORT HISTORICAL PRICE')
print('DONE IMPORTING')
