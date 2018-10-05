import mechanicalsoup

def westernunion():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.westernunion.com/us/en/send-money/app/start")
    print(browser.get_current_page())
    browser.select_form()
    browser["country"] = "India"
    exchRate = browser.get_current_page().select('span#exchangeRate')
    print(exchRate)

def xoom():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.xoom.com/india/send-money")    
    page = browser.get_current_page()
    messages = page.find("div", class_="js-exchange-rate")
    if messages:
        print(messages.text)
xoom()