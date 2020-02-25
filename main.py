# 最もシンプルなJSON受け取りプログラム
# PythonのHelloWorldを終わらして間もない人でも理解できるように、コメントは多めにしています。
# 活用しやすいように Flask というWebフレームワークを使用しています。

# flaskのFlaskとrequestをインポート
from flask import Flask, request

# アプリを定義
app = Flask(__name__)

# http://URL/ にアクセスされた時の処理
# GETとPOSTをサポートする
@app.route("/", methods=["GET", "POST"])
def home():
	# リクエストがGETだったとき
	if request.method == "GET":
		return "POST only!"
	# リクエストがPOSTだったとき
	elif request.method == "POST":
		# POSTされたJSONを受け取る
		receivedJSON = request.get_json()
		# JSONを標準出力
		print(receivedJSON)
		# クライアントには何かしら返さないといけない
		return "OK"

if __name__ == "__main__":
	# アプリを稼働
	app.run()