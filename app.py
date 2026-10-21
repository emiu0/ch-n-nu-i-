<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang Trại Thú Cưng 3D Kawaii</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
        body { font-family: 'Nunito', sans-serif; user-select: none; }
        .glow-text { text-shadow: 0 0 10px rgba(255,255,255,0.8); }
        .glass-panel { background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); border: 2px solid rgba(255, 255, 255, 0.6); }
    </style>
</head>
<body class="overflow-hidden bg-emerald-900 m-0 p-0">

    <!-- MÀN HÌNH CHÍNH (START SCREEN) -->
    <div id="start-screen" class="absolute inset-0 z-50 flex flex-col items-center justify-center bg-gradient-to-br from-pink-300 via-purple-300 to-emerald-300 transition-opacity duration-700">
        <div class="glass-panel p-10 rounded-3xl shadow-2xl text-center max-w-lg mx-4 transform hover:scale-105 transition duration-300">
            <h1 class="text-5xl font-black text-pink-600 mb-2 glow-text">🐾 Trang Trại Kawaii 🐾</h1>
            <p class="text-gray-700 font-bold mb-6 text-lg">Chăn nuôi, chăm sóc những người bạn nhỏ siêu đáng yêu trong thế giới 3D!</p>
            <div class="flex justify-center gap-4 mb-6">
                <span class="text-4xl animate-bounce">🐱</span>
                <span class="text-4xl animate-bounce" style="animation-delay: 0.1s">🐰</span>
                <span class="text-4xl animate-bounce" style="animation-delay: 0.2s">🐷</span>
                <span class="text-4xl animate-bounce" style="animation-delay: 0.3s">🐥</span>
            </div>
            <button onclick="startGame()" class="w-full py-4 bg-gradient-to-r from-pink-500 to-purple-600 text-white font-black text-2xl rounded-2xl shadow-lg hover:from-pink-600 hover:to-purple-700 transform hover:-translate-y-1 transition active:translate-y-0">
                🚀 BẮT ĐẦU CHƠI
            </button>
        </div>
    </div>

    <!-- KHUNG GAME CHÍNH -->
    <div id="game-container" class="absolute inset-0"></div>

    <!-- GIAO DIỆN HUD TRONG GAME -->
    <div id="ui-layer" class="absolute inset-0 pointer-events-none hidden flex flex-col justify-between p-4">
        
        <!-- Top Bar: Thông tin & Tài nguyên -->
        <div class="flex justify-between items-start">
            <div class="glass-panel px-5 py-3 rounded-2xl shadow-lg pointer-events-auto flex items-center gap-4">
                <div class="text-3xl" id="pet-avatar">🐱</div>
                <div>
                    <h2 id="pet-name-display" class="font-black text-gray-800 text-lg">Mimi (Mèo)</h2>
                    <div class="flex items-center gap-2 mt-1">
                        <span class="text-xs font-bold text-amber-600 bg-amber-100 px-2 py-0.5 rounded-full" id="time-badge">☀️ Ban Ngày</span>
                        <span class="text-xs font-bold text-yellow-600 bg-yellow-100 px-2 py-0.5 rounded-full" id="coin-display">🪙 150 Xu</span>
                    </div>
                </div>
            </div>

            <!-- Các nút hệ thống -->
            <div class="flex gap-2 pointer-events-auto">
                <button onclick="toggleShop()" class="glass-panel px-4 py-3 rounded-2xl font-black text-purple-600 shadow-lg hover:bg-purple-50 transition flex items-center gap-2">
                    🛍️ Cửa Hàng
                </button>
                <button onclick="toggleQuests()" class="glass-panel px-4 py-3 rounded-2xl font-black text-emerald-600 shadow-lg hover:bg-emerald-50 transition flex items-center gap-2">
                    📜 Nhiệm Vụ <span id="quest-dot" class="w-2.5 h-2.5 bg-red-500 rounded-full inline-block"></span>
                </button>
            </div>
        </div>

        <!-- Center Notification -->
        <div id="notification" class="self-center glass-panel px-6 py-2 rounded-full shadow-lg text-gray-800 font-bold text-sm transition-all duration-300 opacity-0 transform -translate-y-4">
            Chào mừng bạn đến với trang trại!
        </div>

        <!-- Bottom Bar: Bảng điều khiển chăm sóc -->
        <div class="glass-panel p-4 rounded-3xl shadow-xl pointer-events-auto max-w-3xl mx-auto w-full flex flex-col gap-3">
            <!-- Thanh chỉ số -->
            <div class="grid grid-cols-3 gap-4">
                <div>
                    <div class="flex justify-between text-xs font-bold text-gray-700 mb-1">
                        <span>🍖 Độ No</span> <span id="hunger-val">80/100</span>
                    </div>
                    <div class="w-full bg-gray-200 h-3 rounded-full overflow-hidden">
                        <div id="hunger-bar" class="bg-amber-500 h-full w-4/5 transition-all duration-300"></div>
                    </div>
                </div>
                <div>
                    <div class="flex justify-between text-xs font-bold text-gray-700 mb-1">
                        <span>⭐ Vui Vẻ</span> <span id="happy-val">80/100</span>
                    </div>
                    <div class="w-full bg-gray-200 h-3 rounded-full overflow-hidden">
                        <div id="happy-bar" class="bg-pink-500 h-full w-4/5 transition-all duration-300"></div>
                    </div>
                </div>
                <div>
                    <div class="flex justify-between text-xs font-bold text-gray-700 mb-1">
                        <span>⚡ Năng Lượng</span> <span id="energy-val">80/100</span>
                    </div>
                    <div class="w-full bg-gray-200 h-3 rounded-full overflow-hidden">
                        <div id="energy-bar" class="bg-cyan-500 h-full w-4/5 transition-all duration-300"></div>
                    </div>
                </div>
            </div>

            <!-- Các nút hành động -->
            <div class="grid grid-cols-4 gap-3">
                <button onclick="feedPet()" class="py-3 bg-amber-400 hover:bg-amber-500 text-white font-black rounded-2xl shadow-md transition transform active:scale-95 flex items-center justify-center gap-2">
                    🍖 Cho Ăn (-10🪙)
                </button>
                <button onclick="playPet()" class="py-3 bg-pink-400 hover:bg-pink-500 text-white font-black rounded-2xl shadow-md transition transform active:scale-95 flex items-center justify-center gap-2">
                    🎾 Chơi Đùa
                </button>
                <button onclick="sleepPet()" class="py-3 bg-indigo-400 hover:bg-indigo-500 text-white font-black rounded-2xl shadow-md transition transform active:scale-95 flex items-center justify-center gap-2">
                    💤 Đi Ngủ
                </button>
                <button onclick="cleanPet()" class="py-3 bg-emerald-400 hover:bg-emerald-500 text-white font-black rounded-2xl shadow-md transition transform active:scale-95 flex items-center justify-center gap-2">
                    ✨ Dọn Vệ Sinh
                </button>
            </div>
        </div>
    </div>

    <!-- CỬA HÀNG MODAL -->
    <div id="shop-modal" class="absolute inset-0 z-40 bg-black/50 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="glass-panel p-6 rounded-3xl max-w-md w-full shadow-2xl relative">
            <button onclick="toggleShop()" class="absolute top-4 right-4 text-gray-500 hover:text-black font-black text-xl">✕</button>
            <h3 class="text-2xl font-black text-purple-700 mb-4">🛍️ Cửa Hàng Động Vật & Vật Phẩm</h3>
            <div class="space-y-3 max-h-96 overflow-y-auto pr-2">
                <div class="flex justify-between items-center p-3 bg-white/60 rounded-2xl">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl">🐰</span>
                        <div><h4 class="font-bold text-gray-800">Thỏ Hồng Kawaii</h4><p class="text-xs text-gray-500">Siêu đáng yêu, nhanh nhẹn</p></div>
                    </div>
                    <button onclick="switchPet('Thỏ', '🐰', 0xffb6c1)" class="px-4 py-2 bg-purple-600 text-white font-bold rounded-xl text-sm hover:bg-purple-700">Chọn (50🪙)</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/60 rounded-2xl">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl">🐷</span>
                        <div><h4 class="font-bold text-gray-800">Heo Sữa Ú nu</h4><p class="text-xs text-gray-500">Mập mạp tròn xoe</p></div>
                    </div>
                    <button onclick="switchPet('Heo', '🐷', 0xffc0cb)" class="px-4 py-2 bg-purple-600 text-white font-bold rounded-xl text-sm hover:bg-purple-700">Chọn (50🪙)</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/60 rounded-2xl">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl">🐥</span>
                        <div><h4 class="font-bold text-gray-800">Gà Vàng Chip</h4><p class="text-xs text-gray-500">Nhỏ nhắn tinh nghịch</p></div>
                    </div>
                    <button onclick="switchPet('Gà', '🐥', 0xffd700)" class="px-4 py-2 bg-purple-600 text-white font-bold rounded-xl text-sm hover:bg-purple-700">Chọn (50🪙)</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/60 rounded-2xl">
                    <div class="flex items-center gap-3">
                        <span class="text-3xl">🐑</span>
                        <div><h4 class="font-bold text-gray-800">Cừu Bông Xù</h4><p class="text-xs text-gray-500">Lông mềm mịn ấm áp</p></div>
                    </div>
                    <button onclick="switchPet('Cừu', '🐑', 0xf0f8ff)" class="px-4 py-2 bg-purple-600 text-white font-bold rounded-xl text-sm hover:bg-purple-700">Chọn (50🪙)</button>
                </div>
            </div>
        </div>
    </div>

    <!-- NHIỆM VỤ MODAL -->
    <div id="quest-modal" class="absolute inset-0 z-40 bg-black/50 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="glass-panel p-6 rounded-3xl max-w-md w-full shadow-2xl relative">
            <button onclick="toggleQuests()" class="absolute top-4 right-4 text-gray-500 hover:text-black font-black text-xl">✕</button>
            <h3 class="text-2xl font-black text-emerald-700 mb-4">📜 Nhiệm Vụ Hàng Ngày</h3>
            <div class="space-y-3">
                <div class="flex justify-between items-center p-3 bg-white/60 rounded-2xl">
                    <div>
                        <h4 class="font-bold text-gray-800">Cho thú cưng ăn 3 lần</h4>
                        <p class="text-xs text-gray-500" id="q1-status">Tiến độ: 0/3</p>
                    </div>
                    <button id="q1-btn" onclick="claimQuest(1, 30)" class="px-4 py-2 bg-gray-300 text-gray-600 font-bold rounded-xl text-sm cursor-not-allowed" disabled>Nhận 30🪙</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/60 rounded-2xl">
                    <div>
                        <h4 class="font-bold text-gray-800">Chơi đùa cùng thú cưng 2 lần</h4>
                        <p class="text-xs text-gray-500" id="q2-status">Tiến độ: 0/2</p>
                    </div>
                    <button id="q2-btn" onclick="claimQuest(2, 40)" class="px-4 py-2 bg-gray-300 text-gray-600 font-bold rounded-xl text-sm cursor-not-allowed" disabled>Nhận 40🪙</button>
                </div>
            </div>
        </div>
    </div>

    <!-- LOGIC JAVASCRIPT & THREE.JS -->
    <script>
        // Game State
        let gameStarted = false;
        let coins = 150;
        let hunger = 80;
        let happy = 80;
        let energy = 80;
        let petName = "Mimi";
        let petType = "Mèo";
        let petColor = 0xffe4e1;
        let isNight = false;

        // Quest Data
        let quests = {
            feedCount: 0,
            playCount: 0,
            q1Claimed: false,
            q2Claimed: false
        };

        // Web Audio API Synthesizer (Không cần tải file ngoài)
        let audioCtx = null;
        function initAudio() {
            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        function playSound(type) {
            if (!audioCtx) return;
            let osc = audioCtx.createOscillator();
            let gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            let now = audioCtx.currentTime;

            if (type === 'click') {
                osc.frequency.setValueAtTime(400, now);
                osc.frequency.exponentialRampToValueAtTime(800, now + 0.1);
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.linearRampToValueAtTime(0.01, now + 0.1);
                osc.start(now); osc.stop(now + 0.1);
            } else if (type === 'eat') {
                osc.frequency.setValueAtTime(300, now);
                osc.frequency.setValueAtTime(500, now + 0.1);
                gain.gain.setValueAtTime(0.15, now);
                gain.gain.linearRampToValueAtTime(0.01, now + 0.2);
                osc.start(now); osc.stop(now + 0.2);
            } else if (type === 'success') {
                osc.frequency.setValueAtTime(523.25, now); // C5
                osc.frequency.setValueAtTime(659.25, now + 0.1); // E5
                osc.frequency.setValueAtTime(783.99, now + 0.2); // G5
                gain.gain.setValueAtTime(0.2, now);
                gain.gain.linearRampToValueAtTime(0.01, now + 0.4);
                osc.start(now); osc.stop(now + 0.4);
            }
        }

        // Three.js Setup
        const container = document.getElementById('game-container');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xa0e0ff);
        scene.fog = new THREE.FogExp2(0xa0e0ff, 0.015);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 6, 12);
        camera.lookAt(0, 1, 0);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        container.appendChild(renderer.domElement);

        // Ánh sáng
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        scene.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0xfffaed, 0.8);
        dirLight.position.set(10, 20, 10);
        dirLight.castShadow = true;
        dirLight.shadow.mapSize.width = 1024;
        dirLight.shadow.mapSize.height = 1024;
        scene.add(dirLight);

        // Sân cỏ trang trại
        const groundGeo = new THREE.CylinderGeometry(10, 10, 0.8, 32);
        const groundMat = new THREE.MeshStandardMaterial({ color: 0x7cfc00, roughness: 0.8 });
        const ground = new THREE.Mesh(groundGeo, groundMat);
        ground.position.y = -0.4;
        ground.receiveShadow = true;
        scene.add(ground);

        // Tạo mô hình thú cưng Chibi Cute (Thân tròn, má hồng, tai)
        let petGroup = new THREE.Group();
        scene.add(petGroup);

        let bodyMesh, leftCheek, rightCheek, leftEar, rightEar;

        function buildPetModel(colorHex) {
            // Xóa thú cưng cũ nếu có
            while(petGroup.children.length > 0){ 
                petGroup.remove(petGroup.children[0]); 
            }

            const material = new THREE.MeshStandardMaterial({ color: colorHex, roughness: 0.4 });
            const blushMat = new THREE.MeshBasicMaterial({ color: 0xff69b4 });
            const eyeMat = new THREE.MeshBasicMaterial({ color: 0x222222 });

            // Thân chính (Tròn trĩnh)
            const bodyGeo = new THREE.SphereGeometry(1.2, 32, 32);
            bodyMesh = new THREE.Mesh(bodyGeo, material);
            bodyMesh.position.y = 1.2;
            bodyMesh.castShadow = true;
            petGroup.add(bodyMesh);

            // Má hồng xinh xắn chuẩn ảnh mẫu
            const cheekGeo = new THREE.CircleGeometry(0.25, 16);
            leftCheek = new THREE.Mesh(cheekGeo, blushMat);
            leftCheek.position.set(-0.6, 1.1, 1.02);
            petGroup.add(leftCheek);

            rightCheek = new THREE.Mesh(cheekGeo, blushMat);
            rightCheek.position.set(0.6, 1.1, 1.02);
            petGroup.add(rightCheek);

            // Mắt to tròn long lanh
            const eyeGeo = new THREE.SphereGeometry(0.15, 16, 16);
            const leftEye = new THREE.Mesh(eyeGeo, eyeMat);
            leftEye.position.set(-0.4, 1.4, 1.05);
            petGroup.add(leftEye);

            const rightEye = new THREE.Mesh(eyeGeo, eyeMat);
            rightEye.position.set(0.4, 1.4, 1.05);
            petGroup.add(rightEye);

            // Tai thú cưng
            const earGeo = new THREE.ConeGeometry(0.35, 0.7, 16);
            leftEar = new THREE.Mesh(earGeo, material);
            leftEar.position.set(-0.7, 2.2, 0);
            leftEar.rotation.z = -0.2;
            petGroup.add(leftEar);

            rightEar = new THREE.Mesh(earGeo, material);
            rightEar.position.set(0.7, 2.2, 0);
            rightEar.rotation.z = 0.2;
            petGroup.add(rightEar);
        }

        buildPetModel(petColor);

        // Vòng lặp animation
        let clock = new THREE.Clock();
        function animate() {
            requestAnimationFrame(animate);
            let elapsedTime = clock.getElapsedTime();

            // Hiệu ứng thở & nhấp nhô nhẹ nhàng siêu cute
            if (bodyMesh) {
                bodyMesh.scale.y = 1 + Math.sin(elapsedTime * 4) * 0.04;
                bodyMesh.scale.x = 1 - Math.sin(elapsedTime * 4) * 0.02;
                petGroup.position.y = Math.sin(elapsedTime * 3) * 0.08;
            }

            renderer.render(scene, camera);
        }
        animate();

        // --- HÀM TƯƠNG TÁC GAME ---
        function startGame() {
            initAudio();
            playSound('success');
            gameStarted = true;
            document.getElementById('start-screen').classList.add('opacity-0', 'pointer-events-none');
            setTimeout(() => document.getElementById('start-screen').style.display = 'none', 700);
            document.getElementById('ui-layer').classList.remove('hidden');
            showNotification("Chào mừng bạn trở lại trang trại nông trại 3D!");
        }

        function showNotification(text) {
            const notif = document.getElementById('notification');
            notif.innerText = text;
            notif.classList.remove('opacity-0', '-translate-y-4');
            setTimeout(() => {
                notif.classList.add('opacity-0', '-translate-y-4');
            }, 3000);
        }

        function updateUI() {
            document.getElementById('coin-display').innerText = `🪙 ${coins} Xu`;
            document.getElementById('hunger-val').innerText = `${hunger}/100`;
            document.getElementById('hunger-bar.style.width') = `${hunger}%`;
            document.getElementById('hunger-bar').style.width = `${hunger}%`;
            
            document.getElementById('happy-val').innerText = `${happy}/100`;
            document.getElementById('happy-bar').style.width = `${happy}%`;
            
            document.getElementById('energy-val').innerText = `${energy}/100`;
            document.getElementById('energy-bar').style.width = `${energy}%`;

            // Kiểm tra nhiệm vụ 1
            if (quests.feedCount >= 3 && !quests.q1Claimed) {
                document.getElementById('q1-btn').classList.remove('bg-gray-300', 'text-gray-600', 'cursor-not-allowed');
                document.getElementById('q1-btn').classList.add('bg-emerald-600', 'text-white', 'hover:bg-emerald-700');
                document.getElementById('q1-btn').removeAttribute('disabled');
            }
            document.getElementById('q1-status').innerText = `Tiến độ: ${quests.feedCount}/3`;

            // Kiểm tra nhiệm vụ 2
            if (quests.playCount >= 2 && !quests.q2Claimed) {
                document.getElementById('q2-btn').classList.remove('bg-gray-300', 'text-gray-600', 'cursor-not-allowed');
                document.getElementById('q2-btn').classList.add('bg-emerald-600', 'text-white', 'hover:bg-emerald-700');
                document.getElementById('q2-btn').removeAttribute('disabled');
            }
            document.getElementById('q2-status').innerText = `Tiến độ: ${quests.playCount}/2`;
        }

        function feedPet() {
            if (coins < 10) {
                showNotification("Bạn không đủ xu để mua thức ăn!");
                return;
            }
            coins -= 10;
            hunger = Math.min(100, hunger + 25);
            quests.feedCount++;
            playSound('eat');
            showNotification(`Yummy! ${petName} ăn rất ngon miệng.`);
            updateUI();
        }

        function playPet() {
            happy = Math.min(100, happy + 20);
            energy = Math.max(0, energy - 10);
            quests.playCount++;
            coins += 15;
            playSound('success');
            showNotification(`Tuyệt vời! ${petName} chơi đùa vui vẻ và thưởng 15🪙.`);
            updateUI();
        }

        function sleepPet() {
            energy = 100;
            hunger = Math.max(0, hunger - 15);
            isNight = !isNight;
            if (isNight) {
                scene.background.setHex(0x1a1a3a);
                scene.fog.color.setHex(0x1a1a3a);
                ambientLight.color.setHex(0x6688cc);
                document.getElementById('time-badge').innerText = "🌙 Ban Đêm";
                showNotification(`Khò khò... ${petName} đã đi ngủ và hồi phục năng lượng.`);
            } else {
                scene.background.setHex(0xa0e0ff);
                scene.fog.color.setHex(0xa0e0ff);
                ambientLight.color.setHex(0xffffff);
                document.getElementById('time-badge').innerText = "☀️ Ban Ngày";
                showNotification(`Chào buổi sáng! ${petName} thức dậy tràn đầy năng lượng.`);
            }
            updateUI();
        }

        function cleanPet() {
            happy = Math.min(100, happy + 10);
            coins += 5;
            playSound('success');
            showNotification(`Sạch sẽ thơm tho! ${petName} rất thích.`);
            updateUI();
        }

        function toggleShop() {
            const modal = document.getElementById('shop-modal');
            modal.classList.toggle('hidden');
        }

        function toggleQuests() {
            const modal = document.getElementById('quest-modal');
            modal.classList.toggle('hidden');
        }

        function switchPet(name, emoji, color) {
            if (coins < 50) {
                showNotification("Bạn cần 50 xu để nhận nuôi thú cưng mới!");
                return;
            }
            coins -= 50;
            petName = name;
            petType = name;
            document.getElementById('pet-avatar').innerText = emoji;
            document.getElementById('pet-name-display').innerText = `${petName} (${petType})`;
            buildPetModel(color);
            playSound('success');
            showNotification(`Đã đón thành công bé ${petName} về trang trại!`);
            toggleShop();
            updateUI();
        }

        function claimQuest(id, reward) {
            coins += reward;
            if (id === 1) {
                quests.q1Claimed = true;
                document.getElementById('q1-btn').innerText = "Đã nhận";
                document.getElementById('q1-btn').className = "px-4 py-2 bg-gray-300 text-gray-500 font-bold rounded-xl text-sm cursor-not-allowed";
                document.getElementById('q1-btn').setAttribute('disabled', 'true');
            } else if (id === 2) {
                quests.q2Claimed = true;
                document.getElementById('q2-btn').innerText = "Đã nhận";
                document.getElementById('q2-btn').className = "px-4 py-2 bg-gray-300 text-gray-500 font-bold rounded-xl text-sm cursor-not-allowed";
                document.getElementById('q2-btn').setAttribute('disabled', 'true');
            }
            document.getElementById('quest-dot').style.display = 'none';
            playSound('success');
            showNotification(`Nhận thành công ${reward} xu thưởng nhiệm vụ!`);
            updateUI();
        }

        // Xử lý resize màn hình
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
</body>
</html>
