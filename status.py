import requests
from bs4 import BeautifulSoup
import smtplib


def check_status():
        URL='https://www.amazon.in/dp/B081JWZQJB/ref=fs_a_mn_3'
        headers={
            "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
            } 
        page = requests.get(URL,headers=headers)
        #gets the page



        soup = BeautifulSoup(page.content,'html.parser')

        #prints the page contentd
        #print(soup.prettify())

        status=soup.find(id="availability",text=False, recursive=True).get_text()
        strippedStatus=status.strip()
        currentstatus=strippedStatus[0:21]
        print(strippedStatus[0:21])
        if currentstatus == "Currently unavailable":
            send_mail()



def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(youremail1,yourpassword1)
    subject="Product in stock"
    body="Check the product https://www.amazon.in/dp/B081JWZQJB/ref=fs_a_mn_3"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        youremail1,
        youremail2,
        msg
    )
    print("email sent")
    server.quit()

check_status()