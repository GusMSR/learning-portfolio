from manim import *

class CirclesPartition(Scene):
    def construct(self):
        # Plano cartesiano
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_color": TEAL, "stroke_opacity": 0.1}
        )
        self.add(plane)

        # Origen
        origin = ORIGIN
        o_dot = Dot(origin, color=WHITE)
        o_label = MathTex("0").next_to(o_dot, DOWN, buff=0.1)
        self.play(FadeIn(o_dot), Write(o_label))

        # Radios (clases de equivalencia: círculos)
        radii = [1.0, 2.0, 3.0]
        circles = VGroup(*[Circle(radius=r, stroke_width=2).move_to(origin) for r in radii])

        # Colorear y animar la creación de los círculos
        colors = [BLUE, GREEN, YELLOW]
        for circ, col in zip(circles, colors):
            circ.set_stroke(col)
            self.play(Create(circ), run_time=0.8)

        # Elegimos un radio para p y q (mismo radio -> misma clase)
        r = 2.0
        # Coordenadas angulares para p y q
        angle_p = 30 * DEGREES
        angle_q = 160 * DEGREES

        p_pos = np.array([r * np.cos(angle_p), r * np.sin(angle_p), 0])
        q_pos = np.array([r * np.cos(angle_q), r * np.sin(angle_q), 0])

        # Puntos p y q, flechas desde el origen y etiquetas
        p_dot = Dot(p_pos, color=RED)
        q_dot = Dot(q_pos, color=RED)
        p_label = MathTex("p").next_to(p_dot, UR, buff=0.1)
        q_label = MathTex("q").next_to(q_dot, UL, buff=0.1)

        arrow_p = Arrow(origin, p_pos, buff=0, stroke_width=2)
        arrow_q = Arrow(origin, q_pos, buff=0, stroke_width=2)

        # Mostrar p y q con sus flechas
        self.play(GrowFromCenter(p_dot), Write(p_label), Create(arrow_p))
        self.play(GrowFromCenter(q_dot), Write(q_label), Create(arrow_q))

        # Mostrar la igualdad de normas
        eq_text = MathTex(r"\lVert p\rVert = \lVert q\rVert").to_edge(UP)
        self.play(Write(eq_text))

        # Animación que resalta que p y q pertenecen al mismo círculo:
        # primero resaltamos el círculo r=2
        circ_highlight = Circle(radius=r).move_to(origin).set_stroke(width=6, color=ORANGE)
        self.play(Indicate(circ_highlight), run_time=1.2)

        # Animación opcional: mover p alrededor del círculo y mostrar que su norma no cambia
        path = Circle(radius=r).move_to(origin)
        mover = p_dot.copy()
        self.play(MoveAlongPath(mover, path), run_time=3)
        # mostrar que mover sobre el círculo mantiene misma distancia al origen
        dist_text = MathTex(r"\text{Clase de equivalencia: } \{ x \in \mathbb{R}^2 : \lVert x\rVert =", f"{r} \\").to_edge(DOWN)
        self.play(Write(dist_text))

        # Fade out final dejando plano y círculos
        self.wait(1.0)
        self.play(
            FadeOut(mover),
            circ_highlight.animate.set_opacity(0),
            run_time=0.6
        )
        self.wait(1.2)
