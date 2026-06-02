from manim import *

class FirstScene(Scene):
    def construct(self):
        # Ejes
        ax = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 24}
        )
        self.play(Create(ax))

        # Vectores A y B
        A = np.array([2, 2, 0])
        B = np.array([3, 0.5, 0])

        vecA = Arrow(start=ax.get_origin(), end=ax.c2p(*A), buff=0, color=BLUE)
        vecB = Arrow(start=ax.get_origin(), end=ax.c2p(*B), buff=0, color=GREEN)

        labelA = MathTex("A", color=BLUE).next_to(vecA.get_end(), UP)
        labelB = MathTex("B", color=GREEN).next_to(vecB.get_end(), RIGHT)

        self.play(GrowArrow(vecA), FadeIn(labelA))
        self.play(GrowArrow(vecB), FadeIn(labelB))
        self.wait(1)

        # Vector A-B (desde punta de B hasta punta de A)
        vecAB = Arrow(
            start=ax.c2p(*A),
            end=ax.c2p(*B),
            buff=0,
            color=YELLOW
        )
        labelAB = MathTex("A-B", color=YELLOW).next_to(vecAB.get_center(), UP, LEFT, LEFT)

        self.play(GrowArrow(vecAB), FadeIn(labelAB))
        self.wait(3)

        # Quitar todos los números excepto el 0 de forma instantánea
        for num in ax.x_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        for num in ax.y_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)

        self.wait(2)

        # "Mover" el vector A-B para que se deslice hacia el origen
        vecAB_moved = Arrow(
            start=ax.c2p(*A),
            end=ax.c2p(0, 0),
            buff=0,
            color=YELLOW
        )
        labelAB_moved = MathTex("A^*", color=YELLOW).next_to(vecAB_moved.get_center(), LEFT)

        self.play(Transform(vecAB, vecAB_moved), Transform(labelAB, labelAB_moved), run_time=5)
        self.wait(3)

        # Mostrar el inverso aditivo de A: -A
        vecA_inv = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(-A[0], -A[1]),
            buff=0,
            color=RED
        )
        labelA_inv = MathTex("-A", color=RED).next_to(vecA_inv.get_end(), DOWN)

        self.play(GrowArrow(vecA_inv), FadeIn(labelA_inv))
        self.play(Transform(vecA_inv, vecAB_moved), Transform(labelA_inv, labelAB_moved), run_time=5)
        self.wait(3)

        # Mostrar que A + A* = 0
        text = MathTex("A + A^* = 0").to_edge(DOWN)
        text2 = MathTex("A + (-A) = 0").to_edge(DOWN)
        self.play(Write(text))
        self.wait(2)
        self.play(Transform(text, text2))

        self.wait(2)
