import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="赤ちゃんぷくぷく記録", page_icon="👶")

# カスタムCSS：背景色と文字色のコントラストを改善
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f5; /* 薄いピンクの背景 */
    }
    /* 全体の文字色を濃いグレーにして読みやすくする */
    .main .block-container {
        color: #2c3e50;
    }
    /* タイトルとサブヘッダーの色を強調 */
    h1, h2, h3 {
        color: #d63384 !important; /* 濃いピンク */
    }
    .status-card {
        background-color: rgba(255, 255, 255, 0.9); /* 白背景を少し透過 */
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #ffccd5;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    /* ボタンを押しやすく */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👶 赤ちゃんミルク記録")
st.write("今日のミルクの合計量を記録しましょう。")

# 2. ミルク量の入力（スライダー＋ボタンで使い勝手向上）
# セッション状態を使って数値を管理（育児中の忙しいパパ向け）
if 'milk' not in st.session_state:
    st.session_state.milk = 400

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("＋20ml"):
        st.session_state.milk += 20
with col2:
    if st.button("＋100ml"):
        st.session_state.milk += 100
with col3:
    if st.button("リセット"):
        st.session_state.milk = 0

milk_amount = st.slider("現在の合計量 (ml)", 0, 1000, st.session_state.milk)
st.session_state.milk = milk_amount

# 3. ミルク量に応じた判定
if milk_amount < 200:
    status, msg, color = "スリム期", "これからたくさん飲むよ！", "#6c757d"
    img_url = "https://placehold.jp/24/ff9999/ffffff/300x300.png?text=Slim+Baby"
elif milk_amount < 400:
    status, msg, color = "標準期", "順調に育ってるね！", "#198754"
    img_url = "https://placehold.jp/24/ffcc99/ffffff/300x300.png?text=Normal+Baby"
elif milk_amount < 600:
    status, msg, color = "ぷくぷく予備軍", "ほっぺが柔らかくなってきた？", "#fd7e14"
    img_url = "https://placehold.jp/24/ffff99/ffffff/300x300.png?text=Puku+Puku+Step1"
elif milk_amount < 800:
    status, msg, color = "ぷくぷく期", "いい感じのぷくぷく具合！", "#dc3545"
    img_url = "https://placehold.jp/24/ccff99/ffffff/300x300.png?text=Puku+Puku+Step2"
else:
    status, msg, color = "超ぷくぷく期", "最高のわがままボディです！", "#d63384"
    img_url = "https://placehold.jp/24/99ffcc/ffffff/300x300.png?text=Max+Puku+Puku"

# 4. 表示エリア
st.markdown(f"<div class='status-card'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color: {color};'>現在の状態：{status}</h2>", unsafe_allow_html=True)
st.image(img_url, caption=f"ミルク累計：{milk_amount}ml", width=300)
st.write(f"### {msg}")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.caption("未経験パパのアプリ開発ロードマップ。背景色と文字のコントラストを改善しました。")