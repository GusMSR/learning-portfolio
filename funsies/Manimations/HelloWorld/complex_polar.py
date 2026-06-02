from manim import *
import numpy as np

class polar_representation(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            tips=True,
        )

        labels = ax.get_axis_labels(MathTex(r"\mathrm{Re}"), MathTex(r"\mathrm{Im}"))
        self.play(Create(ax), FadeIn(labels))

        # Número complejo
        z = np.array([3, 3, 0])
        r = np.linalg.norm(z[:2])
        theta = np.arctan2(z[1], z[0])

        vec = Arrow(ax.get_origin(), ax.c2p(*z), buff=0, color=RED)
        self.play(GrowArrow(vec))

        # Radio
        label_r = MathTex("r", color=GREEN).next_to(vec.get_center(), RIGHT)
        self.play(FadeIn(label_r))

        # Ángulo
        angle = Angle(
            Line(ax.get_origin(), ax.c2p(1, 0)),
            Line(ax.get_origin(), ax.c2p(*z)),
            radius=0.8
        )

        label_theta = MathTex(r"\theta").next_to(angle, RIGHT)

        self.play(Create(angle), FadeIn(label_theta))

        # Forma polar
        polar_form = MathTex(
            r"z = r(\cos\theta + i\sin\theta)",
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(polar_form))
        self.wait(3)