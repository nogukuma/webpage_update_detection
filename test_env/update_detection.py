from bs4 import BeautifulSoup
import requests


def detect_updates():
    # 取得してきたいページのurl
    url = "https://scraping.official.ec/items/40792454"

    # urlの取得
    res = requests.get(url)

    # htmlの整形
    soup = BeautifulSoup(res.text,"html.parser")

    # 取ってきたいクラスを取得し，文字列として変数に格納
    new_elem = str(soup.select(".item-detail_soldOut_9108a3fe"))

    try:
        with open('old_elem.txt') as f:
            old_elem = f.read()
    except:
        old_elem = ""
    print(old_elem)

    if new_elem == old_elem:
        print("変化なし")
        return False
    else:
        print("Webページが更新された")
        with open('old_elem.txt',"w") as f:
            f.write(new_elem)
        return True

detect_updates()