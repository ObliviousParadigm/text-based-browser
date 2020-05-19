import requests
import sys
import os
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore


# Saving the data locally, if a directory has been specified
def save_local(dir_name, url, data):
    stripped_name = url.rsplit('.', 1)[0].lstrip('https://www.')
    with open(f'{dir_name}/{stripped_name}', 'w') as local:
        # Writing the shortened url and its data
        local.write(data)

# Display the cached data
def read_cached(dir_name, name):
    with open(f'{dir_name}/{name}') as file:
        for line in file:
            print(line, end='')

def scrape_and_display(url):
    try:
        # Send GET request
        r = requests.get(url)
        scraped_data = ''

        # Retrieve the data
        soup = BeautifulSoup(r.content, 'html.parser')

        # This list can be customized to the user's needs
        scrape_list = ['p', 'h1', 'h2', 'h3', 'il', 'h4', 'h5', 'h6', 'ul', 'ol']

        # Get body and title
        body = soup.find('body')
        title = soup.html.head.title.text + '\n'

        # Storing the title in a different color
        scraped_data += Fore.MAGENTA + title + Fore.RESET

        descendants = body.descendants
        for tag in descendants:
            # Highlight the anchor tags in blue
            if tag.name == 'a':
                scraped_data += Fore.BLUE + tag.text + Fore.RESET + '\n'
            elif tag.name in scrape_list:
                scraped_data += tag.text + '\n'
    except requests.exceptions.RequestException:
        scraped_data = Fore.RED + 'Error performing GET request' + Fore.RESET

    print(scraped_data)
    return scraped_data


# Getting the name of the directory
# If directory doesn't exist, create one
args = sys.argv
try:
    dir_name = args[1]
except IndexError:
    dir_name = 'cache'

# Create directory if it doesn't exist already
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

# Creating the back button
back_button = deque()

# Getting the first input
page = input('> ')
flag = 1  # Assuming that the website is invalid

while page != 'exit':

    # Check for Cache / Error first
    if not ('.' in page):
        flag = 0  # Website is valid
        name = page.lstrip('https://')
        # print file if it exists
        if os.path.isfile(f'{dir_name}/{name}'):
            read_cached(dir_name, name)
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

    if flag:
        print('Error: File does not exist')
        flag = 1

    # Get next input
    new_page = input('> ')

    # Check if user wants to go back
    if new_page == 'back':
        page = back_button.pop()
    else:
        back_button.append(page)
        page = new_page
