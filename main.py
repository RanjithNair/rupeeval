import mechanicalsoup
import requests

def westernunion():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.westernunion.com/us/en/send-money/app/start")
    print(browser.get_current_page())
    browser.select_form()
    browser["country"] = "India"
    exchRate = browser.get_current_page().select('span#exchangeRate')
    print(exchRate)

def xoom():
    print("****** XOOM ******")
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.xoom.com/india/send-money")    
    page = browser.get_current_page()
    messages = page.find("div", class_="js-exchange-rate")
    if messages:
        print(messages.text)


def remitly():
    print("****** REMITLY ******")
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.remitly.com/us/en/india/pricing")
    page = browser.get_current_page()
    rates = page.find("div", class_="f1jkwmje fawncrr")
    if rates:
        print(rates.text)

def forex():
    print("****** FOREX RATES *******")
    r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y')
    print(r.json()['USD_INR']['val'])

xoom()
remitly()
forex()