import streamlit as st
import random

# 1. Cấu hình trang
st.set_page_config(page_title="Nông Trại Mèo & Thú Cưng", page_icon="🐷", layout="centered")

# 2. CSS Tùy chỉnh giao diện Nông Trại
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f0f9eb 0%, #e1f5fe 100%);
    }
    .farm-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        text-align: center;
        border: 2px solid #c8e6c9;
    }
    .animal-box {
        background: #fff9c4;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #fbc02d;
    }
</style>
""", unsafe_allow_html=True)

# 3. Khởi tạo Trạng thái Game (Session State)
if "game_state" not in st.session_state:
    st.session_state.game_state = "MENU"
if "gold" not in st.session_state:
    st.session_state.gold = 150
if "chickens" not in st.session_state:
    st.session_state.chickens = 1
if "pigs" not in st.session_state:
    st.session_state.pigs = 0
if "cows" not in st.session_state:
    st.session_state.cows = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# ==========================================
# MÀN HÌNH CHÍNH (MAIN MENU)
# ==========================================
if st.session_state.game_state == "MENU":
    st.title("🌾 Nông Trại Mộng Mơ: Animal Tycoon")
    st.subheader("Xây dựng trang trại động vật siêu đáng yêu của riêng bạn!")
    
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1eXp2ZnR4bmRzc292eXFud2x4OW8zeGNuOW14a3BxODR4c2VnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mCRJDo24UvJMA/giphy.gif",
        use_container_width=True,
        caption="Những chú thú cưng đang chờ bạn chăm sóc!"
    )
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚜 VÀO NÔNG TRẠI", use_container_width=True, type="primary"):
            st.session_state.game_state = "PLAYING"
            st.rerun()
    with col2:
        with st.popover("📖 Hướng Dẫn Chơi"):
            st.write("""
            1. **Nuôi thú:** Mua gà, heo, bò để sản xuất tài nguyên (Trứng, Thịt, Sữa).
            2. **Thu hoạch:** Bấm nút thu hoạch để quy đổi nông sản thành tiền vàng.
            3. **Mở rộng:** Dùng tiền vàng để mua thêm nhiều con vật mới!
            """)

# ==========================================
# MÀN HÌNH CHƠI GAME (GAMEPLAY)
# ==========================================
elif st.session_state.game_state == "PLAYING":
    # Thanh điều hướng phía trên
    col_nav1, col_nav2 = st.columns([3, 1])
    with col_nav1:
        st.title("🚜 Nông Trại Của Bạn")
    with col_nav2:
        if st.button("🏠 Màn chính"):
            st.session_state.game_state = "MENU"
            st.rerun()
            
    # Hiển thị Chỉ số kinh tế
    c1, c2 = st.columns(2)
    c1.metric("💰 Tiền Vàng", f"{st.session_state.gold} G")
    c2.metric("✨ Điểm Kinh Nghiệm", f"{st.session_state.score} XP")
    
    st.write("---")

    # KHU VỰC HIỂN THỊ NÔNG TRẠI & ĐỘNG VẬT
    st.markdown("""
    <div class="farm-card">
        <h3>🏡 Chuồng Trại Động Vật Sôi Động</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmN5ZXRwbWx1YnJzeHg0NDc5bzlyZWR4eG01azlhbW9vZjFvd3M4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lq0h93752f6J9tijrh/giphy.gif",
        use_container_width=True,
        caption="Các bé thú cưng đang nhởn nhơ gặm cỏ."
    )

    # Hiển thị số lượng vật nuôi hiện tại
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("🐔 Gà con", f"{st.session_state.chickens} con")
    col_b.metric("🐷 Heo mũm mĩm", f"{st.session_state.pigs} con")
    col_c.metric("🐮 Bò sữa", f"{st.session_state.cows} con")

    st.write("---")

    # KHU VỰC THU HOẠCH & CHĂM SÓC
    st.subheader("🧺 Hoạt Động Nông Trại")
    
    col_act1, col_act2 = st.columns(2)
    with col_act1:
        if st.button("🌾 Cho ăn & Thu hoạch nông sản", type="primary", use_container_width=True):
            # Tính toán thu nhập dựa trên số lượng thú nuôi
            earned_gold = (st.session_state.chickens * 10) + (st.session_state.pigs * 30) + (st.session_state.cows * 70)
            st.session_state.gold += earned_gold
            st.session_state.score += 5
            st.success(f"🎉 Thu hoạch thành công! Bạn kiếm được +{earned_gold} Vàng từ trứng, sữa và nông sản.")
            st.rerun()
            
    with col_act2:
        if st.button("✨ Cưng nựng thú cưng (+10 XP)", use_container_width=True):
            st.session_state.score += 10
            st.balloons()
            st.success("💖 Các con vật rất vui và quấn quýt lấy bạn!")

    st.write("---")

    # KHU VỰC CỬA HÀNG MUA THÚ NUÔI
    st.subheader("🛒 Cửa Hàng Nông Trại (Mua Thú)")
    
    shop_c1, shop_c2, shop_c3 = st.columns(3)
    
    with shop_c1:
        if st.button("➕ Mua Gà (50 G)", use_container_width=True):
            if st.session_state.gold >= 50:
                st.session_state.gold -= 50
                st.session_state.chickens += 1
                st.success("Đã mua 1 chú Gà mới!")
                st.rerun()
            else:
                st.error("Không đủ vàng!")
                
    with shop_c2:
        if st.button("➕ Mua Heo (150 G)", use_container_width=True):
            if st.session_state.gold >= 150:
                st.session_state.gold -= 150
                st.session_state.pigs += 1
                st.success("Đã mua 1 chú Heo mũm mĩm!")
                st.rerun()
            else:
                st.error("Không đủ vàng!")

    with shop_c3:
        if st.button("➕ Mua Bò (350 G)", use_container_width=True):
            if st.session_state.gold >= 350:
                st.session_state.gold -= 350
                st.session_state.cows += 1
                st.success("Đã mua 1 chú Bò sữa!")
                st.rerun()
            else:
                st.error("Không đủ vàng!")
