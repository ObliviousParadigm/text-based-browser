import requests
import sys
import os
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore, Style


# Saving the data locally, if a directory has been specified
def save_local(dir_name, url, data):
    stripped_name = url.rsplit(".", 1)[0].lstrip('https://www.')
    with open(f'{dir_name}/{stripped_name}.txt', 'w') as local:
        # Writing the shortened url and its data
        local.write(data)


def scrape_and_display(url):
    r = requests.get(url)
    page = ""
    soup = BeautifulSoup(r.content, 'html.parser')
    body = soup.find('body')  # get body by tag <body></body>
    descendants = body.descendants
    for descendant in descendants:
        if descendant.name in ["p", 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']:
            try:
                if descendant.name == 'a':
                    page += Fore.BLUE + descendant.get_text().strip()
                else:
                    page += Style.RESET_ALL + descendant.get_text().strip()  # try to get descendants content.
            except:
                pass
        else:
            pass
    print(page)
    return page


# Getting the name of the directory and creating the back button
args = sys.argv
dir_name = args[1]
back_button = deque()

# Create directory if it doesn't exist already
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

page = input()
flag = 1  # Assuming that the website is invalid

while page != 'exit':
    # Check for Cache / Error first
    if not ('.' in page):
        flag = 0  # Website is valid
        name = page.lstrip('https://')
        # print file if it exists
        if os.path.isfile(f'{dir_name}/{name}.txt'):
            with open(f'{dir_name}/{name}.txt') as file:
                print(file.readlines())
        else:
            # no cache file and no '.'
            print('Error: Incorrect URL')

    else:
        # Making sure to add https to the starting of the site
        if not page.startswith('https://'):
            page = f'https://{page}'
        data = scrape_and_display(page)
        # Creating a local copy
        save_local(dir_name, page, data)

    if not flag:
        print('Error: File does not exist')
        flag = 1

    new_page = input()
    if new_page == 'back':
        page = back_button.pop()
    else:
        back_button.append(page)
        page = new_page
