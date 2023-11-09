#!/usr/bin/env python3
import time
import pygame
import textwrap
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)


# Define a function to read text blocks from a file
def read_text_blocks(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            text_blocks = content.split('\n\n')
        return text_blocks
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Initialize pygame and create a fullscreen window
def init_pygame():
    pygame.init()
    pygame.display.init()
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption('Text Blocks Display')
    pygame.mouse.set_visible(False) # Hide the mouse cursor
    return screen

# Display a block of text on the screen
def display_text(screen, text):
    screen.fill((255, 255, 255))  # White background
    lines = text.split('\n')
    
    # Load fonts
    font_title = pygame.font.SysFont('arial', 72, bold=True)
    font_artist = pygame.font.SysFont('arial', 36, bold=True)
    font_rest = pygame.font.SysFont('arial', 24)

    text_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

    # Starting position on the screen
    top_padding = 40
    current_height = top_padding
    wrap_width = 93

    # Wrap and render the title (first line)
    if lines:
        title_surface = font_title.render(lines[0], True, (0, 0, 0))
        screen.blit(title_surface, (20, current_height))
        current_height += title_surface.get_height() + 20

    # Wrap and render the artist (second line)
    if len(lines) > 1:
        artist_surface = font_artist.render(lines[1], True, (0, 0, 0))
        screen.blit(artist_surface, (20, current_height))
        current_height += artist_surface.get_height() + 30

    # Wrap and render the rest of the text
    for line in lines[2:]:
        wrapped_lines = textwrap.wrap(line, width=wrap_width)  # Wrap the text
        for wrapped_line in wrapped_lines:
            rest_surface = font_rest.render(wrapped_line, True, (0, 0, 0))
            screen.blit(rest_surface, (20, current_height))
            current_height += rest_surface.get_height() + 5

    # Flip the text_surface vertically
    flipped_surface = pygame.transform.flip(text)surface, False, True)

    # Blit the flipped surface onto the screen

    screen.blit(flipped_surface, (0,0))

    pygame.display.flip()  # Update the display

# Display the text blocks in an infinite loop
def display_text_blocks(text_blocks):
    screen = init_pygame()
    running = True
    while running:
        for block in text_blocks:
            display_text(screen, block)  # Display the block
            
            # Instead of sleeping for 10 seconds, check for events every 0.5 seconds
            for _ in range(20):  # 20 times 5 equals 100 seconds
                time.sleep(5)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break  # Exit the inner loop
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:  # Quit if 'q' is pressed
                            running = False
                            break  # Exit the inner loop
                if not running:
                    break  # Exit the sleep loop if the flag is set to False
            
            if not running:
                break  # Exit the text block loop if the flag is set to False

    pygame.quit()



# Main program
if __name__ == "__main__":
    # The path to the file containing the text blocks
    file_path = 'textBlocks.txt'

    # Read the text blocks from the file
    text_blocks = read_text_blocks(file_path)

    # Display each text block in a loop if the file was read successfully
    if text_blocks:
        display_text_blocks(text_blocks)
    else:
        print("No text blocks to display.")
