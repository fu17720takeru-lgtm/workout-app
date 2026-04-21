import streamlit as st
from datetime import datetime, timedelta

# ===== 回復時間 =====
recovery_time = {
    "chest": 72,
    "back": 72,
    "legs": 72,
    "shoulders": 48,
    "arms": 48,
    "abs": 24
}

# ===== 仮データ =====
last_trained = {
    "chest": datetime(2026, 4, 19, 10),
    "back": datetime(2026, 4, 20, 12),
    "legs": datetime(2026, 4, 18, 9),
    "shoulders": datetime(2026, 4, 20, 15),
    "arms": datetime(2026, 4, 20, 15),
    "abs": datetime(2026, 4, 21, 8)
}

# ===== 部位判定 =====
def get_available_parts():
    now = datetime.now()
    available = []

    for part, last_time in last_trained.items():
        if now - last_time >= timedelta(hours=recovery_time[part]):
            available.append(part)

    return available

# ===== 仮メニュー（APIなし）=====
def generate_menu(parts):
    return f"""
### トレーニングメニュー（{parts}）

- スクワット 10回 × 3セット  
- ランジ 10回 × 3セット  
- レッグプレス 10回 × 3セット  
"""

# ===== UI =====
st.title("筋トレメニュー自動作成アプリ")

if st.button("今日のメニューを作る"):
    parts = get_available_parts()

    if not parts:
        st.write("今日は休養日がおすすめ")
    else:
        st.write("今日のおすすめ部位:", parts)
        st.markdown(generate_menu(parts))