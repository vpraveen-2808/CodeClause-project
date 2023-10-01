import pygame
import os
import random
from mutagen.mp3 import MP3

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the Pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")

# Set the path to the directory containing your music files
MUSIC_DIRECTORY = r"C:\Users\hp\Music\music player"

# Store the list of music files
music_files = []

# Load music files from the directory
for file in os.listdir(MUSIC_DIRECTORY):
    if file.endswith(".mp3"):
        music_files.append(os.path.join(MUSIC_DIRECTORY, file))

# Initialize the current music index
current_music_index = 0

# Initialize music control variables
paused = False
shuffle = False
repeat = False

# Load the current music file
pygame.mixer.music.load(music_files[current_music_index])

# Play the music
pygame.mixer.music.play()

# Function to play the next music file
def play_next_song():
    global current_music_index
    if shuffle:
        current_music_index = random.randint(0, len(music_files) - 1)
    else:
        current_music_index = (current_music_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play()

# Load button images with specified dimensions
button_width = 50
button_height = 50
play_image = pygame.transform.scale(pygame.image.load("play.png"), (button_width, button_height))
pause_image = pygame.transform.scale(pygame.image.load("pause.png"), (button_width, button_height))
previous_image = pygame.transform.scale(pygame.image.load("previous.png"), (button_width, button_height))
next_image = pygame.transform.scale(pygame.image.load("next.png"), (button_width, button_height))
shuffle_on_image = pygame.transform.scale(pygame.image.load("shuffle_on.png"), (button_width, button_height))
shuffle_off_image = pygame.transform.scale(pygame.image.load("shuffle_off.png"), (button_width, button_height))
repeat_on_image = pygame.transform.scale(pygame.image.load("repeat_on.png"), (button_width, button_height))
repeat_off_image = pygame.transform.scale(pygame.image.load("repeat_off.png"), (button_width, button_height))
volume_up_image = pygame.transform.scale(pygame.image.load("volume_up.png"), (button_width, button_height))
volume_down_image = pygame.transform.scale(pygame.image.load("volume_down.png"), (button_width, button_height))

# Calculate button positions
play_pos = (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT - button_height - 20)
previous_pos = (play_pos[0] - 100, play_pos[1])
next_pos = (play_pos[0] + 100, play_pos[1])
shuffle_pos = (50, play_pos[1] + 20)
repeat_pos = (150, play_pos[1] + 20)
volume_up_pos = (WINDOW_WIDTH - 150, play_pos[1] + 20)
volume_down_pos = (WINDOW_WIDTH - 50, play_pos[1] + 20)

# ... (the rest of your code remains the same)


# Font settings for song information and duration
font = pygame.font.Font(None, 24)
text_color = (255, 255, 255)
song_info_pos = (50, 400)
duration_bar_pos = (50, 450)
duration_bar_width = WINDOW_WIDTH - 100
duration_bar_height = 10

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if play_pos[0] <= mouse_pos[0] <= play_pos[0] + button_width and play_pos[1] <= mouse_pos[1] <= play_pos[1] + button_height:
                # Toggle play/pause
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            elif previous_pos[0] <= mouse_pos[0] <= previous_pos[0] + button_width and previous_pos[1] <= mouse_pos[1] <= previous_pos[1] + button_height:
                # Play the previous music file
                current_music_index = (current_music_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music_index])
                pygame.mixer.music.play()

            elif next_pos[0] <= mouse_pos[0] <= next_pos[0] + button_width and next_pos[1] <= mouse_pos[1] <= next_pos[1] + button_height:
                # Play the next music file
                play_next_song()

            elif shuffle_pos[0] <= mouse_pos[0] <= shuffle_pos[0] + button_width and shuffle_pos[1] <= mouse_pos[1] <= shuffle_pos[1] + button_height:
                # Toggle shuffle mode
                shuffle = not shuffle

            elif repeat_pos[0] <= mouse_pos[0] <= repeat_pos[0] + button_width and repeat_pos[1] <= mouse_pos[1] <= repeat_pos[1] + button_height:
                # Toggle repeat mode
                repeat = not repeat

            elif volume_up_pos[0] <= mouse_pos[0] <= volume_up_pos[0] + button_width and volume_up_pos[1] <= mouse_pos[1] <= volume_up_pos[1] + button_height:
                # Increase volume
                pygame.mixer.music.set_volume(min(1, pygame.mixer.music.get_volume() + 0.1))

            elif volume_down_pos[0] <= mouse_pos[0] <= volume_down_pos[0] + button_width and volume_down_pos[1] <= mouse_pos[1] <= volume_down_pos[1] + button_height:
                # Decrease volume
                pygame.mixer.music.set_volume(max(0, pygame.mixer.music.get_volume() - 0.1))

    current_time = pygame.mixer.music.get_pos() / 1000
    audio = MP3(music_files[current_music_index])
    total_time = audio.info.length

    song_info_text = f"Playing: {os.path.basename(music_files[current_music_index])}"
    duration_text = f"{int(current_time)}s / {int(total_time)}s"
    song_info_surface = font.render(song_info_text, True, text_color)
    duration_surface = font.render(duration_text, True, text_color)

    duration_bar_width_filled = int((current_time / total_time) * duration_bar_width)

    window.fill((30, 30, 30))
    window.blit(previous_image, previous_pos)
    window.blit(play_image if not paused else pause_image, play_pos)
    window.blit(next_image, next_pos)
    window.blit(shuffle_on_image if shuffle else shuffle_off_image, shuffle_pos)
    window.blit(repeat_on_image if repeat else repeat_off_image, repeat_pos)
    window.blit(volume_up_image, volume_up_pos)
    window.blit(volume_down_image, volume_down_pos)
    window.blit(song_info_surface, song_info_pos)
    window.blit(duration_surface, (WINDOW_WIDTH - 150, 400))
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(duration_bar_pos[0], duration_bar_pos[1], duration_bar_width, duration_bar_height))
    pygame.draw.rect(window, (0, 255, 0), pygame.Rect(duration_bar_pos[0], duration_bar_pos[1], duration_bar_width_filled, duration_bar_height))

    pygame.display.update()

# Quit Pygame
pygame.quit()
