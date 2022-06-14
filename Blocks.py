from Block import Block


class Blocks:
    def __init__(self):
        self.blocks = []
        self.render_order = []
        self.to_drag = []
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

    def drag(self, mouse_pos):
        for block in self.render_order:
            if block.rect.collidepoint(mouse_pos):
                self.to_drag.append(block)
        if self.to_drag:
            self.drag_this = self.to_drag[-1]
            self.to_drag.clear()
            self.to_front(self.drag_this.id)

    def drop(self):
        if self.drag_this:
            self.drag_this.drag_offset = None
            self.drag_this = None
