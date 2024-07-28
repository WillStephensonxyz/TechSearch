from bs4 import BeautifulSoup
import webbrowser 
import requests 
import sys 
# import urllib 
import json 

def cliUrls(query): 
    url = f"https://google.com/search?q='{query}'"
    response = requests.get(url) 
    soup = BeautifulSoup(response.text, "html.parser") 

    title_objects = soup.find_all('h3') 

    for info in title_objects: 
        print(info.getText()) 

# def webBrowser(): 

if __name__ == "__main__": 
    if len(sys.argv) < 2: 
        print("Usage: python3 isearch.py <query>") 
    else: 
        query = ' '.join(sys.argv[1:]) 
        cliUrls(query) 
