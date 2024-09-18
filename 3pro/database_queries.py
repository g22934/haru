import sqlite3

def get_movie_info(title):
    conn = sqlite3.connect('anime_pilgrimage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, overview, image FROM titles WHERE title = ?', (title,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"id": result[0], "overview": result[1], "image": result[2]}
    return None

def get_pilgrimage_info(title_id):
    conn = sqlite3.connect('anime_pilgrimage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, address, image FROM pilgrimage_locations WHERE title_id = ?', (title_id,))
    results = cursor.fetchall()
    conn.close()
    return [{"name": row[0], "address": row[1], "image": row[2]} for row in results]
