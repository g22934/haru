import requests

# TMDb APIキーを設定
TMDB_API_KEY = 'your_tmdb_api_key'  # ここに正しいAPIキーを設定

# 作品情報を取得する関数
def get_movie_info(title):
    url = f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&query={title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]
        else:
            print(f"No results found for {title}")
    else:
        print(f"Error fetching data for {title}: {response.status_code}")
    return None

# 仮の聖地巡礼情報を取得する関数（東京都限定）
def get_pilgrimage_info(title):
    pilgrimage_data = {
        "Attack on Titan": [
            {"name": "Hachiko Statue", "address": "Shibuya, Tokyo, Japan"}
        ],
        "Your Name": [
            {"name": "Suga Shrine", "address": "Yotsuya, Tokyo, Japan"}
        ],
        "Spirited Away": [
            {"name": "Edo-Tokyo Open Air Architectural Museum", "address": "Koganei, Tokyo, Japan"}
        ],
        "Demon Slayer": [
            {"name": "Mt. Kumotori", "address": "Okutama, Tokyo, Japan"}
        ],
        "My Hero Academia": [
            {"name": "Takatsuki City", "address": "Takatsuki, Tokyo, Japan"}
        ]
    }
    return pilgrimage_data.get(title, None)

# 聖地巡礼情報を表示する関数
def display_pilgrimage_info(title):
    print(f"Fetching movie info for {title}...")
    info = get_movie_info(title)
    pilgrimage = get_pilgrimage_info(title)
    if info:
        print(f"Title: {title}")
        print(f"Overview: {info['overview']}")
    else:
        print(f"No information found for {title}")

    if pilgrimage:
        print("Pilgrimage Locations:")
        for location in pilgrimage:
            print(f" - {location['name']} ({location['address']})")
        print()
    else:
        print(f"No pilgrimage information found for {title}")

# ユーザーの選択肢を設定
options = ["1. Attack on Titan", "2. Your Name", "3. Spirited Away", "4. Demon Slayer", "5. My Hero Academia"]

print("Select a title to get pilgrimage information:")
for option in options:
    print(option)

# ユーザーの選択を受け取る
choice = input("Enter the number of your choice: ")

# 選択に基づいてタイトルを取得
titles = {
    "1": "Attack on Titan",
    "2": "Your Name",
    "3": "Spirited Away",
    "4": "Demon Slayer",
    "5": "My Hero Academia"
}

selected_title = titles.get(choice)
if selected_title:
    display_pilgrimage_info(selected_title)
else:
    print("Invalid choice")
