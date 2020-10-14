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
x = 0

details = soup.find_all(class_ = 'maincounter-number')
print(f'\nCoronavirus details for: {user_country}\n')
for detail in details:
    print('', headings[x].center(25))
    print('.........' + detail.get_text() + '.........\n')
    x += 1
