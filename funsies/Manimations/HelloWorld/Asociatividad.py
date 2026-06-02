from manim import *

class Asociatividad(Scene):
    def construct(self):
        # Ejes
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=8,
            y_length=6,
            tips=True,
            axis_config={"include_numbers": True, "font_size": 24}
        )
        self.play(Create(ax))

        # Vectores A, B y C
        A = np.array([2, 8, 0])
        B = np.array([7, 7, 0])
        C = np.array([8, 2, 0])

        vecA = Arrow(start=ax.get_origin(), end=ax.c2p(*A), buff=0, color=BLUE)
        vecB = Arrow(start=ax.c2p(*A), end=ax.c2p(*B), buff=0, color=GREEN)
        vecC = Arrow(start=ax.c2p(*B), end=ax.c2p(*C), buff=0, color=RED)

        labelA = MathTex("A", color=BLUE).next_to(vecA.get_end(), LEFT)
        labelB = MathTex("B", color=GREEN).next_to(vecB.get_end())
        labelC = MathTex("C", color=RED).next_to(vecC.get_end())

        self.play(GrowArrow(vecA), FadeIn(labelA))
        self.play(GrowArrow(vecB), FadeIn(labelB))
        self.play(GrowArrow(vecC), FadeIn(labelC))
        self.wait(3)

        # Quitar todos los números excepto el 0 de forma instantánea
        for num in ax.x_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        for num in ax.y_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        self.wait(2)

        # Vector A+B 
        vecAB = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*B),
            buff=0,
            color=YELLOW
        )
        labelAB = MathTex("A+B", color=YELLOW).next_to(vecAB.get_center())

        # Vector B+C 
        vecBC = Arrow(
            start=ax.c2p(*A),
            end=ax.c2p(*C),
            buff=0,
            color=PINK
        )
        labelBC = MathTex("B+C", color=PINK).next_to(vecBC.get_center())

        # Vector A + B + C 
        vecABC = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*C),
            buff=0,
            color=PURPLE_A
        )
        labelABC = MathTex("A+B+C ", color=PURPLE_A).next_to(vecABC.get_center(), RIGHT)

        text = MathTex("A+(B+C)").to_edge(RIGHT)
        text2 = MathTex("(A+B)+C").to_edge(RIGHT)
        text3 = MathTex("(A+B)+C = A+(B+C)").to_edge(UP,RIGHT)

        self.play(GrowArrow(vecBC), FadeIn(labelBC), run_time=3)
        self.play(GrowArrow(vecABC), FadeIn(labelABC), run_time=5)
        self.wait(1)
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(vecBC), FadeOut(labelBC), FadeOut(vecABC), FadeOut(labelABC), FadeOut(text))
        self.wait(2)

        self.play(GrowArrow(vecAB), FadeIn(labelAB), run_time=3)
        self.play(GrowArrow(vecABC), FadeIn(labelABC), run_time=5)
        self.wait(1)
        self.play(Write(text2))
        self.wait(3)

        self.play(FadeIn(vecBC), FadeIn(labelBC), FadeOut(labelABC), FadeOut(text2))
        self.wait(1)
        self.play(Write(text3))



