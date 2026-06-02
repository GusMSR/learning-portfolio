from manim import *

class CompletitudR2(Scene):
    def construct(self):
        # Crear ejes cartesianos
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 6, 1],
            x_length=8,
            y_length=5,
            tips=True,
        )
        self.play(Create(axes))
        self.wait(0.5)

        # Rectángulos anidados
        rect_sizes = [
            (8, 5),   # ancho, alto
            (6, 4),
            (4.5, 3),
            (3, 2),
            (2, 1.2),
        ]
        colors = [BLUE, GREEN, YELLOW, RED, PURPLE]

        for size, color in zip(rect_sizes, colors):
            rect = Rectangle(width=size[0], height=size[1], color=color)
            rect.move_to(axes.c2p(5, 3))  # centrar en el plano cartesiano
            self.play(Create(rect))
            self.wait(0.5)

        self.wait(1)
