from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from mongo import MongoConnection
from datos import index

db_client = MongoConnection().client
db = db_client.get_database('TFINALTD')
col = db.get_collection('peliPuss')

driver = webdriver.Chrome()
driver.get("https://pelisplus.ai/")
panel_conte = driver.find_elements(By.CLASS_NAME, "main__right")


for a in panel_conte:
    #encabez = a.find_element(by=By.TAG_NAME, value="message")
    agg_reciente = a.find_element(by=By.CSS_SELECTOR, value="#wrapper__main > div.main__right > div:nth-child(2)").text.split(",")
    recomenda= a.find_element(by=By.CSS_SELECTOR, value="#wrapper__main > div.main__right > div:nth-child(3)").text
    estrenos = a.find_element(by=By.CSS_SELECTOR, value="#wrapper__main > div.main__right > div.index-module__box___Lufb8.box--slider").text
    print(agg_reciente)
    document = {
        "agg_reciente": agg_reciente,
        "recomenda": recomenda,
        "estrenos": estrenos,

    }

    col.insert_one(document=document)
index()
driver.close()