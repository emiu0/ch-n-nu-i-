<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang Trại Thú Cưng 3D Nâng Cấp</title>
    <!-- Tailwind CSS for UI -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700;800&display=swap" rel="stylesheet">
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Three.js Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <!-- Canvas Confetti for celebrations -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        body {
            font-family: 'Quicksand', sans-serif;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            overflow: hidden;
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 8px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
        .pulse-slow {
            animation: pulseSlow 3s infinite ease-in-out;
        }
        @keyframes pulseSlow {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        .float-anim {
            animation: floatText 1.5s ease-out forwards;
        }
        @keyframes floatText {
            0% { transform: translateY(0px) scale(0.8); opacity: 1; }
            100% { transform: translateY(-50px) scale(1.2); opacity: 0; }
        }
    </style>
</head>
<body class="bg-emerald-900 text-slate-800 m-0 p-0 w-screen h-screen overflow-hidden">

    <!-- Audio toggle & Background Music status badge -->
    <div id="audio-indicator" class="fixed top-4 right-4 z-50 flex items-center gap-2 bg-white/85 backdrop-blur-md px-3.5 py-2 rounded-full shadow-lg border border-white/50 text-xs font-bold text-emerald-700 cursor-pointer transition hover:bg-white" onclick="toggleAudioSystem()">
        <i id="audio-icon" class="fa-solid fa-volume-high text-emerald-600 text-sm"></i>
        <span id="audio-text">Âm thanh: Bật</span>
    </div>

    <!-- TITLE SCREEN / MAIN MENU -->
    <div id="title-screen" class="fixed inset-0 z-50 flex flex-col items-center justify-center bg-gradient-to-b from-sky-300 via-emerald-200 to-emerald-400 p-4 transition-opacity duration-700">
        <div class="absolute top-10 left-10 w-24 h-12 bg-white/60 rounded-full blur-sm pulse-slow"></div>
        <div class="absolute top-20 right-16 w-32 h-16 bg-white/60 rounded-full blur-sm pulse-slow" style="animation-delay: 1s;"></div>
        
        <div class="bg-white/90 backdrop-blur-md p-8 md:p-12 rounded-3xl shadow-2xl border-4 border-emerald-500 max-w-lg w-full text-center relative overflow-hidden transform transition-all">
            <div class="absolute -top-10 -right-10 w-28 h-28 bg-amber-400 rounded-full flex items-end justify-start p-6 shadow-inner rotate-12">
                <span class="text-2xl">🌟</span>
            </div>

            <h1 class="text-3xl md:text-5xl font-extrabold text-emerald-700 mb-2 drop-shadow-md tracking-wide">
                Trang Trại Thú Cưng <span class="text-pink-500">Chibi 3D</span>
            </h1>
            <p class="text-emerald-600 font-semibold mb-6 text-sm md:text-base">
                16 bé động vật siêu tròn trĩnh, má hồng kawaii như tranh vẽ!
            </p>

            <div class="flex flex-col gap-3">
                <button onclick="startGame()" class="group relative inline-flex items-center justify-center px-8 py-4 font-bold text-white transition-all bg-emerald-500 rounded-2xl shadow-lg hover:bg-emerald-600 active:scale-95 border-b-4 border-emerald-700 text-lg">
                    <i class="fa-solid fa-play mr-3 text-xl group-hover:scale-125 transition-transform"></i> Vào Nông Trại
                </button>
                <button onclick="openTutorial()" class="inline-flex items-center justify-center px-6 py-3 font-bold text-emerald-700 transition-all bg-emerald-100 rounded-2xl shadow hover:bg-emerald-200 active:scale-95 border-b-2 border-emerald-300 text-sm md:text-base">
                    <i class="fa-solid fa-book-open mr-2"></i> Hướng dẫn chơi
                </button>
                <button onclick="openCredits()" class="inline-flex items-center justify-center px-6 py-3 font-bold text-slate-600 transition-all bg-slate-100 rounded-2xl shadow hover:bg-slate-200 active:scale-95 text-xs">
                    <i class="fa-solid fa-circle-info mr-1"></i> Thông tin phiên bản
                </button>
            </div>
        </div>
        <div class="mt-6 text-emerald-800 font-bold text-xs md:text-sm bg-white/40 px-4 py-1.5 rounded-full shadow backdrop-blur-sm">
            ✨ Thiết kế Chibi siêu dễ thương, má hồng rực rỡ, nhiệm vụ phong phú ✨
        </div>
    </div>

    <!-- TUTORIAL MODAL -->
    <div id="tutorial-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm p-4 hidden">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border-4 border-emerald-400 relative">
            <h2 class="text-2xl font-extrabold text-emerald-700 mb-4 flex items-center gap-2">
                <i class="fa-solid fa-circle-question text-amber-500"></i> Hướng Dẫn Chơi
            </h2>
            <div class="space-y-3 text-sm text-slate-700 max-h-[60vh] overflow-y-auto pr-2">
                <div class="flex items-start gap-3 bg-emerald-50 p-3 rounded-xl">
                    <span class="text-xl">🐾</span>
                    <div><strong>Vuốt ve thú:</strong> Click/Chạm vào bất kỳ bé thú nào để vuốt ve, làm má hồng rực rỡ và tăng hạnh phúc!</div>
                </div>
                <div class="flex items-start gap-3 bg-amber-50 p-3 rounded-xl">
                    <span class="text-xl">🍎</span>
                    <div><strong>Cho ăn uống:</strong> Mở Cửa hàng Thức ăn để mua táo, cỏ, sữa, ngô hoặc nước cho các bé.</div>
                </div>
                <div class="flex items-start gap-3 bg-pink-50 p-3 rounded-xl">
                    <span class="text-xl">🧹</span>
                    <div><strong>Dọn dẹp:</strong> Thú cưng thỉnh thoảng thải phân. Nhấp vào phân để dọn dẹp và nhận xu vàng!</div>
                </div>
                <div class="flex items-start gap-3 bg-blue-50 p-3 rounded-xl">
                    <span class="text-xl">📜</span>
                    <div><strong>Nhiệm vụ:</strong> Hoàn thành thanh nhiệm vụ hàng ngày để nhận thưởng xu vàng hấp dẫn.</div>
                </div>
            </div>
            <button onclick="closeTutorial()" class="w-full mt-6 bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-3 rounded-xl shadow transition active:scale-95">
                Đã hiểu, vào game ngay!
            </button>
        </div>
    </div>

    <!-- CREDITS MODAL -->
    <div id="credits-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm p-4 hidden">
        <div class="bg-white rounded-3xl max-w-sm w-full p-6 shadow-2xl border-4 border-amber-400 text-center">
            <div class="text-4xl mb-2">🐾</div>
            <h2 class="text-xl font-extrabold text-slate-800 mb-1">Trang Trại Thú Cưng Chibi 3D</h2>
            <p class="text-xs text-slate-500 mb-4">Phiên bản 16 Loài Động Vật Siêu Dễ Thương</p>
            <p class="text-sm text-slate-600 mb-6 bg-amber-50 p-3 rounded-xl">
                Lấy cảm hứng từ phong cách chibi tròn trĩnh với má hồng kawaii, mang lại trải nghiệm thư giãn tuyệt vời.
            </p>
            <button onclick="closeCredits()" class="w-full bg-slate-800 hover:bg-slate-900 text-white font-bold py-2.5 rounded-xl text-sm transition">
                Đóng
            </button>
        </div>
    </div>

    <!-- GAME UI OVERLAY -->
    <div id="game-ui" class="absolute inset-0 pointer-events-none flex flex-col justify-between p-4 md:p-6 hidden">
        
        <!-- TOP BAR -->
        <div class="flex justify-between items-center pointer-events-auto gap-2 flex-wrap">
            <div class="flex items-center gap-3 bg-white/90 backdrop-blur-md px-4 py-2 rounded-2xl shadow-lg border border-white/60">
                <div class="flex items-center gap-1.5 font-bold text-amber-600">
                    <i class="fa-solid fa-coins text-amber-500"></i>
                    <span id="coin-count">250</span>
                </div>
                <div class="h-4 w-px bg-slate-200"></div>
                <div class="flex items-center gap-1.5 font-bold text-emerald-600">
                    <i class="fa-solid fa-paw text-emerald-500"></i>
                    <span id="pet-count">4</span>/16
                </div>
            </div>

            <div class="flex items-center gap-2 bg-white/90 backdrop-blur-md px-3 py-1.5 rounded-2xl shadow-lg border border-white/60">
                <button onclick="toggleDayNight()" id="daynight-btn" class="flex items-center gap-1.5 px-3 py-1 rounded-xl bg-amber-100 text-amber-700 font-bold text-xs hover:bg-amber-200 transition">
                    <i id="daynight-icon" class="fa-solid fa-sun text-amber-500"></i> <span id="daynight-label">Ban ngày</span>
                </button>
            </div>

            <div class="flex items-center gap-2">
                <button onclick="openQuestModal()" class="flex items-center gap-1.5 bg-gradient-to-r from-yellow-400 to-amber-500 hover:from-yellow-500 hover:to-amber-600 text-white font-bold px-3.5 py-2 rounded-2xl shadow-lg transition active:scale-95 text-xs md:text-sm">
                    <i class="fa-solid fa-scroll"></i> <span class="hidden sm:inline">Nhiệm vụ</span>
                </button>
                <button onclick="openShopModal('food')" class="flex items-center gap-1.5 bg-gradient-to-r from-orange-400 to-amber-500 hover:from-orange-500 hover:to-amber-600 text-white font-bold px-3.5 py-2 rounded-2xl shadow-lg transition active:scale-95 text-xs md:text-sm">
                    <i class="fa-solid fa-bowl-food"></i> <span class="hidden sm:inline">Thức ăn</span>
                </button>
                <button onclick="openShopModal('animals')" class="flex items-center gap-1.5 bg-gradient-to-r from-emerald-400 to-teal-500 hover:from-emerald-500 hover:to-teal-600 text-white font-bold px-3.5 py-2 rounded-2xl shadow-lg transition active:scale-95 text-xs md:text-sm">
                    <i class="fa-solid fa-store"></i> <span class="hidden sm:inline">Thú cưng</span>
                </button>
                <button onclick="openShopModal('decor')" class="flex items-center gap-1.5 bg-gradient-to-r from-purple-400 to-pink-500 hover:from-purple-500 hover:to-pink-600 text-white font-bold px-3.5 py-2 rounded-2xl shadow-lg transition active:scale-95 text-xs md:text-sm">
                    <i class="fa-solid fa-house-chimney"></i> <span class="hidden sm:inline">Trang trí</span>
                </button>
            </div>
        </div>

        <!-- BOTTOM BAR -->
        <div class="flex justify-between items-end pointer-events-auto">
            <div id="selected-pet-panel" class="bg-white/90 backdrop-blur-md p-4 rounded-3xl shadow-xl border border-white/60 max-w-xs w-full hidden transition-all duration-300">
                <div class="flex justify-between items-center mb-2">
                    <h3 id="panel-pet-name" class="font-extrabold text-emerald-700 text-base">Bé Cừu Chibi</h3>
                    <button onclick="closePetPanel()" class="text-slate-400 hover:text-slate-600 text-xs font-bold"><i class="fa-solid fa-xmark text-lg"></i></button>
                </div>
                <div class="space-y-2 text-xs font-semibold">
                    <div>
                        <div class="flex justify-between text-slate-600 mb-1">
                            <span>Độ đói</span> <span id="stat-hunger-val">85%</span>
                        </div>
                        <div class="w-full bg-slate-200 h-2.5 rounded-full overflow-hidden">
                            <div id="stat-hunger-bar" class="bg-amber-500 h-full rounded-full transition-all duration-300" style="width: 85%"></div>
                        </div>
                    </div>
                    <div>
                        <div class="flex justify-between text-slate-600 mb-1">
                            <span>Độ khát</span> <span id="stat-thirst-val">85%</span>
                        </div>
                        <div class="w-full bg-slate-200 h-2.5 rounded-full overflow-hidden">
                            <div id="stat-thirst-bar" class="bg-sky-500 h-full rounded-full transition-all duration-300" style="width: 85%"></div>
                        </div>
                    </div>
                    <div>
                        <div class="flex justify-between text-slate-600 mb-1">
                            <span>Hạnh phúc</span> <span id="stat-happy-val">90%</span>
                        </div>
                        <div class="w-full bg-slate-200 h-2.5 rounded-full overflow-hidden">
                            <div id="stat-happy-bar" class="bg-pink-500 h-full rounded-full transition-all duration-300" style="width: 90%"></div>
                        </div>
                    </div>
                </div>
                <div class="mt-3 flex gap-2">
                    <button onclick="feedSelectedPet('food')" class="flex-1 bg-amber-500 hover:bg-amber-600 text-white font-bold py-1.5 rounded-xl text-xs transition shadow">Cho ăn</button>
                    <button onclick="feedSelectedPet('drink')" class="flex-1 bg-sky-500 hover:bg-sky-600 text-white font-bold py-1.5 rounded-xl text-xs transition shadow">Cho uống</button>
                </div>
            </div>

            <div class="bg-white/85 backdrop-blur-md px-4 py-2 rounded-2xl shadow-lg border border-white/55 text-emerald-800 text-xs font-bold hidden sm:block">
                💡 Click vào thú cưng để vuốt ve má hồng kawaii!
            </div>
        </div>
    </div>

    <!-- SHOP MODAL -->
    <div id="shop-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm p-4 hidden">
        <div class="bg-white rounded-3xl max-w-xl w-full p-6 shadow-2xl border-4 border-emerald-400 relative flex flex-col max-h-[85vh]">
            <div class="flex justify-between items-center pb-3 border-b border-slate-100">
                <div class="flex items-center gap-2">
                    <i id="shop-modal-icon" class="fa-solid fa-store text-emerald-600 text-xl"></i>
                    <h2 id="shop-modal-title" class="text-xl font-extrabold text-emerald-700">Cửa hàng</h2>
                </div>
                <button onclick="closeShopModal()" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-600 font-bold transition">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <div class="flex gap-2 my-4 border-b border-slate-100 pb-2 overflow-x-auto">
                <button onclick="switchShopTab('food')" id="tab-food" class="px-4 py-2 rounded-xl font-bold text-xs transition bg-emerald-500 text-white shadow">Thức ăn & Đồ uống</button>
                <button onclick="switchShopTab('animals')" id="tab-animals" class="px-4 py-2 rounded-xl font-bold text-xs transition bg-slate-100 text-slate-600 hover:bg-slate-200">16 Loài Thú Cưng</button>
                <button onclick="switchShopTab('decor')" id="tab-decor" class="px-4 py-2 rounded-xl font-bold text-xs transition bg-slate-100 text-slate-600 hover:bg-slate-200">Trang trí</button>
            </div>

            <div id="shop-content-area" class="flex-1 overflow-y-auto pr-1 space-y-3"></div>
        </div>
    </div>

    <!-- QUEST MODAL -->
    <div id="quest-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm p-4 hidden">
        <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl border-4 border-amber-400 relative flex flex-col max-h-[85vh]">
            <div class="flex justify-between items-center pb-3 border-b border-slate-100">
                <div class="flex items-center gap-2">
                    <i class="fa-solid fa-scroll text-amber-500 text-xl"></i>
                    <h2 class="text-xl font-extrabold text-amber-700">Nhiệm Vụ Trang Trại</h2>
                </div>
                <button onclick="closeQuestModal()" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-600 font-bold transition">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>
            <p class="text-xs text-slate-500 my-2">Hoàn thành các nhiệm vụ hàng ngày để nhận xu vàng!</p>
            <div id="quest-content-area" class="flex-1 overflow-y-auto pr-1 space-y-3 my-2"></div>
        </div>
    </div>

    <!-- Three.js Canvas Container -->
    <div id="canvas-container" class="absolute inset-0 w-full h-full -z-10"></div>

    <!-- SCRIPT LOGIC -->
    <script>
        // --- WEB AUDIO API SOUND SYSTEM ---
        let audioCtx = null;
        let isAudioEnabled = true;

        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
        }

        function toggleAudioSystem() {
            initAudio();
            isAudioEnabled = !isAudioEnabled;
            const icon = document.getElementById('audio-icon');
            const text = document.getElementById('audio-text');
            if (isAudioEnabled) {
                icon.className = 'fa-solid fa-volume-high text-emerald-600 text-sm';
                text.textContent = 'Âm thanh: Bật';
                playChime(523.25, 0.1);
            } else {
                icon.className = 'fa-solid fa-volume-xmark text-slate-400 text-sm';
                text.textContent = 'Âm thanh: Tắt';
            }
        }

        function playTone(freq, type, duration, gainVal = 0.1) {
            if (!isAudioEnabled || !audioCtx) return;
            try {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(gainVal, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            } catch (e) { console.error(e); }
        }

        function playChime(freq = 600, duration = 0.2) {
            playTone(freq, 'sine', duration, 0.15);
        }

        function playCoinSound() {
            if (!isAudioEnabled || !audioCtx) return;
            playTone(987.77, 'sine', 0.1, 0.1);
            setTimeout(() => playTone(1318.51, 'sine', 0.2, 0.15), 80);
        }

        function playEatSound() {
            if (!isAudioEnabled || !audioCtx) return;
            playTone(250, 'triangle', 0.08, 0.2);
            setTimeout(() => playTone(300, 'triangle', 0.08, 0.2), 90);
        }

        function playPetSound() {
            if (!isAudioEnabled || !audioCtx) return;
            playTone(440, 'sine', 0.15, 0.1);
            setTimeout(() => playTone(554.37, 'sine', 0.2, 0.12), 100);
        }

        let bgmInterval = null;
        const melodyNotes = [261.63, 329.63, 392.00, 523.25, 392.00, 329.63];
        let noteIndex = 0;
        function startBackgroundMusic() {
            if (bgmInterval) clearInterval(bgmInterval);
            bgmInterval = setInterval(() => {
                if (!isAudioEnabled || !audioCtx || gameStarted === false) return;
                playTone(melodyNotes[noteIndex], 'sine', 0.6, 0.03);
                noteIndex = (noteIndex + 1) % melodyNotes.length;
            }, 1200);
        }

        // --- GAME STATE & ECONOMY ---
        let gameStarted = false;
        let coins = 250;
        let isNight = false;
        let animals = [];
        let decors = [];
        let poops = [];
        let selectedPet = null;
        let currentShopTab = 'food';

        let quests = [
            { id: 'pet_3', title: 'Vuốt ve thú cưng', desc: 'Tương tác vuốt ve thú cưng 3 lần', target: 3, progress: 0, reward: 40, completed: false },
            { id: 'clean_2', title: 'Dọn dẹp chuồng trại', desc: 'Dọn 2 đống phân trong nông trại', target: 2, progress: 0, reward: 35, completed: false },
            { id: 'feed_2', title: 'Cho thú ăn uống', desc: 'Cho thú cưng ăn hoặc uống nước 2 lần', target: 2, progress: 0, reward: 45, completed: false },
            { id: 'buy_decor', title: 'Trang trí nông trại', desc: 'Mua 1 vật phẩm trang trí bất kỳ', target: 1, progress: 0, reward: 60, completed: false }
        ];

        let inventory = {
            grass: 5,
            apple: 4,
            milk: 3,
            corn: 4,
            water: 5
        };

        const catalog = {
            food: [
                { id: 'grass', name: 'Cỏ tươi xanh', icon: 'fa-seedling', price: 10, desc: 'Thức ăn khoái khẩu cho cừu, dê, bò', qtyKey: 'grass' },
                { id: 'apple', name: 'Táo mọng nước', icon: 'fa-apple-whole', price: 15, desc: 'Giúp thú cưng tăng hạnh phúc & no bụng', qtyKey: 'apple' },
                { id: 'milk', name: 'Bình sữa tươi', icon: 'fa-bottle-droplet', price: 20, desc: 'Thức uống bổ dưỡng cho mọi loài', qtyKey: 'milk' },
                { id: 'corn', name: 'Hạt ngô vàng', icon: 'fa-wheat-awn', price: 12, desc: 'Món ngon tuyệt vời cho gà, vịt, khỉ', qtyKey: 'corn' },
                { id: 'water', name: 'Nước suối mát', icon: 'fa-droplet', price: 8, desc: 'Giải khát tức thì cho thú cưng', qtyKey: 'water' },
            ],
            animals: [
                { id: 'cat', name: 'Bé Mèo Chibi', icon: 'fa-cat', price: 55, desc: 'Tam thể siêu cute với đôi tai dựng' },
                { id: 'monkey', name: 'Bé Khỉ Tinh Nghịch', icon: 'fa-face-grin-tongue', price: 65, desc: 'Đuôi cong đáng yêu, má lúm' },
                { id: 'hamster', name: 'Bé Hamster Tròn', icon: 'fa-paw', price: 45, desc: 'Má phúng phính, nhỏ nhắn xinh xắn' },
                { id: 'chick', name: 'Bé Gà Con Vàng', icon: 'fa-feather', price: 40, desc: 'Quả cầu lông vàng óng' },
                { id: 'bunny', name: 'Bé Thỏ Trắng', icon: 'fa-rabbit', price: 60, desc: 'Tai dài ôm cà rốt cực kute' },
                { id: 'redpanda', name: 'Bé Gấu Trúc Đỏ', icon: 'fa-shield-cat', price: 75, desc: 'Khăn choàng đỏ, lông cam ấm áp' },
                { id: 'duck', name: 'Bé Vịt Con', icon: 'fa-kiwi-bird', price: 50, desc: 'Mỏ cam xinh xắn, lạch bạch' },
                { id: 'penguin', name: 'Bé Chim Cánh Cụt', icon: 'fa-crow', price: 70, desc: 'Quàng khăn đỏ ấm áp, bụng tròn' },
                { id: 'crocodile', name: 'Bé Cá Sấu Xanh', icon: 'fa-dragon', price: 80, desc: 'Màu xanh lá hiền lành ngốc nghếch' },
                { id: 'shiba', name: 'Bé Chó Shiba', icon: 'fa-dog', price: 70, desc: 'Lông vàng óng, mặt cười híp mắt' },
                { id: 'sheep', name: 'Bé Cừu Bồng Bềnh', icon: 'fa-cloud', price: 60, desc: 'Bộ lông xù tròn xoe như cục bông' },
                { id: 'tiger', name: 'Bé Hổ Con', icon: 'fa-cat', price: 85, desc: 'Vằn hổ tinh nghịch, ôm đùi gà' },
                { id: 'husky', name: 'Bé Chó Husky', icon: 'fa-dog', price: 75, desc: 'Lông xám ngầu nhưng cực cute' },
                { id: 'elephant', name: 'Bé Voi Xanh', icon: 'fa-hippo', price: 90, desc: 'Tai to vẫy vẫy, vòi cuốn ngộ nghĩnh' },
                { id: 'pig', name: 'Bé Heo Hồng Mập', icon: 'fa-piggy-bank', price: 65, desc: 'Mũi ủn ỉn, thân hình bầu bĩnh' },
                { id: 'cow', name: 'Bé Bò Sữa', icon: 'fa-cow', price: 80, desc: 'Đốm đen trắng mượt mà thân thiện' }
            ],
            decor: [
                { id: 'fence', name: 'Hàng rào gỗ xinh', icon: 'fa-border-all', price: 25, type: 'fence', desc: 'Trang trí ranh giới trang trại' },
                { id: 'windmill', name: 'Cối xay gió cổ tích', icon: 'fa-fan', price: 130, type: 'windmill', desc: 'Cánh quạt quay êm dịu, sống động' },
                { id: 'tree', name: 'Cây táo ngọt ngào', icon: 'fa-tree', price: 50, type: 'tree', desc: 'Tạo bóng mát và cảnh quan xanh tươi' },
                { id: 'barn', name: 'Chuồng gỗ ấm cúng', icon: 'fa-house', price: 160, type: 'barn', desc: 'Ngôi nhà nhỏ xinh cho thú cưng' }
            ]
        };

        // --- THREE.JS 3D SCENE SETUP ---
        let scene, camera, renderer, clock;
        let ground, sunLight, ambientLight;
        let raycaster, mouse;

        function init3D() {
            const container = document.getElementById('canvas-container');
            
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0xbae6fd);
            scene.fog = new THREE.FogExp2(0xbae6fd, 0.012);

            camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 18, 26);
            camera.lookAt(0, 0, 0);

            renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.shadowMap.enabled = true;
            renderer.shadowMap.type = THREE.PCFSoftShadowMap;
            container.appendChild(renderer.domElement);

            clock = new THREE.Clock();
            raycaster = new THREE.Raycaster();
            mouse = new THREE.Vector2();

            ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
            scene.add(ambientLight);

            sunLight = new THREE.DirectionalLight(0xfffbeb, 1.2);
            sunLight.position.set(25, 35, 20);
            sunLight.castShadow = true;
            sunLight.shadow.mapSize.width = 2048;
            sunLight.shadow.mapSize.height = 2048;
            sunLight.shadow.camera.near = 0.5;
            sunLight.shadow.camera.far = 100;
            const d = 30;
            sunLight.shadow.camera.left = -d;
            sunLight.shadow.camera.right = d;
            sunLight.shadow.camera.top = d;
            sunLight.shadow.camera.bottom = -d;
            scene.add(sunLight);

            const groundGeo = new THREE.PlaneGeometry(80, 80, 32, 32);
            const groundMat = new THREE.MeshStandardMaterial({ 
                color: 0x4ade80, 
                roughness: 0.85,
                metalness: 0.05
            });
            ground = new THREE.Mesh(groundGeo, groundMat);
            ground.rotation.x = -Math.PI / 2;
            ground.receiveShadow = true;
            scene.add(ground);

            createFarmEnvironment();

            window.addEventListener('resize', onWindowResize);
            window.addEventListener('pointerdown', onPointerDown);

            spawnInitialEntities();
            animate3D();
        }

        function createFarmEnvironment() {
            const pathGeo = new THREE.CircleGeometry(14, 32);
            const pathMat = new THREE.MeshStandardMaterial({ color: 0xd4a373, roughness: 0.9 });
            const path = new THREE.Mesh(pathGeo, pathMat);
            path.rotation.x = -Math.PI / 2;
            path.position.y = 0.02;
            path.receiveShadow = true;
            scene.add(path);

            for (let i = -22; i <= 22; i += 5.5) {
                createFencePiece(i, -22, 0);
                createFencePiece(i, 22, 0);
                createFencePiece(-22, i, Math.PI / 2);
                createFencePiece(22, i, Math.PI / 2);
            }

            spawnDecorItem('windmill', 11, -11);
            spawnDecorItem('barn', -11, -11);
            spawnDecorItem('tree', -13, 9);
        }

        function createFencePiece(x, z, rotation) {
            const group = new THREE.Group();
            const postMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b, roughness: 0.8 });
            const postGeo = new THREE.BoxGeometry(0.35, 1.3, 0.35);
            
            const p1 = new THREE.Mesh(postGeo, postMat);
            p1.position.set(-2.2, 0.65, 0);
            p1.castShadow = true;
            group.add(p1);

            const railMat = new THREE.MeshStandardMaterial({ color: 0xa0522d, roughness: 0.7 });
            const railGeo = new THREE.BoxGeometry(4.4, 0.22, 0.16);
            
            const r1 = new THREE.Mesh(railGeo, railMat);
            r1.position.set(0, 0.9, 0);
            r1.castShadow = true;
            group.add(r1);

            const r2 = new THREE.Mesh(railGeo, railMat);
            r2.position.set(0, 0.45, 0);
            r2.castShadow = true;
            group.add(r2);

            group.position.set(x, 0, z);
            group.rotation.y = rotation;
            scene.add(group);
        }

        function spawnInitialEntities() {
            addAnimalToScene('sheep', 2, 2);
            addAnimalToScene('cat', -4, 3);
            addAnimalToScene('bunny', 4, -3);
            addAnimalToScene('shiba', -3, -4);
        }

        // --- ULTRA-CUTE CHIBI ROUND 3D ANIMALS (MATCHING REFERENCE IMAGE) ---
        class CuteAnimal {
            constructor(type, x, z) {
                this.type = type;
                this.x = x;
                this.z = z;
                this.hunger = 85;
                this.thirst = 85;
                this.happiness = 90;
                this.mesh = this.createChibiAnimalMesh(type);
                this.mesh.position.set(x, 0, z);
                scene.add(this.mesh);

                this.targetX = x;
                this.targetZ = z;
                this.moveTimer = Math.random() * 3;
                this.walkCycle = Math.random() * 10;
                this.breathCycle = Math.random() * 5;
            }

            createChibiAnimalMesh(type) {
                const group = new THREE.Group();
                let bodyColor = 0xffffff;
                let scale = 1.0;

                // Color mapping matching reference image chibi palette
                switch (type) {
                    case 'cat': bodyColor = 0xfef08a; break; // Calico/Yellow
                    case 'monkey': bodyColor = 0xf59e0b; break; // Orange-brown
                    case 'hamster': bodyColor = 0xe2e8f0; break; // Light grey/purple
                    case 'chick': bodyColor = 0xfde047; scale = 0.8; break;
                    case 'bunny': bodyColor = 0xffffff; break; // White rabbit
                    case 'redpanda': bodyColor = 0xea580c; break; // Red panda orange
                    case 'duck': bodyColor = 0xffffff; scale = 0.85; break;
                    case 'penguin': bodyColor = 0x334155; break; // Dark grey/black penguin
                    case 'crocodile': bodyColor = 0x84cc16; break; // Green croc
                    case 'shiba': bodyColor = 0xf97316; break; // Shiba orange
                    case 'sheep': bodyColor = 0xffffff; break; // Fluffy sheep
                    case 'tiger': bodyColor = 0xfb923c; break; // Tiger orange
                    case 'husky': bodyColor = 0x64748b; break; // Husky dark grey
                    case 'elephant': bodyColor = 0x93c5fd; break; // Cute blue elephant
                    case 'pig': bodyColor = 0xfbcfe8; break; // Pastel pink pig
                    case 'cow': bodyColor = 0xffffff; break; // Cow white
                }

                // Chibi Round Squishy Body (Sphere/Ellipsoid)
                const bodyGeo = new THREE.SphereGeometry(1.0 * scale, 24, 24);
                bodyGeo.scale(1, 0.9, 0.9);
                const bodyMat = new THREE.MeshStandardMaterial({ color: bodyColor, roughness: 0.6, metalness: 0.05 });
                const body = new THREE.Mesh(bodyGeo, bodyMat);
                body.position.y = 1.0 * scale;
                body.castShadow = true;
                body.receiveShadow = true;
                group.add(body);

                // Specific chibi details for each animal
                if (type === 'cow') {
                    const spotMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.7 });
                    const spot = new THREE.Mesh(new THREE.SphereGeometry(0.35, 12, 12), spotMat);
                    spot.position.set(0.4, 0.3, 0.6);
                    body.add(spot);
                } else if (type === 'tiger') {
                    const stripeMat = new THREE.MeshStandardMaterial({ color: 0x1c1917, roughness: 0.8 });
                    const stripe = new THREE.Mesh(new THREE.BoxGeometry(1.1, 0.15, 0.15), stripeMat);
                    stripe.position.set(0, 0.4, 0.75);
                    body.add(stripe);
                } else if (type === 'penguin') {
                    const bellyMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.5 });
                    const belly = new THREE.Mesh(new THREE.SphereGeometry(0.65, 16, 16), bellyMat);
                    belly.position.set(0, -0.1, 0.5);
                    body.add(belly);
                }

                // Chibi Head & Face Group
                const headGroup = new THREE.Group();
                headGroup.position.set(0, 1.85 * scale, 0.3 * scale);

                const headGeo = new THREE.SphereGeometry(0.85 * scale, 24, 24);
                const head = new THREE.Mesh(headGeo, bodyMat);
                head.castShadow = true;
                headGroup.add(head);

                // ULTRA CUTE BLUSHING CHEEKS (Kawaii Pink Blush)
                const blushMat = new THREE.MeshBasicMaterial({ color: 0xff3366, transparent: true, opacity: 0.9 });
                const leftBlush = new THREE.Mesh(new THREE.CircleGeometry(0.22, 16), blushMat);
                leftBlush.position.set(-0.52 * scale, -0.08 * scale, 0.65 * scale);
                leftBlush.rotation.y = -Math.PI / 4;
                headGroup.add(leftBlush);

                const rightBlush = new THREE.Mesh(new THREE.CircleGeometry(0.22, 16), blushMat);
                rightBlush.position.set(0.52 * scale, -0.08 * scale, 0.65 * scale);
                rightBlush.rotation.y = Math.PI / 4;
                headGroup.add(rightBlush);

                // Expressive Sparkle Eyes
                const eyeMat = new THREE.MeshBasicMaterial({ color: 0x0f172a });
                const leftEye = new THREE.Mesh(new THREE.SphereGeometry(0.12 * scale, 12, 12), eyeMat);
                leftEye.position.set(-0.3 * scale, 0.1 * scale, 0.7 * scale);
                headGroup.add(leftEye);

                const rightEye = new THREE.Mesh(new THREE.SphereGeometry(0.12 * scale, 12, 12), eyeMat);
                rightEye.position.set(0.3 * scale, 0.1 * scale, 0.7 * scale);
                headGroup.add(rightEye);

                // Cute Ears / Horns / Features based on type
                if (type === 'bunny' || type === 'sheep') {
                    const earGeo = new THREE.ConeGeometry(0.22 * scale, 0.7 * scale, 8);
                    const lEar = new THREE.Mesh(earGeo, bodyMat);
                    lEar.position.set(-0.45 * scale, 0.85 * scale, 0);
                    lEar.rotation.z = -0.2;
                    headGroup.add(lEar);
                    const rEar = new THREE.Mesh(earGeo, bodyMat);
                    rEar.position.set(0.45 * scale, 0.85 * scale, 0);
                    rEar.rotation.z = 0.2;
                    headGroup.add(rEar);
                } else if (type === 'cat' || type === 'shiba' || type === 'husky' || type === 'redpanda' || type === 'tiger') {
                    const earMat = new THREE.MeshStandardMaterial({ color: bodyColor, roughness: 0.6 });
                    const lEar = new THREE.Mesh(new THREE.ConeGeometry(0.3 * scale, 0.5 * scale, 8), earMat);
                    lEar.position.set(-0.5 * scale, 0.7 * scale, 0.1);
                    headGroup.add(lEar);
                    const rEar = new THREE.Mesh(new THREE.ConeGeometry(0.3 * scale, 0.5 * scale, 8), earMat);
                    rEar.position.set(0.5 * scale, 0.7 * scale, 0.1);
                    headGroup.add(rEar);
                } else if (type === 'elephant') {
                    const trunkMat = new THREE.MeshStandardMaterial({ color: 0x93c5fd, roughness: 0.6 });
                    const trunk = new THREE.Mesh(new THREE.CylinderGeometry(0.15, 0.1, 0.7, 10), trunkMat);
                    trunk.position.set(0, -0.2, 0.8);
                    trunk.rotation.x = Math.PI / 3;
                    headGroup.add(trunk);
                }

                group.add(headGroup);

                // Tiny Chibi Feet
                const footGeo = new THREE.SphereGeometry(0.25 * scale, 12, 12);
                const footMat = new THREE.MeshStandardMaterial({ color: bodyColor, roughness: 0.7 });
                const feet = [];
                [-0.45, 0.45].forEach(fx => {
                    const foot = new THREE.Mesh(footGeo, footMat);
                    foot.position.set(fx * scale, 0.2 * scale, 0.3 * scale);
                    foot.castShadow = true;
                    group.add(foot);
                    feet.push(foot);
                });

                group.userData = { animal: this, feet: feet, head: headGroup };
                return group;
            }

            update(delta) {
                // AI Movement logic
                this.moveTimer -= delta;
                if (this.moveTimer <= 0) {
                    this.moveTimer = 4 + Math.random() * 5;
                    this.targetX = (Math.random() - 0.5) * 32;
                    this.targetZ = (Math.random() - 0.5) * 32;
                }

                const dx = this.targetX - this.mesh.position.x;
                const dz = this.targetZ - this.mesh.position.z;
                const dist = Math.sqrt(dx * dx + dz * dz);

                if (dist > 0.6) {
                    const speed = 2.0 * delta;
                    this.mesh.position.x += (dx / dist) * speed;
                    this.mesh.position.z += (dz / dist) * speed;
                    
                    const targetRotation = Math.atan2(dx, dz);
                    let diff = targetRotation - this.mesh.rotation.y;
                    while (diff < -Math.PI) diff += Math.PI * 2;
                    while (diff > Math.PI) diff -= Math.PI * 2;
                    this.mesh.rotation.y += diff * 5 * delta;

                    // Chibi hopping walk
                    this.walkCycle += delta * 14;
                    this.mesh.position.y = Math.abs(Math.sin(this.walkCycle)) * 0.25;
                } else {
                    this.mesh.position.y = 0;
                }

                // Breathing idle animation
                this.breathCycle += delta * 3;
                const scaleY = 1 + Math.sin(this.breathCycle) * 0.035;
                const scaleXZ = 1 + Math.cos(this.breathCycle) * 0.02;
                this.mesh.scale.set(scaleXZ, scaleY, scaleXZ);
            }

            pet() {
                playPetSound();
                this.happiness = Math.min(100, this.happiness + 15);
                updateQuestProgress('pet_3', 1);
                showFloatingText("❤️ +15 Hạnh phúc!", this.mesh.position);
                
                // Cute Chibi Jump
                let t = 0;
                const jumpInterval = setInterval(() => {
                    t += 0.12;
                    this.mesh.position.y = Math.sin(t * Math.PI) * 1.5;
                    if (t >= 1) {
                        clearInterval(jumpInterval);
                        this.mesh.position.y = 0;
                    }
                }, 30);
            }

            feed(type) {
                playEatSound();
                if (type === 'food') {
                    this.hunger = Math.min(100, this.hunger + 35);
                    showFloatingText("🍏 +35 No bụng!", this.mesh.position);
                } else {
                    this.thirst = Math.min(100, this.thirst + 35);
                    showFloatingText("💧 +35 Giải khát!", this.mesh.position);
                }
                updateQuestProgress('feed_2', 1);

                if (Math.random() > 0.4) {
                    setTimeout(() => spawnPoop(this.mesh.position.x + (Math.random() - 0.5) * 2.5, this.mesh.position.z + (Math.random() - 0.5) * 2.5), 1500);
                }
            }
        }

        // --- DECORATION & POOP SYSTEMS ---
        class DecorItem {
            constructor(type, x, z) {
                this.type = type;
                this.mesh = this.createMesh(type);
                this.mesh.position.set(x, 0, z);
                scene.add(this.mesh);
            }

            createMesh(type) {
                const group = new THREE.Group();
                if (type === 'windmill') {
                    const tower = new THREE.Mesh(
                        new THREE.ConeGeometry(1.6, 4.5, 8),
                        new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.5 })
                    );
                    tower.position.y = 2.25;
                    tower.castShadow = true;
                    group.add(tower);

                    const bladeGroup = new THREE.Group();
                    bladeGroup.position.set(0, 3.8, 1.4);
                    const bladeMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.4 });
                    for (let i = 0; i < 4; i++) {
                        const b = new THREE.Mesh(new THREE.BoxGeometry(0.35, 2.4, 0.1), bladeMat);
                        b.rotation.z = (Math.PI / 2) * i;
                        bladeGroup.add(b);
                    }
                    group.userData = { bladeGroup: bladeGroup };
                    group.add(bladeGroup);
                } else if (type === 'tree') {
                    const trunk = new THREE.Mesh(
                        new THREE.CylinderGeometry(0.45, 0.65, 2.2, 10),
                        new THREE.MeshStandardMaterial({ color: 0x854d0e, roughness: 0.8 })
                    );
                    trunk.position.y = 1.1;
                    group.add(trunk);
                    const leaves = new THREE.Mesh(
                        new THREE.DodecahedronGeometry(2.2, 1),
                        new THREE.MeshStandardMaterial({ color: 0x22c55e, roughness: 0.6 })
                    );
                    leaves.position.y = 3.2;
                    group.add(leaves);
                } else if (type === 'barn') {
                    const barnBox = new THREE.Mesh(
                        new THREE.BoxGeometry(4.2, 3.2, 4.2),
                        new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.7 })
                    );
                    barnBox.position.y = 1.6;
                    group.add(barnBox);

                    const roof = new THREE.Mesh(
                        new THREE.ConeGeometry(3.5, 2.2, 4),
                        new THREE.MeshStandardMaterial({ color: 0xef4444, roughness: 0.5 })
                    );
                    roof.position.y = 4.3;
                    roof.rotation.y = Math.PI / 4;
                    group.add(roof);
                } else {
                    const box = new THREE.Mesh(
                        new THREE.BoxGeometry(1.6, 1.1, 1.6),
                        new THREE.MeshStandardMaterial({ color: 0xa16207, roughness: 0.8 })
                    );
                    box.position.y = 0.55;
                    group.add(box);
                }
                return group;
            }
        }

        function spawnDecorItem(type, x, z) {
            const decor = new DecorItem(type, x, z);
            decors.push(decor);
        }

        function spawnPoop(x, z) {
            const poopGeo = new THREE.SphereGeometry(0.32, 10, 10);
            const poopMat = new THREE.MeshStandardMaterial({ color: 0x78350f, roughness: 0.9 });
            const poop = new THREE.Mesh(poopGeo, poopMat);
            poop.position.set(x, 0.2, z);
            poop.scale.set(1, 0.6, 1);
            poop.castShadow = true;
            scene.add(poop);
            poops.push(poop);
        }

        function addAnimalToScene(type, x, z) {
            const animal = new CuteAnimal(type, x, z);
            animals.push(animal);
            updatePetCount();
        }

        function updatePetCount() {
            document.getElementById('pet-count').textContent = animals.length;
        }

        // --- RAYCASTING & INTERACTIONS ---
        function onPointerDown(event) {
            if (!gameStarted) return;
            if (event.clientX < 0 || event.clientY < 0) return;

            mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

            raycaster.setFromCamera(mouse, camera);

            const animalMeshes = animals.map(a => a.mesh);
            const intersects = raycaster.intersectObjects(animalMeshes, true);

            if (intersects.length > 0) {
                let obj = intersects[0].object;
                while (obj.parent && !obj.userData.animal) {
                    obj = obj.parent;
                }
                if (obj.userData && obj.userData.animal) {
                    const pet = obj.userData.animal;
                    pet.pet();
                    selectPet(pet);
                    return;
                }
            }

            const poopIntersects = raycaster.intersectObjects(poops);
            if (poopIntersects.length > 0) {
                const clickedPoop = poopIntersects[0].object;
                scene.remove(clickedPoop);
                poops = poops.filter(p => p !== clickedPoop);
                coins += 15;
                updateCoins();
                playCoinSound();
                updateQuestProgress('clean_2', 1);
                showFloatingText("🪙 +15 Xu dọn phân!", clickedPoop.position);
                return;
            }
        }

        function selectPet(pet) {
            selectedPet = pet;
            const panel = document.getElementById('selected-pet-panel');
            panel.classList.remove('hidden');
            document.getElementById('panel-pet-name').textContent = getAnimalDisplayName(pet.type);
            updateSelectedPetStats();
        }

        function closePetPanel() {
            selectedPet = null;
            document.getElementById('selected-pet-panel').classList.add('hidden');
        }

        function updateSelectedPetStats() {
            if (!selectedPet) return;
            document.getElementById('stat-hunger-val').textContent = Math.round(selectedPet.hunger) + '%';
            document.getElementById('stat-hunger-bar').style.width = selectedPet.hunger + '%';
            document.getElementById('stat-thirst-val').textContent = Math.round(selectedPet.thirst) + '%';
            document.getElementById('stat-thirst-bar').style.width = selectedPet.thirst + '%';
            document.getElementById('stat-happy-val').textContent = Math.round(selectedPet.happiness) + '%';
            document.getElementById('stat-happy-bar').style.width = selectedPet.happiness + '%';
        }

        function feedSelectedPet(kind) {
            if (!selectedPet) return;
            if (kind === 'food') {
                if (inventory.grass > 0 || inventory.apple > 0 || inventory.corn > 0) {
                    inventory.grass = Math.max(0, inventory.grass - 1);
                    selectedPet.feed('food');
                } else {
                    showNotification("Hết thức ăn rồi! Hãy vào cửa hàng mua thêm.");
                    return;
                }
            } else {
                if (inventory.milk > 0 || inventory.water > 0) {
                    inventory.water = Math.max(0, inventory.water - 1);
                    selectedPet.feed('drink');
                } else {
                    showNotification("Hết nước uống rồi! Hãy vào cửa hàng mua thêm.");
                    return;
                }
            }
            updateSelectedPetStats();
        }

        function showFloatingText(text, pos) {
            const div = document.createElement('div');
            div.className = 'absolute z-40 text-sm font-extrabold text-white bg-emerald-600/90 px-3 py-1 rounded-full shadow-lg float-anim pointer-events-none';
            div.textContent = text;
            
            const vector = pos.clone();
            vector.project(camera);
            const x = (vector.x * 0.5 + 0.5) * window.innerWidth;
            const z = (-(vector.y * 0.5) + 0.5) * window.innerHeight;
            
            div.style.left = x + 'px';
            div.style.top = z + 'px';
            document.body.appendChild(div);
            setTimeout(() => div.remove(), 1500);
        }

        function showNotification(msg) {
            const div = document.createElement('div');
            div.className = 'fixed top-20 left-1/2 -translate-x-1/2 z-50 bg-amber-500 text-white font-bold px-6 py-3 rounded-2xl shadow-xl transition animate-bounce';
            div.textContent = msg;
            document.body.appendChild(div);
            setTimeout(() => div.remove(), 2500);
        }

        // --- ANIMATION LOOP ---
        function animate3D() {
            requestAnimationFrame(animate3D);

            const delta = clock.getDelta();

            animals.forEach(animal => animal.update(delta));

            decors.forEach(d => {
                if (d.mesh.userData && d.mesh.userData.bladeGroup) {
                    d.mesh.userData.bladeGroup.rotation.z += delta * 1.8;
                }
            });

            if (isNight) {
                scene.background.lerp(new THREE.Color(0x0f172a), 0.05);
                scene.fog.color.lerp(new THREE.Color(0x0f172a), 0.05);
                sunLight.intensity = Math.max(0.1, sunLight.intensity - 0.02);
                ambientLight.intensity = Math.max(0.25, ambientLight.intensity - 0.01);
            } else {
                scene.background.lerp(new THREE.Color(0xbae6fd), 0.05);
                scene.fog.color.lerp(new THREE.Color(0xbae6fd), 0.05);
                sunLight.intensity = Math.min(1.2, sunLight.intensity + 0.02);
                ambientLight.intensity = Math.min(0.7, ambientLight.intensity + 0.01);
            }

            renderer.render(scene, camera);
        }

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        // --- UI & SHOP & QUEST MODALS ---
        function startGame() {
            initAudio();
            document.getElementById('title-screen').style.opacity = '0';
            setTimeout(() => {
                document.getElementById('title-screen').classList.add('hidden');
                document.getElementById('game-ui').classList.remove('hidden');
                gameStarted = true;
                startBackgroundMusic();
                confetti({ particleCount: 90, spread: 75, origin: { y: 0.6 } });
            }, 700);
        }

        function openTutorial() { document.getElementById('tutorial-modal').classList.remove('hidden'); }
        function closeTutorial() { document.getElementById('tutorial-modal').classList.add('hidden'); }
        function openCredits() { document.getElementById('credits-modal').classList.remove('hidden'); }
        function closeCredits() { document.getElementById('credits-modal').classList.add('hidden'); }

        function toggleDayNight() {
            isNight = !isNight;
            const btn = document.getElementById('daynight-btn');
            const icon = document.getElementById('daynight-icon');
            const label = document.getElementById('daynight-label');
            if (isNight) {
                btn.className = 'flex items-center gap-1.5 px-3 py-1 rounded-xl bg-indigo-900 text-indigo-200 font-bold text-xs hover:bg-indigo-800 transition';
                icon.className = 'fa-solid fa-moon text-indigo-300';
                label.textContent = 'Ban đêm';
            } else {
                btn.className = 'flex items-center gap-1.5 px-3 py-1 rounded-xl bg-amber-100 text-amber-700 font-bold text-xs hover:bg-amber-200 transition';
                icon.className = 'fa-solid fa-sun text-amber-500';
                label.textContent = 'Ban ngày';
            }
        }

        function openShopModal(tab = 'food') {
            currentShopTab = tab;
            document.getElementById('shop-modal').classList.remove('hidden');
            renderShopTabs();
            renderShopContent();
        }

        function closeShopModal() {
            document.getElementById('shop-modal').classList.add('hidden');
        }

        function switchShopTab(tab) {
            currentShopTab = tab;
            renderShopTabs();
            renderShopContent();
        }

        function renderShopTabs() {
            const tabs = ['food', 'animals', 'decor'];
            const titles = { food: 'Thức ăn & Đồ uống', animals: '16 Loài Thú Cưng Chibi', decor: 'Trang trí nông trại' };
            const icons = { food: 'fa-bowl-food', animals: 'fa-store', decor: 'fa-house-chimney' };

            document.getElementById('shop-modal-title').textContent = titles[currentShopTab];
            document.getElementById('shop-modal-icon').className = `fa-solid ${icons[currentShopTab]} text-emerald-600 text-xl`;

            tabs.forEach(t => {
                const btn = document.getElementById(`tab-${t}`);
                if (t === currentShopTab) {
                    btn.className = 'px-4 py-2 rounded-xl font-bold text-xs transition bg-emerald-500 text-white shadow';
                } else {
                    btn.className = 'px-4 py-2 rounded-xl font-bold text-xs transition bg-slate-100 text-slate-600 hover:bg-slate-200';
                }
            });
        }

        function renderShopContent() {
            const area = document.getElementById('shop-content-area');
            area.innerHTML = '';
            const items = catalog[currentShopTab];

            items.forEach(item => {
                const card = document.createElement('div');
                card.className = 'flex items-center justify-between p-3.5 bg-emerald-50/70 hover:bg-emerald-100/80 rounded-2xl border border-emerald-100 transition';
                
                let qtyBadge = '';
                if (currentShopTab === 'food') {
                    qtyBadge = `<span class="text-xs font-bold text-emerald-700 bg-emerald-200 px-2 py-0.5 rounded-lg ml-2">Đang có: ${inventory[item.id]}</span>`;
                }

                card.innerHTML = `
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-2xl bg-white shadow flex items-center justify-center text-emerald-600 text-xl">
                            <i class="fa-solid ${item.icon}"></i>
                        </div>
                        <div>
                            <div class="flex items-center">
                                <h4 class="font-bold text-slate-800 text-sm">${item.name}</h4>
                                ${qtyBadge}
                            </div>
                            <p class="text-xs text-slate-500">${item.desc}</p>
                        </div>
                    </div>
                    <button onclick="buyShopItem('${item.id}', ${item.price}, '${currentShopTab}')" class="flex items-center gap-1.5 bg-amber-500 hover:bg-amber-600 text-white font-bold px-4 py-2 rounded-xl text-xs transition shadow active:scale-95">
                        <i class="fa-solid fa-coins"></i> ${item.price}
                    </button>
                `;
                area.appendChild(card);
            });
        }

        function buyShopItem(id, price, tab) {
            if (coins < price) {
                playChime(300, 0.3);
                showNotification("Không đủ xu vàng! Hãy hoàn thành nhiệm vụ để nhận thêm xu.");
                return;
            }

            coins -= price;
            updateCoins();
            playChime(750, 0.15);

            if (tab === 'food') {
                inventory[id] = (inventory[id] || 0) + 1;
                showNotification("Đã mua thành công thức ăn!");
                renderShopContent();
            } else if (tab === 'animals') {
                if (animals.length >= 16) {
                    showNotification("Nông trại đã đầy 16 thú cưng rồi!");
                    return;
                }
                const rx = (Math.random() - 0.5) * 18;
                const rz = (Math.random() - 0.5) * 18;
                addAnimalToScene(id, rx, rz);
                showNotification("Đã thêm bé thú cưng chibi mới vào nông trại!");
                closeShopModal();
                confetti({ particleCount: 50, spread: 60 });
            } else if (tab === 'decor') {
                const rx = (Math.random() - 0.5) * 22;
                const rz = (Math.random() - 0.5) * 22;
                spawnDecorItem(id, rx, rz);
                updateQuestProgress('buy_decor', 1);
                showNotification("Đã đặt trang trí mới vào nông trại!");
                closeShopModal();
            }
        }

        function openQuestModal() {
            document.getElementById('quest-modal').classList.remove('hidden');
            renderQuests();
        }

        function closeQuestModal() {
            document.getElementById('quest-modal').classList.add('hidden');
        }

        function updateQuestProgress(questId, amount) {
            const q = quests.find(item => item.id === questId);
            if (q && !q.completed) {
                q.progress = Math.min(q.target, q.progress + amount);
                if (q.progress >= q.target) {
                    showNotification(`🎉 Hoàn thành nhiệm vụ: "${q.title}"! Vào bảng nhiệm vụ nhận thưởng.`);
                }
            }
        }

        function renderQuests() {
            const area = document.getElementById('quest-content-area');
            area.innerHTML = '';

            quests.forEach(q => {
                const card = document.createElement('div');
                card.className = 'flex items-center justify-between p-4 bg-amber-50/70 rounded-2xl border border-amber-200 transition';

                const percent = Math.round((q.progress / q.target) * 100);
                
                let actionBtn = '';
                if (q.completed) {
                    actionBtn = `<span class="bg-emerald-100 text-emerald-700 font-bold px-3 py-1.5 rounded-xl text-xs"><i class="fa-solid fa-check"></i> Đã nhận</span>`;
                } else if (q.progress >= q.target) {
                    actionBtn = `<button onclick="claimQuestReward('${q.id}')" class="bg-emerald-500 hover:bg-emerald-600 text-white font-bold px-4 py-2 rounded-xl text-xs transition shadow animate-pulse">Nhận thưởng</button>`;
                } else {
                    actionBtn = `<span class="bg-amber-100 text-amber-700 font-bold px-3 py-1.5 rounded-xl text-xs">${q.progress}/${q.target}</span>`;
                }

                card.innerHTML = `
                    <div class="flex-1 pr-3">
                        <div class="flex items-center gap-2 mb-1">
                            <h4 class="font-bold text-slate-800 text-sm">${q.title}</h4>
                            <span class="text-xs font-extrabold text-amber-600 bg-amber-200/60 px-2 py-0.5 rounded-md">+${q.reward} 🪙</span>
                        </div>
                        <p class="text-xs text-slate-500 mb-2">${q.desc}</p>
                        <div class="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
                            <div class="bg-amber-500 h-full rounded-full transition-all duration-300" style="width: ${percent}%"></div>
                        </div>
                    </div>
                    <div>
                        ${actionBtn}
                    </div>
                `;
                area.appendChild(card);
            });
        }

        function claimQuestReward(id) {
            const q = quests.find(item => item.id === id);
            if (q && !q.completed && q.progress >= q.target) {
                q.completed = true;
                coins += q.reward;
                updateCoins();
                playCoinSound();
                confetti({ particleCount: 40, spread: 50 });
                showNotification(`Nhận thành công +${q.reward} xu vàng!`);
                renderQuests();
            }
        }

        function updateCoins() {
            document.getElementById('coin-count').textContent = coins;
        }

        function getAnimalDisplayName(type) {
            const names = { 
                cat: 'Bé Mèo Chibi', monkey: 'Bé Khỉ Tinh Nghịch', hamster: 'Bé Hamster Tròn', 
                chick: 'Bé Gà Con', bunny: 'Bé Thỏ Trắng', redpanda: 'Bé Gấu Trúc Đỏ', 
                duck: 'Bé Vịt Con', penguin: 'Bé Chim Cánh Cụt', crocodile: 'Bé Cá Sấu Xanh', 
                shiba: 'Bé Chó Shiba', sheep: 'Bé Cừu Bồng Bềnh', tiger: 'Bé Hổ Con', 
                husky: 'Bé Chó Husky', elephant: 'Bé Voi Xanh', pig: 'Bé Heo Hồng', cow: 'Bé Bò Sữa' 
            };
            return names[type] || 'Thú cưng chibi';
        }

        window.onload = function() {
            init3D();
        };
    </script>
</body>
</html>
```
eof
