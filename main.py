from selenium import webdriver
import csv
import time

driver = webdriver.Firefox()
page_now = 0
url = ''


def load_document(name):
    file = open(name, 'r', encoding='UTF-8').readlines()
    return map(lambda x: x.replace('\n', '').split(';'), file)


def open_page(request):
    global form, button
    form.clear()
    form.send_keys(request)
    time.sleep(0.2)
    button.click()
    form = driver.find_element_by_name('text')
    button = driver.find_element_by_xpath(
        '/html/body/header/div/div/div[3]/form/div[2]/button')


queries = list(load_document('errors.txt'))

out = csv.writer(open('out3.csv', 'w', encoding='UTF-8'), delimiter=';', quotechar='"')

driver.get('https://yandex.ru/search/?lr=43&text=лицей')
form = driver.find_element_by_name('text')
button = driver.find_element_by_xpath(
    '/html/body/header/div/div/div[3]/form/div[2]/button')

for i in queries:
    try:
        name = i[0]
        num = i[1]
    except:
        continue
    try:
        open_page(f'{name} url:"magazintrav.ru*"')
        errors = driver.find_elements_by_class_name('misspell__error')
        results_num = driver.find_elements_by_class_name('serp-adv__found')
        not_found = driver.find_elements_by_class_name('misspell__message')
        if errors:
            print(errors[0].text)
            out.writerow([name, num, errors[0].text,
                        " ".join(results_num[0].text.split()[1:-1])])
        elif not_found:
            print('Ничего')
            out.writerow([name, num, not_found[0].text, 0])
        else:
            print('ok')
            out.writerow([name, num, 'ok', " ".join(
                results_num[0].text.split()[1:-1])])
    except:
        print(f'Ошибка запроса {name}')
        if 'Нам очень жаль, но запросы, поступившие с вашего IP-адреса, похожи на автоматические.' in driver.page_source:
            driver.delete_all_cookies()
            time.sleep(10)
            driver.get('https://yandex.ru/search/?lr=43&text=кино')
            form = driver.find_element_by_name('text')
            button = driver.find_element_by_xpath(
                '/html/body/header/div/div/div[3]/form/div[2]/button')
        time.sleep(1)
    page_now += 1
    if page_now % 100 == 0:
        print(page_now)
