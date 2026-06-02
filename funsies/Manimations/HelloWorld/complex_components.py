from manim import *
import numpy as np

class complex_properties(Scene):
    def construct(self):
        # Plano complejo
        ax = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            tips=True,
        )

        labels = ax.get_axis_labels(
            MathTex(r"\mathrm{Re}"),
            MathTex(r"\mathrm{Im}")
        )

        self.play(Create(ax), FadeIn(labels))

        # Número complejo
        z = np.array([3, 2, 0])
        z_conj = np.array([3, -2, 0])

        vec_z = Arrow(ax.get_origin(), ax.c2p(*z), buff=0, color=RED)
        label_z = MathTex("z", color=RED).next_to(vec_z.get_end(), UP)

        self.play(GrowArrow(vec_z), FadeIn(label_z))
        self.wait(1)

        # =========================
        # 🔵 CONJUGADO (REFLEXIÓN)
        # =========================
        vec_conj = Arrow(ax.get_origin(), ax.c2p(*z_conj), buff=0, color=BLUE)
        label_conj = MathTex(r"\bar{z}", color=BLUE).next_to(vec_conj.get_end(), DOWN)

        self.play(Transform(vec_z.copy(), vec_conj), FadeIn(label_conj))

        self.wait(2)

        # Línea de simetría
        real_axis = ax.get_x_axis()
        self.play(Indicate(real_axis))

        self.wait(2)

        # =========================
        # 🟢 NORMA
        # =========================
        norm = np.linalg.norm(z[:2])

        circle = Circle(
            radius=ax.c2p(norm, 0)[0] - ax.c2p(0, 0)[0]
        ).move_to(ax.get_origin())

        label_norm = MathTex(r"|z|", color=GREEN).next_to(circle, RIGHT)

        self.play(Create(circle), FadeIn(label_norm))
        self.wait(2)

        # =========================
        # 🟡 PRODUCTO z * z̄
        # =========================
        real_point = np.array([norm**2, 0, 0])
        dot_real = Dot(ax.c2p(*real_point), color=YELLOW)

        label_real = MathTex(r"z\bar{z} = |z|^2", color=YELLOW).to_edge(DOWN)

        self.play(FadeIn(dot_real), Write(label_real))
        self.wait(2)

        # =========================
        # 🟣 INVERSO
        # =========================
        # z^{-1} = conjugado / |z|^2
        inv = z_conj / (norm**2)

        vec_inv = Arrow(ax.get_origin(), ax.c2p(*inv), buff=0, color=PURPLE)
        label_inv = MathTex(r"z^{-1}", color=PURPLE).next_to(vec_inv.get_end(), RIGHT)

        self.play(GrowArrow(vec_inv), FadeIn(label_inv))
        self.wait(2)

        # Mostrar relación
        relation = MathTex(
            r"z^{-1} = \frac{\bar{z}}{|z|^2}",
            color=PURPLE
        ).to_edge(UP)

        self.play(Write(relation))
        self.wait(3)

        # =========================
        # 🔁 INTERPRETACIÓN GEOMÉTRICA
        # =========================
        explanation = MathTex(
            r"\text{Reflexión + Escalamiento}",
            color=WHITE
        ).next_to(relation, DOWN)

        self.play(Write(explanation))
        self.wait(3)