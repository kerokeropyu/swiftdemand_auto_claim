## 概要
このプロジェクトは、[Swiftdemand](https://www.swiftdemand.com/)という毎日クリックすることで仮想通貨をもらえるサイトのページのボタンを自動でクリックするための Python スクリプトです。

## 準備
1. **Python のインストール**: もし未インストールの場合は、[こちら](https://www.python.org/)から最新版の Python をインストールしてください。

    下記が動作確認済みのpythonバージョンです。
    ```
    >> python --version
    Python 3.11.2
    ```
2. #### 仮想環境の作成と起動:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. #### 必要なパッケージをインストール:
    ```コマンドプロンプト
    pip install -r requirements.txt
    ```  

4. #### 仮想環境の終了
    ```コマンドプロンプト
    deactivate
    ``` 

## 使い方
1. `config.json` ファイルを作成し、ユーザーのIDとパスワードを設定します。
    ```json
    {
      "user_email": "your_email@example.com",
      "user_password": "your_password"
    }
    ```
   ※ ユーザーの実際のメールアドレスとパスワードをそれぞれ `your_email@example.com` と `your_password` の部分に置き換えてください。

2. 以下のコマンドを実行して、プログラムを起動します。
    ```bash
    python main.py
    ```

3. ログイン、クリック、ログアウトが自動で行われます。必要に応じて、cron などで定期実行することで、より便利に使えます。

## 備考
* ロギングの使い方: [Python 公式ドキュメント - ロギングの詳細](https://docs.python.org/ja/3/howto/logging.html#advanced-logging-tutorial)
* bandit（静的セキュリティー検査ツール）の使い方:
    ```bash
    bandit main.py
    ```
    * banditについての詳細は [こちらの資料](https://scrapbox.io/PythonOsaka/Python%E3%81%AE%E9%9D%99%E7%9A%84%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%83%BC%E6%A4%9C%E6%9F%BB%E3%83%84%E3%83%BC%E3%83%ABbandit%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86) を参照してください。
* README.mdの書き方は下記のサイトを参照しました（自分用メモ）: [Markdown記法 サンプル集](https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa)
