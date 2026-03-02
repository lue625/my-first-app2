import streamlit as st
import base64
import os

# 1. ページ設定
st.set_page_config(page_title="赤ちゃんぷくぷく記録", page_icon="👶")

# 画像をBase64で読み込む関数（確実に表示させるため）
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# カスタムCSS：背景と文字のコントラストを調整
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f5;
    }
    .main .block-container {
        color: #2c3e50; /* 濃いグレーで文字を読みやすく */
    }
    h1 {
        color: #d63384 !important;
        text-align: center;
        font-weight: bold;
    }
    .status-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 30px;
        border-radius: 25px;
        border: 2px solid #ffccd5;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3em;
        background-color: #ffccd5;
        color: #d63384;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👶 赤ちゃんミルク記録")

# 2. ミルク量の管理（セッション状態）
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

# 最大1000mlまでに制限
st.session_state.milk = min(st.session_state.milk, 1000)
milk_amount = st.slider("今日の合計ミルク量 (ml)", 0, 1000, st.session_state.milk)
st.session_state.milk = milk_amount

# 3. ミルク量に応じた画像・メッセージ判定
if milk_amount < 200:
    img_name, status, msg, color = "baby1.jpg", "スリム期", "これからたくさん飲むよ！", "#6c757d"
elif milk_amount < 400:
    img_name, status, msg, color = "baby2.jpg", "標準期", "順調に育ってるね！", "#198754"
elif milk_amount < 600:
    img_name, status, msg, color = "baby3.jpg", "ぷくぷく予備軍", "ほっぺが柔らかくなってきた？", "#fd7e14"
elif milk_amount < 800:
    img_name, status, msg, color = "baby4.jpg", "ぷくぷく期", "いい感じのぷくぷく具合！", "#dc3545"
else:
    img_name, status, msg, color = "baby5.jpg", "超ぷくぷく期", "最高のわがままボディ！", "#d63384"

# 4. メイン表示エリア
st.markdown("<div class='status-card'>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color: {color};'>現在の状態：{status}</h2>", unsafe_allow_html=True)

# 画像の読み込みと表示
img_base64 = get_image_base64(img_name)
if img_base64:
    st.markdown(f'<img src="data:image/jpg;base64,{img_base64}" width="300" style="border-radius: 20px;">', unsafe_allow_html=True)
else:
    st.warning(f"画像ファイル {img_name} が見つかりません。GitHubにアップロードしてください。")

st.write(f"### {msg}")
st.write(f"合計ミルク量: **{milk_amount} ml**")
st.markdown("</div>", unsafe_allow_html=True)

# 5. フッター
st.divider()
st.caption("未経験パパのアプリ開発物語。奥様へのプレゼントアプリ第1弾！")