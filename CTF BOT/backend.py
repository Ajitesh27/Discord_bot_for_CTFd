import os
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from validate_email import validate_email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import csv
import base64
from datetime import datetime
import pytz


def validate(receiver):
    if validate_email(receiver, verify=True):
        return True
    else:
        return False


def send_mail(username, receiver, user_password):
    sender = "noreply.kalpanaCTF@gmail.com"
    passwd = "3m411_f02_k41p4n4_c7f"
    subject = "Credentials for Kalpana 2020 CTF"
    message = f"Hello {username},\nHere are your credentails for the Kalpana 2020 CTF:\nUsername: {username}\nPassword: {user_password} \n\nLink to the CTF will be provided as soon as the event starts.\n\nThanks & Regards"

    session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    session.login(sender, passwd)

    email = MIMEMultipart()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject
    email.attach(MIMEText(message))

    session.sendmail(sender, receiver, email.as_string())
    session.quit()

    return 0


def register(username, mail):
    
    base_url = "http://52.230.99.155"

    if not validate(mail):
        return False

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
    driver.get(f"{base_url}/register")

    name = driver.find_element_by_name("name")
    name.clear()
    name.send_keys(username)

    email = driver.find_element_by_name("email")
    email.clear()
    email.send_keys(mail)

    passwd = subprocess.check_output("cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1", shell=True).decode('utf-8').strip()
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(passwd)

    password.send_keys(Keys.RETURN)

    driver.get(f"{base_url}/logout")
    driver.close()

    send_mail(username, mail, passwd)

    return True


def register_all(member_list):
    with open("participants.csv", "r") as file:
        participants = csv.reader(file)

        for line in participants:
            if line[0] in member_list:
                register(line[0], line[1])
            else:
                print(f"Cannot register {line[1]}")


def firstblood():
    username = "ctf_bot"
    passwd = "h4nd5_0ff_my_4cc0un7"
    base_url = "http://52.230.99.155"    

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    driver.get(f"{base_url}/login")

    name = driver.find_element_by_name("name")
    name.clear()
    name.send_keys(username)

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(passwd)

    password.send_keys(Keys.RETURN)

    driver.get(f"{base_url}/admin/challenges")

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')

    chal_count = 0
    chal_name = []
    for _ in soup.find_all("td", class_='d-block border-right text-center'):
        chal_count += 1
        chal_name.append(str(soup.find_all("a", href=f'/admin/challenges/{chal_count}')[0]).split(">")[1][:-3])

    blood_list = {}
    for i in range(1, chal_count + 1):
        driver.get(f"{base_url}/admin/submissions/correct?field=challenge_id&q={i}")
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        team_list = []
        for ele in soup.find_all("td", class_='team'):
            team_list.append(str(ele))

        if len(team_list) > 0:
            blood_team = team_list[-1].split('\n')[2].strip()
            blood_list[chal_name[i - 1]] = blood_team

    driver.close()

    new_blood_list = json.dumps(blood_list, indent=4)

    message = ""

    with open("firstblood.json") as blood_file:
        parsed = json.load(blood_file)
        old_blood_list = json.dumps(parsed, indent=4)

        if new_blood_list == old_blood_list:
            return "NULL"
        else:
            for key, value in blood_list.items():
                if key not in old_blood_list:
                    message += f"First blood stolen by **{value}** for **{key}**\n"

            with open("firstblood.json", "w") as blood_file:
                blood_file.write(new_blood_list)

    return message


def send_backup_mail():
    UTC = pytz.utc
    timeZ_Kl = pytz.timezone('Asia/Kolkata')
    sender = "noreply.kalpanaCTF@gmail.com"
    passwd = "3m411_f02_k41p4n4_c7f"
    subject = "CTF backup-" + str(datetime.now().astimezone(timeZ_Kl))
    message = f"Backup for Kalpana CTF"

    session = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    session.login(sender, passwd)

    # Add all challenge-creators emails here
    receivers = ['keshav.raju.r@gmail.com', 'vihardevalla@gmail.com', 'aasim.md00@gmail.com']

    email = MIMEMultipart()
    email['From'] = sender
    email['To'] = ", ".join(receivers)
    email['Subject'] = subject
    email.attach(MIMEText(message))

    for backup_file in os.listdir():
        if backup_file.startswith("Kalpana"):
            break

    base64.encode(open(backup_file, 'rb'), open('encrypted_backup.txt', 'wb'))

    filename = os.path.basename("encrypted_backup.txt")
    attachement = open("encrypted_backup.txt", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachement.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachement; filename={filename}")
    email.attach(part)

    session.sendmail(sender, receivers, email.as_string())
    session.quit()

    os.remove("encrypted_backup.txt")

    return 0


def backup():
    for backup_file in os.listdir():
        if backup_file.startswith("Kalpana"):
            os.remove(backup_file)
            break

    username = "ctf_bot"
    passwd = "h4nd5_0ff_my_4cc0un7"
    base_url = "http://52.230.99.155"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--window-size=1440, 900")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    prefs = {'download.default_directory': os.getcwd(),
             'download.prompt_for_download': False,
             'download.directory_upgrade': True,
             'safebrowsing.enabled': False,
             'safebrowsing.disable_download_protection': True}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': os.getcwd()}}
    command_result = driver.execute("send_command", params)

    '''
    print("response from browser:")
    for key in command_result:
        print("result:" + key + ":" + str(command_result[key]))
    '''

    driver.get(f"{base_url}/login")

    name = driver.find_element_by_name("name")
    name.clear()
    name.send_keys(username)

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(passwd)

    password.send_keys(Keys.RETURN)

    driver.get(f"{base_url}/admin/export")

    flag = True
    while flag:
        for backup_file in os.listdir():
            if backup_file.startswith("Kalpana") and backup_file.endswith("zip"):
                flag = False
                break

    driver.close()

    send_backup_mail()
    
    return 0
