import sqlite3

def setup_database():
    conn = sqlite3.connect('anime_pilgrimage.db')
    cursor = conn.cursor()

    # 既存のテーブルを削除
    cursor.execute('DROP TABLE IF EXISTS pilgrimage_locations')
    cursor.execute('DROP TABLE IF EXISTS titles')

    # titles テーブルを作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS titles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        overview TEXT,
        image TEXT
    )
    ''')

    # pilgrimage_locations テーブルを作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pilgrimage_locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title_id INTEGER,
        name TEXT,
        address TEXT,
        image TEXT,
        FOREIGN KEY (title_id) REFERENCES titles(id)
    )
    ''')

    # タイトルデータ
    titles = [
        ("進撃の巨人", "人類が巨人により滅亡の危機に瀕している世界で...", "attack_on_titan.jpg"),
        ("君の名は。", "高校生の男女が入れ替わる不思議な現象を通じて繋がる...", "your_name.jpg"),
        ("千と千尋の神隠し", "引っ越しの途中で不思議な世界に迷い込んだ少女の冒険...", "spirited_away.jpg"),
        ("鬼滅の刃", "家族が鬼に襲われ、生き残った炭治郎と妹の禰豆子の物語...", "demon_slayer.jpg"),
        ("僕のヒーローアカデミア", "個性がほとんどの人に備わった世界で、ヒーローを夢見る少年の物語...", "my_hero_academia.jpg"),
    ]

    # タイトルデータを挿入
    cursor.executemany('INSERT INTO titles (title, overview, image) VALUES (?, ?, ?)', titles)

    # 聖地巡礼の場所データ
    pilgrimage_locations = [
        (1, "ハチ公像", "東京都渋谷区", "hachiko_statue.jpg"),
        (2, "須賀神社", "東京都新宿区四谷", "suga_shrine.jpg"),
        (3, "江戸東京たてもの園", "東京都小金井市", "edo_tokyo_open_air_architectural_museum.jpg"),
        (4, "雲取山", "東京都奥多摩町", "mt_kumotori.jpg"),
        (5, "高槻市", "東京都高槻市", "takatsuki_city.jpg"),
    ]

    # 聖地巡礼の場所データを挿入
    cursor.executemany('INSERT INTO pilgrimage_locations (title_id, name, address, image) VALUES (?, ?, ?, ?)', pilgrimage_locations)

    # 変更をコミットして接続を閉じる
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
