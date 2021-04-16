import time
from selenium import webdriver
from twocaptcha import TwoCaptcha
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.headless = True # True or False - Decide if you want a GUI for the browser
opts.add_argument("user-agent=Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)") # This user-agent makes sure you do not get banned from the website
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)
browser.minimize_window()
solver = TwoCaptcha('PUT API') # 2captcha.com API key needs to be put here
TEXT = 'Put your text message over here' # Message you want to send people
name = "dajkatal" # Put the name you want on the site

def register():
    try:
        browser.get('http://www.chatiw.com?old=interface')
        time.sleep(5)
        browser.find_element_by_id('input1').send_keys(name)  # Set name
        browser.find_element_by_xpath('//*[@id="age_list"]/option[2]').click()  # Set age to 18
        browser.find_element_by_xpath('//*[@id="start_form"]/div[5]/div/input[2]').click()  # Set female
        browser.find_element_by_id('submit_btn').click()  # Submit
        time.sleep(5)
        key = browser.find_element_by_xpath('//*[@id="bot_check_form"]/div[1]/div/div').get_attribute('data-sitekey')
        result = solver.recaptcha(sitekey=key, url=browser.current_url)
        browser.execute_script("document.querySelector('#g-recaptcha-response').textContent='{}'".format(result['code']))
        browser.execute_script('not_bot()')
        time.sleep(5)
    except Exception as e:
        print(e)
        browser.delete_all_cookies()
        register()

while True:
    try:
        register()
        time.sleep(5)
        try:
            element = browser.find_element_by_class_name('swal2-modal')
            browser.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)
        except:
            element = browser.find_element_by_id('respect_modal')
            element2 = browser.find_element_by_class_name('modal-backdrop')
            browser.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)
            browser.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element2)
        time.sleep(5)
        try:
            browser.find_element_by_xpath('//a[text()="Use the old interface"]').click()
        except Exception as e:
            print(e)

        time.sleep(5)
        inbox = browser.find_element_by_id('_inbox_btn')
        while True:
            try:
                inbox.click()
                time.sleep(5)
                table = browser.find_element_by_id('inbox_list')
                msgs = table.find_elements_by_tag_name("li")
                if len(msgs) == 1:
                    continue
                person = msgs[0]
                print(person)
                btns = person.find_elements_by_tag_name('a')
                try:
                    age = int(btns[0].find_elements_by_tag_name('span')[1].text)
                    print(age)
                    if age >= 25:
                        btns[0].click()
                        time.sleep(3)
                        browser.find_element_by_xpath('//*[@id="chat_textarea"]').send_keys(TEXT)
                        browser.find_element_by_xpath('//*[@id="chat_textarea"]').send_keys(Keys.ENTER)
                        inbox.click()
                    else:
                        btns[1].click()
                except:
                    try:
                        btns[1].click()
                    except:
                        inbox.click()
            except Exception as e:
                print(e)
                continue
    except:
        continue






