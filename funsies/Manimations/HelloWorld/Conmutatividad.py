from manim import *

class Conmutatividad(Scene):
    def construct(self):
        # Ejes
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=6,
            tips=True,
            axis_config={"include_numbers": True, "font_size": 24}
        )
        self.play(Create(ax))

        # Vectores A y B
        A = np.array([1.5, 3.5, 0])
        B = np.array([3, 1, 0])
        AB = np.array([4.5, 4.5, 0])

        vecA = Arrow(start=ax.get_origin(), end=ax.c2p(*A), buff=0, color=BLUE)
        vecA_dumb = Arrow(start=ax.get_origin(), end=ax.c2p(*A), buff=0, color=BLUE)
        vecB = Arrow(start=ax.get_origin(), end=ax.c2p(*B), buff=0, color=GREEN)
        vecB_dumb = Arrow(start=ax.get_origin(), end=ax.c2p(*B), buff=0, color=GREEN)

        labelA = MathTex("A", color=BLUE).next_to(vecA.get_end(), UP)
        labelB = MathTex("B", color=GREEN).next_to(vecB.get_end(), RIGHT)

        self.play(GrowArrow(vecA), FadeIn(labelA))
        self.play(GrowArrow(vecB), FadeIn(labelB))
        self.wait(3)

        # Quitar todos los números excepto el 0 de forma instantánea
        for num in ax.x_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        for num in ax.y_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        self.wait(2)

        # Poner el vector A en la punta del vector B y viceversa 
        vecA_moved = Arrow(
            start=ax.c2p(*B),
            end=ax.c2p(*AB),
            buff=0,
            color=BLUE
        )
        labelA_moved = MathTex("A", color=BLUE).next_to(vecA_moved.get_center())

        vecB_moved = Arrow(
            start=ax.c2p(*A),
            end=ax.c2p(*AB),
            buff=0,
            color=GREEN
        )
        labelB_moved = MathTex("B", color=GREEN).next_to(vecB_moved.get_center(), UP)

        # Vector A+B 
        vecAB = Arrow(
            start=ax.get_origin(),
            end=ax.c2p(*AB),
            buff=0,
            color=YELLOW
        )
        labelAB = MathTex("A+B", color=YELLOW).next_to(vecAB.get_center())
        labelBA = MathTex("B+A", color=YELLOW).next_to(vecAB.get_center())
        

        self.play(Transform(vecA_dumb, vecA_moved), FadeIn(labelA_moved),run_time=3)        
        self.play(GrowArrow(vecAB), FadeIn(labelAB),run_time=5)
        self.wait(3)

        vecA_moved.set_opacity(0)
        vecA_dumb.set_opacity(0)
        labelA_moved.set_opacity(0)
        self.play(FadeOut(vecAB))
        labelAB.set_opacity(0)
        self.wait(3)

        self.play(Transform(vecB_dumb, vecB_moved), FadeIn(labelB_moved),run_time=3)        
        self.play(GrowArrow(vecAB), FadeIn(labelBA),run_time=5)
        self.wait(3)

        self.play(FadeOut(labelBA))
        vecA_moved.set_opacity(1)
        vecA_dumb.set_opacity(1)
        labelA_moved.set_opacity(1)

        # Mostrar que A + B = B + A
        text = MathTex("A + B = B + A").to_edge(RIGHT)
        self.play(Write(text))
        self.wait(2)