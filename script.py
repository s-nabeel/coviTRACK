# coviTRACK is a lightweight COVID-19 tracking application.
# Simply, enter the country in which you'd like to get statistics for, and
# then be greated with easy-to-read information.
# coviTRACK eliminates the need for digging around, scrolling and seeing pop-up ads with its
# simple, yet effective usecase.

import requests
from bs4 import BeautifulSoup

print("""\
\nWelcome to,
               _ _________  ___  _______ __
 _______ _  __(_)_  __/ _ \/ _ |/ ___/ //_/
/ __/ _ \ |/ / / / / / , _/ __ / /__/ ,<
\__/\___/___/_/ /_/ /_/|_/_/ |_\___/_/|_|
""")

user_country = input('Country: ')
user_request = 'https://www.worldometers.info/coronavirus/country/' + user_country.lower() + '/'

URL = user_request
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

headings = ['Coronavirus cases', 'Deaths', 'Recoveries']

heading_index = 0
totals = []

details = soup.find_all(class_ = 'maincounter-number')
print(f'\nCoronavirus details for: {user_country.upper()}\n')

for detail in details:
    print('', headings[heading_index].center(25))
    print('.........' + detail.get_text() + '.........\n')
    heading_index += 1
    totals.append(detail.get_text())

print('Summary'.center(28))
recovery_rate = round(int(totals[2].strip('\n').replace(',', '')) / int(totals[0].strip('\n').replace(',', '')) * 100, 2)
mortality_rate = round(int(totals[1].strip('\n').replace(',', '')) / int(totals[0].strip('\n').replace(',', '')) * 100, 2)
print(f'Current recovery rate: {recovery_rate} %')
print(f'Current mortality rate: {mortality_rate} %\n')

if recovery_rate >= 80:
    print(f'{user_country.upper()} is doing well based on current statistics!\n')
elif recovery_rate <= 79:
    print(f"{user_country.upper()} isn't doing too well based on current statistics.\n")
