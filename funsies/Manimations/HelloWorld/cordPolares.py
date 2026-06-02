from manim import *
import numpy as np

class VectorPolar(Scene):
    def construct(self):
        # --- Ejes ---
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            axis_config={"color": GREY},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))
        self.wait()

        # --- Vector u ---
        u = [3, 2]  # coordenadas (x,y) del vector en el sistema de ejes
        start = axes.get_origin()
        end = axes.c2p(u[0], u[1])
        vector_u = Arrow(start=start, end=end, buff=0, color=BLUE)
        label_u = MathTex(r"\vec{u}").next_to(end, UR)

        self.play(Create(vector_u), Write(label_u))
        self.wait()

        # --- Componentes x e y ---
        comp_x = DashedLine(
            start, 
            axes.c2p(u[0], 0), 
            color=GREEN
        )
        comp_y = DashedLine(
            axes.c2p(u[0], 0), 
            end, 
            color=GREEN
        )

        label_x = MathTex("x").next_to(comp_x, DOWN)
        label_y = MathTex("y").next_to(comp_y, RIGHT)

        self.play(Create(comp_x), Create(comp_y))
        self.play(Write(label_x), Write(label_y))
        self.wait()

        # --- Ángulo θ con el eje x ---
        theta = np.arctan2(u[1], u[0])
        arc = Arc(
            radius=1,             # más pequeño para que no tape todo
            start_angle=0, 
            angle=theta*0.7 , 
            color=YELLOW
        ).move_arc_center_to(start)
        theta_label = MathTex(r"\theta").next_to(arc, RIGHT)

        self.play(Create(arc), Write(theta_label))
        self.wait()
