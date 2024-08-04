from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
import webbrowser 
import requests 
import sys 
# import urllib 
import json 

def getUserAgent():
    options = Options() 
    options.add_argument("-headless")  
    driver = webdriver.Firefox(options=options)
    user_agent = driver.execute_script("return navigator.userAgent;")
    driver.quit()
    return {"User-Agent": user_agent}   

def getUrls(query, user_agent): 
    url = f"https://google.com/search?q='{query}'"
    response = requests.get(url, headers=user_agent) 
    soup = BeautifulSoup(response.text, "html.parser") 

    title_objects = soup.find_all('h3') 
    links = [a['href'] for a in soup.find_all('a', href=True)]

    return title_objects, links 

def main(title, link): 
    results = [] 
    
    for h3 in title_objects: 
        parent = h3.parent 
        if parent.name == 'a': 
            link = parent['href'] 
            title = h3.getText() 
            results.append((title, link)) 

    for index, (title, link) in enumerate(results, start=1):
        print(f"{title} \n {link}") 


if __name__ == "__main__": 
    if len(sys.argv) < 2: 
        print("Usage: python3 isearch.py <query>") 
    else: 
        query = ' '.join(sys.argv[1:]) 
        
        user_agent = getUserAgent()
        title_objects, links = getUrls(query, user_agent) 
        main(title_objects, links)
