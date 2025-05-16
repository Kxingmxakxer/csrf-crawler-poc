import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

def crawl(url):
    print(f"[INFO] Crawling {url}...")
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        forms = soup.find_all('form')

        for i, form in enumerate(forms, 1):
            print(f"\n[FORM {i}] {form.get('action')}")
            inputs = form.find_all('input')
            has_csrf = any('csrf' in inp.get('name', '').lower() for inp in inputs)

            if has_csrf:
                print("  [+] CSRF Token Detected")
            else:
                print("  [-] No CSRF Token Found")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <URL>")
    else:
        crawl(sys.argv[1])
