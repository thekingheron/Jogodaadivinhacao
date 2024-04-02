import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da adivinhação")

# Set up the font
FONT = pygame.font.SysFont("Arial", 24)

# Set up the game state
number_to_guess = random.randint(1, 100)
guess = ""
guesses = 0
notification = ""

# Function to draw text on screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if guess.isdigit():
                    guesses += 1
                    if int(guess) < number_to_guess:
                        notification = "O valor é maior do que seu palpite!"
                    elif int(guess) > number_to_guess:
                        notification = "O valor é menor do que seu palpite!"
                    else:
                        notification = "Parabens! Você acertou em " + str(guesses) + " tentativas!"
                        guess = ""
                else:
                    notification = "Inválido!"
                    guess = ""
            elif event.key == pygame.K_BACKSPACE:
                guess = guess[:-1]
            else:
                if event.unicode.isdigit() and len(guess) < 3:
                    guess += str(event.unicode)

    # Update the screen
    screen.fill(WHITE)
    draw_text("Advinhe em que número estou pensando em entre 1 e 100!", FONT, BLACK, screen, 10, 10)
    draw_text("Palpite: " + guess, FONT, BLACK, screen, 10, 50)
    draw_text(notification, FONT, BLACK, screen, 10, 90)

    # Draw input box
    pygame.draw.rect(screen, BLACK, (10, 130, 200, 40), 2)
    pygame.draw.rect(screen, GRAY, (12, 132, 196, 36))

    # Draw buttons
    pygame.draw.rect(screen, BLACK, (250, 130, 100, 40), 2)
    draw_text("Palpite", FONT, BLACK, screen, 260, 140)

    pygame.draw.rect(screen, BLACK, (370, 130, 100, 40), 2)
    draw_text("Resetar", FONT, BLACK, screen, 380, 140)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
