from manim import *

class IntervalosCerrando(Scene):
    def construct(self):
        # Eje real de 0 a 1
        eje = NumberLine(
            x_range=[0, 1, 0.1],
            length=8,
            include_numbers=True,
            decimal_number_config={"num_decimal_places": 2},
        )
        self.play(Create(eje))

        # Intervalos anidados (0, 1/n)
        ns = [2, 3, 4, 5]
        intervalos = [(0, 1/n) for n in ns]
        colores = [BLUE, GREEN, YELLOW, RED]

        grupos = []
        for (a, b), c in zip(intervalos, colores):
            # Paréntesis
            paren_izq = Tex("(", font_size=60, color=c).move_to(eje.n2p(a) + DOWN*0.3)
            paren_der = Tex(")", font_size=60, color=c).move_to(eje.n2p(b) + DOWN*0.3)

            # Segmento
            segmento = Line(eje.n2p(a), eje.n2p(b), color=c, stroke_width=6)

            grupos.append(VGroup(paren_izq, segmento, paren_der))

        # Texto inclusiones abajo
        texto = MathTex(
            "(0,1/2) \\supseteq (0,1/3) \\supseteq (0,1/4) \\supseteq (0,1/5)"
        )
        texto.next_to(eje, DOWN, buff=1.2)

        # Animación de los intervalos acumulándose
        for g in grupos:
            self.play(Create(g))
            self.wait(0.5)

        self.play(Write(texto))
        self.wait(2)
