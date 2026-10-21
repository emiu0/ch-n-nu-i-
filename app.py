import time
import random
import streamlit as st

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Trang Trại Thú Cưng 2D-3D GIFHUD",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- CSS TÙY CHỈNH GIAO DIỆN (GIFHUD & KUTE STYLE) ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #fbc531 0%, #e84118 100%);
    }
    .stButton>button {
        border-radius: 15px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    .pet-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        backdrop-filter: blur(8px);
        border: 2px solid rgba(255, 255, 255, 0.8);
        text-align: center;
    }
    .title-glow {
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# --- KHỞI TẠO TRẠNG THÁI GAME (SESSION STATE) ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.pet_name = "Mimi"
    st.session_state.pet_type = "Mèo Chibi 🐱"
    st.session_state.hunger = 80
    st.session_state.happiness = 80
    st.session_state.energy = 80
    st.session_state.cleanliness = 80
    st.session_state.coins = 200
    st.session_state.is_night = False
    st.session_state.quest_feed_count = 0
    st.session_state.quest_play_count = 0
    st.session_state.quest_claimed = [False, False]
    st.session_state.status_msg = "Chào mừng bạn đến với nông trại 2D-3D tuyệt đẹp!"
    st.session_state.current_gif = "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"

# --- KHO DỮ LIỆU GIF CÁC LOÀI ĐỘNG VẬT CHIBI CUTE ---
PET_DATABASE = {
    "Mèo Chibi 🐱": {
        "normal": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        "eat": "https://media.giphy.com/media/13CoX4K6orM0py/giphy.gif",
        "play": "https://media.giphy.com/media/5VKbvrjxpUJCM/giphy.gif",
        "sleep": "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
        "clean": "https://media.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif"
    },
    "Thỏ Ngọc 🐰": {
        "normal": "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif",
        "eat": "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",
        "play": "https://media.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.gif",
        "sleep": "https://media.giphy.com/media/10qyQYDe87nUI/giphy.gif",
        "clean": "https://media.giphy.com/media/ISOckXUybVfQ4/giphy.gif"
    },
    "Heo Sữa 🐷": {
        "normal": "https://media.giphy.com/media/10rNBP8yt1LOnm/giphy.gif",
        "eat": "https://media.giphy.com/media/13CoX4K6orM0py/giphy.gif",
        "play": "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif",
        "sleep": "https://media.giphy.com/media/ZVik7n0SM5iO4/giphy.gif",
        "clean": "https://media.giphy.com/media/3otPoEHWQx0v6dMkFy/giphy.gif"
    },
    "Cún Vàng 🐶": {
        "normal": "https://media.giphy.com/media/8v6Z3YyULB5Q0/giphy.gif",
        "eat": "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",
        "play": "https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif",
        "sleep": "https://media.giphy.com/media/3ohzdWqB150v0a74By/giphy.gif",
        "clean": "https://media.giphy.com/media/5GoLvjsfT7mlO/giphy.gif"
    }
}

# --- 1. MÀN HÌNH CHÍNH (START SCREEN) ---
if not st.session_state.game_started:
    st.markdown("<h1 style='text-align: center; color: white;' class='title-glow'>🐾 Nông Trại Thú Cưng 2D-3D (GIFHUD) 🐾</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #f1f2f6; font-size: 18px;'>Trải nghiệm nuôi thú cưng ảo sống động với hiệu ứng động tuyệt đẹp!</p>", unsafe_allow_html=True)
    
    # Nhúng âm thanh nền (Background Music) tự động phát qua HTML5 audio
    st.markdown("""
        <audio autoplay loop hidden>
            <source src="https://www.bensound.com/bensound-music/bensound-buddy.mp3" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", width=300)
        selected_type = st.selectbox("🌟 Chọn loài thú cưng khởi đầu:", list(PET_DATABASE.keys()))
        custom_name = st.text_input("✏️ Đặt tên cho thú cưng:", "Mimi")
        
        if st.button("🚀 BẮT ĐẦU VÀO TRANG TRẠI", use_container_width=True):
            st.session_state.pet_type = selected_type
            st.session_state.pet_name = custom_name
            st.session_state.current_gif = PET_DATABASE[selected_type]["normal"]
            st.session_state.game_started = True
            st.rerun()

else:
    # --- 2. GIAO DIỆN GAME CHÍNH (HUD & NÔNG TRẠI) ---
    
    # Nhúng âm thanh nền liên tục trong game
    st.markdown("""
        <audio autoplay loop hidden>
            <source src="https://www.bensound.com/bensound-music/bensound-buddy.mp3" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

    # Header hiển thị thông tin & nút đổi Ngày/Đêm
    col_h1, col_h2, col_h3 = st.columns([2, 2, 2])
    with col_h1:
        time_mode = "🌙 Đêm Lãng Mạn" if st.session_state.is_night else "☀️ Ngày Nắng Đẹp"
        st.markdown(f"### 🏡 {st.session_state.pet_name} ({st.session_state.pet_type})")
        st.caption(f"Thời gian: {time_mode}")
    with col_h2:
        st.markdown(f"### 🪙 Xu Vàng: {st.session_state.coins}")
    with col_h3:
        if st.button("🌗 Chuyển Ngày / Đêm"):
            st.session_state.is_night = not st.session_state.is_night
            st.rerun()

    st.markdown("---")

    # Layout hiển thị GIFHUD bên trái và Chỉ số bên phải
    col_left, col_right = st.columns([1.2, 1.8])

    with col_left:
        st.markdown(f"""
        <div class="pet-card">
            <img src="{st.session_state.current_gif}" width="100%" style="border-radius: 20px; max-height: 240px; object-fit: contain;">
            <h3 style="margin-top: 12px; color: #2f3640;">{st.session_state.pet_name}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.info(f"💬 **Trạng thái:** {st.session_state.status_msg}")

    with col_right:
        st.subheader("📊 Bảng Chỉ Số Sức Khỏe")
        
        # Giới hạn chỉ số từ 0 đến 100
        st.session_state.hunger = max(0, min(100, st.session_state.hunger))
        st.session_state.happiness = max(0, min(100, st.session_state.happiness))
        st.session_state.energy = max(0, min(100, st.session_state.energy))
        st.session_state.cleanliness = max(0, min(100, st.session_state.cleanliness))

        st.write(f"🍖 Độ No (Hunger): {st.session_state.hunger}/100")
        st.progress(st.session_state.hunger)

        st.write(f"⭐ Vui Vẻ (Happiness): {st.session_state.happiness}/100")
        st.progress(st.session_state.happiness)

        st.write(f"⚡ Năng Lượng (Energy): {st.session_state.energy}/100")
        st.progress(st.session_state.energy)

        st.write(f"✨ Sạch Sẽ (Cleanliness): {st.session_state.cleanliness}/100")
        st.progress(st.session_state.cleanliness)

    st.markdown("---")

    # --- 3. BẢNG ĐIỀU KHIỂN HÀNH ĐỘNG CHĂM SÓC ---
    st.subheader("🎮 Hành Động Chăm Sóc")
    b1, b2, b3, b4 = st.columns(4)

    with b1:
        if st.button("🍖 Cho Ăn (-10🪙)", use_container_width=True):
            if st.session_state.coins >= 10:
                st.session_state.coins -= 10
                st.session_state.hunger = min(100, st.session_state.hunger + 30)
                st.session_state.energy = min(100, st.session_state.energy + 5)
                st.session_state.quest_feed_count += 1
                st.session_state.current_gif = PET_DATABASE[st.session_state.pet_type]["eat"]
                st.session_state.status_msg = f"Ngon quá! {st.session_state.pet_name} đang thưởng thức đồ ăn."
                st.rerun()
            else:
                st.warning("Bạn không đủ xu để mua thức ăn!")

    with b2:
        if st.button("🎾 Chơi Đùa", use_container_width=True):
            if st.session_state.energy >= 15:
                st.session_state.happiness = min(100, st.session_state.happiness + 25)
                st.session_state.energy -= 15
                st.session_state.hunger = max(0, st.session_state.hunger - 10)
                st.session_state.coins += 20
                st.session_state.quest_play_count += 1
                st.session_state.current_gif = PET_DATABASE[st.session_state.pet_type]["play"]
                st.session_state.status_msg = f"Tuyệt vời! {st.session_state.pet_name} chơi vui vẻ và kiếm được 20🪙."
                st.rerun()
            else:
                st.warning(f"{st.session_state.pet_name} đã mệt, hãy cho bé đi ngủ nhé!")

    with b3:
        if st.button("💤 Đi Ngủ", use_container_width=True):
            st.session_state.energy = 100
            st.session_state.hunger = max(0, st.session_state.hunger - 15)
            st.session_state.current_gif = PET_DATABASE[st.session_state.pet_type]["sleep"]
            st.session_state.status_msg = f"Khò khò... {st.session_state.pet_name} đang ngủ một giấc thật sâu."
            st.rerun()

    with b4:
        if st.button("🚿 Tắm Rửa", use_container_width=True):
            st.session_state.cleanliness = 100
            st.session_state.happiness = min(100, st.session_state.happiness + 15)
            st.session_state.coins += 10
            st.session_state.current_gif = PET_DATABASE[st.session_state.pet_type]["clean"]
            st.session_state.status_msg = f"Thơm tho sạch sẽ! {st.session_state.pet_name} rất thích tắm."
            st.rerun()

    st.markdown("---")

    # --- 4. CỬA HÀNG VÀ THANH NHIỆM VỤ ---
    tab_shop, tab_quest = st.tabs(["🛍️ Cửa Hàng Thú Cưng", "📜 Thanh Nhiệm Vụ Kiếm Xu"])

    with tab_shop:
        st.write("Đổi hoặc nhận nuôi thêm các bé thú cưng siêu cute khác:")
        sc1, sc2, sc3, sc4 = st.columns(4)
        with sc1:
            if st.button("Nhận nuôi Mèo 🐱 (50🪙)") and st.session_state.coins >= 50:
                st.session_state.coins -= 50
                st.session_state.pet_type = "Mèo Chibi 🐱"
                st.session_state.pet_name = "Mimi"
                st.session_state.current_gif = PET_DATABASE["Mèo Chibi 🐱"]["normal"]
                st.rerun()
        with sc2:
            if st.button("Nhận nuôi Thỏ 🐰 (50🪙)") and st.session_state.coins >= 50:
                st.session_state.coins -= 50
                st.session_state.pet_type = "Thỏ Ngọc 🐰"
                st.session_state.pet_name = "Bouncy"
                st.session_state.current_gif = PET_DATABASE["Thỏ Ngọc 🐰"]["normal"]
                st.rerun()
        with sc3:
            if st.button("Nhận nuôi Heo 🐷 (50🪙)") and st.session_state.coins >= 50:
                st.session_state.coins -= 50
                st.session_state.pet_type = "Heo Sữa 🐷"
                st.session_state.pet_name = "Ú Nu"
                st.session_state.current_gif = PET_DATABASE["Heo Sữa 🐷"]["normal"]
                st.rerun()
        with sc4:
            if st.button("Nhận nuôi Cún 🐶 (50🪙)") and st.session_state.coins >= 50:
                st.session_state.coins -= 50
                st.session_state.pet_type = "Cún Vàng 🐶"
                st.session_state.pet_name = "Bobby"
                st.session_state.current_gif = PET_DATABASE["Cún Vàng 🐶"]["normal"]
                st.rerun()

    with tab_quest:
        st.write("Hoàn thành các mốc thử thách để nhận xu thưởng:")
        
        # Nhiệm vụ 1: Cho ăn 3 lần
        qc1, qc2 = st.columns([3, 1])
        with qc1:
            st.write(f"🍖 **Cho thú cưng ăn 3 lần** (Tiến độ: {st.session_state.quest_feed_count}/3)")
        with qc2:
            if st.session_state.quest_feed_count >= 3 and not st.session_state.quest_claimed[0]:
                if st.button("Nhận 30🪙", key="q1"):
                    st.session_state.coins += 30
                    st.session_state.quest_claimed[0] = True
                    st.success("Nhận thưởng thành công!")
                    st.rerun()
            elif st.session_state.quest_claimed[0]:
                st.write("✅ Đã nhận")
            else:
                st.write("🔒 Chưa xong")

        # Nhiệm vụ 2: Chơi đùa 2 lần
        qc3, qc4 = st.columns([3, 1])
        with qc3:
            st.write(f"🎾 **Chơi đùa với thú cưng 2 lần** (Tiến độ: {st.session_state.quest_play_count}/2)")
        with qc4:
            if st.session_state.quest_play_count >= 2 and not st.session_state.quest_claimed[1]:
                if st.button("Nhận 40🪙", key="q2"):
                    st.session_state.coins += 40
                    st.session_state.quest_claimed[1] = True
                    st.success("Nhận thưởng thành công!")
                    st.rerun()
            elif st.session_state.quest_claimed[1]:
                st.write("✅ Đã nhận")
            else:
                st.write("🔒 Chưa xong")

    # Sidebar cài đặt hệ thống
    with st.sidebar:
        st.header("⚙️ Cài Đặt Hệ Thống")
        if st.button("🔄 Chơi Lại Từ Đầu"):
            st.session_state.clear()
            st.rerun()
