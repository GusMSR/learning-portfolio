from manim import *
import numpy as np

class complex_operations(Scene):
    def construct(self):
        # Ejes
        ax = Axes(
            x_range=[-2, 8, 1],
            y_range=[-2, 8, 1],
            x_length=8,
            y_length=6,
            tips=True,
        )

        labels = ax.get_axis_labels(
            MathTex(r"\mathrm{Re}"), 
            MathTex(r"\mathrm{Im}")
        )

        self.play(Create(ax), FadeIn(labels))

        # --- Complejos base ---
        z = np.array([4, 2, 0])
        w = np.array([2, 3, 0])

        vecZ = Arrow(ax.get_origin(), ax.c2p(*z), buff=0, color=RED)
        vecW = Arrow(ax.get_origin(), ax.c2p(*w), buff=0, color=BLUE)

        labelZ = MathTex("z", color=RED).next_to(vecZ.get_end(), RIGHT)
        labelW = MathTex("w", color=BLUE).next_to(vecW.get_end(), UP)

        self.play(GrowArrow(vecZ), FadeIn(labelZ))
        self.play(GrowArrow(vecW), FadeIn(labelW))

        self.wait(1)

        # =========================
        # 🔵 SUMA (PARALELOGRAMO)
        # =========================
        z_plus_w = z + w

        vec_sum = Arrow(ax.get_origin(), ax.c2p(*z_plus_w), buff=0, color=YELLOW)
        label_sum = MathTex("z+w", color=YELLOW).next_to(vec_sum.get_end(), RIGHT)

        # Paralelogramo
        trans_w = Arrow(ax.c2p(*z), ax.c2p(*(z + w)), buff=0, color=BLUE_B)
        trans_z = Arrow(ax.c2p(*w), ax.c2p(*(z + w)), buff=0, color=RED_B)

        self.play(GrowArrow(trans_w), GrowArrow(trans_z))
        self.play(GrowArrow(vec_sum), FadeIn(label_sum))

        self.wait(2)

        # =========================
        # 🔴 RESTA (TRIÁNGULO)
        # =========================
        z_minus_w = z - w

        vec_diff = Arrow(ax.c2p(*w), ax.c2p(*z), buff=0, color=PURPLE)
        label_diff = MathTex("z-w", color=PURPLE).next_to(vec_diff.get_center(), UP)

        self.play(GrowArrow(vec_diff), FadeIn(label_diff))

        self.wait(2)

        # =========================
        # 🟢 MULTIPLICACIÓN POR i
        # =========================
        # i*z = (-y, x)
        iz = np.array([-z[1], z[0], 0])

        vec_iz = Arrow(ax.get_origin(), ax.c2p(*iz), buff=0, color=GREEN)
        label_iz = MathTex("iz", color=GREEN).next_to(vec_iz.get_end(), LEFT)

        self.play(Transform(vecZ.copy(), vec_iz), FadeIn(label_iz))

        self.wait(2)

        # Rotación visual
        rotating_vec = vecZ.copy()
        self.add(rotating_vec)

        self.play(
            Rotate(
                rotating_vec,
                angle=PI/2,
                about_point=ax.get_origin()
            ),
            run_time=2
        )

        self.wait(3)