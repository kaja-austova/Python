# Insert everything into: https://notebooks.gesis.org/binder/jupyter/user/ksp-ksp-serial-34-hu9we6qy/lab/tree/serial1.ipynb

%%manim -v WARNING -qm Animate

class Animate(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        circle = Circle(color=BLUE).shift(LEFT * 2.2)
        circle1 = Circle(color=BLACK)
        circle2 = Circle(color=RED).shift(RIGHT * 2.2)
        circle3 = Circle(color=YELLOW).shift(DOWN * 1.2, LEFT * 1.2)
        circle4 = Circle(color=GREEN).shift(DOWN * 1.2, RIGHT * 1.2)
        text = Tex("Olympijské hry 2024")

        self.play(Write(circle),Write(circle1),Write(circle2), Write(circle3), Write(circle4))
        self.play(circle3.animate.shift(UP * 1.2), circle4.animate.shift(UP * 1.2))
        self.play(circle.animate.shift(RIGHT * 2.2), circle2.animate.shift(LEFT * 2.2), circle3.animate.shift(RIGHT * 1.2), circle4.animate.shift(LEFT * 1.2))
        
    
        self.play(
            circle1.animate.scale(0.7).set_fill(BLACK, 1),
            circle.animate.scale(0.7).set_fill(BLUE, 1), 
            circle2.animate.scale(0.7).set_fill(RED, 1), 
            circle3.animate.scale(0.7).set_fill(YELLOW, 1), 
            circle4.animate.scale(0.7).set_fill(GREEN, 1)
        )
        
        self.play(
            circle3.animate.shift(LEFT * 2.8),
            circle.animate.shift(LEFT * 1.4),
            circle2.animate.shift( RIGHT * 1.4),
            circle4.animate.shift(RIGHT * 2.8)
            )
        self.play(Write(text))
        
        self.play(FadeOut(circle), FadeOut(circle1),FadeOut(circle2),FadeOut(circle3),FadeOut(circle4),FadeOut(text))
