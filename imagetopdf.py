import img2pdf
import os

# 画像があるフォルダ
SAVE_DIR = "my_book_images"
# 出力するPDFの名前
OUTPUT_PDF = "book_complete.pdf"

def main():
    print("PDFを作成中...")
    
    # 画像ファイルだけを集めて、名前順（001, 002...）に並べる
    images = [i for i in os.listdir(SAVE_DIR) if i.endswith(".png")]
    images.sort()
    
    # フルパス（フォルダ名/ファイル名）のリストにする
    img_paths = [os.path.join(SAVE_DIR, i) for i in images]

    if not img_paths:
        print("エラー: 画像が見つかりません。")
        return

    # PDF変換
    try:
        with open(OUTPUT_PDF, "wb") as f:
            f.write(img2pdf.convert(img_paths))
        print(f"成功！ '{OUTPUT_PDF}' が作成されました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()