from Block import Block
from itertools import chain
import pygame


pygame.init()
display = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)


class Blocks:
    def __init__(self):
        self.blocks = []
        self.render_order = []
        self.hovering_over = []
        self.drag_this = None
        self.block_chains = {}
        self.block_chain_outline = None

    def render(self):
        if self.drag_this:  # grr, too many ifs. nOt EfFiCiEnT
            self.drag_this.highlight = False

        for block in self.render_order:
            block.render()

        if self.drag_this:
            pygame.draw.rect(surface=self.block_chain_outline, color=(255, 255, 255),
                             rect=self.block_chain_outline.get_rect(), width=2)
            display.blit(self.block_chain_outline, self.drag_this.rect.topleft)

    def new(self, btype=None, pos=[0, 0]):
        new_block = Block(btype=btype, pos=pos)
        self.blocks.append(new_block)
        self.render_order.append(new_block)

    def to_front(self, bid=None):
        if bid is not None:
            num = len(self.render_order)
            for i in range(num):
                if self.render_order[i].id == bid:
                    self.render_order.insert(num, self.render_order.pop(i))
                    break

    def hover_over(self, mouse_pos):
        self.hovering_over.clear()
        for block in self.render_order:
            block.highlight = False
            if block.rect.collidepoint(mouse_pos):
                self.hovering_over.append(block)

        if self.hovering_over:
            self.hovering_over[-1].highlight = True

    def drag(self):
        if self.hovering_over:
            self.drag_this = self.hovering_over[-1]
            self.to_front(self.drag_this.id)

        if self.drag_this in chain.from_iterable(list(self.block_chains.values())):  # remakes blockchains
            self.remake_chains(top=self.drag_this.parent, bottom=self.drag_this)

        # for super_parent in self.block_chains:  # for debug
        #     print(f"{super_parent.id}: {[block.id for block in self.block_chains[super_parent]]}")
        # print("\n")

        self.chain_outline()

    def chain_outline(self):  # will need to redo if different shapes/sizes
        super_child = self.get_super_child(self.drag_this)
        size = [super_child.rect.bottomright[0] - self.drag_this.rect.topleft[0],
                super_child.rect.bottomright[1] - self.drag_this.rect.topleft[1]]
        self.block_chain_outline = pygame.Surface(size, pygame.SRCALPHA)

    def get_super_parent(self, block):
        super_parent = block
        while 1:
            if super_parent.parent:
                super_parent = super_parent.parent
            else:
                break
        return super_parent

    def get_super_child(self, block):
        super_child = block
        while 1:
            if super_child.child:
                super_child = super_child.child
            else:
                break
        return super_child

    def drop(self):
        if self.drag_this:
            self.drag_this.drag_offset = None
            if len(self.hovering_over) >= 2:
                self.snap(parent=self.hovering_over[-2], child=self.drag_this)
            self.drag_this = None

    def snap(self, parent, child):
        if parent and child and not parent.child:
            if child.snap_zone_top.colliderect(parent.snap_zone_bottom):
                parent.child = child
                child.parent = parent
                child.update_pos()
                self.chains(parent, child)

    def remake_chains(self, top, bottom):
        child = top
        parent = bottom
        child.child = None
        parent.parent = None
        if parent.child:
            self.chains(parent=parent, child=parent.child)

        if child.parent:
            self.chains(parent=child.parent, child=child)
        else:
            self.block_chains.pop(child)

    def chains(self, parent, child):  # I wish I could think of a better way to do this whole part
        super_parent = self.get_super_parent(parent)

        if child and child in self.block_chains:  # removes old chain
            self.block_chains.pop(child)

        self.block_chains[super_parent] = []
        parent_child = super_parent
        while 1:  # places all blocks in connected order into super parent key
            if parent_child and parent_child.child:
                self.block_chains[super_parent].append(parent_child.child)
                parent_child = parent_child.child
            else:
                break
