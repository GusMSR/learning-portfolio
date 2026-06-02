from manim import *

class Escalar2(Scene):
    def construct(self):
        # Ejes
        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            tips=True,
            axis_config={"include_numbers": True, "font_size": 24}
        )
        self.play(Create(ax))

        text = MathTex(r"\text{Hay infinitos vectores ortogonales a A}").to_edge(DOWN)

        # Vector A y resultados de transformaciones
        A = np.array([1, 1, 0])
        A1 = np.array([-1, 1, 0])
        A2 = np.array([1, -1, 0])
        B1 = np.array([3, -3, 0])
        B2 = np.array([2.3, -2.3, 0])

        vecA = Arrow(start=ax.get_origin(), end=ax.c2p(*A), buff=0, color=BLUE)
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

        vecA1 = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*A1),
            buff=0,
            color=GREEN
        )
        labelA1 = MathTex(r"A_{1} \perp A", color=GREEN).next_to(vecA1.get_end()).shift(2.5*LEFT)

        vecA2 = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*A2),
            buff=0,
            color=YELLOW
        )
        labelA2 = MathTex(r"A_{2} \perp A", color=YELLOW).next_to(vecA2.get_end())

        vecA3 = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*B1),
            buff=0,
            color=PURPLE
        )
        labelA3 = MathTex(r"A_{3} \perp A", color=PURPLE).next_to(vecA3.get_end())

        vecA4 = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*B2),
            buff=0,
            color=RED
        )
        labelA4 = MathTex(r"A_{4} \perp A", color=RED).next_to(vecA4.get_end())

        self.play(GrowArrow(vecA1), FadeIn(labelA1))
        self.wait(2)
        self.play(GrowArrow(vecA2), FadeIn(labelA2))
        self.wait(2)
        self.play(GrowArrow(vecA3), FadeIn(labelA3))
        self.wait(2)
        self.play(GrowArrow(vecA4), FadeIn(labelA4))
        self.wait(2)

        # Definir la función
        linea = ax.plot(lambda x: -x, color=BLUE)

        # Etiqueta
        label = ax.get_graph_label(linea, label="y=-x", x_val=-4, direction=UR)

        self.play(Create(linea), FadeIn(label), run_time = 5)
        self.wait(2)
        self.play(Write(text))