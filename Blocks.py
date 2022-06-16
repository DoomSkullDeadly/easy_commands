from Block import Block


class Blocks:
    def __init__(self):
        self.blocks = []
        self.render_order = []
        self.hovering_over = []
        self.drag_this = None

    def render(self):
        for block in self.render_order:
            block.render()

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
