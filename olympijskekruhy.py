# Insert everything into: https://notebooks.gesis.org/binder/jupyter/user/ksp-ksp-serial-34-hu9we6qy/lab/tree/serial1.ipynb

class Animate(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        circle = Circle(color=BLUE).shift(LEFT * 2)
        circle1 = Circle(color=BLACK)
        circle2 = Circle(color=RED).shift(RIGHT * 2)
        circle3 = Circle(color=YELLOW).shift(DOWN * 1.5, LEFT * 1.2)
        circle4 = Circle(color=GREEN).shift(DOWN * 1.5, RIGHT * 1.2)

        self.play(Write(circle),Write(circle1),Write(circle2), Write(circle3), Write(circle4))