import pygame
import time
import random

pygame.init()
pygame.mixer.init()

# Fullscreen window
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = window.get_size()

# ---------- MUSIC ----------
# Soothing music
pygame.mixer.music.load(r"c:\Users\panka\Downloads\soothing-sleep-197943.mp3")
pygame.mixer.music.play()
time.sleep(5)

# Scary music
pygame.mixer.music.load(r"c:\Users\panka\Downloads\horror-scary-music-376357.mp3")
pygame.mixer.music.play(-1)  # loop scary music

# ---------- LOAD & SCALE IMAGES ----------
img1 = pygame.image.load(
    r"c:\Users\panka\OneDrive\Pictures\Screenshots\Screenshot 2026-01-18 152013.png"
)
img2 = pygame.image.load(
    r"c:\Users\panka\OneDrive\Pictures\Screenshots\Screenshot 2026-01-18 151156.png"
)
img3 = pygame.image.load(
    r"c:\Users\panka\OneDrive\Pictures\Screenshots\Screenshot 2026-01-18 152240.png")
img4 = pygame.image.load(
    r"c:\Users\panka\OneDrive\Pictures\Screenshots\Screenshot 2026-01-18 151049.png")
img1 = pygame.transform.scale(img1, (screen_width, screen_height))
img2 = pygame.transform.scale(img2, (screen_width, screen_height))
img3 = pygame.transform.scale(img3, (screen_width, screen_height))
img4 = pygame.transform.scale(img3, (screen_width, screen_height))

images = [img1, img2, img3,img4]

# ---------- HORROR LOOP ----------
clock = pygame.time.Clock()
running = True
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.QUIT:
            running = False

    # Random image flicker
    window.blit(random.choice(images), (0, 0))
    pygame.display.update()

    time.sleep(0.15)  # flicker speed
    clock.tick(40)

    # auto exit after 10 seconds
    if time.time() - start_time > 7:
        running = False

pygame.quit()
