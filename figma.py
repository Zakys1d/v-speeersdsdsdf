import pygame
import math
pygame.init()

window = pygame.display.set_mode((1000,800))

pygame.display.set_caption("Portal 3")

pygame_image = pygame.image.load("nigga.webp")
pygame_rect = pygame_image.get_rect()

RED = (255, 0, 0)
YELLOW = (255, 255, 0)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    angle = math.degrees(math.atan2(mouse_y - pygame_rect.centery, mouse_x - pygame_rect.centerx)) - 90

    image_rotated = pygame.transform.rotate(pygame_image, -angle)
    new_rect = image_rotated.get_rect(center=pygame_rect.center)
    window.fill(YELLOW)
    window.blit(image_rotated, new_rect)

    
    pygame.display.flip()
