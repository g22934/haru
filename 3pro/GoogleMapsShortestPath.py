import requests

def main():
    # ユーザーからの入力を受け取る
    start = input("始点の地名または位置情報を入力してください: ")
    point1 = input("経由地1の地名または位置情報を入力してください: ")
    point2 = input("経由地2の地名または位置情報を入力してください: ")
    end = input("終点の地名または位置情報を入力してください: ")

    # APIキー
    API_KEY = "AIzaSyAU1cXfRrjHts2XsDkhSJGKzND9RQBtePA"

    # Directions APIを呼び出すURLを作成
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={end}&waypoints={point1}|{point2}&key={API_KEY}"

    try:
        # HTTP GETリクエストを送信
        response = requests.get(url)

        # レスポンスコードを確認し、200（成功）でない場合は例外をスロー
        if response.status_code != 200:
            raise Exception(f"HttpResponseCode: {response.status_code}")

        # APIからの応答をファイルに保存
        with open("route.json", "w", encoding="utf-8") as file:
            file.write(response.text)
        
        print("Response saved to route.json")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()