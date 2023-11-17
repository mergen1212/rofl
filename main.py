from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from multiprocessing import Pool
import os
def OneG(driver, URL: str) -> list[str]:
    li: list[str] = []
    driver.get(URL)
    # time.sleep(1.5)
    element = driver.find_elements(By.XPATH, '//*[@id="arrticle"]')
    for div in element:
        li.append(div.text)
    return li


# opts.add_argument('--headless')
# opts.add_argument("window-size=1400,600")

d={
    # "a-will-eternal":
    # [
    # "https://ranobes.com/chapters/a-will-eternal/246198-golossarij.html",1315
    # ],
    # "Tales_of_Herding_Gods":
    # [
    #     "https://ranobes.com/chapters/the-hero-returns/402306-1.html",1735
    # ],
    "Against the Gods":[
        "https://ranobes.com/chapters/against-the-gods/100834-nprolog.html",2036
    ]
}

def get_data(n):
    try:
        global d
        URL=d[n][0]
        count=d[n][1]
        opts = Options()
        ua = UserAgent()
        user_agent = ua.random
        opts.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(opts)
        driver.set_script_timeout(30)
        if not(n in os.listdir(path=".")):
            os.mkdir(n)

        for i in range(1, count + 1):
            li: list[str] = OneG(driver, URL)
            with open(f"{n}\\{i}.txt", "w", encoding='utf-8') as f:
                f.writelines('\n'.join(li))
            x = '//*[@id="next"]'
            elo = driver.find_element(By.XPATH, x).click()
            URL = driver.current_url
            print(URL)
        print(d['a-will-eternal'])
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":

    p=Pool(processes=len(d))

    p.map(get_data,d)
