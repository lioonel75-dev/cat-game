from PIL import Image, ImageDraw
import os

# Buat folder assets jika belum ada
os.makedirs("assets/sprites", exist_ok=True)

def create_player_sprite():
    # Cat colors
    cat_body = (255, 140, 60)  # Orange cat
    cat_dark = (200, 100, 40)  # Darker orange
    cat_light = (255, 180, 120)  # Lighter orange
    
    # Player idle - Kucing duduk
    img = Image.new('RGBA', (50, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Kepala kucing (bulat)
    draw.ellipse([12, 8, 38, 34], fill=cat_body)
    
    # Telinga kiri
    draw.polygon([(14, 8), (18, 8), (16, 2)], fill=cat_body)
    draw.polygon([(15, 7), (17, 7), (16, 3)], fill=(255, 200, 200))
    
    # Telinga kanan
    draw.polygon([(32, 8), (36, 8), (34, 2)], fill=cat_body)
    draw.polygon([(33, 7), (35, 7), (34, 3)], fill=(255, 200, 200))
    
    # Mata
    draw.ellipse([18, 16, 22, 22], fill=(50, 50, 50))
    draw.ellipse([28, 16, 32, 22], fill=(50, 50, 50))
    draw.ellipse([19, 17, 21, 20], fill=(100, 255, 100))  # Pupil hijau
    draw.ellipse([29, 17, 31, 20], fill=(100, 255, 100))
    
    # Hidung
    draw.polygon([(25, 24), (23, 26), (27, 26)], fill=(255, 150, 150))
    
    # Kumis
    draw.line([(12, 22), (5, 20)], fill=(0, 0, 0), width=1)
    draw.line([(12, 24), (5, 24)], fill=(0, 0, 0), width=1)
    draw.line([(38, 22), (45, 20)], fill=(0, 0, 0), width=1)
    draw.line([(38, 24), (45, 24)], fill=(0, 0, 0), width=1)
    
    # Badan
    draw.ellipse([15, 30, 35, 50], fill=cat_body)
    
    # Kaki depan
    draw.rectangle([18, 45, 23, 58], fill=cat_dark)
    draw.rectangle([27, 45, 32, 58], fill=cat_dark)
    
    # Ekor
    draw.ellipse([32, 38, 45, 44], fill=cat_body)
    
    img.save("assets/sprites/player_idle.png")
    
    # Player running frame 1 - Kucing lari
    img = Image.new('RGBA', (50, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Kepala
    draw.ellipse([12, 6, 38, 32], fill=cat_body)
    draw.polygon([(14, 6), (18, 6), (16, 0)], fill=cat_body)
    draw.polygon([(32, 6), (36, 6), (34, 0)], fill=cat_body)
    draw.ellipse([18, 14, 22, 20], fill=(50, 50, 50))
    draw.ellipse([28, 14, 32, 20], fill=(50, 50, 50))
    draw.polygon([(25, 22), (23, 24), (27, 24)], fill=(255, 150, 150))
    
    # Kumis
    draw.line([(12, 20), (5, 18)], fill=(0, 0, 0), width=1)
    draw.line([(38, 20), (45, 18)], fill=(0, 0, 0), width=1)
    
    # Badan
    draw.ellipse([15, 28, 35, 48], fill=cat_body)
    
    # Kaki (posisi lari 1)
    draw.rectangle([16, 43, 21, 56], fill=cat_dark)
    draw.rectangle([29, 45, 34, 58], fill=cat_dark)
    
    # Ekor (naik)
    draw.arc([30, 25, 48, 40], 0, 180, fill=cat_body, width=6)
    
    img.save("assets/sprites/player_run1.png")
    
    # Player running frame 2 - Kucing lari
    img = Image.new('RGBA', (50, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Kepala
    draw.ellipse([12, 6, 38, 32], fill=cat_body)
    draw.polygon([(14, 6), (18, 6), (16, 0)], fill=cat_body)
    draw.polygon([(32, 6), (36, 6), (34, 0)], fill=cat_body)
    draw.ellipse([18, 14, 22, 20], fill=(50, 50, 50))
    draw.ellipse([28, 14, 32, 20], fill=(50, 50, 50))
    draw.polygon([(25, 22), (23, 24), (27, 24)], fill=(255, 150, 150))
    
    # Kumis
    draw.line([(12, 20), (5, 18)], fill=(0, 0, 0), width=1)
    draw.line([(38, 20), (45, 18)], fill=(0, 0, 0), width=1)
    
    # Badan
    draw.ellipse([15, 28, 35, 48], fill=cat_body)
    
    # Kaki (posisi lari 2)
    draw.rectangle([20, 45, 25, 58], fill=cat_dark)
    draw.rectangle([25, 43, 30, 56], fill=cat_dark)
    
    # Ekor (turun)
    draw.arc([28, 35, 46, 50], 180, 360, fill=cat_body, width=6)
    
    img.save("assets/sprites/player_run2.png")
    
    # Player jumping - Kucing melompat
    img = Image.new('RGBA', (50, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Kepala (lebih tinggi)
    draw.ellipse([12, 4, 38, 30], fill=cat_body)
    draw.polygon([(14, 4), (18, 4), (16, -2)], fill=cat_body)
    draw.polygon([(32, 4), (36, 4), (34, -2)], fill=cat_body)
    draw.ellipse([18, 12, 22, 18], fill=(50, 50, 50))
    draw.ellipse([28, 12, 32, 18], fill=(50, 50, 50))
    draw.polygon([(25, 20), (23, 22), (27, 22)], fill=(255, 150, 150))
    
    # Kumis
    draw.line([(12, 18), (5, 16)], fill=(0, 0, 0), width=1)
    draw.line([(38, 18), (45, 16)], fill=(0, 0, 0), width=1)
    
    # Badan (stretched)
    draw.ellipse([15, 26, 35, 46], fill=cat_body)
    
    # Kaki (extended jumping pose)
    draw.rectangle([14, 43, 19, 54], fill=cat_dark)
    draw.rectangle([31, 45, 36, 56], fill=cat_dark)
    
    # Ekor (lurus kebelakang)
    draw.ellipse([32, 32, 48, 38], fill=cat_body)
    
    img.save("assets/sprites/player_jump.png")
    
    print("✓ Player sprites created (Cat!)")

def create_enemy_sprite():
    # Enemy idle
    img = Image.new('RGBA', (50, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Kepala
    draw.ellipse([15, 5, 35, 25], fill=(200, 150, 100))
    
    # Badan
    draw.rectangle([18, 25, 32, 45], fill=(150, 0, 0))
    
    # Tangan
    draw.rectangle([10, 28, 18, 40], fill=(200, 150, 100))
    draw.rectangle([32, 28, 40, 40], fill=(200, 150, 100))
    
    # Kaki
    draw.rectangle([18, 45, 24, 58], fill=(80, 80, 80))
    draw.rectangle([26, 45, 32, 58], fill=(80, 80, 80))
    
    # Senjata
    draw.rectangle([3, 30, 15, 33], fill=(80, 80, 80))
    
    img.save("assets/sprites/enemy_idle.png")
    
    # Enemy walking
    img = Image.new('RGBA', (50, 60), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([15, 5, 35, 25], fill=(200, 150, 100))
    draw.rectangle([18, 25, 32, 45], fill=(150, 0, 0))
    draw.rectangle([10, 30, 18, 42], fill=(200, 150, 100))
    draw.rectangle([32, 26, 40, 38], fill=(200, 150, 100))
    draw.rectangle([16, 45, 22, 58], fill=(80, 80, 80))
    draw.rectangle([28, 45, 34, 56], fill=(80, 80, 80))
    draw.rectangle([3, 30, 15, 33], fill=(80, 80, 80))
    img.save("assets/sprites/enemy_walk.png")
    
    print("✓ Enemy sprites created")

def create_bullet_sprite():
    # Peluru player (biru)
    img = Image.new('RGBA', (10, 5), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([0, 0, 10, 5], fill=(255, 255, 0))
    img.save("assets/sprites/bullet_player.png")
    
    # Peluru enemy (merah)
    img = Image.new('RGBA', (10, 5), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([0, 0, 10, 5], fill=(255, 100, 0))
    img.save("assets/sprites/bullet_enemy.png")
    
    print("✓ Bullet sprites created")

def create_platform_sprite():
    img = Image.new('RGBA', (100, 30), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Platform tanah
    draw.rectangle([0, 0, 100, 30], fill=(100, 70, 50))
    # Grass texture
    for i in range(0, 100, 10):
        draw.rectangle([i, 0, i+8, 5], fill=(50, 150, 50))
    
    img.save("assets/sprites/platform.png")
    
    # Platform tembok
    img = Image.new('RGBA', (50, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 50, 100], fill=(120, 120, 120))
    # Brick texture
    for y in range(0, 100, 20):
        for x in range(0, 50, 25):
            draw.rectangle([x, y, x+23, y+18], outline=(80, 80, 80))
    
    img.save("assets/sprites/wall.png")
    
    print("✓ Platform sprites created")

def create_background_sprite():
    img = Image.new('RGBA', (800, 600), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Sky gradient
    for y in range(400):
        color = int(135 + (y / 400) * 120)
        draw.line([(0, y), (800, y)], fill=(135, 206, color))
    
    # Ground
    draw.rectangle([0, 400, 800, 600], fill=(80, 120, 50))
    
    # Mountains di background
    draw.polygon([(100, 400), (200, 250), (300, 400)], fill=(100, 100, 100))
    draw.polygon([(250, 400), (350, 200), (450, 400)], fill=(120, 120, 120))
    draw.polygon([(400, 400), (520, 280), (640, 400)], fill=(90, 90, 90))
    
    img.save("assets/sprites/background.png")
    
    print("✓ Background sprite created")

def create_explosion_sprite():
    colors = [(255, 255, 0), (255, 150, 0), (255, 50, 0), (150, 150, 150)]
    
    for i, color in enumerate(colors):
        img = Image.new('RGBA', (40, 40), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        size = 10 + i * 8
        offset = (40 - size) // 2
        draw.ellipse([offset, offset, offset + size, offset + size], fill=color)
        
        img.save(f"assets/sprites/explosion_{i}.png")
    
    print("✓ Explosion sprites created")

if __name__ == "__main__":
    print("Generating sprites...")
    create_player_sprite()
    create_enemy_sprite()
    create_bullet_sprite()
    create_platform_sprite()
    create_background_sprite()
    create_explosion_sprite()
    print("\n✅ All sprites generated successfully!")
    print("Sprites saved to: assets/sprites/")
