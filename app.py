<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cute 3D Farm Tycoon Game</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800&display=swap');
        body {
            font-family: 'Outfit', sans-serif;
            user-select: none;
            -webkit-user-select: none;
            overflow: hidden;
            background-color: #0f172a;
        }
        canvas {
            display: block;
            width: 100vw;
            height: 100vh;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 0;
        }
        .glass {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.25);
        }
        .glass-card {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.15);
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }
        .animate-float {
            animation: float 3s ease-in-out infinite;
        }
        @keyframes pulseGlow {
            0%, 100% { box-shadow: 0 0 15px rgba(234, 179, 8, 0.4); }
            50% { box-shadow: 0 0 30px rgba(234, 179, 8, 0.8); }
        }
        .pulse-gold {
            animation: pulseGlow 2s infinite;
        }
    </style>
</head>
<body class="text-white relative w-screen h-screen">

    <!-- 3D Canvas Container -->
    <div id="canvas-container"></div>

    <!-- MAIN MENU OVERLAY -->
    <div id="main-menu" class="absolute inset-0 z-50 flex flex-col items-center justify-center bg-gradient-to-b from-indigo-950/80 via-purple-950/80 to-slate-950/90 backdrop-blur-md p-6">
        <div class="text-center max-w-xl mx-auto space-y-6">
            <div class="inline-block px-4 py-1.5 rounded-full glass text-amber-300 font-semibold text-sm mb-2 tracking-wide uppercase shadow-lg">
                ✨ 3D Immersive Farm Tycoon ✨
            </div>
            <h1 class="text-5xl md:text-7xl font-extrabold tracking-tight bg-gradient-to-r from-amber-200 via-emerald-300 to-teal-200 bg-clip-text text-transparent drop-shadow-2xl">
                Dream Farm 3D
            </h1>
            <p class="text-slate-300 text-lg md:text-xl font-medium leading-relaxed">
                Raise adorable chibi animals, manage dynamic day-night cycles & weather, feed your hungry pets, and harvest golden rewards!
            </p>
            <div class="pt-6">
                <button id="start-btn" onclick="startGame()" class="px-10 py-5 bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 text-white font-extrabold text-2xl rounded-2xl shadow-2xl transform hover:scale-105 active:scale-95 transition-all duration-200 border-2 border-white/30 pulse-gold flex items-center justify-center gap-3 mx-auto">
                    <span>🚜</span> Start Farming Now
                </button>
            </div>
            <div class="flex items-center justify-center gap-6 pt-4 text-sm text-slate-400">
                <span>🐑 Cute Animals</span>
                <span>•</span>
                <span>🌧️ Weather System</span>
                <span>•</span>
                <span>🎵 Synth Audio</span>
            </div>
        </div>
    </div>

    <!-- HUD / GAME UI (Hidden initially) -->
    <div id="game-ui" class="absolute inset-0 z-10 pointer-events-none hidden flex flex-col justify-between p-4 md:p-6">
        
        <!-- Top Bar -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4 pointer-events-auto">
            <!-- Stats -->
            <div class="flex items-center gap-3 glass-card px-5 py-3 rounded-2xl shadow-xl">
                <div class="flex items-center gap-2 text-amber-300 font-bold text-xl">
                    <span>🪙</span>
                    <span id="gold-display">250</span>
                </div>
                <div class="h-6 w-[1px] bg-white/20"></div>
                <div class="flex items-center gap-2 text-emerald-300 font-bold text-xl">
                    <span>🌾</span>
                    <span id="food-display">15</span>
                </div>
                <div class="h-6 w-[1px] bg-white/20"></div>
                <div class="flex items-center gap-2 text-sky-300 font-bold text-lg">
                    <span>⭐</span>
                    <span id="score-display">0</span>
                </div>
            </div>

            <!-- Time & Weather Indicator -->
            <div class="glass-card px-5 py-3 rounded-2xl shadow-xl flex items-center gap-4">
                <div class="flex items-center gap-2">
                    <span id="time-icon" class="text-2xl">🌅</span>
                    <div class="flex flex-col">
                        <span id="time-label" class="text-sm font-bold tracking-wide uppercase text-amber-300">Morning</span>
                        <span id="clock-display" class="text-xs text-slate-300 font-mono">06:00 AM</span>
                    </div>
                </div>
                <div class="h-6 w-[1px] bg-white/20"></div>
                <div class="flex items-center gap-2">
                    <span id="weather-icon" class="text-2xl">☀️</span>
                    <span id="weather-label" class="text-xs font-semibold text-slate-200">Sunny</span>
                </div>
            </div>

            <!-- Audio & Controls -->
            <div class="flex items-center gap-2">
                <button onclick="toggleSound()" id="sound-btn" class="glass-card p-3 rounded-2xl hover:bg-white/20 transition text-xl shadow-lg">
                    🔊
                </button>
            </div>
        </div>

        <!-- Center floating notification or hints -->
        <div id="notification-banner" class="self-center glass-card px-6 py-2 rounded-full text-sm font-semibold tracking-wide text-emerald-300 shadow-2xl transition-all duration-300 opacity-0 transform -translate-y-4">
            Welcome to your Farm! Click animals to harvest gold or buy food!
        </div>

        <!-- Bottom Actions & Shop Bar -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4 pointer-events-auto pb-2">
            
            <!-- Weather / Time Override (For testing or player fun) -->
            <div class="glass-card p-2 rounded-2xl flex items-center gap-2 shadow-xl">
                <span class="text-xs font-bold text-slate-400 px-2">TIME:</span>
                <button onclick="setTimePreset('morning')" class="px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/40 text-amber-300 text-xs font-bold transition">Morning</button>
                <button onclick="setTimePreset('noon')" class="px-3 py-1.5 rounded-xl bg-yellow-500/20 hover:bg-yellow-500/40 text-yellow-300 text-xs font-bold transition">Noon</button>
                <button onclick="setTimePreset('evening')" class="px-3 py-1.5 rounded-xl bg-orange-500/20 hover:bg-orange-500/40 text-orange-300 text-xs font-bold transition">Evening</button>
                <button onclick="setTimePreset('night')" class="px-3 py-1.5 rounded-xl bg-indigo-500/20 hover:bg-indigo-500/40 text-indigo-300 text-xs font-bold transition">Night</button>
                <div class="h-5 w-[1px] bg-white/20"></div>
                <button onclick="toggleRain()" id="rain-toggle-btn" class="px-3 py-1.5 rounded-xl bg-sky-500/20 hover:bg-sky-500/40 text-sky-300 text-xs font-bold transition">🌧️ Rain</button>
            </div>

            <!-- Shop / Feeding Actions -->
            <div class="glass-card p-2 rounded-2xl flex items-center gap-3 shadow-xl">
                <button onclick="buyFood(10, 50)" class="flex items-center gap-2 px-4 py-2 bg-emerald-600/60 hover:bg-emerald-500/80 rounded-xl font-bold text-sm transition shadow border border-emerald-400/30">
                    <span>🌾</span> Buy Feed (+10) <span class="text-amber-300 text-xs">50🪙</span>
                </button>
                <button onclick="feedAllAnimals()" class="flex items-center gap-2 px-4 py-2 bg-amber-600/60 hover:bg-amber-500/80 rounded-xl font-bold text-sm transition shadow border border-amber-400/30">
                    <span>🥕</span> Feed All Animals
                </button>
                <button onclick="spawnRandomAnimal()" class="flex items-center gap-2 px-4 py-2 bg-purple-600/60 hover:bg-purple-500/80 rounded-xl font-bold text-sm transition shadow border border-purple-400/30">
                    <span>➕</span> Adopt Pet <span class="text-amber-300 text-xs">100🪙</span>
                </button>
            </div>
        </div>

    </div>

    <!-- Custom Modal Message Box -->
    <div id="modal-box" class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm hidden">
        <div class="glass-card p-6 rounded-3xl max-w-sm w-full mx-4 text-center space-y-4 shadow-2xl border border-white/20">
            <h3 id="modal-title" class="text-2xl font-bold text-amber-300">Notice</h3>
            <p id="modal-message" class="text-slate-200 text-sm">Message content goes here.</p>
            <button onclick="closeModal()" class="w-full py-3 bg-emerald-600 hover:bg-emerald-500 font-bold rounded-xl text-white shadow-lg transition">OK</button>
        </div>
    </div>

    <!-- Game Logic & Three.js Script -->
    <script>
        // --- AUDIO ENGINE (Web Audio API Synthesizer & Sound Effects) ---
        class SoundEngine {
            constructor() {
                this.ctx = null;
                this.enabled = true;
                this.bgmInterval = null;
            }

            init() {
                if (!this.ctx) {
                    const AudioContext = window.AudioContext || window.webkitAudioContext;
                    this.ctx = new AudioContext();
                }
                if (this.ctx.state === 'suspended') {
                    this.ctx.resume();
                }
            }

            playClick() {
                if (!this.enabled) return;
                this.init();
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(600, this.ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.08);
                gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.08);
                osc.connect(gain);
                gain.connect(this.ctx.destination);
                osc.start();
                osc.stop(this.ctx.currentTime + 0.08);
            }

            playCoin() {
                if (!this.enabled) return;
                this.init();
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(987.77, this.ctx.currentTime); // B5
                osc.frequency.setValueAtTime(1318.51, this.ctx.currentTime + 0.08); // E6
                gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.3);
                osc.connect(gain);
                gain.connect(this.ctx.destination);
                osc.start();
                osc.stop(this.ctx.currentTime + 0.3);
            }

            playEat() {
                if (!this.enabled) return;
                this.init();
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(200, this.ctx.currentTime);
                osc.frequency.linearRampToValueAtTime(350, this.ctx.currentTime + 0.15);
                gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
                gain.gain.linearRampToValueAtTime(0.01, this.ctx.currentTime + 0.15);
                osc.connect(gain);
                gain.connect(this.ctx.destination);
                osc.start();
                osc.stop(this.ctx.currentTime + 0.15);
            }

            playThunder() {
                if (!this.enabled) return;
                this.init();
                // White noise buffer for thunder crash
                const bufferSize = this.ctx.sampleRate * 1.5;
                const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
                const data = buffer.getChannelData(0);
                for (let i = 0; i < bufferSize; i++) {
                    data[i] = Math.random() * 2 - 1;
                }
                const noise = this.ctx.createBufferSource();
                noise.buffer = buffer;

                const filter = this.ctx.createBiquadFilter();
                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(300, this.ctx.currentTime);
                filter.frequency.linearRampToValueAtTime(80, this.ctx.currentTime + 1.5);

                const gain = this.ctx.createGain();
                gain.gain.setValueAtTime(0.4, this.ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 1.5);

                noise.connect(filter);
                filter.connect(gain);
                gain.connect(this.ctx.destination);
                noise.start();
            }

            startBGM() {
                if (this.bgmInterval) return;
                const notes = [261.63, 329.63, 392.00, 523.25, 440.00, 349.23, 392.00, 329.63]; // C major upbeat arpeggio
                let step = 0;
                this.bgmInterval = setInterval(() => {
                    if (!this.enabled || !this.ctx) return;
                    try {
                        const osc = this.ctx.createOscillator();
                        const gain = this.ctx.createGain();
                        osc.type = 'sine';
                        osc.frequency.setValueAtTime(notes[step], this.ctx.currentTime);
                        
                        gain.gain.setValueAtTime(0.04, this.ctx.currentTime);
                        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.35);

                        osc.connect(gain);
                        gain.connect(this.ctx.destination);
                        osc.start();
                        osc.stop(this.ctx.currentTime + 0.35);

                        step = (step + 1) % notes.length;
                    } catch (e) {
                        // ignore context errors before user interaction
                    }
                }, 300);
            }

            stopBGM() {
                if (this.bgmInterval) {
                    clearInterval(this.bgmInterval);
                    this.bgmInterval = null;
                }
            }
        }

        const soundEngine = new SoundEngine();

        // --- GAME STATE ---
        const gameState = {
            gold: 250,
            food: 15,
            score: 0,
            timeOfDay: 'morning', // morning, noon, evening, night
            timeValue: 0.15, // 0 to 1 cycle
            isRaining: false,
            soundOn: true,
            animals: [],
            floaters: []
        };

        // --- THREE.JS SETUP ---
        let scene, camera, renderer;
        let ambientLight, dirLight, hemiLight;
        let rainParticles, rainGeo, rainCount = 1200;
        let clock = new THREE.Clock();
        let raycaster = new THREE.Raycaster();
        let mouse = new THREE.Vector2();

        function init3D() {
            const container = document.getElementById('canvas-container');
            
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0xdbeafe);
            scene.fog = new THREE.FogExp2(0xdbeafe, 0.015);

            camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 18, 25);
            camera.lookAt(0, 0, 0);

            renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "high-performance" });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.shadowMap.enabled = true;
            renderer.shadowMap.type = THREE.PCFSoftShadowMap;
            container.appendChild(renderer.domElement);

            // Lighting
            ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
            scene.add(ambientLight);

            hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444, 0.5);
            hemiLight.position.set(0, 50, 0);
            scene.add(hemiLight);

            dirLight = new THREE.DirectionalLight(0xfffbeb, 1.2);
            dirLight.position.set(20, 30, 20);
            dirLight.castShadow = true;
            dirLight.shadow.camera.top = 25;
            dirLight.shadow.camera.bottom = -25;
            dirLight.shadow.camera.left = -25;
            dirLight.shadow.camera.right = 25;
            dirLight.shadow.camera.near = 0.1;
            dirLight.shadow.camera.far = 100;
            dirLight.shadow.mapSize.width = 2048;
            dirLight.shadow.mapSize.height = 2048;
            scene.add(dirLight);

            createEnvironment();
            createRainSystem();

            // Event Listeners
            window.addEventListener('resize', onWindowResize);
            window.addEventListener('pointerdown', onPointerDown);

            // Spawn initial cute animals
            spawnAnimal('sheep', -4, 0, -2);
            spawnAnimal('cow', 4, 0, 2);
            spawnAnimal('pig', -3, 0, 4);
            spawnAnimal('chicken', 3, 0, -4);
        }

        // --- ENVIRONMENT & PROPS ---
        function createEnvironment() {
            // Base Island / Ground
            const groundGeo = new THREE.CylinderGeometry(18, 19, 1.2, 48);
            const groundMat = new THREE.MeshStandardMaterial({ color: 0x4ade80, roughness: 0.8 });
            const ground = new THREE.Mesh(groundGeo, groundMat);
            ground.position.y = -0.6;
            ground.receiveShadow = true;
            scene.add(ground);

            // Dirt path circle
            const pathGeo = new THREE.RingGeometry(4, 9, 32);
            const pathMat = new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.9, side: THREE.DoubleSide });
            const path = new THREE.Mesh(pathGeo, pathMat);
            path.rotation.x = -Math.PI / 2;
            path.position.y = 0.01;
            path.receiveShadow = true;
            scene.add(path);

            // Barn / House
            createBarn();

            // Trees and Fences
            for (let i = 0; i < 8; i++) {
                const angle = (i / 8) * Math.PI * 2;
                const radius = 13 + Math.random() * 2;
                const x = Math.cos(angle) * radius;
                const z = Math.sin(angle) * radius;
                createLowPolyTree(x, z);
            }

            // Floating Clouds
            for (let i = 0; i < 6; i++) {
                createCloud((Math.random() - 0.5) * 35, 12 + Math.random() * 5, (Math.random() - 0.5) * 35);
            }
        }

        function createBarn() {
            const barnGroup = new THREE.Group();
            barnGroup.position.set(0, 0, -8);

            // Main body
            const bodyGeo = new THREE.BoxGeometry(6, 4, 5);
            const bodyMat = new THREE.MeshStandardMaterial({ color: 0xef4444, roughness: 0.5 });
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            body.position.y = 2;
            body.castShadow = true;
            body.receiveShadow = true;
            barnGroup.add(body);

            // Roof
            const roofShape = new THREE.Shape();
            roofShape.moveTo(-3.3, 0);
            roofShape.lineTo(0, 2.5);
            roofShape.lineTo(3.3, 0);
            roofShape.closePath();

            const extrudeSettings = { depth: 5.6, bevelEnabled: false };
            const roofGeo = new THREE.ExtrudeGeometry(roofShape, extrudeSettings);
            const roofMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.4 });
            const roof = new THREE.Mesh(roofGeo, roofMat);
            roof.position.set(0, 4, -2.8);
            roof.castShadow = true;
            barnGroup.add(roof);

            // Door
            const doorGeo = new THREE.BoxGeometry(1.6, 2.5, 0.1);
            const doorMat = new THREE.MeshStandardMaterial({ color: 0x78350f });
            const door = new THREE.Mesh(doorGeo, doorMat);
            door.position.set(0, 1.25, 2.51);
            barnGroup.add(door);

            scene.add(barnGroup);
        }

        function createLowPolyTree(x, z) {
            const treeGroup = new THREE.Group();
            treeGroup.position.set(x, 0, z);

            // Trunk
            const trunkGeo = new THREE.CylinderGeometry(0.3, 0.4, 2, 6);
            const trunkMat = new THREE.MeshStandardMaterial({ color: 0x854d0e });
            const trunk = new THREE.Mesh(trunkGeo, trunkMat);
            trunk.position.y = 1;
            trunk.castShadow = true;
            treeGroup.add(trunk);

            // Foliage
            const leavesGeo = new THREE.DodecahedronGeometry(1.5);
            const leavesMat = new THREE.MeshStandardMaterial({ color: 0x15803d, roughness: 0.6 });
            const leaves = new THREE.Mesh(leavesGeo, leavesMat);
            leaves.position.y = 2.8;
            leaves.castShadow = true;
            treeGroup.add(leaves);

            scene.add(treeGroup);
        }

        function createCloud(x, y, z) {
            const cloudGroup = new THREE.Group();
            cloudGroup.position.set(x, y, z);
            const mat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.1, transparent: true, opacity: 0.85 });

            for (let i = 0; i < 3; i++) {
                const puff = new THREE.Mesh(new THREE.SphereGeometry(1.2 + Math.random() * 0.5, 7, 7), mat);
                puff.position.set((i - 1) * 1.5, Math.random() * 0.4, (Math.random() - 0.5) * 0.8);
                cloudGroup.add(puff);
            }
            cloudGroup.userData = { speed: 0.005 + Math.random() * 0.005 };
            scene.add(cloudGroup);
            window.clouds = window.clouds || [];
            window.clouds.push(cloudGroup);
        }

        // --- RAIN SYSTEM ---
        function createRainSystem() {
            rainGeo = new THREE.BufferGeometry();
            const positions = [];
            for (let i = 0; i < rainCount; i++) {
                positions.push(
                    (Math.random() - 0.5) * 40,
                    Math.random() * 25,
                    (Math.random() - 0.5) * 40
                );
            }
            rainGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
            const rainMat = new THREE.PointsMaterial({
                color: 0x93c5fd,
                size: 0.15,
                transparent: true,
                opacity: 0.7
            });
            rainParticles = new THREE.Points(rainGeo, rainMat);
            rainParticles.visible = false;
            scene.add(rainParticles);
        }

        // --- CHIBI ANIMALS CLASS ---
        class ChibiAnimal {
            constructor(type, x, z) {
                this.type = type;
                this.group = new THREE.Group();
                this.group.position.set(x, 0, z);
                this.hunger = 80; // 0 (starving) to 100 (full)
                this.isSleeping = false;
                this.targetPos = new THREE.Vector3(x, 0, z);
                this.moveTimer = Math.random() * 5;
                this.bounceSpeed = 6 + Math.random() * 4;
                this.bodyParts = {};
                this.thoughtBubble = null;

                this.buildModel();
                scene.add(this.group);
            }

            buildModel() {
                const g = this.group;
                let bodyColor = 0xffffff;
                let scale = 1;

                if (this.type === 'sheep') bodyColor = 0xf8fafc;
                else if (this.type === 'cow') bodyColor = 0x334155;
                else if (this.type === 'pig') bodyColor = 0xf472b6;
                else if (this.type === 'chicken') { bodyColor = 0xfbbf24; scale = 0.6; }

                g.scale.set(scale, scale, scale);

                // Body
                const bodyGeo = new THREE.SphereGeometry(1, 16, 16);
                bodyGeo.scale(1.2, 0.9, 1.4);
                const bodyMat = new THREE.MeshStandardMaterial({ color: bodyColor, roughness: 0.5 });
                const body = new THREE.Mesh(bodyGeo, bodyMat);
                body.position.y = 1;
                body.castShadow = true;
                g.add(body);
                this.bodyParts.body = body;

                // Head
                const headGeo = new THREE.SphereGeometry(0.7, 14, 14);
                const head = new THREE.Mesh(headGeo, bodyMat);
                head.position.set(0, 1.6, 1.1);
                head.castShadow = true;
                g.add(head);
                this.bodyParts.head = head;

                // Snout / Beak
                if (this.type === 'chicken') {
                    const beakGeo = new THREE.ConeGeometry(0.2, 0.4, 4);
                    const beakMat = new THREE.MeshStandardMaterial({ color: 0xea580c });
                    const beak = new THREE.Mesh(beakGeo, beakMat);
                    beak.rotation.x = Math.PI / 2;
                    beak.position.set(0, 1.6, 1.6);
                    g.add(beak);
                } else {
                    const snoutGeo = new THREE.BoxGeometry(0.5, 0.3, 0.4);
                    const snoutMat = new THREE.MeshStandardMaterial({ color: bodyColor === 0xf472b6 ? 0xdb2777 : 0xe2e8f0 });
                    const snout = new THREE.Mesh(snoutGeo, snoutMat);
                    snout.position.set(0, 1.5, 1.5);
                    g.add(snout);
                }

                // Legs (4 stubby chibi legs)
                const legGeo = new THREE.CylinderGeometry(0.18, 0.12, 0.8, 8);
                const legMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
                
                const positions = [
                    [-0.5, 0.4, 0.6], [0.5, 0.4, 0.6],
                    [-0.5, 0.4, -0.6], [0.5, 0.4, -0.6]
                ];

                this.bodyParts.legs = [];
                positions.forEach(pos => {
                    const leg = new THREE.Mesh(legGeo, legMat);
                    leg.position.set(...pos);
                    leg.castShadow = true;
                    g.add(leg);
                    this.bodyParts.legs.push(leg);
                });

                // Thought Bubble container for Hunger/Sleep
                this.createThoughtBubble();
            }

            createThoughtBubble() {
                const canvas = document.createElement('canvas');
                canvas.width = 128;
                canvas.height = 128;
                const ctx = canvas.getContext('2d');
                this.thoughtCanvas = canvas;
                this.thoughtCtx = ctx;

                const texture = new THREE.CanvasTexture(canvas);
                const spriteMat = new THREE.SpriteMaterial({ map: texture, transparent: true });
                const sprite = new THREE.Sprite(spriteMat);
                sprite.scale.set(1.2, 1.2, 1);
                sprite.position.set(0, 2.8, 0);
                sprite.visible = false;
                this.group.add(sprite);
                this.thoughtSprite = sprite;
            }

            updateThoughtTexture(text) {
                const ctx = this.thoughtCtx;
                ctx.clearRect(0, 0, 128, 128);
                
                // Bubble background
                ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
                ctx.beginPath();
                ctx.arc(64, 64, 50, 0, Math.PI * 2);
                ctx.fill();
                ctx.lineWidth = 6;
                ctx.strokeStyle = '#0f172a';
                ctx.stroke();

                // Text / Icon
                ctx.font = 'bold 54px sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(text, 64, 64);

                this.thoughtSprite.material.map.needsUpdate = true;
                this.thoughtSprite.visible = true;
            }

            update(delta, time) {
                // Hunger decay over time
                if (gameState.timeOfDay !== 'night') {
                    this.hunger -= delta * 0.3;
                    if (this.hunger < 0) this.hunger = 0;
                }

                // Nighttime logic: animals go to sleep
                if (gameState.timeOfDay === 'night') {
                    this.isSleeping = true;
                } else {
                    if (this.isSleeping && this.hunger > 30) {
                        this.isSleeping = false;
                    }
                }

                if (this.isSleeping) {
                    // Sleeping pose: lower body, tilt head
                    this.group.position.y = THREE.MathUtils.lerp(this.group.position.y, -0.2, delta * 3);
                    this.bodyParts.head.rotation.x = 0.4;
                    this.updateThoughtTexture('💤');
                    return;
                } else {
                    this.group.position.y = THREE.MathUtils.lerp(this.group.position.y, 0, delta * 3);
                    this.bodyParts.head.rotation.x = 0;
                }

                // Hunger check
                if (this.hunger < 30) {
                    this.updateThoughtTexture('🌾');
                } else {
                    this.thoughtSprite.visible = false;
                }

                // Movement & idle bouncing
                this.moveTimer -= delta;
                if (this.moveTimer <= 0) {
                    this.moveTimer = 4 + Math.random() * 6;
                    const angle = Math.random() * Math.PI * 2;
                    const dist = 2 + Math.random() * 5;
                    const nx = Math.cos(angle) * dist;
                    const nz = Math.sin(angle) * dist;
                    if (Math.hypot(nx, nz) < 14) {
                        this.targetPos.set(nx, 0, nz);
                    }
                }

                // Move towards target
                const currentPos = new THREE.Vector3(this.group.position.x, 0, this.group.position.z);
                if (currentPos.distanceTo(this.targetPos) > 0.5) {
                    this.group.lookAt(this.targetPos.x, this.group.position.y, this.targetPos.z);
                    this.group.translateZ(delta * 1.5);
                    
                    // Bouncing walk animation
                    const bounce = Math.sin(time * this.bounceSpeed) * 0.15;
                    this.bodyParts.body.position.y = 1 + Math.abs(bounce);
                } else {
                    this.bodyParts.body.position.y = THREE.MathUtils.lerp(this.bodyParts.body.position.y, 1, delta * 5);
                }
            }

            feed() {
                if (this.hunger < 100) {
                    this.hunger = 100;
                    this.isSleeping = false;
                    this.thoughtSprite.visible = false;
                    soundEngine.playEat();
                    spawnFloater(this.group.position.x, 2.5, this.group.position.z, '+100% Full!', '#4ade80');
                    return true;
                }
                return false;
            }
        }

        function spawnAnimal(type, x, z) {
            const animal = new ChibiAnimal(type, x, z);
            gameState.animals.push(animal);
        }

        // --- INTERACTION & CLICK HARVESTING ---
        function onPointerDown(event) {
            if (document.getElementById('main-menu').style.display !== 'none') return;

            mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

            raycaster.setFromCamera(mouse, camera);
            
            // Check animal clicks
            const animalMeshes = gameState.animals.map(a => a.group);
            const intersects = raycaster.intersectObjects(animalMeshes, true);

            if (intersects.length > 0) {
                let hitGroup = intersects[0].object;
                while (hitGroup.parent && !gameState.animals.some(a => a.group === hitGroup)) {
                    hitGroup = hitGroup.parent;
                }
                const animal = gameState.animals.find(a => a.group === hitGroup);
                if (animal) {
                    if (animal.hunger < 30) {
                        showNotification('This animal is hungry! Feed it with 🌾 Feed.');
                    } else {
                        // Harvest gold!
                        gameState.gold += 15;
                        gameState.score += 10;
                        updateHUD();
                        soundEngine.playCoin();
                        spawnFloater(animal.group.position.x, 3, animal.group.position.z, '+15 🪙', '#facc15');
                        
                        // Happy jump scale animation
                        animal.group.scale.y = 1.2;
                        setTimeout(() => { animal.group.scale.y = 1; }, 200);
                    }
                }
            }
        }

        // --- FLOATING TEXT PARTICLES ---
        function spawnFloater(x, y, z, text, color) {
            const div = document.createElement('div');
            div.className = 'absolute font-extrabold text-lg pointer-events-none transition-all duration-1000 transform -translate-x-1/2 -translate-y-1/2 z-30 drop-shadow-lg';
            div.style.color = color;
            div.innerText = text;
            document.body.appendChild(div);

            // Project 3D to 2D screen coords
            const vector = new THREE.Vector3(x, y, z);
            vector.project(camera);
            const cx = (vector.x * 0.5 + 0.5) * window.innerWidth;
            const cy = (-(vector.y * 0.5) + 0.5) * window.innerHeight;
            div.style.left = `${cx}px`;
            div.style.top = `${cy}px`;

            setTimeout(() => {
                div.style.transform = `translate(-50%, -80px) scale(1.2)`;
                div.style.opacity = '0';
            }, 50);

            setTimeout(() => {
                div.remove();
            }, 1050);
        }

        // --- GAME LOOP & DYNAMIC TIME / WEATHER ---
        function animate() {
            requestAnimationFrame(animate);
            const delta = clock.getDelta();
            const time = clock.getElapsedTime();

            // Time Cycle progression (day-night cycle)
            gameState.timeValue += delta * 0.005; // complete cycle every ~200 seconds
            if (gameState.timeValue > 1) gameState.timeValue = 0;

            updateDayNightCycle(gameState.timeValue);

            // Cloud animation
            if (window.clouds) {
                window.clouds.forEach(cloud => {
                    cloud.position.x += cloud.userData.speed;
                    if (cloud.position.x > 25) cloud.position.x = -25;
                });
            }

            // Rain animation
            if (gameState.isRaining && rainParticles) {
                const positions = rainGeo.attributes.position.array;
                for (let i = 1; i < positions.length; i += 3) {
                    positions[i] -= 0.8;
                    if (positions[i] < 0) positions[i] = 25;
                }
                rainGeo.attributes.position.needsUpdate = true;
            }

            // Update Animals
            gameState.animals.forEach(animal => animal.update(delta, time));

            renderer.render(scene, camera);
        }

        function updateDayNightCycle(val) {
            // val ranges from 0 to 1
            // 0.0 - 0.25: Morning
            // 0.25 - 0.5: Noon
            // 0.5 - 0.75: Evening
            // 0.75 - 1.0: Night

            let timeOfDay = 'morning';
            let icon = '🌅';
            let labelText = 'Morning';
            let timeStr = '07:00 AM';

            if (val >= 0.25 && val < 0.5) {
                timeOfDay = 'noon';
                icon = '☀️';
                labelText = 'Noon';
                timeStr = '12:00 PM';
            } else if (val >= 0.5 && val < 0.75) {
                timeOfDay = 'evening';
                icon = '🌇';
                labelText = 'Evening';
                timeStr = '05:30 PM';
            } else if (val >= 0.75 || val < 0.1) {
                timeOfDay = 'night';
                icon = '🌙';
                labelText = 'Night';
                timeStr = '11:00 PM';
            }

            gameState.timeOfDay = timeOfDay;

            // Update HUD text if changed
            document.getElementById('time-icon').innerText = icon;
            document.getElementById('time-label').innerText = labelText;
            document.getElementById('clock-display').innerText = timeStr;

            // Smooth lighting / sky transitions based on timeOfDay
            if (timeOfDay === 'morning') {
                scene.background.lerp(new THREE.Color(0xfef08a), 0.05);
                scene.fog.color.lerp(new THREE.Color(0xfef08a), 0.05);
                dirLight.color.setHex(0xfef3c7);
                dirLight.intensity = 1.0;
                ambientLight.intensity = 0.6;
            } else if (timeOfDay === 'noon') {
                scene.background.lerp(new THREE.Color(0xdbeafe), 0.05);
                scene.fog.color.lerp(new THREE.Color(0xdbeafe), 0.05);
                dirLight.color.setHex(0xffffff);
                dirLight.intensity = 1.4;
                ambientLight.intensity = 0.8;
            } else if (timeOfDay === 'evening') {
                scene.background.lerp(new THREE.Color(0xfdb462), 0.05);
                scene.fog.color.lerp(new THREE.Color(0xfdb462), 0.05);
                dirLight.color.setHex(0xf97316);
                dirLight.intensity = 0.9;
                ambientLight.intensity = 0.5;
            } else if (timeOfDay === 'night') {
                scene.background.lerp(new THREE.Color(0x090d16), 0.05);
                scene.fog.color.lerp(new THREE.Color(0x090d16), 0.05);
                dirLight.color.setHex(0x818cf8);
                dirLight.intensity = 0.3;
                ambientLight.intensity = 0.2;
            }
        }

        // --- UI & CONTROLS ACTIONS ---
        function startGame() {
            soundEngine.init();
            soundEngine.startBGM();
            soundEngine.playClick();

            document.getElementById('main-menu').style.display = 'none';
            document.getElementById('game-ui').classList.remove('hidden');

            showNotification('Welcome to your 3D Dream Farm! Click animals to harvest gold.');
        }

        function setTimePreset(preset) {
            soundEngine.playClick();
            if (preset === 'morning') gameState.timeValue = 0.1;
            else if (preset === 'noon') gameState.timeValue = 0.35;
            else if (preset === 'evening') gameState.timeValue = 0.6;
            else if (preset === 'night') gameState.timeValue = 0.85;
            showNotification(`Time set to ${preset.toUpperCase()}`);
        }

        function toggleRain() {
            soundEngine.playClick();
            gameState.isRaining = !gameState.isRaining;
            rainParticles.visible = gameState.isRaining;
            
            const btn = document.getElementById('rain-toggle-btn');
            const weatherIcon = document.getElementById('weather-icon');
            const weatherLabel = document.getElementById('weather-label');

            if (gameState.isRaining) {
                btn.classList.add('bg-sky-500/50');
                weatherIcon.innerText = '🌧️';
                weatherLabel.innerText = 'Rainy';
                soundEngine.playThunder();
                showNotification('Rain started! Crops are watering.');
            } else {
                btn.classList.remove('bg-sky-500/50');
                weatherIcon.innerText = '☀️';
                weatherLabel.innerText = 'Sunny';
                showNotification('The weather cleared up!');
            }
        }

        function buyFood(amount, cost) {
            soundEngine.playClick();
            if (gameState.gold >= cost) {
                gameState.gold -= cost;
                gameState.food += amount;
                updateHUD();
                soundEngine.playCoin();
                showNotification(`Purchased ${amount} feed bags!`);
            } else {
                showModal('Not Enough Gold', 'Earn more gold by harvesting happy animals!');
            }
        }

        function feedAllAnimals() {
            soundEngine.playClick();
            if (gameState.food <= 0) {
                showModal('Out of Feed!', 'Buy more feed bags from the shop bar below.');
                return;
            }
            let fedCount = 0;
            gameState.animals.forEach(a => {
                if (a.hunger < 100 && gameState.food > 0) {
                    if (a.feed()) {
                        gameState.food--;
                        fedCount++;
                    }
                }
            });
            updateHUD();
            if (fedCount > 0) {
                showNotification(`Fed ${fedCount} animals successfully! 🥕`);
            } else {
                showNotification('All animals are already full and happy! ✨');
            }
        }

        function spawnRandomAnimal() {
            soundEngine.playClick();
            if (gameState.gold < 100) {
                showModal('Not Enough Gold', 'Adopt a new pet for 100🪙. Harvest more gold first!');
                return;
            }
            gameState.gold -= 100;
            updateHUD();
            soundEngine.playCoin();

            const types = ['sheep', 'cow', 'pig', 'chicken'];
            const chosen = types[Math.floor(Math.random() * types.length)];
            const angle = Math.random() * Math.PI * 2;
            const dist = 3 + Math.random() * 4;
            spawnAnimal(chosen, Math.cos(angle) * dist, Math.sin(angle) * dist);
            showNotification(`Successfully adopted a cute chibi ${chosen}! 🎉`);
        }

        function updateHUD() {
            document.getElementById('gold-display').innerText = gameState.gold;
            document.getElementById('food-display').innerText = gameState.food;
            document.getElementById('score-display').innerText = gameState.score;
        }

        function toggleSound() {
            soundEngine.enabled = !soundEngine.enabled;
            const btn = document.getElementById('sound-btn');
            if (soundEngine.enabled) {
                btn.innerText = '🔊';
                soundEngine.startBGM();
                showNotification('Sound Enabled');
            } else {
                btn.innerText = '🔇';
                soundEngine.stopBGM();
                showNotification('Sound Muted');
            }
        }

        function showNotification(msg) {
            const banner = document.getElementById('notification-banner');
            banner.innerText = msg;
            banner.style.opacity = '1';
            banner.style.transform = 'translateY(0)';
            setTimeout(() => {
                banner.style.opacity = '0';
                banner.style.transform = 'translateY(-16px)';
            }, 3000);
        }

        function showModal(title, message) {
            document.getElementById('modal-title').innerText = title;
            document.getElementById('modal-message').innerText = message;
            document.getElementById('modal-box').classList.remove('hidden');
        }

        function closeModal() {
            soundEngine.playClick();
            document.getElementById('modal-box').classList.add('hidden');
        }

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        // Initialize on load
        window.onload = function() {
            init3D();
            animate();
        };
    </script>
</body>
</html>
