import requests
from bs4 import BeautifulSoup

def get_anime_pilgrimage_info(anime_title):
    # 検索用のURLを作成
    search_url = f"https://seichimap.jp/spots?utf8=%E2%9C%93&q={anime_title}&lat=&lng="
    
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
    anime_title = "ラブライブ！"  # 取得したいアニメのタイトル
    locations = get_anime_pilgrimage_info(anime_title)
    
    if locations:
        print(f"Pilgrimage Locations for {anime_title}:")
        for location in locations:
            print(f" - Name: {location['name']}, Address: {location['address']}")
    else:
        print(f"No pilgrimage information found for {anime_title}")
