import time
import random
import streamlit as st

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Mô Hình Chăn Nuôi Động Vật GIFHUD",
    page_icon="🐮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS TÙY CHỈNH GIAO DIỆN (GIFHUD & NÔNG TRẠI STYLE) ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e0f2fe 0%, #d1fae5 100%);
    }
    .stButton>button {
        border-radius: 12px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .animal-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 15px;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        border: 2px solid #a7f3d0;
        text-align: center;
    }
    .title-glow {
        text-shadow: 1px 1px 3px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# --- KHỞI TẠO TRẠNG THÁI HỆ THỐNG TRANG TRẠI ---
if "farm_started" not in st.session_state:
    st.session_state.farm_started = False
    st.session_state.coins = 300
    st.session_state.time_mode = "☀️ Ban Ngày"
    st.session_state.quest_fed = 0
    st.session_state.quest_claimed = False
    # Danh sách các mô hình động vật đang nuôi trong trang trại
    st.session_state.animals = [
        {"id": 1, "name": "Bò Sữa Béo", "type": "Bò 🐮", "hunger": 80, "happiness": 80, "stage": "Trưởng thành", "gif": "https://media.giphy.com/media/13CoX4K6orM0py/giphy.gif"},
        {"id": 2, "name": "Heo Hường Ú", "type": "Heo 🐷", "hunger": 70, "happiness": 75, "stage": "Trưởng thành", "gif": "https://media.giphy.com/media/10rNBP8yt1LOnm/giphy.gif"},
        {"id": 3, "name": "Cừu Bông Xù", "type": "Cừu 🐑", "hunger": 85, "happiness": 90, "stage": "Trưởng thành", "gif": "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif"}
    ]

# --- KHO DỮ LIỆU CÁC LOÀI ĐỘNG VẬT NÔNG TRẠI ---
ANIMAL_DATABASE = {
    "Bò 🐮": {"gif": "https://media.giphy.com/media/13CoX4K6orM0py/giphy.gif", "price": 100, "product": "Sữa tươi 🥛"},
    "Heo 🐷": {"gif": "https://media.giphy.com/media/10rNBP8yt1LOnm/giphy.gif", "price": 80, "product": "Trứng/Thịt sạch 🥓"},
    "Cừu 🐑": {"gif": "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", "price": 90, "product": "Len cừu ấm 🧶"},
    "Gà 🐔": {"gif": "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", "price": 50, "product": "Trứng gà ta 🥚"},
    "Ngựa 🐴": {"gif": "https://media.giphy.com/media/8v6Z3YyULB5Q0/giphy.gif", "price": 150, "product": "Sức kéo/Đua 🏆"}
}

# --- 1. MÀN HÌNH CHÍNH (START SCREEN) ---
if not st.session_state.farm_started:
    st.markdown("<h1 style='text-align: center; color: #065f46;' class='title-glow'>🚜 Mô Hình Chăn Nuôi Động Vật (GIFHUD) 🌾</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #047857; font-size: 18px;'>Quản lý trang trại, chăm sóc đàn gia súc và thu hoạch nông sản trực quan sinh động!</p>", unsafe_allow_html=True)
    
    # Nhúng âm thanh nền vui nhộn qua HTML5 audio
    st.markdown("""
        <audio autoplay loop hidden>
            <source src="https://www.bensound.com/bensound-music/bensound-buddy.mp3" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://media.giphy.com/media/13CoX4K6orM0py/giphy.gif", width=350)
        farm_name = st.text_input("🏷️ Đặt tên cho Trang Trại của bạn:", "Trang Trại Xanh Happy")
        
        if st.button("🚀 BẮT ĐẦU QUẢN LÝ TRANG TRẠI", use_container_width=True):
            st.session_state.farm_started = True
            st.session_state.farm_name = farm_name
            st.rerun()

else:
    # --- 2. GIAO DIỆN QUẢN LÝ TRANG TRẠI CHÍNH (HUD) ---
    
    # Âm thanh nền liên tục
    st.markdown("""
        <audio autoplay loop hidden>
            <source src="https://www.bensound.com/bensound-music/bensound-buddy.mp3" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

    # Thanh Header thông tin trang trại
    col_h1, col_h2, col_h3, col_h4 = st.columns([2, 1.5, 1.5, 1.5])
    with col_h1:
        st.markdown(f"### 🚜 {st.session_state.farm_name}")
        st.caption(f"Trạng thái: {st.session_state.time_mode}")
    with col_h2:
        st.markdown(f"### 🪙 Vàng: {st.session_state.coins}")
    with col_h3:
        st.markdown(f"### 🐾 Số lượng: {len(st.session_state.animals)} con")
    with col_h4:
        if st.button("🌗 Đổi Ngày / Đêm"):
            st.session_state.time_mode = "🌙 Đêm Yên Bình" if "☀️" in st.session_state.time_mode else "☀️ Ban Ngày"
            st.rerun()

    st.markdown("---")

    # --- KHU VỰC QUẢN LÝ ĐÀN GIA SÚC TRONG CHUỒNG (GRID VIEW) ---
    st.subheader("🏡 Khu Vực Chuồng Trại Động Vật (GIFHUD)")
    
    if not st.session_state.animals:
        st.info("Chuồng trại đang trống! Hãy vào cửa hàng bên dưới để mua thêm động vật nhé.")
    else:
        # Hiển thị danh sách động vật dưới dạng các cột grid
        cols = st.columns(min(3, len(st.session_state.animals)))
        for idx, animal in enumerate(st.session_state.animals):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="animal-card">
                    <img src="{animal['gif']}" width="100%" style="border-radius: 15px; max-height: 160px; object-fit: contain;">
                    <h4 style="margin-top: 8px; color: #065f46;">{animal['name']} ({animal['type']})</h4>
                    <p style="font-size: 13px; color: #4b5563; margin-bottom: 5px;">Giai đoạn: <b>{animal['stage']}</b></p>
                </div>
                """, unsafe_allow_html=True)
                
                # Thanh chỉ số cho từng con vật
                st.write(f"🍖 Đói: {animal['hunger']}/100")
                st.progress(animal['hunger'])
                st.write(f"⭐ Vui vẻ: {animal['happiness']}/100")
                st.progress(animal['happiness'])

                # Nút tương tác riêng cho từng con vật
                c_btn1, c_btn2 = st.columns(2)
                with c_btn1:
                    if st.button(f"🥕 Cho Ăn", key=f"feed_{animal['id']}"):
                        if st.session_state.coins >= 5:
                            st.session_state.coins -= 5
                            animal['hunger'] = min(100, animal['hunger'] + 30)
                            animal['happiness'] = min(100, animal['happiness'] + 10)
                            st.session_state.quest_fed += 1
                            st.success(f"Đã cho {animal['name']} ăn!")
                            st.rerun()
                        else:
                            st.warning("Không đủ vàng (-5🪙)")
                with c_btn2:
                    prod_name = ANIMAL_DATABASE[animal['type']]['product']
                    if st.button(f"🧺 Thu Hoạch", key=f"harvest_{animal['id']}"):
                        if animal['happiness'] >= 50:
                            earned = 25
                            st.session_state.coins += earned
                            animal['happiness'] = max(0, animal['happiness'] - 20)
                            st.success(f"Thu hoạch {prod_name} thành công (+{earned}🪙)!")
                            st.rerun()
                        else:
                            st.warning(f"{animal['name']} đang buồn chán, hãy chăm sóc thêm!")

                st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")

    # --- CỬA HÀNG VÀ NHIỆM VỤ TRANG TRẠI ---
    tab_shop, tab_quest = st.tabs(["🛒 Cửa Hàng Giống Vật Nuôi", "📜 Sổ Nhiệm Vụ Trang Trại"])

    with tab_shop:
        st.write("Mua thêm các giống động vật mới chất lượng cao cho trang trại của bạn:")
        s_cols = st.columns(len(ANIMAL_DATABASE))
        for idx, (anim_name, data) in enumerate(ANIMAL_DATABASE.items()):
            with s_cols[idx]:
                st.markdown(f"""
                <div style="background: white; padding: 10px; border-radius: 12px; text-align: center; border: 1px solid #d1d5db;">
                    <img src="{data['gif']}" width="80px" style="height: 70px; object-fit: contain;">
                    <p style="font-weight: bold; margin: 5px 0;">{anim_name}</p>
                    <p style="font-size: 12px; color: #6b7280;">Sản phẩm: {data['product']}</p>
                    <p style="font-size: 13px; color: #d97706; font-weight: bold;">Giá: {data['price']}🪙</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Nhận nuôi", key=f"buy_{anim_name}"):
                    if st.session_state.coins >= data['price']:
                        st.session_state.coins -= data['price']
                        new_id = len(st.session_state.animals) + 1
                        st.session_state.animals.append({
                            "id": new_id,
                            "name": f"Bé {anim_name.split()[0]} {new_id}",
                            "type": anim_name,
                            "hunger": 80,
                            "happiness": 80,
                            "stage": "Non",
                            "gif": data['gif']
                        })
                        st.success(f"Đã mua thành công bé {anim_name}!")
                        st.rerun()
                    else:
                        st.warning("Không đủ vàng để mua!")

    with tab_quest:
        st.write("Hoàn thành công việc hàng ngày để nhận thưởng tài chính cho trang trại:")
        qc1, qc2 = st.columns([3, 1])
        with qc1:
            st.write(f"🌾 **Cho gia súc ăn tổng cộng 5 lần** (Tiến độ: {st.session_state.quest_fed}/5)")
        with qc2:
            if st.session_state.quest_fed >= 5 and not st.session_state.quest_claimed:
                if st.button("Nhận 50🪙", key="claim_q"):
                    st.session_state.coins += 50
                    st.session_state.quest_claimed = True
                    st.success("Nhận thưởng thành công!")
                    st.rerun()
            elif st.session_state.quest_claimed:
                st.write("✅ Đã nhận")
            else:
                st.write("🔒 Chưa xong")

    # Sidebar hệ thống
    with st.sidebar:
        st.header("⚙️ Quản Lý Trang Trại")
        if st.button("🔄 Khởi Tạo Lại Trang Trại"):
            st.session_state.clear()
            st.rerun()
