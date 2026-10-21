<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang Trại Thú Cưng 3D Kawaii</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
        body { font-family: 'Nunito', sans-serif; user-select: none; overflow: hidden; background: #0f172a; }
        .glass { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); border: 2px solid rgba(255, 255, 255, 0.6); }
        @keyframes float { 0%, 100% { transform: translateY(0px) rotate(0deg); } 50% { transform: translateY(-12px) rotate(2deg); } }
        .pet-float { animation: float 3s ease-in-out infinite; }
        @keyframes pulse-glow { 0%, 100% { filter: drop-shadow(0 0 15px rgba(255,182,193,0.8)); } 50% { filter: drop-shadow(0 0 30px rgba(255,105,180,1)); } }
        .cute-glow { animation: pulse-glow 2s infinite; }
    </style>
</head>
<body class="w-screen h-screen relative flex flex-col justify-between">

    <!-- MÀN HÌNH CHÍNH BẮT ĐẦU -->
    <div id="start-screen" class="absolute inset-0 z-50 flex items-center justify-center bg-gradient-to-br from-pink-300 via-purple-300 to-emerald-300 transition-opacity duration-700">
        <div class="glass p-10 rounded-3xl shadow-2xl text-center max-w-md mx-4 transform hover:scale-105 transition">
            <div class="text-6xl mb-4 animate-bounce">🐰 🐱 🐷 🐥</div>
            <h1 class="text-4xl font-black text-pink-600 mb-2">Trang Trại Kawaii 3D</h1>
            <p class="text-gray-600 font-bold mb-6">Chăm sóc, cho ăn và chơi đùa cùng các bé thú cưng siêu đáng yêu!</p>
            <button onclick="startGame()" class="w-full py-4 bg-gradient-to-r from-pink-500 to-purple-600 text-white font-black text-xl rounded-2xl shadow-lg hover:opacity-90 transform active:scale-95 transition">
                🚀 BẮT ĐẦU CHƠI NGAY
            </button>
        </div>
    </div>

    <!-- KHU VỰC 3D MÔ PHỎNG NÔNG TRẠI -->
    <div id="world-bg" class="absolute inset-0 transition-colors duration-1000 bg-gradient-to-b from-sky-300 to-emerald-200 flex flex-col items-center justify-center">
        <!-- Đám mây trôi trang trí -->
        <div class="absolute top-10 left-10 text-white/80 text-4xl animate-pulse">☁️</div>
        <div class="absolute top-16 right-20 text-white/80 text-5xl animate-pulse">☁️</div>
        
        <!-- KHU VỰC HIỂN THỊ THÚ CƯNG 3D (CHIBI MÁ HỒNG CHUẨN ẢNH) -->
        <div class="relative mt-12 flex flex-col items-center">
            <!-- Hiệu ứng bóng đổ dưới chân -->
            <div class="w-48 h-12 bg-black/15 rounded-full blur-md absolute -bottom-4"></div>
            
            <!-- Mô hình Thú cưng SVG 3D Layered Chibi Cute -->
            <div id="pet-avatar-container" class="pet-float cute-glow cursor-pointer transition transform active:scale-95" onclick="petTap()">
                <svg id="pet-svg" width="240" height="240" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <!-- Thân mèo/thú cưng tròn trĩnh -->
                    <circle cx="100" cy="110" r="65" fill="#FFF0F5" stroke="#E2A5B8" stroke-width="4"/>
                    <!-- Tai trái & phải -->
                    <path d="M55 70L40 30L80 50Z" fill="#FFF0F5" stroke="#E2A5B8" stroke-width="4" stroke-linejoin="round"/>
                    <path d="M145 70L160 30L120 50Z" fill="#FFF0F5" stroke="#E2A5B8" stroke-width="4" stroke-linejoin="round"/>
                    <path d="M57 65L47 38L73 52Z" fill="#FFB6C1"/>
                    <path d="M143 65L153 38L127 52Z" fill="#FFB6C1"/>
                    <!-- Má hồng lém lỉnh -->
                    <circle cx="70" cy="115" r="12" fill="#FF69B4" opacity="0.6"/>
                    <circle cx="130" cy="115" r="12" fill="#FF69B4" opacity="0.6"/>
                    <!-- Mắt long lanh -->
                    <circle cx="80" cy="95" r="7" fill="#333333"/>
                    <circle cx="120" cy="95" r="7" fill="#333333"/>
                    <circle cx="82" cy="93" r="2.5" fill="white"/>
                    <circle cx="122" cy="93" r="2.5" fill="white"/>
                    <!-- Mũi miệng kawaii -->
                    <path d="M97 105C97 103 103 103 103 105C103 108 97 108 97 105Z" fill="#FF69B4"/>
                    <path d="M93 112C96 115 104 115 107 112" stroke="#4A3B32" stroke-width="3" stroke-linecap="round"/>
                </svg>
            </div>
            
            <h2 id="pet-name-tag" class="mt-4 text-2xl font-black text-white drop-shadow-md">Mimi (Mèo Mập)</h2>
        </div>
    </div>

    <!-- GIAO DIỆN HUD ĐIỀU KHIỂN TRONG GAME -->
    <div id="ui-layer" class="z-20 p-4 flex flex-col justify-between h-full pointer-events-none hidden">
        
        <!-- Top Navigation -->
        <div class="flex justify-between items-center pointer-events-auto">
            <div class="glass px-5 py-3 rounded-2xl shadow-lg flex items-center gap-3">
                <span class="text-2xl" id="hud-emoji">🐱</span>
                <div>
                    <h3 class="font-black text-gray-800 text-sm" id="hud-name">Mimi</h3>
                    <div class="flex gap-2 mt-0.5">
                        <span id="time-badge" class="text-xs font-bold bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full">☀️ Ban Ngày</span>
                        <span id="coin-badge" class="text-xs font-bold bg-yellow-100 text-yellow-700 px-2 py-0.5 rounded-full">🪙 150 Xu</span>
                    </div>
                </div>
            </div>

            <div class="flex gap-2">
                <button onclick="toggleShop()" class="glass px-4 py-3 rounded-2xl font-black text-purple-600 shadow-lg hover:bg-purple-50 transition">🛍️ Cửa Hàng</button>
                <button onclick="toggleQuests()" class="glass px-4 py-3 rounded-2xl font-black text-emerald-600 shadow-lg hover:bg-emerald-50 transition">📜 Nhiệm Vụ</button>
            </div>
        </div>

        <!-- Thông báo giữa màn hình -->
        <div id="toast" class="self-center glass px-6 py-2 rounded-full shadow-lg font-bold text-gray-800 text-sm transition-all duration-300 opacity-0 transform -translate-y-4">
            Chào mừng bạn đến với nông trại!
        </div>

        <!-- Bottom Dashboard Panel -->
        <div class="glass p-5 rounded-3xl shadow-xl pointer-events-auto max-w-2xl mx-auto w-full flex flex-col gap-3">
            <!-- Thanh chỉ số -->
            <div class="grid grid-cols-3 gap-4">
                <div>
                    <div class="flex justify-between text-xs font-bold text-gray-700 mb-1">
                        <span>🍖 No Nê</span> <span id="hunger-txt">80/100</span>
                    </div>
                    <div class="w-full bg-gray-200 h-3 rounded-full overflow-hidden">
                        <div id="hunger-bar" class="bg-amber-500 h-full w-4/5 transition-all"></div>
                    </div>
                </div>
                <div>
                    <div class="flex justify-between text-xs font-bold text-gray-700 mb-1">
                        <span>⭐ Vui Vẻ</span> <span id="happy-txt">80/100</span>
                    </div>
                    <div class="w-full bg-gray-200 h-3 rounded-full overflow-hidden">
                        <div id="happy-bar" class="bg-pink-500 h-full w-4/5 transition-all"></div>
                    </div>
                </div>
                <div>
                    <div class="flex justify-between text-xs font-bold text-gray-700 mb-1">
                        <span>⚡ Năng Lượng</span> <span id="energy-txt">80/100</span>
                    </div>
                    <div class="w-full bg-gray-200 h-3 rounded-full overflow-hidden">
                        <div id="energy-bar" class="bg-cyan-500 h-full w-4/5 transition-all"></div>
                    </div>
                </div>
            </div>

            <!-- Các nút hành động chăm sóc -->
            <div class="grid grid-cols-4 gap-3 pt-1">
                <button onclick="feedPet()" class="py-3 bg-amber-400 hover:bg-amber-500 text-white font-black rounded-2xl shadow transition transform active:scale-95">🍖 Cho Ăn (-10🪙)</button>
                <button onclick="playPet()" class="py-3 bg-pink-400 hover:bg-pink-500 text-white font-black rounded-2xl shadow transition transform active:scale-95">🎾 Chơi Đùa</button>
                <button onclick="sleepPet()" class="py-3 bg-indigo-400 hover:bg-indigo-500 text-white font-black rounded-2xl shadow transition transform active:scale-95">💤 Đi Ngủ</button>
                <button onclick="cleanPet()" class="py-3 bg-emerald-400 hover:bg-emerald-500 text-white font-black rounded-2xl shadow transition transform active:scale-95">✨ Dọn Vệ Sinh</button>
            </div>
        </div>
    </div>

    <!-- CỬA HÀNG MODAL -->
    <div id="shop-modal" class="fixed inset-0 z-40 bg-black/50 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="glass p-6 rounded-3xl max-w-md w-full shadow-2xl relative">
            <button onclick="toggleShop()" class="absolute top-4 right-4 text-gray-500 hover:text-black font-black text-xl">✕</button>
            <h3 class="text-2xl font-black text-purple-700 mb-4">🛍️ Cửa Hàng Thú Cưng</h3>
            <div class="space-y-3 max-h-96 overflow-y-auto pr-1">
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div class="flex items-center gap-3"><span class="text-3xl">🐱</span><div><h4 class="font-bold">Mèo Mập Mimi</h4><p class="text-xs text-gray-500">Đáng yêu, dễ nuôi</p></div></div>
                    <button onclick="changePet('Mimi', '🐱', 'cat')" class="px-3 py-1.5 bg-purple-600 text-white font-bold rounded-xl text-sm">Chọn</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div class="flex items-center gap-3"><span class="text-3xl">🐰</span><div><h4 class="font-bold">Thỏ Hồng Bouncy</h4><p class="text-xs text-gray-500">Năng động, thích nhảy</p></div></div>
                    <button onclick="changePet('Bouncy', '🐰', 'rabbit')" class="px-3 py-1.5 bg-purple-600 text-white font-bold rounded-xl text-sm">Mua (50🪙)</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div class="flex items-center gap-3"><span class="text-3xl">🐷</span><div><h4 class="font-bold">Heo Sữa Ú Nu</h4><p class="text-xs text-gray-500">Mập mạp tròn xoe</p></div></div>
                    <button onclick="changePet('Ú Nu', '🐷', 'pig')" class="px-3 py-1.5 bg-purple-600 text-white font-bold rounded-xl text-sm">Mua (50🪙)</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div class="flex items-center gap-3"><span class="text-3xl">🐥</span><div><h4 class="font-bold">Gà Vàng Chip</h4><p class="text-xs text-gray-500">Tinh nghịch, lém lỉnh</p></div></div>
                    <button onclick="changePet('Chip', '🐥', 'chick')" class="px-3 py-1.5 bg-purple-600 text-white font-bold rounded-xl text-sm">Mua (50🪙)</button>
                </div>
            </div>
        </div>
    </div>

    <!-- NHIỆM VỤ MODAL -->
    <div id="quest-modal" class="fixed inset-0 z-40 bg-black/50 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="glass p-6 rounded-3xl max-w-md w-full shadow-2xl relative">
            <button onclick="toggleQuests()" class="absolute top-4 right-4 text-gray-500 hover:text-black font-black text-xl">✕</button>
            <h3 class="text-2xl font-black text-emerald-700 mb-4">📜 Nhiệm Vụ Hàng Ngày</h3>
            <div class="space-y-3">
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div><h4 class="font-bold text-gray-800">Cho thú cưng ăn 3 lần</h4><p class="text-xs text-gray-500" id="q1-desc">Tiến độ: 0/3</p></div>
                    <button id="q1-btn" onclick="claimQuest(1, 30)" class="px-3 py-1.5 bg-gray-300 text-gray-600 font-bold rounded-xl text-sm cursor-not-allowed" disabled>Nhận 30🪙</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div><h4 class="font-bold text-gray-800">Chơi đùa 2 lần</h4><p class="text-xs text-gray-500" id="q2-desc">Tiến độ: 0/2</p></div>
                    <button id="q2-btn" onclick="claimQuest(2, 40)" class="px-3 py-1.5 bg-gray-300 text-gray-600 font-bold rounded-xl text-sm cursor-not-allowed" disabled>Nhận 40🪙</button>
                </div>
            </div>
        </div>
    </div>

    <!-- JAVASCRIPT GAME LOGIC -->
    <script>
        let coins = 150;
        let hunger = 80;
        let happy = 80;
        let energy = 80;
        let petName = "Mimi";
        let petType = "cat";
        let isNight = false;

        let quests = { feed: 0, play: 0, q1Done: false, q2Done: false };

        // Web Audio API Tổng hợp âm thanh vui nhộn
        let audioCtx = null;
        function playSound(type) {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                let osc = audioCtx.createOscillator();
                let gain = audioCtx.createGain();
                osc.connect(gain); gain.connect(audioCtx.destination);
                let now = audioCtx.currentTime;

                if (type === 'click') {
                    osc.frequency.setValueAtTime(400, now); osc.frequency.exponentialRampToValueAtTime(700, now + 0.1);
                    gain.gain.setValueAtTime(0.1, now); gain.gain.linearRampToValueAtTime(0.01, now + 0.1);
                    osc.start(now); osc.stop(now + 0.1);
                } else if (type === 'success') {
                    osc.frequency.setValueAtTime(523.25, now); osc.frequency.setValueAtTime(659.25, now + 0.1); osc.frequency.setValueAtTime(783.99, now + 0.2);
                    gain.gain.setValueAtTime(0.15, now); gain.gain.linearRampToValueAtTime(0.01, now + 0.3);
                    osc.start(now); osc.stop(now + 0.3);
                }
            } catch(e) {}
        }

        function startGame() {
            playSound('success');
            document.getElementById('start-screen').classList.add('opacity-0', 'pointer-events-none');
            setTimeout(() => document.getElementById('start-screen').style.display = 'none', 700);
            document.getElementById('ui-layer').classList.remove('hidden');
            showToast("Chào mừng bạn đến với thế giới thú cưng 3D!");
        }

        function showToast(msg) {
            let t = document.getElementById('toast');
            t.innerText = msg;
            t.classList.remove('opacity-0', '-translate-y-4');
            setTimeout(() => t.classList.add('opacity-0', '-translate-y-4'), 2500);
        }

        function updateUI() {
            document.getElementById('coin-badge').innerText = `🪙 ${coins} Xu`;
            document.getElementById('hunger-txt').innerText = `${hunger}/100`;
            document.getElementById('hunger-bar').style.width = `${hunger}%`;
            document.getElementById('happy-txt').innerText = `${happy}/100`;
            document.getElementById('happy-bar').style.width = `${happy}%`;
            document.getElementById('energy-txt').innerText = `${energy}/100`;
            document.getElementById('energy-bar').style.width = `${energy}%`;

            // Kiểm tra nhiệm vụ
            if (quests.feed >= 3 && !quests.q1Done) {
                let btn = document.getElementById('q1-btn');
                btn.className = "px-3 py-1.5 bg-emerald-600 text-white font-bold rounded-xl text-sm hover:bg-emerald-700";
                btn.removeAttribute('disabled');
            }
            document.getElementById('q1-desc').innerText = `Tiến độ: ${quests.feed}/3`;

            if (quests.play >= 2 && !quests.q2Done) {
                let btn = document.getElementById('q2-btn');
                btn.className = "px-3 py-1.5 bg-emerald-600 text-white font-bold rounded-xl text-sm hover:bg-emerald-700";
                btn.removeAttribute('disabled');
            }
            document.getElementById('q2-desc').innerText = `Tiến độ: ${quests.play}/2`;
        }

        function petTap() {
            happy = Math.min(100, happy + 5);
            playSound('click');
            showToast(`${petName} kêu gừ gừ rất thích thú!`);
            updateUI();
        }

        function feedPet() {
            if (coins < 10) { showToast("Bạn không đủ 10 xu!"); return; }
            coins -= 10;
            hunger = Math.min(100, hunger + 25);
            quests.feed++;
            playSound('success');
            showToast(`Yummy! ${petName} đã ăn rất ngon.`);
            updateUI();
        }

        function playPet() {
            happy = Math.min(100, happy + 20);
            energy = Math.max(0, energy - 10);
            coins += 15;
            quests.play++;
            playSound('success');
            showToast(`${petName} chơi đùa vui vẻ và kiếm được 15 xu!`);
            updateUI();
        }

        function sleepPet() {
            energy = 100;
            hunger = Math.max(0, hunger - 15);
            isNight = !isNight;
            let bg = document.getElementById('world-bg');
            let badge = document.getElementById('time-badge');
            if (isNight) {
                bg.className = "absolute inset-0 transition-colors duration-1000 bg-gradient-to-b from-indigo-950 to-slate-900 flex flex-col items-center justify-center";
                badge.className = "text-xs font-bold bg-indigo-900 text-indigo-200 px-2 py-0.5 rounded-full";
                badge.innerText = "🌙 Ban Đêm";
                showToast(`Khò khò... ${petName} đã đi ngủ ngon giấc.`);
            } else {
                bg.className = "absolute inset-0 transition-colors duration-1000 bg-gradient-to-b from-sky-300 to-emerald-200 flex flex-col items-center justify-center";
                badge.className = "text-xs font-bold bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full";
                badge.innerText = "☀️ Ban Ngày";
                showToast(`Chào buổi sáng! ${petName} đã thức dậy.`);
            }
            updateUI();
        }

        function cleanPet() {
            happy = Math.min(100, happy + 10);
            coins += 5;
            playSound('success');
            showToast(`Sạch sẽ thơm tho! Nhận 5 xu.`);
            updateUI();
        }

        function toggleShop() { document.getElementById('shop-modal').classList.toggle('hidden'); }
        function toggleQuests() { document.getElementById('quest-modal').classList.toggle('hidden'); }

        function changePet(name, emoji, type) {
            petName = name;
            petType = type;
            document.getElementById('hud-emoji').innerText = emoji;
            document.getElementById('hud-name').innerText = name;
            document.getElementById('pet-name-tag').innerText = `${name} (${emoji})`;
            
            // Thay đổi SVG hình dáng phù hợp
            let svg = document.getElementById('pet-svg');
            if (type === 'rabbit') {
                svg.innerHTML = `<circle cx="100" cy="110" r="60" fill="#FFF0F5" stroke="#E2A5B8" stroke-width="4"/><path d="M75 55L70 15C70 10 90 10 90 25L85 55Z" fill="#FFF0F5" stroke="#E2A5B8" stroke-width="3"/><path d="M125 55L130 15C130 10 110 10 110 25L115 55Z" fill="#FFF0F5" stroke="#E2A5B8" stroke-width="3"/><circle cx="70" cy="110" r="10" fill="#FF69B4" opacity="0.6"/><circle cx="130" cy="110" r="10" fill="#FF69B4" opacity="0.6"/><circle cx="80" cy="95" r="6" fill="#33"/><circle cx="120" cy="95" r="6" fill="#33"/><path d="M97 105C97 103 103 103 103 105C103 108 97 108 97 105Z" fill="#FF69B4"/><path d="M94 112L106 112" stroke="#333" stroke-width="3" stroke-linecap="round"/>`;
            } else if (type === 'pig') {
                svg.innerHTML = `<circle cx="100" cy="110" r="65" fill="#FFC0CB" stroke="#E095A5" stroke-width="4"/><ellipse cx="70" cy="65" rx="15" ry="12" fill="#FFB6C1"/><ellipse cx="130" cy="65" rx="15" ry="12" fill="#FFB6C1"/><circle cx="70" cy="115" r="12" fill="#FF69B4" opacity="0.5"/><circle cx="130" cy="115" r="12" fill="#FF69B4" opacity="0.5"/><circle cx="80" cy="95" r="6" fill="#33"/><circle cx="120" cy="95" r="6" fill="#33"/><ellipse cx="100" cy="110" rx="14" ry="10" fill="#FF94B8"/><circle cx="95" cy="110" r="2" fill="#D87093"/><circle cx="105" cy="110" r="2" fill="#D87093"/>`;
            } else if (type === 'chick') {
                svg.innerHTML = `<circle cx="100" cy="110" r="60" fill="#FFD700" stroke="#E5B800" stroke-width="4"/><circle cx="70" cy="110" r="10" fill="#FF8C00" opacity="0.6"/><circle cx="130" cy="110" r="10" fill="#FF8C00" opacity="0.6"/><circle cx="80" cy="95" r="6" fill="#33"/><circle cx="120" cy="95" r="6" fill="#33"/><polygon points="95,105 105,105 100,115" fill="#FF8C00"/>`;
            }
            
            playSound('success');
            showToast(`Đã đổi sang bé ${name} thành công!`);
            toggleShop();
            updateUI();
        }

        function claimQuest(id, reward) {
            coins += reward;
            if (id === 1) {
                quests.q1Done = true;
                let b = document.getElementById('q1-btn'); b.innerText = "Đã Nhận"; b.className = "px-3 py-1.5 bg-gray-300 text-gray-500 font-bold rounded-xl text-sm cursor-not-allowed"; b.setAttribute('disabled', 'true');
            } else if (id === 2) {
                quests.q2Done = true;
                let b = document.getElementById('q2-btn'); b.innerText = "Đã Nhận"; b.className = "px-3 py-1.5 bg-gray-300 text-gray-500 font-bold rounded-xl text-sm cursor-not-allowed"; b.setAttribute('disabled', 'true');
            }
            playSound('success');
            showToast(`Nhận thành công ${reward} xu thưởng nhiệm vụ!`);
            updateUI();
        }
    </script>
</body>
</html>
