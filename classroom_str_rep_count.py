#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

# Chormeを起動
def start_chrome():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  # 画面サイズの最大化
    # Google Classroomの取得したい課題のURLを指定
    driver.get(url)
    return driver

# classroomにログイン
def login_classroom(driver):
    # 待機時間を設定
    wait_time = 30
    # IDを入力
    login_id_xpath = '//*[@id="identifierNext"]'
 
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_name("identifier").send_keys(login_id)
    driver.find_element_by_xpath(login_id_xpath).click()
    time.sleep(3)
    
    # パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    driver.find_element_by_name("password").send_keys(login_pw)
    time.sleep(3)  # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath(login_pw_xpath).click()
    time.sleep(3)
    
# ストリームはスクロールしなければ更新されないためページ下部までスクロール
def scroll_browser():
    #ブラウザのウインドウ高を取得する
    win_height = driver.execute_script("return window.innerHeight")

    #スクロール開始位置の初期値（ページの先頭からスクロールを開始する）
    last_top = 1
    
    #ページの最下部までスクロールする無限ループ
    while True:

      #スクロール前のページの高さを取得
      last_height = driver.execute_script("return document.body.scrollHeight")

      #スクロール開始位置を設定
      top = last_top

      #ページ最下部まで、徐々にスクロールしていく
      while top < last_height:
        top += int(win_height * 0.8)
        driver.execute_script("window.scrollTo(0, %d)" % top)
        time.sleep(0.5)

      #１秒待って、スクロール後のページの高さを取得する
      time.sleep(1)
      new_last_height = driver.execute_script("return document.body.scrollHeight")

      #スクロール前後でページの高さに変化がなくなったら無限スクロール終了とみなしてループを抜ける
      if last_height == new_last_height:
        break

      #次のループのスクロール開始位置を設定
      last_top = last_height

# HTMLを取得
def get_html(driver):
    time.sleep(6)
    html = driver.page_source
    return html

# HTMLをsoupに加工
def get_soup(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

# ストリームに参加している学生データフレーム化
def get_student():
    df = []
    list = []
 
    #　学生を確認する
    for element in soup.find_all(class_="dZVZab"):
 
        #　名前、返信回数をdfに登録
        reply_name = element.find(class_="gJItbc asQXV").text
        for i in list:
            if not reply_name in i:
                continue
            else:
                break
        else:
            list.append([reply_name,0])
 
    #　作ったリストをデータフレームに変換
    df = pd.DataFrame(list, columns=["名前", "返信回数"])
    return df

# 返信の回数をカウント
def reply_count():
    # 名前を検索
    for element in soup.find_all(class_="gJItbc asQXV"):
        name = element.text
 
        # 名前を元に返信数をカウント
        num_list = (df.index[df["名前"] == name].tolist())
        num = num_list[0]
        df.iat[num, 1] += 1

# CSVファイルに出力
def df_output_csv():
    now = dt.datetime.now()
    time = now.strftime("%Y%m%d-%H%M%S")
    df.to_csv("str_output_{}.csv".format(time), index=False, encoding='utf_8_sig')
    print("str_output_{}.csvで出力しました".format(time))

if __name__ == "__main__":
    
    url = input("取得したいクラスルームのストリームページのURLをペーストしてください：")
    login_id = input("クラスルームに参加している教員アカウントのメールアドレスを入力してください：")
    login_pw = getpass("上記のメールアドレスのログインパスワードを入力してください：")
    
    driver = start_chrome()
    login_classroom(driver)
    scroll_browser()
    html = get_html(driver)
    soup = get_soup(html)
    df = get_student()
    reply_count()
    time.sleep(3)
    driver.quit()
    df_output_csv()
    
    input("Entarキーを押してください")


# In[ ]:




