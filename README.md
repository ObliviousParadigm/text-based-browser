# text-based-browser

## Getting Started

This is a simple text-based browser which will scrape the data from the website entered by the user. It is mainly targetted towards those individuals who want to do everything from their browser, and those who don't want to spend their time scraping websites but want some data without using the mouse.

## Prerequisites

To run and use the project you need python, and pip.

## Installing

Run the following command to clone this repository and install the required Python libraries

```bash
git clone https://github.com/ObliviousParadigm/text-based-browser.git

pip install -r requirements.txt
```

## How to use the browser

- 'name_of_dir' argument is required, for now. This directory will be used to cache the websites you visit.
- All the websites you look for will be stored in the form of a stack. You can use the *back* command to go to the previous website.
- You can use the *exit* command to exit the browser.
- The links are highlighted in blue.

```bash
python3 browser.py name_of_dir
> Enter_name_of_website, say website1
...
> Enter_another_website, say website2
...
> back
'Takes you back to the previous website(ie, website1)'
>exit
```
