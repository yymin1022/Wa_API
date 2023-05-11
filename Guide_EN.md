# API Usage Guide

[English](Guide_EN.md)<br/>
[한국어](Guide_KO.md)

## Install

### Setup Using Docker

You must Forward 80 Container Port.

[DockerHub](https://hub.docker.com/repository/docker/yymin1022/wa-api)

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

## Requirements

Tested on ```Ubuntu 20.04 LTS amd64```. Other platform might need some modifying.

These requirements will be installed automatically with ```setupServer.sh``` Script.

```
sudo apt install apache2 libapache2-mod-wsgi-py3 python3 python3-pip python3-flask
sudo python3 -m pip install flask requests
```

## Run

If installed with ```setupServer.sh``` script, Apach2 service will be installed automatically.

Service can be started with command one of these.

```
service apache2 start
/etc/init.d/apache2 start
```

## How To Use

Send POST Restful API Data to ```http://localhost:port/getMessage```

API Format is like this.

```
{
    "msg": "와..",
    "room": "ChatRoom 1",
    "sender": "yymin1022"
}
```

|Variable|Data Type|Data Content|
|---|---|---|
|msg|String|Message Content|
|room|String|ChatRoom Name|
|sender|String|Chat Talker|

---

And then API Return Data is like this.

```
{
    "RESULT": {
        "RESULT_CODE": 0,
        "RESULT_MSG": "RESULT OK"
        },
    "DATA": {
        "msg":"갑부;;",
        "room":"ChatRoom 1",
        "sender":"yymin1022"
        }
}
```

|Variable|Data Type|Data Content|
|---|---|---|
|RESULT_CODE|String|API Result Code|
|RESULT_MSG|String|API Result Message|
|msg|String|Message Content|
|room|String|ChatRoom Name|
|sender|String|Chat Talker|

|API Result Code||
|---|---|
|0|Result OK|
|100|Message that Wa.. API does not support|
|200|Other Error. Check RESULT_MSG|

---

Returned RESULT_MSG can include Two types of Line-Breaking Character, that is ```\\m``` and ```\\n```.

```\\n``` is Line-Breaking in One Message, and ```\\m``` is Splited Message with Line-Breaking.

<img src="/README_IMG/WaSans.jpg" width="50%" />

## API Example

These Eamples are just a part of API.

You can check all messages on ```message.py```

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

## Example

[Wa.. for Discord](https://github.com/yymin1022/Wa_Bot_Discord)<br/>
[Wa.. for Telegram](https://github.com/yymin1022/Wa_Bot_Telegram)

## Want Contribute?

If you want contribute on this Bot, check ```message.py``` and write code. I will ```Merge``` the code when you register ```Pull Request``` after checking code.
