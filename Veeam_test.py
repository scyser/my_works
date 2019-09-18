from selenium import webdriver
import time

# entering data

input_country = input("Enter country: ").strip().title()
input_language = input("Enter language: ").strip().capitalize()
input_quantity_vac = int(input("Enter quantity of expected vacancies: "))

# dictionary of available languages

code_languages = {
    "Arabic": "ch-1",
    "Chinese": "ch3",
    "Czech": "ch-4",
    "English": "ch-7",
    "French": "ch-10",
    "German": "ch-11",
    "Italian": "ch-15",
    "Portuguese": "ch-20",
    "Russian": "ch-22",
    "Spanish": "ch-24",
    "Turkish": "ch-26"
}

# test accordance of entered and real data

try:
    browser = webdriver.Chrome()
    browser.get("https://careers.veeam.com/")
    browser.maximize_window()
    
    browser.implicitly_wait(5)
    try:
        cookie = browser.find_element_by_css_selector("a.cookie-messaging__button")
        cookie.click()
    except:
        pass
    time.sleep(1)
    country_list = browser.find_element_by_css_selector("#country-element")
    country_list.click()
    country = browser.find_element_by_css_selector("#country-element .scroller-content [data-value='{0}']".format(input_country))
    country.click()

    language_list = browser.find_element_by_css_selector("#language")
    language_list.click()
    language = browser.find_element_by_css_selector("#language [for='{0}']".format(code_languages[input_language]))
    language.click()

    apply = browser.find_element_by_css_selector("#language .selecter-fieldset-submit")
    apply.click()

    show_vacancies = browser.find_element_by_css_selector(".content-loader-button")
    show_vacancies.click()
    time.sleep(1)
    all_vacancies_1 = browser.find_elements_by_css_selector(".vacancies-blocks-container:nth-child(2) .vacancies-blocks-col")
    all_vacancies_2 = []
    if len(all_vacancies_1) == 12:
        all_vacancies_2 = browser.find_elements_by_css_selector(".vacancies-blocks-container:nth-child(3) .vacancies-blocks-col")
    quantity_vac = len(all_vacancies_1) + len(all_vacancies_2)
    assert quantity_vac == input_quantity_vac, "Failed test! :( Entered {0}, found {1}.".format(input_quantity_vac, quantity_vac)
    print("Successful test!")
finally:
    browser.quit()