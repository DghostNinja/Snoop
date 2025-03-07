import requests
import time
import random
import re
from urllib.parse import urlencode, urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ASCII Banner
ASCII_BANNER = """
   ___|                              
 \___ \   __ \    _ \    _ \   __ \  
       |  |   |  (   |  (   |  |   | 
 _____/  _|  _| \___/  \___/   .__/  
                              _|     

        Open Redirect Tester by iPsalmy
"""

# List of common browser user-agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/537.36"
]

# Common redirect parameters developers use
COMMON_REDIRECT_PARAMS = ["redirect", "url", "next", "return", "returnTo", "destination", "goto", "forward", "continue"]

# Common payloads for open redirect testing with different variations
PAYLOADS = [
    "http://evil.com", "https://attacker.com", "//evil.com", "//google.com", "//127.0.0.1", "//localhost",
    "\\evil.com", "%2Fevil.com", "%2F%2Fevil.com", "%5C%5Cevil.com",
    "targetsite.com@evil.com", "targetsite.com//evil.com", "//www.google.com/%2Fevil.com"
]

# Function to setup Selenium headless browser
def setup_browser():
    options = Options()
    options.headless = True
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=options)

def test_open_redirect(base_url, session, cookies=None):
    """Tests for open redirects using predefined redirect parameters and payloads."""
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Referer": base_url
    }
    
    if cookies:
        headers["Cookie"] = cookies  # Enable session-aware testing
    
    for param in COMMON_REDIRECT_PARAMS:
        for payload in PAYLOADS:
            full_url = f"{base_url}?{urlencode({param: payload})}"
            print(f"[>] Testing: {full_url}")
            time.sleep(random.uniform(1.5, 3.5))  # Random delays for WAF evasion
            try:
                response = session.get(full_url, headers=headers, allow_redirects=False, timeout=5)
                location_header = response.headers.get('Location', '')
                
                if location_header == payload:
                    print(f"[!!] Possible Open Redirect! Status: {response.status_code}, Location: {location_header}")
                elif payload in location_header:
                    print(f"[!] Partial Match (May be Sanitized): Status: {response.status_code}, Location: {location_header}")
                elif payload in response.text:
                    print(f"[!] Payload Found in Response Body: Status: {response.status_code}")
                else:
                    print(f"[-] Not Vulnerable: Status: {response.status_code}, Location: {location_header}")
                
                # Recursive redirect chain analysis
                if 300 <= response.status_code < 400 and 'Location' in response.headers:
                    redirected_url = response.headers['Location']
                    print(f"[*] Following redirect: {redirected_url}")
                    test_open_redirect(redirected_url, session, cookies)
                
            except requests.RequestException as e:
                print(f"[-] Request failed: {e}")

# Function to test JavaScript-based redirects with Selenium
def test_js_redirects(target_url):
    browser = setup_browser()
    try:
        print("[+] Testing for JavaScript-based redirects...")
        browser.get(target_url)
        time.sleep(3)  # Wait for potential redirect
        final_url = browser.current_url
        if final_url != target_url:
            print(f"[!!] JavaScript Redirect Detected: {final_url}")
        else:
            print("[-] No JavaScript redirect found.")
    finally:
        browser.quit()

if __name__ == "__main__":
    print(ASCII_BANNER)
    target_url = input("Enter the target website URL: ").strip()
    session = requests.Session()
    
    # Test normal and JS-based redirects
    test_open_redirect(target_url, session)
    test_js_redirects(target_url)
