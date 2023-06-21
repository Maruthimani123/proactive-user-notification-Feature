import schedule
import time
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def job():
    OPTIONS = Options()
    OPTIONS.add_argument("--incognito")
    OPTIONS.add_argument('--disable-infobars')
    OPTIONS.add_argument("--start-fullscreen")
    OPTIONS.add_argument("--ignore-certificate-errors")
    OPTIONS.add_experimental_option("excludeSwitches", ['enable-automation'])
    OPTIONS.add_experimental_option('useAutomationExtension', False)
    OPTIONS.add_experimental_option(
        'prefs', {
            'credentials_enable_service': False,
            'profile': {
                'password_manager_enabled': False
            }
        }
    )

    # Initialize Chrome driver
    
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=OPTIONS)

    # Gmail account credentials for sending emails
    sender_email = "maruthimani05@gmail.com"
    sender_password = "xerj afhz xioa kfbp"
    recipient_email = "maruthimani05@gmail.com"

    # Function to send email
    def send_email(subject, message):
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print("Failed to send email.")
            print(e)


    # LinkedIn login
    linkedin_username, linkedin_password = 'vcmmguptha@gmail.com', 'M@ruthimani2003'
    url = "https://www.linkedin.com/login"
    driver.get(url)
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(linkedin_username)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(linkedin_password)
    password_field.submit()

    # Manual verification
    message_xpath = '//*[@id="ember12"]//span[@class="notification-badge__count "]'
    notification_xpath = '//*[@id="ember13"]//span[@class="notification-badge__count "]'
    messages_count = driver.find_element(By.XPATH, message_xpath).text
    notification_count = driver.find_element(By.XPATH, notification_xpath).text

    # Print the message and notification counts
    print("Messages count:", messages_count)
    print("Notifications count:", notification_count)
    send_email(subject='Notification mail',message='messages count : {} \n Notifications count : {}'.format(messages_count,notification_count))
    # Close the driver
    driver.quit()
job()
# Schedule the job to run every 3 hours
schedule.every(3).hours.do(job)



while True:
    schedule.run_pending()
    time.sleep(1)