import requests
import json

companyList = ['AAPL', 'AMZN', 'CLDR', 'CSCO', 'DBX', 'FB', 'GOOGL', 'HPQ', 'IBM', 'JNPR', 'MSFT', 'NFLX', 'NTAP',
               'ORCL', 'RHT', 'SNAP', 'SPOT', 'TSLA', 'TWTR', 'VMW']

'''
Import Company Profile
'''

# Import Header
print('Writing Companyprofile Header CSV')
url = 'https://api.unibit.ai/companyprofile/' + companyList[0] + '?size=10&datatype=json&AccessKey=ZiG0VQseAh5yrWa7E3NWwkwi93Gb1FUk'
r = requests.get(url).json()
with open("header.csv", "w") as file:
    for key in r:
        file.write(key + '\t')

#import Companyprofile CSV
print('Writing Companyprofile CSV')
with open("data.csv", "w") as file:
    for company in companyList:
        url = 'https://api.unibit.ai/companyprofile/' + company + '?size=10&datatype=json&AccessKey=ZiG0VQseAh5yrWa7E3NWwkwi93Gb1FUk'
        r = requests.get(url).json()
        file.write(r['ticker'] + '\t' + r['company_name'] + '\t' + r['industry'] + '\t' + r['website'] + '\t' + r['company_decription'] + '\t' + r['company_leadership'] + '\t' + r['sector'] + '\t' + r['asset_type'] + '\n')

#import Companyprofile JSON
print('Writing Companyprofile JSON')
with open("unibit-ai-Companyprofile-20y-jq.json", "w") as file:
    jsonArray = []
    for company in companyList:
        url = 'https://api.unibit.ai/companyprofile/' + company + '?size=10&datatype=json&AccessKey=ZiG0VQseAh5yrWa7E3NWwkwi93Gb1FUk'
        r = requests.get(url).json()
        json.dump(r, file)

print('FINISHED IMPORT COMPANY PROFILE')

'''
Import Historical Stock Price
'''

# Import Header
print('Writing Historical Stock Price Header CSV')
url = 'https://api.unibit.ai/historicalstockprice/' + companyList[0] + '?range=20y&datatype=json&AccessKey=ZiG0VQseAh5yrWa7E3NWwkwi93Gb1FUk'
r = requests.get(url).json()
with open("header.csv", "w") as file:
    for key in r:
        file.write(key + '\t')