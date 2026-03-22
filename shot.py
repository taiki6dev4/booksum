import pyautogui
import time
import os
from datetime import datetime

# ================= 設定エリア =================
# 撮影したいページ数（少し多めに設定しても途中で止められます）
TOTAL_PAGES = 250

# ページをめくってから撮影するまでの待ち時間（秒）
# ※表示が遅いアプリなら 2.0 や 3.0 に増やしてください
INTERVAL = 0.5

# 保存するフォルダ名
SAVE_DIR = "my_book_images"
# ============================================

def main():
    # 保存フォルダがなければ作成
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        print(f"フォルダ作成: {SAVE_DIR}")

    print("------------------------------------------------")
    print("【開始準備】")
    print("1. 撮影したい本（アプリ/ブラウザ）を開いてください。")
    print("2. 5秒後に撮影を開始します。その間にウィンドウをアクティブにしてください。")
    print("※ 緊急停止したいときは、マウスカーソルを画面の四隅のどこかに素早く移動させてください（フェイルセーフ機能）。")
    print("------------------------------------------------")
    
    # 5秒カウントダウン
    for i in range(3, 0, -1):
        print(f"開始まで {i} 秒...")
        time.sleep(1)

    print("撮影開始！")

    for i in range(TOTAL_PAGES):
        # 1. ファイル名を作成 (例: 001.png)
        file_name = f"{i+1:03}.png"
        file_path = os.path.join(SAVE_DIR, file_name)

        # 2. スクリーンショット撮影
        # MacのRetinaディスプレイの場合、解像度が高く保存されることがあります
        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)
        print(f"[{i+1}/{TOTAL_PAGES}] 保存完了: {file_name}")

        # 3. ページめくり（左矢印キー） 適宜変える
        pyautogui.press('right')

        # 4. 次のページが表示されるのを待つ
        time.sleep(INTERVAL)

    print("------------------------------------------------")
    print("すべての撮影が完了しました！")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nプログラムを中断しました。")
    except pyautogui.FailSafeException:
        print("\n【緊急停止】マウスが画面端に移動されたため停止しました。")