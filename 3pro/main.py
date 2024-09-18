import sqlite3
from PIL import Image
import os

# データベースからタイトル情報を取得する関数
def get_title_info(title):
    conn = sqlite3.connect('anime_pilgrimage.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, overview, image FROM titles WHERE title=?", (title,))
    title_info = cursor.fetchone()
    conn.close()
    return title_info

# データベースから聖地巡礼情報を取得する関数
def get_pilgrimage_info(title_id):
    conn = sqlite3.connect('anime_pilgrimage.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, address, image FROM pilgrimage_locations WHERE title_id=?", (title_id,))
    locations = cursor.fetchall()
    conn.close()
    return locations

# 画像を表示する関数
def display_image(image_path):
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img.show()
    else:
        print(f"Image not found: {image_path}")

# 聖地巡礼情報を表示する関数
def display_pilgrimage_info(title):
    title_info = get_title_info(title)
    if title_info:
        title_id, title, overview, image_path = title_info
        print(f"タイトル: {title}")
        print(f"概要: {overview}")
        display_image(image_path)

        locations = get_pilgrimage_info(title_id)
        if locations:
            print("聖地巡礼の場所:")
            for name, address, location_image in locations:
                print(f" - {name} ({address})")
                display_image(location_image)
        else:
            print("聖地巡礼情報が見つかりませんでした。")
    else:
        print(f"タイトル情報が見つかりませんでした: {title}")

# ユーザーの選択肢を設定
options = ["1. 進撃の巨人", "2. 君の名は。", "3. 千と千尋の神隠し", "4. 鬼滅の刃", "5. 僕のヒーローアカデミア"]

print("作品のタイトルを選んでください:")
for option in options:
    print(option)

# ユーザーの選択を受け取る
choice = input("選択肢の番号を入力してください: ")

# 選択に基づいてタイトルを取得
titles = {
    "1": "進撃の巨人",
    "2": "君の名は。",
    "3": "千と千尋の神隠し",
    "4": "鬼滅の刃",
    "5": "僕のヒーローアカデミア"
}

selected_title = titles.get(choice)
if selected_title:
    display_pilgrimage_info(selected_title)
else:
    print("無効な選択です。")
