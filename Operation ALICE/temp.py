
import pygame, sys
from pygame.locals import *


#Kode for å teste tegning og posisjonering av datamus
def main():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    mouse_position = (0, 0)
    drawing = False
    screen = pygame.display.set_mode((500, 500), 0, 32)
    screen.fill(WHITE)
    pygame.display.set_caption("ScratchBoard")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if (drawing):
                    mouse_position = pygame.mouse.get_pos()
                    pygame.draw.line(screen, BLACK, mouse_position, mouse_position, 1)
                    print(mouse_position)
            elif event.type == MOUSEBUTTONUP:
                mouse_position = (0, 0)
                drawing = False
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True

        pygame.display.update()
        pygame.display.flip()
        
if __name__ == "__main__":

    main()


