import requests
import json
path = '/products/5'
query = ''
url = 'https://api.liquid.com' + path + query
res = requests.get(url)
data = json.loads(res.text)
print(data)



# 鴻上企画(konkon1000)
# お世話になります。
#
# 仮払い入金させていただきました。
# 今回のロジックが三角裁定なのでサンプルページとレイアウト変わると思います。
# こちらで作成してファイルお渡ししたいと思いますので少々お待ちください。
#
# ロジックについてですが、
# Liquidの板取引の円建て、BTC建て、ETH建て、QASH建てとあると思いますが
# 例えばXRP/JPYの価格とXRP/BTCの価格(円換算)の差を抽出、
# BTC価格の方が安い場合BTCでXRPを購入しJPYで売ると利益になると思います。
# これを全てのペアで監視して利益が出る組み合わせを表示したいです。

