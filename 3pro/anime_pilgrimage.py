import requests
from bs4 import BeautifulSoup

def get_anime_pilgrimage_info(title):
    # 検索用のURLを作成
    search_url = f"https://seichimap.jp/search?keyword={title}"
    
    # 指定されたURLに対してHTTP GETリクエストを送信
    response = requests.get(search_url)
    
    # レスポンスの内容を解析するためにBeautifulSoupを使用
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 聖地情報を格納するリストを作成
    pilgrimage_locations = []
    
    # 検索結果から聖地情報を抽出
    results = soup.find_all('div', class_='place_list_detail')
    for result in results:
        name = result.find('h3').text.strip()  # 聖地の名前を取得
        address = result.find('p', class_='address').text.strip()  # 聖地の住所を取得
        pilgrimage_locations.append({'name': name, 'address': address})  # リストに追加
    
    return pilgrimage_locations  # 聖地情報のリストを返す

# メイン関数
def main():
    # ユーザーの選択肢を設定
    options = ["1. Attack on Titan", "2. 君の名は", "3. Spirited Away", "4. Demon Slayer", "5. My Hero Academia"]
    
    print("Select a title to get pilgrimage information:")
    for option in options:
        print(option)

    # ユーザーの選択を受け取る
    choice = input("Enter the number of your choice: ")
    
    # 選択に基づいてタイトルを取得
    titles = {
        "1": "Attack on Titan",
        "2": "君の名は",
        "3": "Spirited Away",
        "4": "Demon Slayer",
        "5": "My Hero Academia"
    }

    selected_title = titles.get(choice)
    if selected_title:
        # 聖地情報を取得
        locations = get_anime_pilgrimage_info(selected_title)
        
        # 取得した聖地情報を表示
        if locations:
            print(f"Pilgrimage Locations for {selected_title}:")
            for location in locations:
                print(f" - Name: {location['name']}, Address: {location['address']}")
        else:
            print(f"No pilgrimage information found for {selected_title}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
