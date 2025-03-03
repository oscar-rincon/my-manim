from manim import *

class SingleLayerNNApproximation(Scene):
    def construct(self):
        # Ajustar el tamaño del marco
        self.camera.frame_height = 8.5
        self.camera.frame_width = 14

        # Cambiar el color de fondo a blanco
        self.camera.background_color = WHITE

        # Crear los ejes
        axes = Axes(
            x_range=[-1.05, 1.05, 0.25],  # Ajustar el rango del eje x
            y_range=[-0.6, 2.6, 0.5],  # Ajustar el rango del eje y
            x_length=12,
            y_length=6,
            axis_config={"color": BLACK},  # Cambiar el color de los ejes a negro
            tips=False,
        ).shift(DOWN * 0.7)  # Desplazar los ejes hacia abajo para dejar espacio arriba

        # Función original
        f = axes.plot(lambda x: np.exp(x) + np.sin(5*x), color=BLUE)

        # Funciones de aproximación (ejemplo)
        approx_f_1 = axes.plot(lambda x: 0.4630 * np.atan(57.3259 * x + -1.9612) + 1.2033, color=RED)
        approx_f_2 = axes.plot(lambda x: 39.5405 * np.atan(2.2982 * x + 0.1134) + 41.3316 * np.atan(-2.0346 * x + -0.1264) + 1.7708, color=RED)
        approx_f_3 = axes.plot(lambda x: -244.9229 * np.atan(-0.4151 * x + 0.2063) + -444.7161 * np.atan(-1.0822 * x + 0.0822) + 610.0167 * np.atan(-0.9411 * x + 0.0909) + 31.9190, color=RED)
        approx_f_4 = axes.plot(lambda x: 2.1930 * np.atan(-3.6508 * x + -2.0453) + -6.4635 * np.atan(-1.8571 * x + 0.1619) + 5.4553 * np.atan(-2.0688 * x + 1.1278) + 4.6033 * np.atan(3.8904 * x + -5.0540) + 6.2000, color=RED)
        approx_f_5 = axes.plot(lambda x: 0.0360 * np.atan(-38.2202 * x + 29.2498) + -25.9117 * np.atan(1.4345 * x + 0.8985) + -34.5235 * np.atan(-0.9677 * x + 0.3201) + -34.7587 * np.atan(-0.6725 * x + -0.6112) + 22.3801 * np.atan(-1.6601 * x + 0.8868) + -4.7047, color=RED)

        # Agregar etiquetas a los ejes
        labels = axes.get_axis_labels(x_label="x", y_label=r"f = \exp(x) + \sin(5x)").set_color(BLACK)

        # Agregar valores de guía en los ejes
        x_values = [-1, -0.5, 0.5, 1]
        y_values = [1, 2]
        x_labels = axes.get_x_axis().add_labels({val: str(val) for val in x_values}).set_color(BLACK)
        y_labels = axes.get_y_axis().add_labels({val: str(val) for val in y_values}).set_color(BLACK)

        # Ecuación de la red neuronal de una sola capa en color rojo
        equation = MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{1} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED
        ).to_edge(UP).shift(UP * 0.5)

        plot = VGroup(axes, f, approx_f_1, x_labels, y_labels, equation)
       
        self.add(plot)
        self.wait(2)  # Esperar 2 segundos antes de la transición

    

        # Transiciones de approx_f_1 a approx_f_2, approx_f_3, approx_f_4 y approx_f_5
        self.play(Transform(approx_f_1, approx_f_2), equation.animate.become(MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{2} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED).to_edge(UP).shift(UP * 0.5)))
        self.wait(2)  # Esperar 2 segundos después de la transición

        self.play(Transform(approx_f_1, approx_f_3), equation.animate.become(MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{3} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED).to_edge(UP).shift(UP * 0.5)))
        self.wait(2)  # Esperar 2 segundos después de la transición

        self.play(Transform(approx_f_1, approx_f_4), equation.animate.become(MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{4} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED).to_edge(UP).shift(UP * 0.5)))
        self.wait(2)  # Esperar 2 segundos después de la transición

        self.play(Transform(approx_f_1, approx_f_5), equation.animate.become(MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{5} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED).to_edge(UP).shift(UP * 0.5)))
        self.wait(2)  # Esperar 2 segundos después de la transición

  