from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
import webbrowser 
import requests 
import sys 
# import urllib 
import json 

def getUserAgent():
    user_agent = {"User-Agent": ""}
    options = Options() 
    options.add_argument("-headlessw")  
    driver = webdriver.Firefox(options=options)
    user_agent_key = driver.execute_script("return navigator.userAgent;")
    user_agent["User-Agent"] = user_agent_key
    driver.quit()
    return user_agent

def cliUrls(query): 
    header = user_agent
    url = f"https://google.com/search?q='{query}'"
    response = requests.get(url, headers=user_agent) 
    soup = BeautifulSoup(response.text, "html.parser") 

    title_objects = soup.find_all('h3') 
    links = soup.find_all('a')

    results = [] 
    
    for h3 in title_objects: 
        parent = h3.parent 
        if parent.name == 'a': 
            link = parent['href'] 
            title = h3.getText() 
            results.append((title, link)) 

    for index, (title, link) in enumerate(results, start=1):
        print(f"{title} \n {link}") 


# def webBrowser(): 

if __name__ == "__main__": 
    if len(sys.argv) < 2: 
        print("Usage: python3 isearch.py <query>") 
    else: 
        query = ' '.join(sys.argv[1:]) 
        
        user_agent = getUserAgent()
        cliUrls(query) 
