#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import datetime as dt
import pandas as pd
import numpy as np
from getpass import getpass
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def start_chrome():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  # 画面サイズの最大化
    # Google Classroomの取得したい課題のURLを指定
    driver.get(url)
    return driver


def login_classroom(driver):

    wait_time = 30
    # IDを入力
    login_id_xpath = '//*[@id="identifierNext"]'

    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_name("identifier").send_keys(login_id)
    driver.find_element_by_xpath(login_id_xpath).click()
    # パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    driver.find_element_by_name("password").send_keys(login_pw)
    time.sleep(5)  # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath(login_pw_xpath).click()
    time.sleep(5)


def get_html(driver):
    # HTMLを取得
    time.sleep(10)
    html = driver.page_source
    return html


def get_soup(html):
    # HTMLをsoupに加工
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_submission():

    df = []
    list = []

    #　学生の提出を確認する
    for element in soup.find_all(class_="WkZsyc"):

        #　提出しているか確認する
        if element.find(class_="IMvYId zQwDwf").text == "":
            #　提出していない場合
            #　名前、提出"✕"をリスト化
            sub_name = element.find(class_="Evt7cb UmiGNb").text
            sub = "✕"
            sub_date = "✕"
            list.append([sub_name, sub, sub_date, 0])

        else:
            #　提出している場合
            #　名前、提出（"〇"）、提出日をリスト化
            sub_name = element.find(class_="Evt7cb UmiGNb").text
            sub = "〇"
            sub_date = element.find(class_="IMvYId zQwDwf").text
            #提出内容のためコメントアウト sub_content = element.find(class_="NjE5zd").text
            list.append([sub_name, sub, sub_date, 0])

    #　作ったリストをデータフレームに変換
    df = pd.DataFrame(list, columns=["名前", "提出", "提出日", "返信回数"])
    return df

def reply_count():

    for element in soup.find_all(class_="gJItbc asQXV"):
        name = element.text
        #　名前を元に返信数をカウント
        num_list = (df.index[df["名前"] == name].tolist())
        num = num_list[0]
        df.iat[num, 3] += 1
    
# CSVファイルに出力        
def df_output_csv():
    title = soup.find("title").text
    now = dt.datetime.now()
    time = now.strftime("%Y%m%d-%H%M%S")
    df.to_csv(title+"_output_{}.csv".format(time), index=False, encoding='utf_8_sig')
    print(title+"_output_{}.csvで出力しました".format(time))

if __name__ == "__main__":

    url = input("取得したいクラスルームの課題ページのURLをペーストしてください：")
    login_id = input("クラスルームに参加している教員アカウントのメールアドレスを入力してください：")
    login_pw = getpass("上記のメールアドレスのログインパスワードを入力してください：")

    driver = start_chrome()
    login_classroom(driver)
    html = get_html(driver)
    soup = get_soup(html)
    df = get_submission()
    reply_count()

    time.sleep(3)
    driver.quit()
    df_output_csv()
    
    input("Entarキーを押してください")


# In[ ]:




