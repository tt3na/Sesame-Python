#!/usr/local/bin/python3

import datetime, base64, requests, json
from Crypto.Hash import CMAC
from Crypto.Cipher import AES

# UUID, シークレットキー, APIキーの設定
uuid = '[UUID]'
secret_key = '[SECRET_KEY]'
api_key = '[API_KEY]'

# ヘッダー
headers = {'x-api-key': api_key}

# ステータス取得
url = f'https://app.candyhouse.co/api/sesame2/{uuid}'
res = requests.get(url, headers=headers)
text =  res.text.split(",")[3].split(":")

print(text[1].strip())
response = text[1].strip()

# レスポンス"locked"の場合は解錠(cmd=83)
if response=='"locked"' :
	cmd = 83 
else:
	cmd = 82


# 解錠者名の設定 base64でエンコード
history = 'by Python' 
base64_history = base64.b64encode(bytes(history, 'utf-8')).decode()

# cmacで各種情報を署名
cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)
ts = int(datetime.datetime.now().timestamp())
message = ts.to_bytes(4, byteorder='little')
message = message.hex()[2:8]
cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)
cmac.update(bytes.fromhex(message))
sign = cmac.hexdigest()

# POST処理
url = f'https://app.candyhouse.co/api/sesame2/{uuid}/cmd'
body = {
    'cmd': cmd,
    'history': base64_history,
    'sign': sign
}

res = requests.post(url, json.dumps(body), headers=headers)
