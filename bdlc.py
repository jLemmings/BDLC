import requests

companyList = ['AAPL', 'AMZN', 'CLDR', 'CSCO', 'DBX', 'FB', 'GOOGL', 'HPQ', 'IBM', 'JNPR', 'MSFT', 'NFLX', 'NTAP',
               'ORCL', 'RHT', 'SNAP', 'SPOT', 'TSLA', 'TWTR', 'VMW']

'''
Import Company Profile
'''
# Import Header
url = 'https://api.unibit.ai/companyprofile/' + companyList[0] + '?size=10&datatype=json&AccessKey=ZiG0VQseAh5yrWa7E3NWwkwi93Gb1FUk'
r = requests.get(url).json()
with open("header.csv", "w") as file:
    for key in r:
        file.write(key + '\t')




#import data
with open("data.csv", "w") as file:
    for company in companyList:
        url = 'https://api.unibit.ai/companyprofile/' + company + '?size=10&datatype=json&AccessKey=ZiG0VQseAh5yrWa7E3NWwkwi93Gb1FUk'
        r = requests.get(url).json()
        print('Writing Company Details of: ' + company)
        file.write(r['ticker'] + '\t' + r['company_name'] + '\t' + r['industry'] + '\t' + r['website'] + '\t' + r['company_decription'] + '\t' + r['company_leadership'] + '\t' + r['sector'] + '\t' + r['asset_type'] + '\n')
