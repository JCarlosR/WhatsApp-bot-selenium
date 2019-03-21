# WhatsApp Bot

This is a simple WhatsApp Bot developed in Python using Selenium. 

Selenium is used mainly for automating web applications for testing purposes, but is certainly not limited to that. 
Boring web-based administration tasks can (and should!) be automated as well.

Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

# Features

  - Send a message to a particular contact at any time of the day.
  - Send a message to a chat group.
  - It's possible to add delays. This way, WhatsApp can detect URL and show its preview.
  - Contact names are read from a xlsx file.
  - It's possible to schedule messages, to multiple contacts, at different times.
  - The script can also search for the contact (if it's not present in recent chats) and then send the corresponding message.
  
### Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation
* [openpyxl](https://pypi.org/project/openpyxl/) - To read xls files

### Installation

Step 1: Install dependencies.

```sh
$ python -m pip install selenium
```

```sh
$ python -m pip install openpyxl
```

Step 2: Selenium requires a driver to interface with the chosen browser.

- [Click for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Click for FireFox](https://github.com/mozilla/geckodriver/releases)
- [Click for Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10)

Step 3: Extract the downloaded driver onto a folder.

Step 4: Set a new path variable to the environment. Paste this command to the terminal.

```sh
$ export PATH=$PATH:/home/path/to/the/driver/folder/
Eg: $ export PATH=$PATH:/home/harshit/Desktop/WhatsAppBot
```

Step 5: Run `whatsapp.py` using Python3
```sh
$ python whatsapp.py
```
Step 6: When the browser is opened web.whatsapp.com will be opened and will ask to scan a QR code for the first time.

Step 7: After Scanning the QR code, you will be asked to press Enter Key in the terminal.
