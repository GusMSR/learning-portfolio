from manim import *

class MediasInequalities(Scene):
    def construct(self):
        A = np.array([-2.5, 0, 0])
        B = np.array([-0.5, 0, 0 ])
        C = np.array([2.5, 0 , 0 ])
        D = np.array([0, 2.5 , 0 ])
        O = np.array([0, 0, 0])

        labelA = MathTex("A").next_to(A).shift(0.5*DOWN + 0.5*LEFT)
        labelB = MathTex("B").next_to(B).shift(0.5*DOWN + 0.5*LEFT)
        labelC = MathTex("C").next_to(C).shift(0.5*DOWN + 0.5*LEFT)
        labelD = MathTex("D").next_to(D).shift(0.5*UP)
        labelO = MathTex("O").next_to(O).shift(0.5*DOWN + 0.5*LEFT)

        title = Tex(r"Desigualdades de medias con $a,b>0$").to_edge(UP) 
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        self.play(FadeIn(Dot(A)), FadeIn(Dot(B)))

        l1= Line(A, B)
        l2= Line(B, C)

        self.play(FadeIn(l1), run_time = 2)
        self.wait(1)
        self.play(FadeIn(l2), FadeIn(Dot(C)), run_time = 2)
        self.wait(2)

        brace1 = Brace(l1, DOWN)
        label1 = brace1.get_text("a")
        brace2 = Brace(l2, DOWN)
        label2 = brace2.get_text("b")

        self.play(GrowFromCenter(brace1), FadeIn(label1), GrowFromCenter(brace2), FadeIn(label2))
        self.wait(2)
        self.play(FadeOut(brace1), FadeOut(brace2), FadeOut(label1), FadeOut(label2))
        self.wait(1)
        self.play(FadeIn(labelA,labelB, labelC))
        self.wait(1)

        circle = Circle(radius = 2.5)
        self.play(FadeIn(Dot(O)), GrowFromCenter(circle), run_time = 3)
        self.wait(1)
        self.play(FadeIn(labelO), labelA.animate.shift(0.5*LEFT), labelC.animate.shift(0.5*RIGHT))

        l3= Line(O, O+ (2.5*UP))
        self.play(FadeIn(l3), run_time = 2)
        self.wait(1)
        self.play(FadeIn(labelD))
        self.wait(1)
        l4= Line(B, O+ (2.5*UP))
        self.play(FadeIn(l4), run_time = 2)

