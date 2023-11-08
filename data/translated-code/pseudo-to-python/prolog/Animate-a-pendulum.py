import PCE

class pendulum:
    def __init__(self):
        self.window = PCE.window("Pendulum", 560, 300)
        self.line = PCE.line()
        self.small_circle = PCE.circle()
        self.small_circle.set_fill_pattern()
        self.large_circle = PCE.circle()
        self.large_circle.set_fill_pattern()
        self.small_circle.display_at(280, 0)
        self.small_circle.set_handle()
        self.large_circle.set_handle()
        self.line.connect(self.small_circle, self.large_circle)
        self.animation = animation()
        self.window.set_done_message()
        self.animation.start_timer()
        self.window.open()

class animation:
    def __init__(self):
        self.window = None
        self.bob = None
        self.pendulum_length = None
        self.angle = None
        self.delta = None
        self.timer = None

    def initialize(self, window, bob, pendulum_length, angle, delta, timer):
        self.window = window
        self.bob = bob
        self.pendulum_length = pendulum_length
        self.angle = angle
        self.delta = delta
        self.timer = timer

    def unlink(self):
        self.timer.stop()
        # Free resources

    def anim_message(self):
        # Update position and angle of the bob in the animation

def calc():
    # Compute the position of the bob

def next_angle():
    # Compute the next angle based on the current angle and delta