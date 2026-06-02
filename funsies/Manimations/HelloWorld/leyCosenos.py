from manim import *

# Longitudes de los lados
a = 4.0   # lado BC
b = 3.5   # lado AC
c = 5.0   # lado AB

class LeyCosenos(Scene):
    def construct(self):
        # --- Construcción inicial ---
        # Colocamos un triángulo con vértices A, B, C
        A = np.array([0, 0, 0])        # vértice A en el origen
        B = np.array([c, 0, 0])        # vértice B sobre eje x
        # Colocamos C usando coordenadas según ley de cosenos inversa
        # Coseno de ángulo en A: (b^2 + c^2 - a^2)/(2bc)
        cosA = (b**2 + c**2 - a**2)/(2*b*c)
        sinA = (1 - cosA**2)**0.5
        C = np.array([b*cosA, b*sinA, 0])

        # Dibujar el triángulo
        tri = Polygon(A, B, C, color=BLUE)
        labels = VGroup(
            Tex("A").next_to(A, DOWN+LEFT),
            Tex("B").next_to(B, DOWN+RIGHT),
            Tex("C").next_to(C, UP)
        )

        self.play(Create(tri), Write(labels))
        self.wait()

        # --- Altura desde C hacia AB ---
        H = np.array([C[0], 0, 0])   # pie de la altura
        altura = DashedLine(C, H, color=YELLOW)
        puntoH = Dot(H, color=YELLOW)
        labelH = Tex("H").next_to(H, DOWN)

        self.play(Create(altura), FadeIn(puntoH), Write(labelH))
        self.wait()

        # --- Subsegmentos ---
        # AH = c - x, BH = x
        seg_AH = Line(A, H, color=GREEN)
        seg_HB = Line(H, B, color=GREEN)

        x_label = MathTex("x").next_to(seg_HB, DOWN)
        cx_label = MathTex("c-x").next_to(seg_AH, DOWN)

        self.play(Create(seg_AH), Create(seg_HB))
        self.play(Write(x_label), Write(cx_label))
        self.wait()

        # --- Lados a, b, c ---
        side_labels = VGroup(
            MathTex("a").next_to(Line(B, C), RIGHT),
            MathTex("b").next_to(Line(A, C), LEFT),
            MathTex("c").next_to(Line(A, B), DOWN)
        )
        self.play(Write(side_labels))
        self.wait()
