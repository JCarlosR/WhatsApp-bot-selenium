# Send the corresponding message to the specified phone number

# Required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel
import sys, getopt

def read_arguments(args):
	try:
		opts, values = getopt.getopt(args, "hm:p:", ["message=","phone="])
	except getopt.GetoptError:
		print('python to_arguments.py -m <message> -p <phone>')
		sys.exit(2)

	# default values
	phone = ''
	message = "This is an automated message sent from a bot (developed in Python). Please ignore."

	for opt, arg in opts:
		if opt == '-h':
			print('python to_arguments.py -m <message> -p <phone>')
			sys.exit()
		elif opt in ("-m", "--message"):
			message = arg
		elif opt in ("-p", "--phone"):
			phone = arg

	return (phone, message)

# To read from arguments
arguments = read_arguments(sys.argv[1:])
phone = arguments[0]
message = arguments[1]

# input('Press Enter to send the message')
print(f'- Target phone number: {phone}')
print(f'- Message to send: {message}')

# Open browser via the Chrome web driver
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=D:\Python\WhatsAppBot\DataChrome')
driver = webdriver.Chrome(options=options)

# Driver wait time (if internet connection is not good then increase the time)
# This time is used in the logic below
wait17 = WebDriverWait(driver, 17)
wait5 = WebDriverWait(driver, 5)
    
success = False

# Iterate over selected contacts

try:
    # Visit the corresponding link
    driver.get(f'https://api.whatsapp.com/send?phone={phone}&text={message}')
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

    
    # Send message
    input_box.send_keys(Keys.ENTER)

    print(f'Successfully sent message to {phone}\n')

    success = True
    time.sleep(0.5)

except Exception as e:
    print(e)
    pass

print("Successfully sent?: ", success)
print() # empty line

time.sleep(2)
driver.quit()