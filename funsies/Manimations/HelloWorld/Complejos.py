from manim import *
import numpy as np

class complex_intuition(Scene):
    def construct(self):
        # Ejes como plano complejo
        ax = Axes(
            x_range=[-1, 8, 1],
            y_range=[-1, 8, 1],
            x_length=8,
            y_length=6,
            tips=True,
        )

        labels = ax.get_axis_labels(
            MathTex(r"\mathrm{Re}"), 
            MathTex(r"\mathrm{Im}")
        )

        self.play(Create(ax), FadeIn(labels))

        # Base: 1 y i
        A = np.array([1, 0, 0])  # 1
        B = np.array([0, 1, 0])  # i
        Z = np.array([6, 7, 0])  # z

        vecA = Arrow(ax.get_origin(), ax.c2p(*A), buff=0, color=BLUE)
        vecB = Arrow(ax.get_origin(), ax.c2p(*B), buff=0, color=GREEN)
        vecZ = Arrow(ax.get_origin(), ax.c2p(*Z), buff=0, color=RED)

        labelA = MathTex("1", color=BLUE).next_to(vecA.get_end(), DOWN)
        labelB = MathTex("i", color=GREEN).next_to(vecB.get_end(), LEFT)

        self.play(GrowArrow(vecA), FadeIn(labelA))
        self.play(GrowArrow(vecB), FadeIn(labelB))

        self.wait(1)

        # Número complejo
        labelZ = MathTex(r"z = x + iy", color=RED).next_to(vecZ.get_end(), UP)
        self.play(GrowArrow(vecZ), FadeIn(labelZ))

        self.wait(2)

        # Mostrar descomposición
        x = Z[0]
        y = Z[1]

        proj_x = Arrow(ax.get_origin(), ax.c2p(x, 0), buff=0, color=BLUE_B)
        proj_y = Arrow(ax.c2p(x, 0), ax.c2p(x, y), buff=0, color=GREEN_B)

        label_x = MathTex(r"x", color=BLUE_B).next_to(proj_x.get_end(), DOWN)
        label_y = MathTex(r"y", color=GREEN_B).next_to(proj_y.get_end(), RIGHT)

        self.play(GrowArrow(proj_x), FadeIn(label_x))
        self.play(GrowArrow(proj_y), FadeIn(label_y))

        self.wait(2)

        # Igualdad clave
        equation = MathTex(
            r"z = x + iy \;\equiv\; (x,y)",
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(equation))

        self.wait(3)