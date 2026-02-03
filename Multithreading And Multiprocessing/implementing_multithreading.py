'''
Real-World Example: Multithreading for I/O - bound tasks 
Scenario: Web Scrapping 

Web scrapping often involves making numerous netowrk request to 
fetch with pages. These tasks are I/O -bound beacuse they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the perfomance by allowing multiple web pages to be fetched concurrenltly 

'''

'''
https://python.langchain.com/v0.2/docs/introduction/

https://docs.langchain.com/oss/python/releases/changelog

https://reference.langchain.com/python/deepagents/

'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://docs.langchain.com/oss/python/releases/changelog',
    'https://reference.langchain.com/python/deepagents/'
]

output_file = "scraped_content.txt"
file_lock = threading.Lock()

def fetch_content(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)

        # Thread-safe file writing
        with file_lock:
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(f"\n{'='*80}\n")
                f.write(f"URL: {url}\n")
                f.write(f"{'='*80}\n")
                f.write(text)
                f.write("\n\n")

        print(f"[✓] Fetched and saved: {url}")

    except Exception as e:
        print(f"[✗] Failed to fetch {url} → {e}")
        
threads = []

if __name__ == "__main__":
    for url in urls:
        thread = threading.Thread(target=fetch_content, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All web pages extracted and saved.")
