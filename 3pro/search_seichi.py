import requests
from bs4 import BeautifulSoup

def search_seichimap(query):
    base_url = "https://seichimap.jp"
    search_url = f"{base_url}/spots?utf8=%E2%9C%93&q={query}&lat=&lng="

    # HTTP GETリクエストを送信してページの内容を取得
    response = requests.get(search_url)

    # レスポンスのHTMLを解析するためにBeautifulSoupを使用
    soup = BeautifulSoup(response.text, 'html.parser')

    # 聖地情報を格納するリスト
    pilgrimage_locations = []

    # 検索結果から聖地情報を抽出
    results = soup.find_all('div', class_='card-list-item')
    for result in results:
        name = result.find('div', class_='card-list-item__title').text.strip()  # 聖地の名前
        address = result.find('div', class_='card-list-item__address').text.strip()  # 聖地の住所
        pilgrimage_locations.append({'name': name, 'address': address})

    return pilgrimage_locations

# 使用例
if __name__ == "__main__":
    query = input("検索したいアニメや作品のタイトルを入力してください: ")
    locations = search_seichimap(query)
    
    if locations:
        print(f"Pilgrimage Locations for {query}:")
        for location in locations:
            print(f" - Name: {location['name']}, Address: {location['address']}")
    else:
        print(f"No pilgrimage information found for {query}")
