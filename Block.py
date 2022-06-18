import pygame
import itertools

pygame.init()

size = 100, 60
s = pygame.Surface(size=size)
s_snap_bottom = pygame.Surface(size=(100, 20))
s_snap_bottom.set_alpha(50)
s_snap_top = pygame.Surface(size=(20, 20))
s_snap_top.set_alpha(50)
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
counter = itertools.count()
font = pygame.font.SysFont("Arial", 28, bold=True)


def text_render(text):
    return font.render(str(text), True, (0, 0, 0))


class Block:
    def __init__(self, btype=None, pos=[0, 0]):
        self.id = next(counter)
        self.type = btype  # type of block, e.g. for loop, while loop, if, etc.
        self.clicked = False
        self.rect = pygame.Rect(pos, size)
        self.snap_zone_bottom = pygame.Rect([pos[0], pos[1] + 40], (100, 20))
        self.snap_zone_top = pygame.Rect([pos[0] + 40, pos[1]], (20, 20))
        self.drag_offset = None
        self.highlight = False
        self.child = None
        self.parent = None

    def render(self):  # TODO: rework to draw to surface once or when updated, only need to blit surface (efficiency)
        pygame.draw.rect(surface=s, color=(100, 130, 60), rect=s.get_rect())  # idk how to not use s.get_rect() :/
        if self.highlight:
            pygame.draw.rect(surface=s, color=(150, 255, 90), rect=s.get_rect(), width=2)
        else:
            pygame.draw.rect(surface=s, color=(50, 100, 30), rect=s.get_rect(), width=2)  # outline

        s.blit(text_render(self.id), (s.get_rect().centerx-(6*len(str(self.id))), s.get_rect().centery-14))  # debug
        display.blit(s, self.rect)

        pygame.draw.rect(surface=s_snap_bottom, color=(200, 200, 200), rect=s_snap_bottom.get_rect())  # for debugging
        display.blit(s_snap_bottom, self.snap_zone_bottom)
        pygame.draw.rect(surface=s_snap_top, color=(200, 200, 200), rect=s_snap_top.get_rect())
        display.blit(s_snap_top, self.snap_zone_top)

    def drag(self, pos=None):
        if self.parent:
            self.parent.child = None
            self.parent = None

        if not self.drag_offset:
            self.drag_offset = pos[0] - self.rect.x, pos[1] - self.rect.y

        if pos:
            self.rect.x = pos[0] - self.drag_offset[0]
            self.rect.y = pos[1] - self.drag_offset[1]

            self.snap_zone_bottom.topleft = self.rect.x, self.rect.y + 40

            self.snap_zone_top.centerx = pos[0]
            self.snap_zone_top.y = self.rect.y

        if self.child:
            self.child.update_pos()

    def update_pos(self, pos=None):
        if pos:
            self.rect.topleft = pos
            self.snap_zone_bottom.topleft = self.rect.x, self.rect.y + 40
        if self.parent:
            self.rect.topleft = self.parent.rect.bottomleft
            self.snap_zone_bottom.bottomleft = self.rect.bottomleft
            self.snap_zone_top.midtop = self.parent.rect.midbottom
        if self.child:
            self.child.update_pos()
