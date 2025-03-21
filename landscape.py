import pygame
import math
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Initialize global variables
BLUE = (135, 206, 235)
ORANGE = (255, 165, 0)
DARK_BLUE = (25, 25, 112)
YELLOW = (255, 223, 0)
BROWN = (139, 69, 19)
DARK_BROWN = (101, 67, 33)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
LIGHT_YELLOW = (255, 255, 153)

# Sun and moon properties
sun_radius = 45
sun_start_angle = 3
sun_angle = sun_start_angle
sun_center_x = WIDTH // 2
sun_center_y = 450  
sun_radius_orbit = 300 
sun_speed = 0.02
moon_radius = 35
moon_x = 100 
moon_y = 600
moon_rise_speed = 7
moon_max_height = 100  
moon_rising = False  
cloud_speed = 2

# Star and cloud properties
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(200)]
clouds = [(random.randint(-100, WIDTH), random.randint(50, 200)) for _ in range(5)] 

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    # GAME STATE UPDATES
    transition_factor = min((sun_angle - 3) / 3, 1)  # Transition sky
    sky_color = (
        int(BLUE[0] * (1 - transition_factor) + DARK_BLUE[0] * transition_factor),
        int(BLUE[1] * (1 - transition_factor) + DARK_BLUE[1] * transition_factor),
        int(BLUE[2] * (1 - transition_factor) + DARK_BLUE[2] * transition_factor)
    )
    screen.fill(sky_color)

    # All game math and comparisons happen here
    sun_x = int(sun_center_x + sun_radius_orbit * math.cos(sun_angle))
    sun_y = int(sun_center_y + sun_radius_orbit * math.sin(sun_angle))

    if sun_angle < 6:
        pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), sun_radius)
    else:
        moon_rising = True
    
     # Moon rise
    if moon_rising and moon_y > moon_max_height:
        moon_y -= moon_rise_speed

    # DRAWING
    if moon_rising:
        pygame.draw.circle(screen, WHITE, (moon_x, moon_y), moon_radius)
        pygame.draw.circle(screen, sky_color, (moon_x + 15, moon_y - 5), moon_radius - 10)
        if moon_y <= moon_max_height:
            for star in stars:
                pygame.draw.circle(screen, WHITE, star, 2) 

    # Move and draw clouds
    for i, cloud in enumerate(clouds):
        pygame.draw.ellipse(screen, WHITE, (cloud[0], cloud[1], 80, 40))
        pygame.draw.ellipse(screen, WHITE, (cloud[0] + 30, cloud[1] - 10, 60, 30))
        clouds[i] = (cloud[0] + cloud_speed, cloud[1])  
        if clouds[i][0] > WIDTH:
            clouds[i] = (-100, cloud[1]) 

    # Draw the main house
    pygame.draw.rect(screen, BROWN, (300, 350, 200, 150))
    pygame.draw.polygon(screen, DARK_BROWN, [(300, 350), (400, 270), (500, 350)])
    pygame.draw.rect(screen, DARK_BROWN, (375, 430, 50, 70))
    window_color = LIGHT_YELLOW if moon_rising else WHITE
    pygame.draw.rect(screen, window_color, (325, 380, 40, 40))  
    pygame.draw.rect(screen, window_color, (435, 380, 40, 40))  
    pygame.draw.rect(screen, BLACK, (325, 380, 40, 40), 3)  
    pygame.draw.rect(screen, BLACK, (435, 380, 40, 40), 3)  
    pygame.draw.line(screen, BLACK, (325, 400), (365, 400), 3)
    pygame.draw.line(screen, BLACK, (345, 380), (345, 420), 3) 
    pygame.draw.line(screen, BLACK, (435, 400), (475, 400), 3) 
    pygame.draw.line(screen, BLACK, (455, 380), (455, 420), 3)  

    # Draw the left tiny house
    pygame.draw.rect(screen, BROWN, (150, 400, 150, 150))
    pygame.draw.polygon(screen, DARK_BROWN, [(150, 400), (225, 350), (300, 400)])
    # Add windows to the left tiny house
    pygame.draw.rect(screen, window_color, (170, 430, 40, 40))  
    pygame.draw.rect(screen, window_color, (240, 430, 40, 40))  
    pygame.draw.rect(screen, BLACK, (170, 430, 40, 40), 3)  
    pygame.draw.rect(screen, BLACK, (240, 430, 40, 40), 3)  
    pygame.draw.line(screen, BLACK, (170, 450), (210, 450), 3)
    pygame.draw.line(screen, BLACK, (190, 430), (190, 470), 3) 
    pygame.draw.line(screen, BLACK, (240, 450), (280, 450), 3) 
    pygame.draw.line(screen, BLACK, (260, 430), (260, 470), 3)  

    # Draw the right tiny house
    pygame.draw.rect(screen, BROWN, (500, 400, 150, 150))
    pygame.draw.polygon(screen, DARK_BROWN, [(500, 400), (575, 350), (650, 400)])
    # Add windows to the right tiny house
    pygame.draw.rect(screen, window_color, (520, 430, 40, 40))  
    pygame.draw.rect(screen, window_color, (590, 430, 40, 40))  
    pygame.draw.rect(screen, BLACK, (520, 430, 40, 40), 3)  
    pygame.draw.rect(screen, BLACK, (590, 430, 40, 40), 3)  
    pygame.draw.line(screen, BLACK, (520, 450), (560, 450), 3)
    pygame.draw.line(screen, BLACK, (540, 430), (540, 470), 3) 
    pygame.draw.line(screen, BLACK, (590, 450), (630, 450), 3) 
    pygame.draw.line(screen, BLACK, (610, 430), (610, 470), 3)  

    pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))

    # Update sun position
    if sun_angle < 6:
        sun_angle += sun_speed

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
