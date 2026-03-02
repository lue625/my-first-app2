import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="赤ちゃんぷくぷく記録", page_icon="👶")

# カスタムCSSで見た目を可愛く
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f5;
    }
    .status-card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #ffccd5;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👶 赤ちゃんミルク記録")
st.write("今日のミルクの合計量に合わせて、赤ちゃんが成長（？）します。")

# 2. ミルク量の入力（0〜1000ml）
milk_amount = st.slider("今日の合計ミルク量 (ml)", 0, 1000, 400)

# 3. ミルク量に応じた画像とメッセージの判定
# 本来はここに生成AIで作った5枚の画像をセットします
if milk_amount < 200:
    status = "スリム期"
    msg = "これからたくさん飲むよ！"
    img_url = "https://placehold.jp/24/ff9999/ffffff/300x300.png?text=Slim+Baby"
elif milk_amount < 400:
    status = "標準期"
    msg = "順調に育ってるね！"
    img_url = "https://placehold.jp/24/ffcc99/ffffff/300x300.png?text=Normal+Baby"
elif milk_amount < 600:
    status = "ぷくぷく予備軍"
    msg = "ほっぺが柔らかくなってきた？"
    img_url = "https://placehold.jp/24/ffff99/ffffff/300x300.png?text=Puku+Puku+Step1"
elif milk_amount < 800:
    status = "ぷくぷく期"
    msg = "いい感じのぷくぷく具合！"
    img_url = "https://placehold.jp/24/ccff99/ffffff/300x300.png?text=Puku+Puku+Step2"
else:
    status = "超ぷくぷく期（完成！）"
    msg = "最高のわがままボディです！"
    img_url = "https://placehold.jp/24/99ffcc/ffffff/300x300.png?text=Max+Puku+Puku"

# 4. 表示エリア
st.markdown(f"<div class='status-card'>", unsafe_allow_html=True)
st.subheader(f"現在の状態：{status}")
st.image(img_url, caption=f"ミルク量：{milk_amount}ml", width=300)
st.write(f"### {msg}")
st.markdown("</div>", unsafe_allow_html=True)

# 5. フッター
st.divider()
st.info("💡 ヒント: 画像を自分で用意して 'baby1.jpg' 〜 'baby5.jpg' のように保存すれば、本当のアニメ調赤ちゃんに差し替えられますよ！")