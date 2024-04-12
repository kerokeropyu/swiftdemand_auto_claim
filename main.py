import datetime
import json
import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# 実行時のバージョンと同様の ChromeDriverをインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 指定した要素が見つかるまでの待ち時間を設定（1秒）
driver.implicitly_wait(1)

# 本日日付取得
dt = datetime.datetime.today() 
d = dt.date()

# ロガーをインスタンス化
logger = logging.getLogger(__name__)
logging.basicConfig(filename=f"logs\{d}.log", encoding='utf-8', level=logging.DEBUG)

# 設定ファイルからユーザーのメールアドレスとパスワードを読み込む
with open('config.json', 'r') as f:
    config = json.load(f)
    user_email = config['user_email']
    user_password = config['user_password']

# メイン処理
def main():
    # swiftdemandにアクセス
    driver.get('https://www.swiftdemand.com/')
    # ログインボタンを押下し、ユーザーIDとパスワードを入力
    driver.find_element(By.XPATH, '//*[@id="welcome"]/div[2]/div[4]/div[1]/div[3]/a[2]/div').click()
    driver.find_element(By.XPATH, '//*[@id="user_email"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//*[@id="user_password"]').send_keys(user_password)
    driver.find_element(By.XPATH, '//*[@id="new_user"]/div/div[4]/input').click()

    # Claimボタンを押下
    try:
        claim_button = driver.find_element(By.XPATH, '//*[@id="account"]/div[2]/div[1]/section/div/div[3]/input')
        if claim_button.is_enabled():
            claim_button.click()
            logger.info('Claim button clicked.')
        else:
            logger.warning('Claim button is disabled.')
    except:
        logger.warning('Claim button is not found.')
    # ログアウト
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/a[2]/div').click()
    # ブラウザを閉じる
    driver.quit()
    logger.info('Input completed!')

if __name__ == '__main__':
    main()