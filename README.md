### [django] API から JSON 取得 

testJson/webapp/openNotify/

urls.py => httpリクエストを受けて、対応するビューを返す  
vews.py =>urls.pyから呼び出されると、処理を行う  
models.py => DBのテーブル定義  
index.html => 受信した HTML を表示  

**http://<ホスト>:8000/fetch/json3/**  
にアクセスすると
views.pyの  
**ai_analysis_log**
が実行され

http://example.com/<画像パス>
にアクセスするとAPIからJSONを取得して画像の分類クラスをMySQLに保存する


**http://<ホスト>:8000/fetch/json2/**
にアクセスすると http://open-notify.org/Open-Notify-API/ISS-Pass-Times/　から iSS の位置情報を JSON で受け取り、各JSONのバリューを DB内の の適当なフィールド に保存

**http://<ホスト>:8000/fetch/json/**
にアクセスすると http://open-notify.org/Open-Notify-API/ISS-Pass-Times/　から iSS の位置情報を JSON で受け取り、JSON形式のデータを JSONField DB に保存
