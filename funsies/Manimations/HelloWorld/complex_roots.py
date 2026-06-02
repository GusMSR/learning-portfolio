from manim import *
import numpy as np

class complex_roots(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=6,
            tips=True,
        )

        self.play(Create(ax))

        # Número complejo base (radio)
        r = 2
        n = 5

        circle = Circle(
            radius=ax.c2p(r, 0)[0] - ax.c2p(0, 0)[0]
        ).move_to(ax.get_origin())

        self.play(Create(circle))

        roots = []
        for k in range(n):
            angle = 2 * np.pi * k / n
            point = np.array([r*np.cos(angle), r*np.sin(angle), 0])
            dot = Dot(ax.c2p(*point), color=YELLOW)
            roots.append(dot)

        self.play(*[FadeIn(root) for root in roots])

        # Conectar como polígono
        polygon = Polygon(*[root.get_center() for root in roots], color=BLUE)
        self.play(Create(polygon))

        # Fórmula
        formula = MathTex(
            r"z_k = r^{1/n} e^{i(\theta + 2\pi k)/n}",
            color=WHITE
        ).to_edge(DOWN)

        self.play(Write(formula))
        self.wait(3)