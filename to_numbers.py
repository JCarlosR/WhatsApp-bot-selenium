# Send messages to phone numbers (registered as contacts or not)

# Required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel
import platform

os = platform.system()

# Read mobile phone numbers from a xlsx file
def readPhones(fileName):
    phones = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    first_column = sheet['A']
    for cell in range(len(first_column)):
        phone = str(first_column[cell].value)
        phones.append(phone)
    return phones

def initWebDriver():
	options = webdriver.ChromeOptions()
	if os == 'Linux':
		options.add_argument('DataChrome')
		options.add_argument("--disable-extensions") # disabling extensions
		options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
		options.add_argument("--no-sandbox")	
		return webdriver.Chrome(options=options, executable_path='/root/Documents/WhatsAppBot/drivers/chromedriver')
	else: # Windows
		options.add_argument('user-data-dir=D:\Python\WhatsAppBot\DataChrome')
		return webdriver.Chrome(options=options)

# Create a list with the numbers (in double quotes)
targets = readPhones('D:/Python/WhatsAppBot/numbers.xlsx')
# print(targets)

# Open browser via the Chrome web driver
driver = initWebDriver()

# Driver wait time (if internet connection is not good then increase the time)
# This time is used in the logic below
wait17 = WebDriverWait(driver, 17)
wait5 = WebDriverWait(driver, 5)

message = "This is an automated message sent from a bot (developed in Python). Please ignore."
    
success_count = 0
failed_list = []
i = 1

# Iterate over selected contacts
for target in targets:
    print(f'{i}- Target phone number: {target}')
    i += 1

    try:
        # Visit the corresponding link
        driver.get(f'https://api.whatsapp.com/send?phone={target}&text={message}')
        # time.sleep(2)

        send_xpath = '//a[contains(@title, "Share on WhatsApp")]'
        try:
            wait5.until(EC.presence_of_element_located((
                By.XPATH, send_xpath
            )))
        except Exception as e:
            print(e)          

        send_button = driver.find_element_by_xpath(send_xpath)
        # print('xpath found (send button)')
        send_button.click()
        print('send button clicked')
        
        # Select the input box        
        input_box_xpath = "//div[@contenteditable='true']"
        input_box = wait17.until(EC.presence_of_element_located((
            By.XPATH, input_box_xpath
        )))

        '''       
        # Send message
        # input_box.send_keys(f'Hey!')
        input_box.send_keys(f'Hi {target}!')
        input_box.send_keys(Keys.SHIFT + Keys.ENTER)
        input_box.send_keys(message + Keys.SPACE)
        '''
        input_box.send_keys(Keys.ENTER)

        print(f'Successfully sent message to {target}\n')

        success_count += 1
        time.sleep(0.5)
        input('Press Enter to send the next message')

    except Exception as e:
        print(e)
        failed_list.append(target)
        input('Failed message - Press Enter to continue')
        pass

print("Successfully sent to: ", success_count)
print("Failed messages: ", len(failed_list))
print(failed_list)
print() # empty line

time.sleep(2)
driver.quit()