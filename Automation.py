from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
# Configuration
#Change as per your details 
LINKEDIN_USERNAME = "abc@gmail.com"
LINKEDIN_PASSWORD = "abc123"
#You can Change as per your message It is just a Add Note 
NOTE_TEXT = "Hi {{name}},Great to connect with a fellow cybersecurity enthusiast!I'm excited to exchange insights and learn from your experience in the field..."

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
def login_to_linkedin():
    driver.get("https://www.linkedin.com/login")
    sleep(2)
    driver.find_element(By.ID, "username").send_keys(LINKEDIN_USERNAME)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(3)
#

def send_connection_requests(page):
        # EG: LINK : -> This is just an example link you can change as per your requirement go to search bar and search for the specific details and Copy the url and paste it here 
        driver.get(f'https://www.linkedin.com/search/results/people/?keywords=cyber%20security%20analyst&origin=SWITCH_SEARCH_VERTICAL&page={page}')
        sleep(3)

    # Find and iterate through "Connect" buttons
        connect_buttons = driver.find_elements(By.XPATH, "//button[span[text()='Connect']]")
        print(len(connect_buttons)) 
        for button in connect_buttons:
            button.click()
            sleep(2)
            try:
                # If "Add a note" appears, click it and send the note
                add_note_button = driver.find_element(By.XPATH, "//button[span[text()='Add a note']]")
                add_note_button.click()
                sleep(4)
                note_box = driver.find_element(By.ID, "custom-message")
                note_box.send_keys(NOTE_TEXT.replace("{{name}}", ""))
                driver.find_element(By.XPATH, "//button[span[text()='Send']]").click()
                print("Connection requests sent successfully.")
            except:
                # Otherwise, just click Send
                driver.find_element(By.XPATH, "//button[span[text()='Send']]").click()
            sleep(10)

    

# Main workflow
try:
    login_to_linkedin()
    for i in range(1,10): #You can change as per your requirement this is only page number after current page connect request sent to all the user it will navigate to the another page 
        send_connection_requests(i)
finally:
    driver.quit()
