<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cute Farm Tycoon - Nông Trại Siêu Dễ Thương</title>
    <!-- Tailwind CSS & FontAwesome -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Three.js (Sử dụng đúng phiên bản ổn định) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&display=swap');
        body {
            font-family: 'Quicksand', sans-serif;
            user-select: none;
            overflow: hidden;
            margin: 0;
            padding: 0;
        }
        .glass {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            border: 2px solid rgba(255, 255, 255, 0.6);
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        .animate-float {
            animation: float 3s ease-in-out infinite;
        }
    </style>
</head>
<body class="relative w-screen h-screen bg-sky-200">

    <!-- CANVAS 3D -->
    <div id="canvas-container" class="absolute inset-0 z-0"></div>

    <!-- MÀN HÌNH CHÍNH (MAIN MENU) -->
    <div id="main-menu" class="absolute inset-0 z-50 flex flex-col items-center justify-center bg-gradient-to-b from-pink-300 via-purple-300 to-sky-300">
        <div class="text-center animate-float p-8 max-w-md glass rounded-3xl shadow-2xl">
            <div class="text-6xl mb-3">🌸🐰🌾🐱</div>
            <h1 class="text-4xl font-extrabold text-pink-600 mb-2 drop-shadow">Cute Farm Tycoon</h1>
            <p class="text-gray-700 font-bold mb-6 text-sm">Xây dựng nông trại phép thuật với những bé thú siêu cấp đáng yêu!</p>
            
            <button onclick="startGame()" class="px-8 py-4 bg-gradient-to-r from-pink-500 to-rose-500 text-white font-extrabold text-lg rounded-full shadow-lg hover:scale-105 transition transform active:scale-95 border-4 border-white cursor-pointer">
                <i class="fa-solid fa-play mr-2"></i> VÀO NÔNG TRẠI
            </button>
        </div>
    </div>

    <!-- GIAO DIỆN TRONG GAME (HUD) -->
    <div id="game-hud" class="absolute inset-0 z-10 pointer-events-none hidden flex flex-col justify-between p-4 md:p-6">
        
        <!-- Thanh Trên Cùng: Tiền, Điểm, Thời Gian -->
        <div class="flex flex-wrap justify-between items-center gap-3 pointer-events-auto">
            <!-- Thông tin kinh tế -->
            <div class="flex items-center gap-3 glass px-5 py-2.5 rounded-2xl shadow-lg">
                <div class="flex items-center gap-1.5 text-amber-600 font-extrabold text-lg">
                    <i class="fa-solid fa-coins"></i> <span id="gold-val">250</span> G
                </div>
                <div class="h-6 w-px bg-gray-300"></div>
                <div class="flex items-center gap-1.5 text-pink-600 font-extrabold text-lg">
                    <i class="fa-solid fa-star"></i> <span id="score-val">0</span>
                </div>
            </div>

            <!-- Đồng hồ & Thời tiết -->
            <div class="glass px-5 py-2.5 rounded-2xl shadow-lg flex items-center gap-3 font-bold text-gray-700">
                <span id="time-icon" class="text-xl">☀️</span>
                <span id="time-text">Buổi trưa (12:00)</span>
            </div>

            <!-- Nút Âm thanh & Trợ giúp -->
            <div class="flex items-center gap-2">
                <button onclick="toggleSound()" id="sound-btn" class="glass p-3 rounded-2xl shadow-lg hover:bg-white text-gray-700 transition cursor-pointer">
                    <i class="fa-solid fa-volume-high"></i>
                </button>
                <button onclick="toggleHelp()" class="glass p-3 rounded-2xl shadow-lg hover:bg-white text-gray-700 transition cursor-pointer">
                    <i class="fa-solid fa-question"></i>
                </button>
            </div>
        </div>

        <!-- Bảng Thông Báo Nổi -->
        <div id="notification" class="self-center glass px-6 py-2 rounded-full shadow-lg text-pink-600 font-bold text-sm transition-opacity duration-300 opacity-0">
            Chào mừng bạn đến với nông trại!
        </div>

        <!-- Thanh Dưới Cùng: Mua Thú & Thức Ăn -->
        <div class="flex flex-wrap justify-between items-end gap-3 pointer-events-auto">
            
            <!-- Cửa hàng Mua Thú -->
            <div class="glass p-3 rounded-3xl shadow-xl flex flex-wrap gap-2 max-w-xl">
                <button onclick="buyAnimal('sheep')" class="flex flex-col items-center bg-white/80 hover:bg-white p-2 rounded-2xl border-2 border-pink-200 transition shadow-sm w-16 cursor-pointer">
                    <span class="text-2xl">🐑</span>
                    <span class="text-xs font-bold text-gray-700 mt-1">Cừu(80G)</span>
                </button>
                <button onclick="buyAnimal('brown_sheep')" class="flex flex-col items-center bg-white/80 hover:bg-white p-2 rounded-2xl border-2 border-amber-200 transition shadow-sm w-16 cursor-pointer">
                    <span class="text-2xl">🐏</span>
                    <span class="text-xs font-bold text-gray-700 mt-1">C.nâu(90G)</span>
                </button>
                <button onclick="buyAnimal('horse')" class="flex flex-col items-center bg-white/80 hover:bg-white p-2 rounded-2xl border-2 border-amber-300 transition shadow-sm w-16 cursor-pointer">
                    <span class="text-2xl">🐴</span>
                    <span class="text-xs font-bold text-gray-700 mt-1">Ngựa(150G)</span>
                </button>
                <button onclick="buyAnimal('chicken')" class="flex flex-col items-center bg-white/80 hover:bg-white p-2 rounded-2xl border-2 border-yellow-200 transition shadow-sm w-16 cursor-pointer">
                    <span class="text-2xl">🐥</span>
                    <span class="text-xs font-bold text-gray-700 mt-1">Gà(50G)</span>
                </button>
                <button onclick="buyAnimal('duck')" class="flex flex-col items-center bg-white/80 hover:bg-white p-2 rounded-2xl border-2 border-yellow-300 transition shadow-sm w-16 cursor-pointer">
                    <span class="text-2xl">🦆</span>
                    <span class="text-xs font-bold text-gray-700 mt-1">Vịt(60G)</span>
                </button>
                <button onclick="buyAnimal('pig')" class="flex flex-col items-center bg-white/80 hover:bg-white p-2 rounded-2xl border-2 border-pink-300 transition shadow-sm w-16 cursor-pointer">
                    <span class="text-2xl">🐷</span>
                    <span class="text-xs font-bold text-gray-700 mt-1">Heo(120G)</span>
                </button>
                <button onclick="buyAnimal('goat')" class="flex flex-col items-center bg-white/80 hover:bg-white p-2 rounded-2xl border-2 border-orange-200 transition shadow-sm w-16 cursor-pointer">
                    <span class="text-2xl">🐐</span>
                    <span class="text-xs font-bold text-gray-700 mt-1">Dê(100G)</span>
                </button>
            </div>

            <!-- Nút Thức Ăn & Thu Hoạch -->
            <div class="flex gap-2">
                <button onclick="feedAllAnimals()" class="glass bg-amber-100 hover:bg-amber-200 text-amber-800 font-extrabold px-5 py-3 rounded-2xl shadow-xl flex items-center gap-2 transition cursor-pointer">
                    <i class="fa-solid fa-bowl-food text-xl"></i> Cho ăn (20G)
                </button>
                <button onclick="harvestAll()" class="glass bg-pink-100 hover:bg-pink-200 text-pink-700 font-extrabold px-5 py-3 rounded-2xl shadow-xl flex items-center gap-2 transition cursor-pointer">
                    <i class="fa-solid fa-hand-holding-heart text-xl"></i> Thu Hoạch
                </button>
            </div>

        </div>
    </div>

    <!-- Hướng dẫn Modal -->
    <div id="help-modal" class="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm hidden flex items-center justify-center p-4">
        <div class="glass p-6 rounded-3xl max-w-md w-full shadow-2xl relative">
            <button onclick="toggleHelp()" class="absolute top-4 right-4 text-gray-500 hover:text-black text-xl cursor-pointer"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="text-2xl font-extrabold text-pink-600 mb-3"><i class="fa-solid fa-book-open mr-2"></i> Hướng Dẫn Chơi</h3>
            <ul class="space-y-2 text-gray-700 font-medium text-sm">
                <li>🐑 <b>Mua thú cưng:</b> Dùng tiền vàng để mua các bé động vật siêu dễ thương.</li>
                <li>🌙 <b>Ngày & Đêm:</b> Ban đêm các bé sẽ buồn ngủ và nghỉ ngơi.</li>
                <li>🍼 <b>Cho ăn:</b> Bấm "Cho ăn" để giữ năng lượng cho thú cưng.</li>
                <li>✨ <b>Thu hoạch:</b> Chạm vào thú cưng hoặc bấm "Thu hoạch" để nhận vàng!</li>
            </ul>
        </div>
    </div>

    <!-- LOGIC SCRIPT -->
    <script>
        let audioCtx = null;
        let soundEnabled = true;

        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        function playSound(type) {
            if (!soundEnabled) return;
            initAudio();
            if (!audioCtx) return;

            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            const now = audioCtx.currentTime;

            if (type === 'click') {
                osc.frequency.setValueAtTime(400, now);
                osc.frequency.exponentialRampToValueAtTime(800, now + 0.1);
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
                osc.start(now);
                osc.stop(now + 0.1);
            } else if (type === 'buy') {
                osc.frequency.setValueAtTime(300, now);
                osc.frequency.setValueAtTime(500, now + 0.1);
                osc.frequency.setValueAtTime(700, now + 0.2);
                gain.gain.setValueAtTime(0.15, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
                osc.start(now);
                osc.stop(now + 0.3);
            } else if (type === 'harvest') {
                osc.frequency.setValueAtTime(523.25, now);
                osc.frequency.setValueAtTime(659.25, now + 0.1);
                osc.frequency.setValueAtTime(783.99, now + 0.2);
                gain.gain.setValueAtTime(0.15, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
                osc.start(now);
                osc.stop(now + 0.35);
            }
        }

        function toggleSound() {
            soundEnabled = !soundEnabled;
            const btn = document.getElementById('sound-btn');
            btn.innerHTML = soundEnabled ? '<i class="fa-solid fa-volume-high"></i>' : '<i class="fa-solid fa-volume-xmark text-red-500"></i>';
            showNotification(soundEnabled ? "Đã bật âm thanh!" : "Đã tắt âm thanh!");
        }

        function toggleHelp() {
            playSound('click');
            const modal = document.getElementById('help-modal');
            modal.classList.toggle('hidden');
        }

        function showNotification(text) {
            const notif = document.getElementById('notification');
            notif.innerText = text;
            notif.style.opacity = '1';
            setTimeout(() => { notif.style.opacity = '0'; }, 2000);
        }

        // --- THREE.JS GAME ENGINE ---
        let scene, camera, renderer;
        let animals = [];
        let gameData = { gold: 250, score: 0, time: 8, isNight: false };

        const animalTypes = {
            sheep: { name: 'Cừu Trắng', cost: 80, color: 0xffffff, reward: 15 },
            brown_sheep: { name: 'Cừu Nâu', cost: 90, color: 0x8d5524, reward: 18 },
            horse: { name: 'Ngựa Con', cost: 150, color: 0x7c4a03, reward: 30 },
            chicken: { name: 'Gà Vàng', cost: 50, color: 0xffd700, reward: 10 },
            duck: { name: 'Vịt Con', cost: 60, color: 0xffea00, reward: 12 },
            pig: { name: 'Heo Hồng', cost: 120, color: 0xffb6c1, reward: 22 },
            goat: { name: 'Dê Sừng', cost: 100, color: 0xd2b48c, reward: 20 }
        };

        function init3D() {
            const container = document.getElementById('canvas-container');
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0xbfe3f7);

            camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 16, 24);
            camera.lookAt(0, 0, 0);

            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            container.appendChild(renderer.domElement);

            const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
            scene.add(ambientLight);

            const dirLight = new THREE.DirectionalLight(0xfffaed, 0.8);
            dirLight.position.set(20, 30, 20);
            dirLight.castShadow = true;
            scene.add(dirLight);

            // Sân cỏ
            const groundGeo = new THREE.PlaneGeometry(60, 60);
            const groundMat = new THREE.MeshStandardMaterial({ color: 0x7cfc00, roughness: 0.8 });
            const ground = new THREE.Mesh(groundGeo, groundMat);
            ground.rotation.x = -Math.PI / 2;
            ground.receiveShadow = true;
            scene.add(ground);

            // Tạo các con thú ban đầu
            spawnAnimal('sheep');
            spawnAnimal('chicken');
            spawnAnimal('pig');

            window.addEventListener('resize', onWindowResize);
            window.addEventListener('pointerdown', onPointerDown);
        }

        function spawnAnimal(typeKey) {
            const info = animalTypes[typeKey];
            const group = new THREE.Group();

            // Thân thú
            const body = new THREE.Mesh(
                new THREE.SphereGeometry(1.2, 16, 16),
                new THREE.MeshStandardMaterial({ color: info.color, roughness: 0.5 })
            );
            body.position.y = 1.2;
            body.castShadow = true;
            group.add(body);

            // Đầu thú
            const head = new THREE.Mesh(
                new THREE.SphereGeometry(0.8, 16, 16),
                new THREE.MeshStandardMaterial({ color: info.color, roughness: 0.5 })
            );
            head.position.set(0, 2.2, 0.8);
            group.add(head);

            // Vị trí ngẫu nhiên
            const rx = (Math.random() - 0.5) * 25;
            const rz = (Math.random() - 0.5) * 25;
            group.position.set(rx, 0, rz);

            scene.add(group);
            animals.push({ mesh: group, info: info, moveTimer: Math.random() * 100 });
        }

        function onPointerDown(event) {
            const raycaster = new THREE.Raycaster();
            const mouse = new THREE.Vector2();
            mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(scene.children, true);

            if (intersects.length > 0) {
                for (let anim of animals) {
                    let hit = false;
                    anim.mesh.traverse(child => { if (child === intersects[0].object) hit = true; });
                    if (hit) {
                        harvestAnimal(anim);
                        break;
                    }
                }
            }
        }

        function harvestAnimal(anim) {
            playSound('harvest');
            gameData.gold += anim.info.reward;
            gameData.score += 5;
            updateHUD();
            showNotification(`Thu hoạch thành công (+${anim.info.reward}G)! 💖`);
            
            anim.mesh.position.y += 0.8;
            setTimeout(() => { anim.mesh.position.y -= 0.8; }, 200);
        }

        function buyAnimal(typeKey) {
            const info = animalTypes[typeKey];
            if (gameData.gold >= info.cost) {
                gameData.gold -= info.cost;
                updateHUD();
                spawnAnimal(typeKey);
                playSound('buy');
                showNotification(`Đã mua ${info.name}! 🎉`);
            } else {
                showNotification("Không đủ tiền vàng! 🥲");
            }
        }

        function feedAllAnimals() {
            if (gameData.gold >= 20) {
                gameData.gold -= 20;
                updateHUD();
                playSound('buy');
                showNotification("Đã cho tất cả thú cưng ăn no nê! 🍼✨");
            } else {
                showNotification("Cần ít nhất 20G để mua thức ăn! 🪙");
            }
        }

        function harvestAll() {
            let total = 0;
            animals.forEach(anim => { total += anim.info.reward; });
            if (total > 0) {
                gameData.gold += total;
                gameData.score += animals.length * 2;
                updateHUD();
                playSound('harvest');
                showNotification(`Thu hoạch toàn nông trại được +${total}G! 🌟`);
            }
        }

        function updateHUD() {
            document.getElementById('gold-val').innerText = gameData.gold;
            document.getElementById('score-val').innerText = gameData.score;
        }

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        function updateClock() {
            gameData.time += 0.1;
            if (gameData.time >= 24) gameData.time = 0;
            let hour = Math.floor(gameData.time);
            let minute = Math.floor((gameData.time - hour) * 60);
            let timeStr = `${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`;
            
            if (hour >= 18 || hour < 6) {
                document.getElementById('time-icon').innerText = "🌙";
                document.getElementById('time-text').innerText = `Ban đêm (${timeStr})`;
                scene.background.set(0x1a1a2e);
            } else {
                document.getElementById('time-icon').innerText = "☀️";
                document.getElementById('time-text').innerText = `Ban ngày (${timeStr})`;
                scene.background.set(0xbfe3f7);
            }
        }

        function animate() {
            requestAnimationFrame(animate);
            animals.forEach((anim, idx) => {
                anim.moveTimer += 0.02;
                anim.mesh.position.y = Math.sin(anim.moveTimer * 5 + idx) * 0.15;
                let angle = anim.moveTimer * 0.5 + idx;
                anim.mesh.position.x += Math.sin(angle) * 0.02;
                anim.mesh.position.z += Math.cos(angle) * 0.02;
                anim.mesh.position.x = Math.max(-20, Math.min(20, anim.mesh.position.x));
                anim.mesh.position.z = Math.max(-20, Math.min(20, anim.mesh.position.z));
            });
            renderer.render(scene, camera);
        }

        function startGame() {
            playSound('buy');
            document.getElementById('main-menu').style.display = 'none';
            document.getElementById('game-hud').classList.remove('hidden');
            init3D();
            animate();
            setInterval(updateClock, 1000);
            showNotification("Chào mừng bạn đến với Nông Trại Siêu Dễ Thương! 🌸");
        }
    </script>
</body>
</html>
