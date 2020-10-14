# coviTRACK is a lightweight COVID-19 tracking application.
# Simply enter the country in which you'd like to get statistics for, and
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
print('Current recovery rate:', round(int(totals[2].strip('\n').replace(',', '')) / int(totals[0].strip('\n').replace(',', '')), 2) * 100, '%')
print('Current mortality rate:', round(int(totals[1].strip('\n').replace(',', '')) / int(totals[0].strip('\n').replace(',', '')), 2) * 100, '%\n')
