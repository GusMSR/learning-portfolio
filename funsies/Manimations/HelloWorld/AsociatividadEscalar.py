from manim import *

class Escalar1(Scene):
    def construct(self):
        # Ejes
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=6,
            tips=True,
            axis_config={"include_numbers": True, "font_size": 24}
        )
        self.play(Create(ax))

        text = MathTex(r"\lambda = 2").to_edge(RIGHT).shift(0.5*UP)
        text2 = MathTex(r"\mu = \tfrac{1}{4}").to_edge(RIGHT)
        text3 = MathTex(r"\lambda \mu = \tfrac{1}{2}").to_edge(RIGHT).shift(0.8*DOWN)


        # Vector A y resultados de transformaciones
        A = np.array([2, 2, 0])
        A_moved = np.array([4, 4, 0])
        A_moved2 = np.array([1, 1, 0])

        vecA = Arrow(start=ax.get_origin(), end=ax.c2p(*A), buff=0, color=BLUE)
        vecA_dumb = Arrow(start=ax.get_origin(), end=ax.c2p(*A), buff=0, color=BLUE)

        labelA = MathTex("A", color=BLUE).next_to(vecA.get_end(), UP)

        self.play(GrowArrow(vecA), FadeIn(labelA))
        self.wait(3)

        # Quitar todos los números excepto el 0 de forma instantánea
        for num in ax.x_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        for num in ax.y_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        self.wait(2)

        vecA_moved = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*A_moved),
            buff=0,
            color=GREEN
        )
        labelA_moved = MathTex(r"(\lambda) A", color=GREEN).next_to(vecA_moved.get_end())

        
        vecA_moved2 = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*A_moved2),
            buff=0,
            color=YELLOW
        )
        labelA_moved2 = MathTex(r"(\lambda \mu) A", color=YELLOW).next_to(vecA_moved2.get_end())

        vecA_moved3 = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*A_moved2),
            buff=0,
            color=PURPLE
        )
        labelA_moved3 = MathTex(r" = \tfrac{1}{2} A", color=PURPLE).next_to(vecA_moved3.get_end()).shift(2*RIGHT)

        self.play(Write(text))
        self.wait(2)
        self.play(GrowArrow(vecA_moved), FadeIn(labelA_moved))
        self.wait(2)
        self.play(Write(text2))
        self.play(GrowArrow(vecA_moved2), FadeIn(labelA_moved2))
        self.wait(3)
        self.play(GrowArrow(vecA_moved3), FadeIn(labelA_moved3))
        self.wait(3)
        self.play(Write(text3))