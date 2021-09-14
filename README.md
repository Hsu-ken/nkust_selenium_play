# 高科爬蟲Play
for fun 簡單的快速查找到個人資料 成績

## 環境
python3
selenium
chrome driver

## 問題與解決

### frame
一開始定位不到位置 原來是frame會卡 要先定位到哪個find_elements_by_tag_name('frame')[0] 
回朔位置使用switch_to.default_content()

### 定位方法使用
原則上有id name 直接使用就好 比較快
沒有的話可以用css select 可以不用全部都列出來 簡單的照標籤去找 
td input就抓的到 input.class input#id 分別找該標籤class或id 不用也行 精度問題
xpath需要全部列出 小麻煩

### javascript
execute_script也滿方便的 如果可以打直接用也快