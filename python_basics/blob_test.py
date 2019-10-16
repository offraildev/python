import random 
import pygame

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

init_blue_blobs = 5
init_red_blobs = 7

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()


class Blob:
    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH

        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.x = HEIGHT

# def get_color():
#     return [random.randint(0,255) for _ in range(3)]

def draw_frame(blob_list):
    game_display.fill(WHITE)
    
    for blobs in blob_list:
        for blob_id in blobs:
            blob = blobs[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move() 
    pygame.display.update()

def main():
    blue_blobs = {i: Blob(BLUE) for i in range(init_blue_blobs)}
    red_blobs = {i: Blob(RED) for i in range(init_red_blobs)}
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        draw_frame([red_blobs, blue_blobs])
        clock.tick(60)

if __name__ == "__main__":
    main()