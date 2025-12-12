# Cat Climber 🐱 - Vertical Platformer Game

Game platformer vertical yang menggemaskan dengan karakter kucing, dibuat menggunakan Python dan Pygame.

**Objective:** Bantu kucing memanjat ke puncak sampai mencapai bendera finish sambil melawan musuh!

## 📋 Requirements

- Python 3.7 atau lebih tinggi
- Pygame 2.5.2
- Pillow (PIL) 10.1.0
- Git (untuk clone repository)

## 🚀 Cara Install dan Menjalankan Game

### Step 1: Clone Repository

Clone project dari GitHub atau copy folder ini:

```bash
# Jika dari GitHub
git clone <repository-url>
cd cat-game

# Atau jika sudah punya folder
cd /path/to/cat-game
```

### Step 2: Buat Virtual Environment (Opsional tapi Disarankan)

```bash
# Membuat virtual environment
python3 -m venv .venv

# Aktivasi virtual environment
# Di Linux/Mac:
source .venv/bin/activate

# Di Windows:
.venv\Scripts\activate
```

### Step 3: Install Dependencies

Install semua library yang dibutuhkan:

```bash
# Install dari requirements.txt
pip install -r requirements.txt

# Atau install manual
pip install pygame==2.5.2 pillow==10.1.0
```

### Step 4: Generate Sprite Assets

Sebelum menjalankan game, generate dulu semua sprite dummy:

```bash
python generate_sprites.py
```

Output yang akan muncul:
```
Generating sprites...
✓ Player sprites created
✓ Enemy sprites created
✓ Bullet sprites created
✓ Platform sprites created
✓ Background sprite created
✓ Explosion sprites created

✅ All sprites generated successfully!
Sprites saved to: assets/sprites/
```

### Step 5: Jalankan Game! 🎮

```bash
python main.py
```

Game window akan terbuka dan Anda siap bermain!

## 🎮 Cara Bermain

### 🎯 Objective (Tujuan Game):
- **PANJAT KE ATAS** sampai mencapai bendera GOAL di puncak!
- Kalahkan musuh yang menghalangi jalan
- Hindari tembakan musuh
- Jaga health bar agar tidak habis
- Jangan jatuh ke bawah!

### ⌨️ Kontrol:
- **Gerak Kiri/Kanan**: `A` / `D` atau `Arrow Left` / `Arrow Right`
- **Lompat**: `W` / `Space` / `Arrow Up` - **DOUBLE JUMP!** (Tekan 2x untuk lompat ganda)
- **Tembak**: `X` atau `Left Ctrl`
- **Restart**: `R` (setelah game over atau menang)
- **Keluar**: `ESC`

### 💡 Tips Bermain:
1. **Gunakan DOUBLE JUMP!** - Tekan jump 2x di udara untuk mencapai platform tinggi!
2. **Lompat dari platform ke platform** - Platform zigzag kiri-kanan
3. **Tembak musuh dari jauh** - Lebih aman daripada dekat
4. **Kombinasi lompat + gerak** - Running jump untuk jarak lebih jauh
5. **Perhatikan health bar** - Ada di pojok kiri atas
6. **Lihat progress bar** - Menunjukkan seberapa dekat Anda dengan puncak
7. **Waspadai musuh yang menembak** - Mereka akan menembak jika Anda dalam jangkauan

### 📊 Game UI:
- **Health Bar (Hijau)**: Pojok kiri atas - HP Anda
- **Score**: Pojok kanan atas - Skor Anda (+100 per musuh, +1000 untuk finish)
- **Enemies**: Jumlah musuh yang masih hidup
- **Progress**: Persentase seberapa tinggi Anda sudah naik (0% = bawah, 100% = puncak)

### 🏆 Cara Menang:
Capai bendera GOAL kuning di puncak! Kamera akan mengikuti karakter Anda saat naik.

## 📁 Struktur Project

```
cat-game/
├── assets/
│   ├── sprites/          # Sprite dummy yang di-generate (PNG files)
│   │   ├── player_*.png
│   │   ├── enemy_*.png
│   │   ├── bullet_*.png
│   │   ├── platform.png
│   │   ├── background.png
│   │   └── explosion_*.png
│   └── sounds/           # (Belum diimplementasi)
├── src/
│   ├── player.py         # Class untuk karakter pemain
│   ├── enemy.py          # Class untuk musuh dengan AI
│   ├── bullet.py         # Projectile system
│   ├── platform.py       # Platform dan level
│   ├── explosion.py      # Efek ledakan
│   └── goal.py           # Finish line / goal
├── .venv/                # Virtual environment (after setup)
├── generate_sprites.py   # Script untuk generate sprite dummy
├── main.py               # File utama game (jalankan ini!)
├── requirements.txt      # Daftar dependencies
└── README.md             # Dokumentasi ini
```

## 🎨 Fitur Game

- ✅ **Vertical Platforming** - Panjat ke atas setinggi 2400 pixels!
- ✅ **DOUBLE JUMP!** 🐱💨 - Tekan jump 2x untuk lompat ganda di udara!
- ✅ **Cat Character** - Player adalah kucing lucu dengan animasi
- ✅ **Camera System** - Kamera smooth follow player
- ✅ **Player dengan animasi** (idle, run, jump) - Kucing dengan telinga & ekor
- ✅ **22 Enemy** tersebar di berbagai ketinggian dengan AI (patrol, chase, shoot)
- ✅ **Sistem tembakan** - Player dan enemy bisa tembak-tembakan
- ✅ **27 Platform** - Level design zigzag vertikal
- ✅ **Efek ledakan** - Visual feedback saat hit
- ✅ **Health bar & UI lengkap** - Health, score, enemy count, progress bar
- ✅ **Goal system** - Bendera finish di puncak dengan animasi
- ✅ **Home/Welcome screen** - Menu awal sebelum bermain
- ✅ **Game over & victory screen** - Dengan opsi restart atau back to menu
- ✅ **Sprite dummy auto-generated** - Tidak perlu asset eksternal!

## 🔧 Kustomisasi & Modifikasi

Mau memodifikasi game? Edit parameter di file-file ini:

### main.py
- `SCREEN_WIDTH`, `SCREEN_HEIGHT`: Ukuran window game (default: 1200x600)
- `LEVEL_HEIGHT`: Tinggi total level (default: 2400)
- `FPS`: Frame rate game (default: 60)
- Method `create_level()`: Ubah posisi platform dan musuh
- `self.camera_y`: Sesuaikan camera smoothness

### src/player.py
- `self.speed`: Kecepatan gerak (default: 5)
- `self.jump_power`: Tinggi lompatan (default: -15)
- `self.gravity`: Gravitasi (default: 0.8)
- `self.health`: HP player (default: 100)
- `self.shoot_delay`: Cooldown tembakan (default: 10 frames)
- `self.max_jumps`: Jumlah maksimal jump (default: 2 = double jump)

### src/enemy.py
- `self.detection_range`: Jarak deteksi player (default: 300)
- `self.shoot_range`: Jarak mulai menembak (default: 250)
- `self.health`: HP musuh (default: 50)
- `self.vel_x`: Kecepatan gerak musuh (default: 2)

### src/bullet.py
- `self.speed`: Kecepatan peluru (default: 10)
- `self.damage`: Damage per bullet (player: 25, enemy: 10)

### generate_sprites.py
- Ubah warna, ukuran, atau style sprite dummy
- Tambah sprite baru sesuai kebutuhan

## 🐛 Troubleshooting

### Error: `No module named 'pygame'` atau `No module named 'PIL'`
**Solusi:**
```bash
# Pastikan virtual environment aktif
pip install -r requirements.txt

# Atau install manual
pip install pygame pillow
```

### Error: `FileNotFoundError: [Errno 2] No such file or directory: 'assets/sprites/player_idle.png'`
**Solusi:** Anda belum generate sprite!
```bash
python generate_sprites.py
```

### Game window tidak muncul / langsung close
**Solusi:**
1. Pastikan semua dependencies ter-install
2. Cek apakah ada error di terminal
3. Pastikan Python version 3.7+
4. Try jalankan dari terminal, bukan IDE

### Game lag atau patah-patah
**Solusi:**
1. Tutup aplikasi lain yang berat
2. Kurangi FPS di `main.py` (ubah `FPS = 60` jadi `FPS = 30`)
3. Update driver graphics card

### Player tidak bisa lompat tinggi
**Solusi:** Ini by design! Game ini butuh timing yang tepat. Tips:
- Lompat dari ujung platform
- Gunakan running jump (gerak + lompat)
- Cari platform yang lebih dekat

### Sprite terlihat jelek / kotak-kotak
**Catatan:** Ini adalah sprite dummy placeholder yang disengaja sederhana. Anda bisa:
1. Mengganti dengan sprite profesional di folder `assets/sprites/`
2. Edit `generate_sprites.py` untuk improve drawing
3. Gunakan sprite dari asset pack external

## 📝 Catatan Penting

- ✨ **Semua sprite adalah placeholder** yang di-generate otomatis menggunakan PIL/Pillow
- 🎨 **Anda bisa mengganti sprite** dengan file PNG yang lebih bagus di `assets/sprites/`
- 📚 **Game ini dibuat untuk edukasi** dan pembelajaran game development dengan Pygame
- 🚀 **Feel free to modify** dan kembangkan sesuai kreativitas Anda!

## 🎓 Belajar dari Code Ini

Code ini cocok untuk belajar:
- ✅ Pygame basics (game loop, sprites, events)
- ✅ Platform game mechanics (gravity, collision, jumping)
- ✅ Camera system untuk scrolling vertical
- ✅ Simple AI untuk enemy (state machine)
- ✅ Sprite animation frame-by-frame
- ✅ Collision detection
- ✅ UI rendering (health bar, score, text)
- ✅ Game states (playing, game over, victory)

## 👨‍💻 Development & Modifikasi

### Menambah Fitur Baru:

**1. Tambah Enemy Type Baru:**
- Edit `src/enemy.py`
- Buat subclass dari `Enemy`
- Override method `ai_behavior()` untuk behavior berbeda

**2. Tambah Weapon/Power-up:**
- Buat file baru `src/powerup.py`
- Implementasi collision dengan player
- Tambah efek ke player stats

**3. Buat Level Baru:**
- Edit method `create_level()` di `main.py`
- Ubah posisi platform di array `platforms_data`
- Tambah atau kurangi musuh di `enemy_positions`

**4. Tambah Sound Effects:**
- Install `pygame.mixer`
- Tambah file audio di `assets/sounds/`
- Panggil `pygame.mixer.Sound().play()` saat event

**5. Improve Sprite Graphics:**
- Gunakan sprite sheet dari asset pack
- Edit `generate_sprites.py` untuk drawing lebih detail
- Atau ganti file PNG langsung di `assets/sprites/`

## 📄 License

Free to use for educational purposes. Modify, share, and learn!

## 🤝 Contributing

Punya ide improvement? Feel free to:
1. Fork repository ini
2. Buat fitur baru
3. Submit pull request
4. Atau share ide di issues

## ❓ FAQ

**Q: Apakah bisa multiplayer?**
A: Belum. Tapi bisa ditambahkan dengan implement network library seperti socket atau pygame-network.

**Q: Bisa dijadikan .exe?**
A: Bisa! Gunakan PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

**Q: Apakah perlu internet untuk main?**
A: Tidak! Game ini offline 100%.

**Q: Bisa dijalankan di Android/iOS?**
A: Tidak langsung. Perlu port menggunakan Kivy atau Pygame Subset for Android.

## 🎮 Selamat Bermain!

Terima kasih sudah mencoba game ini! Semoga bermanfaat untuk belajar game development.

**Happy Climbing!** 🧗‍♂️🏔️

---
