---

### `README.md`
```md
# Snoop - The Open Redirect Tester

## Description

A Python-based tool to test for open redirect vulnerabilities in web applications.  
It checks for both server-side and JavaScript-based redirects using common parameters and payloads.

## Features

- Detects open redirects using common redirect parameters (`redirect`, `url`, `next`, etc.).
- Uses various payloads to identify potential vulnerabilities.
- Supports session-aware testing (cookies).
- Detects JavaScript-based redirects using Selenium.
- Randomized user-agents and request delays for stealth.

## Requirements

- Python 3.x
- Google Chrome (for Selenium headless testing)
- Chrome WebDriver

## Installation

1. Clone the repository:
   ```sh
   git clone https://git@github.com:DghostNinja/Snoop.git
   cd open-redirect-tester
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Ensure you have Google Chrome and ChromeDriver installed:
   - [Download Chrome](https://www.google.com/chrome/)
   - [Download ChromeDriver](https://chromedriver.chromium.org/downloads)

## Usage

Run the script and enter a target URL when prompted:

```sh
python snoop.py
```

## Example

```plaintext
Enter the target website URL: https://example.com
[>] Testing: https://example.com?redirect=http://evil.com
[!!] Possible Open Redirect! Status: 302, Location: http://evil.com
[*] Following redirect: http://evil.com
[+] Testing for JavaScript-based redirects...
[!!] JavaScript Redirect Detected: http://attacker.com
```

## Disclaimer

This tool is for educational and security testing purposes only.  
Do **not** use it on systems without explicit permission.
```

---

### `requirements.txt`
```txt
requests
selenium
```
