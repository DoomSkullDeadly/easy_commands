import pygame

size = 100, 60
s = pygame.Surface(size=size)
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)


class Block:
    def __init__(self, btype=None, pos=[0, 0]):
        self.type = btype  # type of block, e.g. for loop, while loop, if, etc.
        self.clicked = False
        self.dragging = False
        self.rect = pygame.Rect(pos, size)
        self.drag_offset = None

    def render(self):
        pygame.draw.rect(surface=s, color=(100, 130, 60), rect=s.get_rect())  # idk how to not use s.get_rect() :/
        display.blit(s, self.rect)

    def drag(self, pos=None):
        if not self.drag_offset:
            self.drag_offset = pos[0] - self.rect.x, pos[1] - self.rect.y
        if self.dragging and pos:
            self.rect.x = pos[0] - self.drag_offset[0]
            self.rect.y = pos[1] - self.drag_offset[1]
