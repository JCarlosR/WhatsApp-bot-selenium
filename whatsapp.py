# Keep all contacts unique
# Can save contact with their phone Number

# Required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel

# Read contacts from a xlsx file
def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = str(firstCol[cell].value)
        contact = "\"" + contact + "\""
        lst.append(contact)
    return lst

# Target Contacts, keep them in double colons
# Not tested on Broadcast
targets = readContacts("contacts.xlsx")

# can comment out below line
print(targets)

# Driver to open a browser
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=D:\Python\WhatsAppBot\DataChrome')
driver = webdriver.Chrome(options=options)

#link to open a site
driver.get("https://web.whatsapp.com/")

# 10 sec wait time to load, if good internet connection is not good then increase the time
# units in seconds
# note this time is being used below also
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)
input("Scan the QR code and then press Enter")

# Messages to send (at a particular time)
# 1st parameter: Hour (0-23)
# 2nd parameter: Minutes
# 3rd parameter: Seconds (keep it zero)
# 4th parameter: Text message to send 

# You can use '\n' in the message, it is identified as Enter Key.
# Keep a nice gap between successive messages.
# Keys.SHIFT + Keys.ENTER give a new line effect in your message.
msgToSend = [
    (
        22, 7, 0, 
        # "This is an automated message sent from a bot (developed in Python). Please ignore." + Keys.SHIFT + Keys.ENTER + "https://programacionymas.com"
        "This is an automated message sent from a bot (developed in Python). Please ignore."
    )
]

# Count variable to identify the number of messages to be sent
count = 0
while count < len(msgToSend):

    # Identify time
    curTime = datetime.datetime.now()
    curHour = curTime.time().hour
    curMin = curTime.time().minute
    curSec = curTime.time().second

    # if time matches then move further
    if msgToSend[count][0]==curHour and msgToSend[count][1]==curMin and msgToSend[count][2]==curSec:
        # variables to track count of success and fails
        success = 0
        sNo = 1
        failList = []

        # Iterate over selected contacts
        for target in targets:
            print(sNo, ". Target is: " + target)
            sNo+=1
            try:
                # Select the target
                x_arg = '//span[contains(@title,' + target + ') and contains(@class, "_1wjpf")]'
                try:
                    wait5.until(EC.presence_of_element_located((
                        By.XPATH, x_arg
                    )))
                except:
                    # If contact not found, then search for it
                    wait5.until(EC.presence_of_element_located((
                        By.CSS_SELECTOR, '.jN-F5.copyable-text.selectable-text'
                    )))

                    inputSearchBox = driver.find_element_by_css_selector('.jN-F5.copyable-text.selectable-text')
                    # print('class name found (input search box)', inputSearchBox)
                    time.sleep(0.5)

                    # click the search button
                    searchButton = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/div/button')
                    # print('xpath found (search button)', inputSearchBox)
                    searchButton.click()
                    time.sleep(1)

                    inputSearchBox.clear()
                    inputSearchBox.send_keys(target[1:len(target) - 1])
                    print('Target searched')
                    # Increase the time if searching a contact is taking a long time
                    time.sleep(3)

                # Select the target
                driver.find_element_by_xpath(x_arg).click()
                print('Target successfully selected: ', x_arg)
                time.sleep(2)

                # Select the Input Box
                inp_xpath = "//div[@contenteditable='true']"
                input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath
                )))
                time.sleep(1)

                # Send message
                # taeget is your target Name and msgToSend is you message
                input_box.send_keys(f'Hello {target}!')
                input_box.send_keys(Keys.SHIFT + Keys.ENTER)
                input_box.send_keys(msgToSend[count][3] + Keys.SPACE)

                # Wait for link preview (reduce this time if internet connection is good)
                # time.sleep(3)

                input_box.send_keys(Keys.ENTER)
                print("Successfully sent message to : "+ target + '\n')

                success += 1
                time.sleep(0.5)

            except Exception as e:
                # If target not found, add it to the failed List
                print("Could not find target: " + target)
                print(e)
                failList.append(target)
                pass

        print("\nSuccessfully sent to: ", success)
        print("Failed messages: ", len(failList))
        print(failList)
        print('\n\n')
        count += 1

driver.quit()