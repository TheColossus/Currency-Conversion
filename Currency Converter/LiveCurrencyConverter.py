from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

currencies={}
key_list=[]
currencylist=[]

options = webdriver.ChromeOptions()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(2)
dynamic_elements=driver.get('https://finance.yahoo.com/currencies/')
table=driver.find_element(By.CLASS_NAME,'W\(100\%\)')
print(len(table.find_elements(By.CLASS_NAME,'simpTblRow')))
rows =table.find_elements(By.CLASS_NAME,'simpTblRow')

for row in rows:
    for cell in row.find_elements(By.TAG_NAME, 'td'):
        if cell.get_attribute('aria-label')=='Name':
            temp_key=cell.get_attribute('innerHTML')
            currencies[temp_key]=0
        if cell.get_attribute('aria-label')== 'Last Price':
            value=cell.find_element(By.TAG_NAME,'fin-streamer').text
            currencies[temp_key]=float(value.replace(',', ''))

i=0
for key in currencies:
    key_list.append([key.split('/'),(currencies[key])])
    if key_list[i][0][1]=='USD':
        key_list[i][1]=(1/float((key_list[i][1])))
        currencylist.append(key_list[i][0][0])

    i=i+1

key_list_filtered = [item for item in key_list if 'USD' in item[0]]

for i in range(len(key_list_filtered)):
    key_list_filtered[i][0] = [currency for currency in key_list_filtered[i][0] if currency != 'USD']
key_list_filtered.append([['USD'],1.00])

currencies.clear()

for currency, rate in key_list_filtered:
    currencies[currency[0]] = rate

listofcurrencies=[]
for currency in currencies:
    listofcurrencies.append(currency)
print('-----------------------------------------------------------------------------------------------------------------------------------------')
print("This program uses live data to give you the most up to date conversions. The data is sourced from https://finance.yahoo.com/currencies/.")
print('-----------------------------------------------------------------------------------------------------------------------------------------')
print("Which two currencies would you like to convert between?\n")
print("You have the following options", listofcurrencies)
print('\nYour starting currency:')
starting_currency= input()
print('The currency you want to convert to:')
final_currency=input()
print('How many', starting_currency,'would you like to exchange?:')
initial_value=int(input())
converted_amount=(initial_value*(currencies[final_currency]/currencies[starting_currency]))
print('Your converted amount is', round(converted_amount,2), final_currency)