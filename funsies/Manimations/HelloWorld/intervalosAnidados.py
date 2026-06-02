from manim import *

class IntervalosAnidados(Scene):
    def construct(self):
        # Eje real
        eje = NumberLine(
            x_range=[-4, 4, 1],
            length=8,
            include_numbers=True
        )
        self.play(Create(eje))

        # Intervalos anidados
        intervalos = [
            (-3, 3),
            (-2, 2),
            (-1.2, 1.2),
            (-0.6, 0.6)
        ]
        colores = [BLUE, GREEN, YELLOW, RED]

        # Lista de grupos para guardar paréntesis e intervalos
        grupos = []

        for (a, b), c in zip(intervalos, colores):
            # Paréntesis como "}" y "{" rotados para intervalos abiertos
            paren_izq = Tex("(", font_size=60, color=c).move_to(eje.n2p(a) + DOWN*0.3)
            paren_der = Tex(")", font_size=60, color=c).move_to(eje.n2p(b) + DOWN*0.3)

            # Segmento entre los puntos
            segmento = Line(eje.n2p(a), eje.n2p(b), color=c, stroke_width=6)

            grupos.append(VGroup(paren_izq, segmento, paren_der))

        # Texto inclusiones abajo
        texto = MathTex(
            "(a_1,b_1) \\supseteq (a_2,b_2) \\supseteq (a_3,b_3) \\supseteq (a_4,b_4)"
        )
        texto.next_to(eje, DOWN, buff=1.2)

        # Animación: cada intervalo aparece y se queda
        for g in grupos:
            self.play(Create(g))
            self.wait(0.5)

        # Aparece el texto
        self.play(Write(texto))
        self.wait(2)
