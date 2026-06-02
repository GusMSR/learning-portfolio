from manim import *

class trans(Scene):
    def construct(self):
        hexagono = RegularPolygon(
            n=6,               
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.5
        )

        poly = RegularPolygon(
            n=3,               
            color=RED,
            fill_color=RED,
            fill_opacity=0.5
        )

        
        poly3 = RegularPolygon(
            n=20,               
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.5
        )

        text = MathTex(r"\text{Traslación}").to_edge(UP)
        text2 = MathTex(r"\text{Rotación}").to_edge(UP)
        text3 = MathTex(r"\text{Reflexión}").to_edge(UP)

        self.play(Create(hexagono))
        self.wait(2)
        self.play(Write(text))
        self.wait(2)
        self.play(hexagono.animate.shift(RIGHT*4 + DOWN*2))  # move right and up
        self.wait(2)
        self.play(FadeOut(hexagono), FadeOut(text))
        self.wait(3)

        self.play(Create(poly))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Rotate(poly, angle=PI/2)) 
        self.play(FadeOut(poly), FadeOut(text2))
        self.wait(3)

        self.play(Create(poly3.shift(LEFT)))
        self.wait(2)
        self.play(Write(text3))
        self.wait(2)

        reflection_x = [[0, 1], [1, 0]]
        self.play(poly3.animate.apply_matrix(reflection_x))
        self.wait(2)