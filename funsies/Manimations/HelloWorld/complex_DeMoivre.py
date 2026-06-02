from manim import *
import numpy as np

class complex_multiplication(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            tips=True,
        )

        self.play(Create(ax))

        # Complejos
        z = np.array([2, 1, 0])
        w = np.array([1, 2, 0])

        vec_z = Arrow(ax.get_origin(), ax.c2p(*z), buff=0, color=RED)
        vec_w = Arrow(ax.get_origin(), ax.c2p(*w), buff=0, color=BLUE)

        self.play(GrowArrow(vec_z), GrowArrow(vec_w))

        # Producto
        z_c = complex(z[0], z[1])
        w_c = complex(w[0], w[1])
        prod = z_c * w_c
        prod_vec = np.array([prod.real, prod.imag, 0])

        vec_prod = Arrow(ax.get_origin(), ax.c2p(*prod_vec), buff=0, color=YELLOW)

        self.play(GrowArrow(vec_prod))

        # Rotación visual
        rotating = vec_z.copy()
        self.add(rotating)

        angle = np.angle(w_c)

        self.play(
            Rotate(rotating, angle=angle, about_point=ax.get_origin()),
            run_time=2
        )

        # Escalamiento
        scale = abs(w_c)
        self.play(rotating.animate.scale(scale, about_point=ax.get_origin()))

        # Fórmula
        formula = MathTex(
            r"(re^{i\theta})^n = r^n e^{in\theta}",
            color=GREEN
        ).to_edge(DOWN)

        self.play(Write(formula))
        self.wait(3)