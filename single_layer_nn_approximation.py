from manim import *
import numpy as np

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
        approx_f_1 = axes.plot(lambda x: 0.4451 * np.atan(64.3133 * x + -2.5594) + 1.2437, color=RED)
        approx_f_2 = axes.plot(lambda x: 34.2915 * np.atan(-2.5181 * x + -0.2240) + 33.4087 * np.atan(2.7962 * x + 0.2092) + 1.7555, color=RED)
        approx_f_3 = axes.plot(lambda x: -19.1674 * np.atan(-2.5665 * x + -0.2488) + -0.3680 * np.atan(-17.8906 * x + -18.3226) + -20.6059 * np.atan(2.0819 * x + 0.2856) + 1.6079, color=RED)
        approx_f_4 = axes.plot(lambda x: 24.0804 * np.atan(-1.4839 * x + -0.8128) + -93.8521 * np.atan(0.9048 * x + -0.4774) + -170.3697 * np.atan(-0.3467 * x + 0.6858) + -55.6373 * np.atan(-1.0170 * x + 0.0378) + 80.1597, color=RED)
        approx_f_5 = axes.plot(lambda x: 3.6031 * np.atan(3.2432 * x + -4.1398) + -2.6883 * np.atan(2.8064 * x + -1.7066) + -3.3040 * np.atan(2.5876 * x + 1.5902) + 3.7498 * np.atan(2.4878 * x + 0.0076) + -2.7125 * np.atan(-3.3972 * x + -4.3498) + 2.6676, color=RED)

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
            color=RED, font_size=40
        ).to_edge(UP).shift(UP * 0.5)

        plot = VGroup(axes, f, approx_f_1, x_labels, y_labels, equation)
       
        self.add(plot)
        self.wait(2)  # Esperar 2 segundos antes de la transición

    

        # Transiciones de approx_f_1 a approx_f_2, approx_f_3, approx_f_4 y approx_f_5
        self.play(Transform(approx_f_1, approx_f_2), equation.animate.become(MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{2} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED, font_size=40).to_edge(UP).shift(UP * 0.5)))
        self.wait(2)  # Esperar 2 segundos después de la transición

        self.play(Transform(approx_f_1, approx_f_3), equation.animate.become(MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{3} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED, font_size=40).to_edge(UP).shift(UP * 0.5)))
        self.wait(2)  # Esperar 2 segundos después de la transición

        self.play(Transform(approx_f_1, approx_f_4), equation.animate.become(MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{4} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED, font_size=40).to_edge(UP).shift(UP * 0.5)))
        self.wait(2)  # Esperar 2 segundos después de la transición

        self.play(Transform(approx_f_1, approx_f_5), equation.animate.become(MathTex(
            r"\hat{f}(x) = \sum_{i=1}^{5} w^{(2)}_i \cdot \tan^{-1} \left( w^{(1)}_i x + b^{(1)}_i \right) + b^{(2)}",
            color=RED, font_size=40).to_edge(UP).shift(UP * 0.5)))
        self.wait(2)  # Esperar 2 segundos después de la transición


if __name__ == "__main__":
    config.output_file = "output/single_layer_nn_approximation.mp4"
    config.frame_rate = 30
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.save_last_frame = True
    config.save_pngs = True
    config.pngs_folder = "output/pngs"
    scene = SingleLayerNNApproximation()
    scene.render()