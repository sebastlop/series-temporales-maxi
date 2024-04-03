from manim import *

class LeyCoulomb(Scene):
    def construct(self):
        # Configura el sistema de coordenadas tridimensionales
        axes = ThreeDAxes()
        self.add(axes)

        # Crea dos esferas para representar las cargas
        charge1 = Sphere(radius=0.1, color=BLUE).move_to([-2, 0, 0])
        charge2 = Sphere(radius=0.1, color=RED).move_to([2, 0, 0])

        # Agrega las cargas a la escena
        self.add(charge1, charge2)

        # Muestra una flecha para representar la fuerza entre las cargas
        force_arrow = Arrow3D(start=charge1.get_center(), end=charge2.get_center(), color=YELLOW)
        self.add(force_arrow)

        # Agrega una etiqueta para representar la Ley de Coulomb
        coulomb_label = MathTex(r"F = \frac{k \cdot |q_1 \cdot q_2|}{r^2}", color=WHITE).next_to(axes, UP)
        self.add(coulomb_label)

        # Anima la escena
        self.play(ShowCreation(charge1), ShowCreation(charge2), ShowCreation(force_arrow))
        self.wait(2)
