from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
from pathlib import Path
import webbrowser 
import requests 
import sys 
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

def openConfig(): 
    with open(f"{config_path}", "r") as f: 
        config_vars = json.load(f) 
        return config_vars

def main(): 
    config_vars = openConfig()
    config = int(config_vars["Open_Tabs"]) 
    user_agent = getUserAgent() 
    title_objects, links = getUrls(query, user_agent) 

    results = [] 

    for h3 in title_objects: 
        parent = h3.parent 
        if parent.name == 'a': 
            link = parent['href'] 
            title = h3.getText() 
            results.append((title, link)) 

    for index, (title, link) in enumerate(results[:config], start=1):
        print(f"{title} \n {link}") 
        if open_browser == True: 
            webbrowser.open(link) 

if __name__ == "__main__": 

    script_path = Path(__file__).resolve() 
    config_path = script_path.with_name("searchconf.json")
    
    if len(sys.argv) < 2: 
        print("Usage: python3 isearch.py [-o] <query>") 
        sys.exit(1) 

    if sys.argv[1].lower() == "-o":
        if len(sys.argv) < 3: 
            print("Usage: python3 isearch.py -o <query>") 
            sys.exit(1)
        open_browser = True 
        query = ' '.join(sys.argv[2:])
        main()

    if sys.argv[1].lower() == "-e": 
        if len(sys.argv) < 3: 
            print("Usage: python3 isearch.py -e <integer>")
            sys.exit(1) 
        config_vars = openConfig()
        config_vars["Open_Tabs"] = sys.argv[2]
        with open(f"{config_path}", "w") as f: 
            json.dump(config_vars, f) 
        print(f"Result variable set to {sys.argv[2]}") 

    else: 
        open_browser = False 
        query = ' '.join(sys.argv[1:]) 
        main()
