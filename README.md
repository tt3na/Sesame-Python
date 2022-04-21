# Sesame-Python
Sesame3をPythonスクリプトで解錠・施錠を行ったときのコードとメモ

自宅のスマートロック(Sesame3)をPythonスクリプトで解錠と施錠をできるようにします。

Sesame3 : https://jp.candyhouse.co/products/sesame3

Sesame WEB API: https://partners.candyhouse.co/login

動作にはSesameのUUID、APIキー、シークレットキーを取得する必要があります。

まずは以下のスクリプトをターミナルにペーストして実行します(適宜置き換えてください)

>/usr/bin/python3 << FIN
>
>import urllib.parse
>
>import base64
>
>a=urllib.parse.parse_qs('[QRコードを読み取ったときのURL]')
>
>print(a)
>
>print()
>
>FIN

次に以下のスクリプトを実行してAPIキーを取得します。

>/usr/bin/python3 << FIN
>
>sk = '[先程のskの値]'
>
>sk_bytes = base64.b64decode(sk)
>
>secret_key_hex = sk_bytes[1:17].hex()
>
>print(secret_key_hex)
>
>FIN
