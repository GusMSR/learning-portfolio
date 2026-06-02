from manim import *

class IntervalosInfinitos(Scene):
    def construct(self):
        # Eje real desde 1 hasta 10
        eje = NumberLine(
            x_range=[1, 10, 1],
            length=8,
            include_numbers=False,
            include_tip=True,
        )
        self.play(Create(eje))
        self.wait(0.5)

        # Intervalos [n, ∞)
        ns = [1, 2, 3, 4, 5]
        colores = [BLUE, GREEN, YELLOW, RED, PURPLE]

        grupos = []
        for n, c in zip(ns, colores):
            # Segmento desde n hasta el extremo derecho
            segmento = Line(eje.n2p(n), eje.n2p(10), color=c, stroke_width=6)

            # Corchete izquierdo como MathTex
            corchete_izq = MathTex("[", color=c, font_size=60)
            corchete_izq.next_to(segmento.get_start(), DOWN*0.3)

            # Infinito como MathTex
            infinito = MathTex("\\infty", color=c, font_size=40)
            infinito.next_to(segmento.get_end(), RIGHT*0.2)

            # Grupo del intervalo
            grupos.append(VGroup(corchete_izq, segmento, infinito))

        # Texto de inclusiones abajo (todo en MathTex)
        texto = MathTex(
            "[5,\\infty) \\subseteq [4,\\infty) \\subseteq [3,\\infty) \\subseteq [2,\\infty) \\subseteq [1,\\infty)"
        ).next_to(eje, DOWN, buff=1)

        # Animación de los intervalos desde el más grande al más pequeño
        for g in grupos[::+1]:
            self.play(Create(g))
            self.wait(0.5)

        self.play(Write(texto))
        self.wait(2)
