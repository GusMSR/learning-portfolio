from manim import *

class combinacionCanonicos(Scene):
    def construct(self):
        # Ejes
        ax = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 8, 1],
            x_length=8,
            y_length=6,
            tips=True,
            axis_config={"include_numbers": True, "font_size": 24}
        )
        self.play(Create(ax))

        # Vectores A, B y X
        A = np.array([1, 0, 0])
        B = np.array([0, 1, 0])
        X = np.array([6, 7, 0])

        vecA = Arrow(start=ax.get_origin(), end=ax.c2p(*A), buff=0, color=BLUE)
        vecB = Arrow(start=ax.get_origin(), end=ax.c2p(*B), buff=0, color=GREEN)
        vecX = Arrow(start=ax.get_origin(), end=ax.c2p(*X), buff=0, color=RED)

        labelA = MathTex(r"e_{1}", color=BLUE).next_to(vecA.get_end())
        labelB = MathTex(r"e_{2}", color=GREEN).next_to(vecB.get_end())
        labelX = MathTex("X", color=RED).next_to(vecX.get_end())

        self.play(GrowArrow(vecA), FadeIn(labelA))
        self.play(GrowArrow(vecB), FadeIn(labelB))
        self.play(GrowArrow(vecX), FadeIn(labelX))
        self.wait(2)

        # Quitar números excepto el 0
        for num in ax.x_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        for num in ax.y_axis.numbers:
            if float(num.get_value()) != 0:
                num.set_opacity(0)
        self.wait(1)

        # --- Líneas punteadas de referencia (direcciones de A y B) ---
        origin = ax.get_origin()
        pA = ax.c2p(*A)
        pB = ax.c2p(*B)
        pX = ax.c2p(*X)

        # Direcciones
        dir_A = pA - origin
        dir_B = pB - origin

        # Rectas principales (dirección A y B pasando por el origen)
        line_A = DashedLine(origin - 10*dir_A, origin + 10*dir_A, color=BLUE, stroke_opacity=0.5)
        line_B = DashedLine(origin - 10*dir_B, origin + 10*dir_B, color=GREEN, stroke_opacity=0.5)

        self.play(Create(line_A), Create(line_B))
        self.wait(1)

        # --- Paralelas pasando por X ---
        line_A_through_X = DashedLine(pX - 10*dir_A, pX + 10*dir_A, color=BLUE)
        line_B_through_X = DashedLine(pX - 10*dir_B, pX + 10*dir_B, color=GREEN)

        self.play(Create(line_A_through_X), Create(line_B_through_X))
        self.wait(1)

        # --- Intersecciones ---
        # Intersección de (line_A) con (line_B_through_X) -> λA
        # Intersección de (line_B) con (line_A_through_X) -> μB
        # Usamos álgebra lineal para resolver
        def intersect(p1, d1, p2, d2):
            """Devuelve el punto de intersección de dos rectas paramétricas p1+t*d1 y p2+s*d2"""
            M = np.column_stack([d1, -d2])
            t, s = np.linalg.lstsq(M, p2 - p1, rcond=None)[0]
            return p1 + t*d1

        inter_lambdaA = intersect(origin, dir_A, pX, dir_B)
        inter_muB = intersect(origin, dir_B, pX, dir_A)

        dot_lambdaA = Dot(inter_lambdaA, color=BLUE)
        dot_muB = Dot(inter_muB, color=GREEN)

        self.play(FadeIn(dot_lambdaA), FadeIn(dot_muB))
        self.wait(2)

        # Etiquetas
        label_lambdaA = MathTex(r"\lambda e_{1}", color=BLUE).next_to(dot_lambdaA, LEFT)
        label_muB = MathTex(r"\mu e_{2}", color=GREEN).next_to(dot_muB, UP)

        self.play(FadeIn(label_lambdaA), FadeIn(label_muB))
        self.wait(2)


        # --- Punto de intersección = combinación lineal ---
        # Resolver X = λA + μB
        A2d = np.array([A[0], A[1]])
        B2d = np.array([B[0], B[1]])
        X2d = np.array([X[0], X[1]])

        M = np.column_stack([A2d, B2d])   # matriz [A | B]
        lambd, mu = np.linalg.solve(M, X2d)

        # Puntos en coordenadas de manim
        p_lambdaA = ax.c2p(*(lambd * A2d))
        p_X = ax.c2p(*X2d)

        dot_inter = Dot(p_X, color=YELLOW)
        self.play(FadeIn(dot_inter))

        # Vectores escalados desde el origen
        lambdaA = Arrow(start=ax.get_origin(), end=p_lambdaA, buff=0, color=BLUE_B)
        muB = Arrow(start=p_lambdaA, end=p_X, buff=0, color=GREEN_B)

        label_lambdaA = MathTex(r"\lambda e_{2}", color=BLUE_B).next_to(p_lambdaA, LEFT)
        label_muB = MathTex(r"\mu e_{2}", color=GREEN_B).next_to(p_X, UP)

        self.play(GrowArrow(lambdaA))
        self.play(GrowArrow(muB), FadeIn(label_muB))
        self.wait(3)

