<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang Trại Thú Cưng 3D Kawaii</title>
    <!-- Tailwind CSS cho giao diện HUD -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Three.js cho đồ họa 3D -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
        body { font-family: 'Nunito', sans-serif; user-select: none; margin: 0; overflow: hidden; }
        .glass { background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); border: 2px solid rgba(255, 255, 255, 0.6); }
    </style>
</head>
<body class="bg-emerald-900">

    <!-- MÀN HÌNH CHÍNH (START SCREEN) -->
    <div id="start-screen" class="absolute inset-0 z-50 flex flex-col items-center justify-center bg-gradient-to-br from-pink-300 via-purple-300 to-emerald-300 transition-opacity duration-700">
        <div class="glass p-10 rounded-3xl shadow-2xl text-center max-w-lg mx-4">
            <h1 class="text-4xl font-black text-pink-600 mb-2">🐾 Trang Trại 3D Kawaii 🐾</h1>
            <p class="text-gray-700 font-bold mb-6 text-sm">Chăm sóc các bé thú cưng chibi má hồng siêu cấp đáng yêu!</p>
            <div class="flex justify-center gap-3 mb-6 text-3xl">
                <span class="animate-bounce">🐱</span>
                <span class="animate-bounce" style="animation-delay: 0.1s">🐰</span>
                <span class="animate-bounce" style="animation-delay: 0.2s">🐷</span>
                <span class="animate-bounce" style="animation-delay: 0.3s">🐥</span>
            </div>
            <button onclick="startGame()" class="w-full py-4 bg-gradient-to-r from-pink-500 to-purple-600 text-white font-black text-xl rounded-2xl shadow-lg hover:opacity-95 transform active:scale-95 transition">
                🚀 BẮT ĐẦU CHƠI NGAY
            </button>
        </div>
    </div>

    <!-- KHUNG HIỂN THỊ 3D (THREE.JS CONTAINER) -->
    <div id="webgl-container" class="absolute inset-0"></div>

    <!-- GIAO DIỆN ĐIỀU KHIỂN (HUD) TRONG GAME -->
    <div id="ui-layer" class="absolute inset-0 pointer-events-none hidden flex flex-col justify-between p-4">
        
        <!-- Top Bar: Thông tin & Trạng thái -->
        <div class="flex justify-between items-start">
            <div class="glass px-5 py-3 rounded-2xl shadow-lg pointer-events-auto flex items-center gap-4">
                <div class="text-3xl" id="pet-avatar-icon">🐱</div>
                <div>
                    <h2 id="pet-name-title" class="font-black text-gray-800 text-base">Mimi (Mèo Chibi)</h2>
                    <div class="flex items-center gap-2 mt-1">
                        <span id="time-badge" class="text-xs font-bold text-amber-700 bg-amber-100 px-2 py-0.5 rounded-full">☀️ Ban Ngày</span>
                        <span id="coin-badge" class="text-xs font-bold text-yellow-700 bg-yellow-100 px-2 py-0.5 rounded-full">🪙 150 Xu</span>
                    </div>
                </div>
            </div>

            <div class="flex gap-2 pointer-events-auto">
                <button onclick="toggleShop()" class="glass px-4 py-3 rounded-2xl font-black text-purple-600 shadow-lg hover:bg-purple-50 transition">🛍️ Cửa Hàng</button>
                <button onclick="toggleQuests()" class="glass px-4 py-3 rounded-2xl font-black text-emerald-600 shadow-lg hover:bg-emerald-50 transition">📜 Nhiệm Vụ</button>
            </div>
        </div>

        <!-- Thông báo nhanh giữa màn hình -->
        <div id="toast" class="self-center glass px-6 py-2 rounded-full shadow-lg text-gray-800 font-bold text-sm transition-all duration-300 opacity-0 transform -translate-y-4">
            Chào mừng bạn đến với nông trại!
        </div>

        <!-- Bottom Dashboard: Thanh chỉ số & Nút chăm sóc -->
        <div class="glass p-4 rounded-3xl shadow-xl pointer-events-auto max-w-3xl mx-auto w-full flex flex-col gap-3">
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

            <div class="grid grid-cols-4 gap-3">
                <button onclick="feedPet()" class="py-3 bg-amber-400 hover:bg-amber-500 text-white font-black rounded-2xl shadow transition active:scale-95 text-sm">🍖 Cho Ăn (-10🪙)</button>
                <button onclick="playPet()" class="py-3 bg-pink-400 hover:bg-pink-500 text-white font-black rounded-2xl shadow transition active:scale-95 text-sm">🎾 Chơi Đùa</button>
                <button onclick="sleepPet()" class="py-3 bg-indigo-400 hover:bg-indigo-500 text-white font-black rounded-2xl shadow transition active:scale-95 text-sm">💤 Đi Ngủ</button>
                <button onclick="cleanPet()" class="py-3 bg-emerald-400 hover:bg-emerald-500 text-white font-black rounded-2xl shadow transition active:scale-95 text-sm">✨ Vệ Sinh</button>
            </div>
        </div>
    </div>

    <!-- CỬA HÀNG MODAL -->
    <div id="shop-modal" class="absolute inset-0 z-40 bg-black/50 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="glass p-6 rounded-3xl max-w-md w-full shadow-2xl relative">
            <button onclick="toggleShop()" class="absolute top-4 right-4 text-gray-500 hover:text-black font-black text-xl">✕</button>
            <h3 class="text-2xl font-black text-purple-700 mb-4">🛍️ Cửa Hàng Thú Cưng 3D</h3>
            <div class="space-y-3 max-h-80 overflow-y-auto pr-1">
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div class="flex items-center gap-3"><span class="text-3xl">🐱</span><div><h4 class="font-bold text-gray-800">Mèo Chibi</h4><p class="text-xs text-gray-500">Ngọt ngào, đáng yêu</p></div></div>
                    <button onclick="switchPet('Mèo Chibi', '🐱', 0xffe4e1, 'cat')" class="px-3 py-1.5 bg-purple-600 text-white font-bold rounded-xl text-sm">Chọn</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div class="flex items-center gap-3"><span class="text-3xl">🐰</span><div><h4 class="font-bold text-gray-800">Thỏ Hồng</h4><p class="text-xs text-gray-500">Năng động, tai dài</p></div></div>
                    <button onclick="switchPet('Thỏ Hồng', '🐰', 0xffb6c1, 'rabbit')" class="px-3 py-1.5 bg-purple-600 text-white font-bold rounded-xl text-sm">Nhận (50🪙)</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div class="flex items-center gap-3"><span class="text-3xl">🐷</span><div><h4 class="font-bold text-gray-800">Heo Sữa</h4><p class="text-xs text-gray-500">Ú nu, tròn trịa</p></div></div>
                    <button onclick="switchPet('Heo Sữa', '🐷', 0xffc0cb, 'pig')" class="px-3 py-1.5 bg-purple-600 text-white font-bold rounded-xl text-sm">Nhận (50🪙)</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div class="flex items-center gap-3"><span class="text-3xl">🐥</span><div><h4 class="font-bold text-gray-800">Gà Vàng</h4><p class="text-xs text-gray-500">Nhỏ nhắn tinh nghịch</p></div></div>
                    <button onclick="switchPet('Gà Vàng', '🐥', 0xffd700, 'chick')" class="px-3 py-1.5 bg-purple-600 text-white font-bold rounded-xl text-sm">Nhận (50🪙)</button>
                </div>
            </div>
        </div>
    </div>

    <!-- NHIỆM VỤ MODAL -->
    <div id="quest-modal" class="absolute inset-0 z-40 bg-black/50 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="glass p-6 rounded-3xl max-w-md w-full shadow-2xl relative">
            <button onclick="toggleQuests()" class="absolute top-4 right-4 text-gray-500 hover:text-black font-black text-xl">✕</button>
            <h3 class="text-2xl font-black text-emerald-700 mb-4">📜 Nhiệm Vụ Hàng Ngày</h3>
            <div class="space-y-3">
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div><h4 class="font-bold text-gray-800">Cho ăn 3 lần</h4><p class="text-xs text-gray-500" id="q1-desc">Tiến độ: 0/3</p></div>
                    <button id="q1-btn" onclick="claimQuest(1, 30)" class="px-3 py-1.5 bg-gray-300 text-gray-500 font-bold rounded-xl text-sm cursor-not-allowed" disabled>Nhận 30🪙</button>
                </div>
                <div class="flex justify-between items-center p-3 bg-white/70 rounded-2xl">
                    <div><h4 class="font-bold text-gray-800">Chơi đùa 2 lần</h4><p class="text-xs text-gray-500" id="q2-desc">Tiến độ: 0/2</p></div>
                    <button id="q2-btn" onclick="claimQuest(2, 40)" class="px-3 py-1.5 bg-gray-300 text-gray-500 font-bold rounded-xl text-sm cursor-not-allowed" disabled>Nhận 40🪙</button>
                </div>
            </div>
        </div>
    </div>

    <!-- SCRIPT XÂY DỰNG 3D VÀ LOGIC GAME -->
    <script>
        let gameStarted = false;
        let coins = 150;
        let hunger = 80;
        let happy = 80;
        let energy = 80;
        let petName = "Mimi";
        let isNight = false;
        let quests = { feed: 0, play: 0, q1Done: false, q2Done: false };

        // Web Audio API Tổng hợp âm thanh không cần file ngoài
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

        // --- KHỞI TẠO THREE.JS 3D ---
        const container = document.getElementById('webgl-container');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xa0e0ff);
        scene.fog = new THREE.FogExp2(0xa0e0ff, 0.015);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 5, 10);
        camera.lookAt(0, 1, 0);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        container.appendChild(renderer.domElement);

        // Ánh sáng môi trường & mặt trời
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        scene.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0xfffaed, 0.9);
        dirLight.position.set(10, 20, 10);
        dirLight.castShadow = true;
        scene.add(dirLight);

        // Nền cỏ nông trại 3D
        const groundGeo = new THREE.CylinderGeometry(8, 8, 0.6, 32);
        const groundMat = new THREE.MeshStandardMaterial({ color: 0x7cfc00, roughness: 0.8 });
        const ground = new THREE.Mesh(groundGeo, groundMat);
        ground.position.y = -0.3;
        ground.receiveShadow = true;
        scene.add(ground);

        // Xây dựng mô hình 3D Chibi Thú Cưng có má hồng chuẩn ảnh mẫu
        let petGroup = new THREE.Group();
        scene.add(petGroup);
        let bodyMesh;

        function buildPet3D(colorHex, type) {
            while(petGroup.children.length > 0) { petGroup.remove(petGroup.children[0]); }

            const bodyMat = new THREE.MeshStandardMaterial({ color: colorHex, roughness: 0.3 });
            const blushMat = new THREE.MeshBasicMaterial({ color: 0xff69b4 }); // Má hồng chibi
            const eyeMat = new THREE.MeshBasicMaterial({ color: 0x222222 });

            // Thân tròn trĩnh đáng yêu
            const bodyGeo = new THREE.SphereGeometry(1.1, 32, 32);
            bodyMesh = new THREE.Mesh(bodyGeo, bodyMat);
            bodyMesh.position.y = 1.1;
            bodyMesh.castShadow = true;
            petGroup.add(bodyMesh);

            // Má hồng bên trái & phải
            const cheekGeo = new THREE.CircleGeometry(0.22, 16);
            const leftCheek = new THREE.Mesh(cheekGeo, blushMat);
            leftCheek.position.set(-0.55, 1.05, 0.96);
            petGroup.add(leftCheek);

            const rightCheek = new THREE.Mesh(cheekGeo, blushMat);
            rightCheek.position.set(0.55, 1.05, 0.96);
            petGroup.add(rightCheek);

            // Mắt to tròn long lanh
            const eyeGeo = new THREE.SphereGeometry(0.12, 16, 16);
            const leftEye = new THREE.Mesh(eyeGeo, eyeMat);
            leftEye.position.set(-0.35, 1.3, 0.98);
            petGroup.add(leftEye);

            const rightEye = new THREE.Mesh(eyeGeo, eyeMat);
            rightEye.position.set(0.35, 1.3, 0.98);
            petGroup.add(rightEye);

            // Tai tùy chỉnh theo loài
            if (type === 'cat' || type === 'rabbit') {
                const earGeo = new THREE.ConeGeometry(0.3, 0.6, 16);
                const leftEar = new THREE.Mesh(earGeo, bodyMat);
                leftEar.position.set(-0.6, 2.0, 0);
                leftEar.rotation.z = -0.2;
                petGroup.add(leftEar);

                const rightEar = new THREE.Mesh(earGeo, bodyMat);
                rightEar.position.set(0.6, 2.0, 0);
                rightEar.rotation.z = 0.2;
                petGroup.add(rightEar);
            }
        }

        buildPet3D(0xffe4e1, 'cat');

        // Vòng lặp Render & Animation nhịp thở 3D
        let clock = new THREE.Clock();
        function animate() {
            requestAnimationFrame(animate);
            let time = clock.getElapsedTime();
            if (bodyMesh) {
                bodyMesh.scale.y = 1 + Math.sin(time * 4) * 0.03;
                petGroup.position.y = Math.sin(time * 3) * 0.06;
            }
            renderer.render(scene, camera);
        }
        animate();

        // --- CÁC HÀM ĐIỀU KHIỂN GAME ---
        function startGame() {
            playSound('success');
            gameStarted = true;
            document.getElementById('start-screen').classList.add('opacity-0', 'pointer-events-none');
            setTimeout(() => document.getElementById('start-screen').style.display = 'none', 700);
            document.getElementById('ui-layer').classList.remove('hidden');
            showToast("Chào mừng bạn đến với nông trại 3D Kawaii!");
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

        function feedPet() {
            if (coins < 10) { showToast("Bạn không đủ 10 xu!"); return; }
            coins -= 10;
            hunger = Math.min(100, hunger + 25);
            quests.feed++;
            playSound('success');
            showToast(`Yummy! ${petName} ăn rất ngon miệng.`);
            updateUI();
        }

        function playPet() {
            happy = Math.min(100, happy + 20);
            energy = Math.max(0, energy - 10);
            coins += 15;
            quests.play++;
            playSound('success');
            showToast(`${petName} chơi đùa vui vẻ và nhận 15 xu!`);
            updateUI();
        }

        function sleepPet() {
            energy = 100;
            hunger = Math.max(0, hunger - 15);
            isNight = !isNight;
            let badge = document.getElementById('time-badge');
            if (isNight) {
                scene.background.setHex(0x1a1a3a);
                scene.fog.color.setHex(0x1a1a3a);
                ambientLight.color.setHex(0x6688cc);
                badge.className = "text-xs font-bold text-indigo-200 bg-indigo-900 px-2 py-0.5 rounded-full";
                badge.innerText = "🌙 Ban Đêm";
                showToast(`Khò khò... ${petName} đã đi ngủ ngon giấc.`);
            } else {
                scene.background.setHex(0xa0e0ff);
                scene.fog.color.setHex(0xa0e0ff);
                ambientLight.color.setHex(0xffffff);
                badge.className = "text-xs font-bold text-amber-700 bg-amber-100 px-2 py-0.5 rounded-full";
                badge.innerText = "☀️ Ban Ngày";
                showToast(`Chào buổi sáng! ${petName} thức dậy tràn đầy năng lượng.`);
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

        function switchPet(name, emoji, color, type) {
            petName = name;
            document.getElementById('pet-avatar-icon').innerText = emoji;
            document.getElementById('pet-name-title').innerText = `${name} (${emoji})`;
            buildPet3D(color, type);
            playSound('success');
            showToast(`Đã đón thành công bé ${name} về trang trại!`);
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

        // Tự động resize màn hình 3D
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
</body>
</html>
