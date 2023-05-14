# API ガイド

[Engligh](Guide_EN.md)<br/>
[한국어](Guide_KO.md)<br/>
[日本語](Guide_JP.md)

## ワーボットの概要

このチャットボットは開発者のyymin1022が知り合いとよくする対話を代りにしてくれることを目指して開発したとものであります。

## インストール

### Setup Using Docker

[DockerHub](https://hub.docker.com/repository/docker/yymin1022/wa-api)

コンテナ８０番ポートを外部にフォーワーディングします。

```
docker pull yymin1022/wa-api
docker run --name wa -p 8080:80 wa-api
```

### Setup Manually
```
git clone https://github.com/yymin1022/Wa_API.git
chmod +x Wa_API/*.sh
./setupServer.sh
```

---

## 要求事項

```Ubuntu 20.04 LTS amd64``` 環境でテストされました。

その他のプラットフォームで利用しようとする場合には、環境の設定条件に変更があるかもしれませんのでご注意ください。

```setupServer.sh``` を使ってインストールする場合、下記のRequirementsも自動的にインストールされます。

```
sudo apt install apache2 libapache2-mod-wsgi-py3 python3 python3-pip python3-flask
sudo python3 -m pip install flask requests
```

---

## サービス実行

```setupServer.sh``` を使ってインストールする場合、Apach2 サービスも自動的にインストールされます。

下記のコードを実行して、サービスを稼働することができます。

```
service apache2 start
/etc/init.d/apache2 start
```

---

## 使用方法

```http://localhost:port/getMessage``` で、POST Restful データセットを転送します。

サーバにAPI申込をする場合のフォーマットは次の通りです。

```
{
    "msg": "ワー",
    "room": "チャットルーム",
    "sender": "yymin1022"
}
```

|Variable|Data Type|Data Content|
|---|---|---|
|msg|String|メッセージ内容|
|room|String|チャットルーム名|
|sender|String|チャット参加者|

---

サーバのAPI結果値は次の通りです。

```
{
    "RESULT": {
        "RESULT_CODE": 0,
        "RESULT_MSG": "RESULT OK"
        },
    "DATA": {
        "msg":"すごい金持ちじゃないか",
        "room":"チャットルーム１",
        "sender":"yymin1022"
        }
}
```

|Variable|Data Type|Data Content|
|---|---|---|
|RESULT_CODE|String|API処理結果コード|
|RESULT_MSG|String|API処理結果メッセージ|
|msg|String|メッセージ内容|
|room|String|チャットルーム名|
|sender|String|チャット参加者|

|API処理結果コード||
|---|---|
|0|正常処理|
|100|ワーボットが支援しないメッセージ|
|200|その他のエーラ(RESULT_MSG を参照)|

---

RESULT_MSGに変換されたメッセージの内容をチャットに返す時、```\\m```　と　```\\n``` の二つの改行文字が含まれることがあります。

```\\n```　は、一つのメッセージ内の改行を意味し、```\\m```　は改行からなるそれぞれのメッセージをそれぞれ転送するようしました。チャットボットの具現にてこのモデルを使う時にはご注意をお願い致します。

<img src="/README_IMG/WaSans.jpg" width="50%" />

## 使用例

次の使用例は応答可能なメッセージの一部であります。

すべてのメッセージ一覧は ```message.py``` でご確認できます。ワーボットの会話の大半は韓国語になっております。

|Message Content|Reply|
|---|---|
|꺼라|전기세 아깝다ㅡㅡ;;|
|ㄹㅇㅋㅋ|ㄹㅇㅋㅋ|
|멈춰|멈춰!!|
|무야호|그만큼 신나신다는거지~|
|아..|글쿤.. / 그래요.. 등 8종|
|와..|갑부;; / 기만;; / ㄹㅇ;; 등 7종|
|와!|샌즈! 아시는구나! 이거 겁.나.어.렵.습.니.다.|
|응애|응애 나 애기 등 3종|
|이런..|안됐군요.. 등 2종|
|자라|전기세 아깝다ㅡㅡ;;|
|자야지|구라ㅡㅡ;;|
|^^7|^^7|

## 具体例

[Wa.. for Discord](https://github.com/yymin1022/Wa_Bot_Discord)<br/>
[Wa.. for Telegram](https://github.com/yymin1022/Wa_Bot_Telegram)

## Want Contribute?

ボット制作に参加を希望する方は、```message.py``` を参照しコードを作成する後、```Pull Request```を登録しましたら管理者が周期的に確認の上、貴方のコードを　```Merge``` させていただきます。。
