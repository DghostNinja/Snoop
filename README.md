# Snoop - The Open Redirect Tester


## Description

A Python-based tool to test for open redirect vulnerabilities in web applications.  
It checks for both server-side and JavaScript-based redirects using common parameters and payloads.

## Features

- ✅ Detects open redirects using common redirect parameters (`redirect`, `url`, `next`, etc.).
- ✅ Uses various payloads to identify potential vulnerabilities.
- ✅ Supports session-aware testing (cookies).
- ✅ Detects JavaScript-based redirects using Selenium.
- ✅ Randomized user-agents and request delays for stealth.

## Requirements

- Python 3.x
- Google Chrome (for Selenium headless testing)
- Chrome WebDriver

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/DghostNinja/Snoop.git
   cd Snoop
   ```

2. Install dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

3. Ensure you have Google Chrome and ChromeDriver installed:
   - [Download Chrome](https://www.google.com/chrome/)
   - [Download ChromeDriver](https://chromedriver.chromium.org/downloads)
   - Or use `webdriver-manager`:
   ```sh
   pip3 install webdriver-manager
   ```

## Running the Tool

To run the script manually:
```sh
python3 snoop.py
```

## Adding Snoop to `/usr/bin/` for Global Access

To run `snoop` from anywhere in the terminal, follow these steps:

1️⃣ **Make the script executable**  
```sh
chmod +x snoop.py
```

2️⃣ **Move it to `/usr/bin/`**  
```sh
sudo mv snoop.py /usr/bin/snoop
```
or create a symbolic link:
```sh
sudo ln -s "$(pwd)/snoop.py" /usr/bin/snoop
```

3️⃣ **Run from anywhere**  
Now, you can simply type:
```sh
snoop
```
instead of `python3 snoop.py`.

### Alternative: Using a Python Shebang (`#!`)
Modify the first line of `snoop.py` to specify the Python interpreter:
```python
#!/usr/bin/env python3
```
This ensures that it runs with Python 3 when executed.

Then, repeat **Step 1** and **Step 2**, and now you can execute `snoop` globally.

## Example Usage

```plaintext

  ___|                              
 \___ \   __ \    _ \    _ \   __ \  
       |  |   |  (   |  (   |  |   | 
 _____/  _|  _| \___/  \___/   .__/  
                              _|     

        Open Redirect Tester by iPsalmy

Enter the target website URL: https://example.com
[>] Testing: https://example.com?redirect=http://evil.com
[!!] Possible Open Redirect! Status: 302, Location: http://evil.com
[*] Following redirect: http://evil.com
[+] Testing for JavaScript-based redirects...
[!!] JavaScript Redirect Detected: http://attacker.com
```
### You can test with this vulnerable docker built for open redirect testing 
   ***Link: https://github.com/DghostNinja/vulnerable-redirect-app***

##


## Troubleshooting

- **ChromeDriver Errors**: Ensure ChromeDriver is installed and matches your Chrome version.
- **Permission Issues**: Run with elevated permissions:
  ```sh
  chmod +x snoop.py
  python3 snoop.py
  ```
- **WebDriver Issues**: If ChromeDriver is missing or outdated, install `webdriver-manager`:
  ```sh
  pip3 install webdriver-manager
  ```

## Disclaimer

This tool is for educational and security testing purposes only.  
Do **not** use it on systems without explicit permission.🚀
