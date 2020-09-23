from manimlib.imports import *
import array as arr


# class Function3D(ThreeDScene):
#
#     def get_axis(self, min_val, max_val, axis_config):
#         new_config = merge_config([
#             axis_config,
#             {"x_min": min_val, "x_max": max_val},
#             self.number_line_config,
#         ])
#         return NumberLine(**new_config)
#
#     def construct(self):
#         axes = ThreeDAxes()
#         # sphere = ParametricSurface(
#         #     lambda u, v: np.array([
#         #         u,
#         #         v,
#         #         -u**2 - v**2
#         #     ]), v_min=-4, v_max=4, u_min=-4, u_max=4, checkerboard_colors=[RED_D, RED_A],
#         #     resolution=(15, 32))
#
#         below1 = ParametricFunction(
#             lambda v: np.array([
#                 v,  # -v, -v**2, 0 gives horizontal perpendicularity
#                 -(v-4),
#                 (-v+2)*(v-2) - 2  # This set up gives expected perpendicularity
#             ]), color=RED, t_min=-4, t_max=4, )
#         origin1 = ParametricFunction(
#             lambda v: np.array([
#                 v,  # -v, -v**2, 0 gives horizontal perpendicularity
#                 -(v-4),
#                 (-v+2)*(v-2) # This set up gives expected perpendicularity
#             ]), color=RED, t_min=-4, t_max=4, )
#         above1 = ParametricFunction(
#             lambda v: np.array([
#                 v,  # -v, -v**2, 0 gives horizontal perpendicularity
#                 -(v-4),
#                 (-v+2)*(v-2) + 2 # This set up gives expected perpendicularity
#             ]), color=RED, t_min=-4, t_max=4, )
#
#         below2 = ParametricFunction(
#             lambda v: np.array([
#                 v,
#                 v,
#                 (v-2)**2 - 2
#             ]), color=BLUE, t_min=-4, t_max=4,)
#         origin2 = ParametricFunction(
#             lambda v: np.array([
#                 v,
#                 v,
#                 (v-2) ** 2
#             ]), color=BLUE, t_min=-4, t_max=4, )
#         above2 = ParametricFunction(
#             lambda v: np.array([
#                 v,
#                 v,
#                 (v-2) ** 2 + 2
#             ]), color=BLUE, t_min=-4, t_max=4, )
#
#         cubic = ParametricFunction(
#             lambda v: np.array([
#                 v,
#                 0,
#                 v**3 + v**2 - v + 1
#             ]), color=BLUE, t_min=-4, t_max=4,
#         )
#
#         self.add(axes)
#         ############################ Portion of Function3D
#         self.set_camera_orientation(phi=86 * DEGREES, theta=5 * DEGREES)
#         self.begin_ambient_camera_rotation(rate=0.4)
#         self.play(ShowCreation(below1), ShowCreation(below2))
#         self.wait(3)
#         self.stop_ambient_camera_rotation()
#         self.wait(1)
#         self.play(ReplacementTransform(below1, origin1), ReplacementTransform(below2, origin2))
#         self.wait(1)
#         self.begin_ambient_camera_rotation(rate=0.4)
#         self.wait(3)
#         self.stop_ambient_camera_rotation()
#         self.wait(1)
#         self.play(ReplacementTransform(origin1, above1), ReplacementTransform(origin2, above2))
#         self.wait(1)
#         self.begin_ambient_camera_rotation(rate=0.4)
#         ############################## Portion of CubicFunction
#         # self.set_camera_orientation(phi=86 * DEGREES, theta=5 * DEGREES)
#         # self.begin_ambient_camera_rotation(rate=0.4)
#         # self.play(ShowCreation(cubic))
#         self.wait(5)
#         ############################## Portion of Hyperbola Function3D2
#
#
# class Hyperbola(GraphScene):
#     CONFIG = {
#         "y_max": 50,
#         "y_min": 0,
#         "x_max": 7,
#         "x_min": 0,
#         "y_tick_frequency": 5,
#         "x_tick_frequency": 1,
#         "axes_color": BLUE,
#         "graph_origin": np.array((-5, -2, 0))
#     }
#
#     def construct(self):
#         self.setup_axes()
#         graph = self.get_graph(lambda x: x ** 2,
#                                color=GREEN,
#                                x_min=2,
#                                x_max=4
#                                )
#         self.play(
#             ShowCreation(graph),
#             run_time=2
#         )
#         self.wait()
#
#     def setup_axes(self):
#         # Add this line
#         GraphScene.setup_axes(self)
#         #   Add Animation
#         self.play(
#             ShowCreation(self.x_axis),
#             ShowCreation(self.y_axis)
#         )
#
#
# class Hyperbola3D(ThreeDScene):
#
#     def construct(self):
#         axes = ThreeDAxes()
#         hyperbola = ParametricFunction(
#             lambda v: np.array([
#                 v,
#                 1/math.cos(v),
#                 math.tan(v),
#             ]), color=BLUE, t_min=-PI, t_max=PI,
#         )
#         self.add(axes)
#         self.set_camera_orientation(phi=80 * DEGREES, theta=5 * DEGREES)
#         self.play(ShowCreation(hyperbola))
#         self.wait()


class Parabola(GraphScene):
    CONFIG = {
        "y_max": 20,
        "y_min": -20,
        "x_max": 9,
        "x_min": -9,
        "y_tick_frequency": 5,
        "x_tick_frequency": 1,
        "axes_color": BLUE,
        "graph_origin": np.array((0, 0, 0))
    }

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

    def construct(self):
        self.setup_axes()

        # Tex for equations in upper right corner
        equation1 = TexMobject("y=x^2 - 9")
        equation1.to_edge(UP + RIGHT)

        equation2 = TexMobject("y=x^2")
        equation2.to_edge(UP + RIGHT)

        equation3 = TexMobject("y=x^2 + 9")
        equation3.to_edge(UP + RIGHT)

        # Text for roots on graph
        root1 = TextMobject("{\\tiny -3}")
        root1.move_to(self.coords_to_point(-3, 0), UP*2)

        root2 = TextMobject("{\\tiny 0}")
        root2.move_to(self.coords_to_point(0, 0), UP*2)

        root3 = TextMobject("{\\tiny 3}")
        root3.move_to(self.coords_to_point(3, 0), UP*2)

        # Descriptive text definition
        describe1 = TextMobject("The equation has two distinct real roots")
        describe1.to_edge(DOWN+LEFT)

        describe2 = TextMobject("The equation has two equal real roots")
        describe2.to_edge(DOWN + LEFT)

        describe3 = TextMobject("The equation has imaginary roots")
        describe3.to_edge(DOWN + LEFT)

        # Definition of our equations to plot
        graph1 = self.get_graph(lambda x: x ** 2 - 9,
                                color=GREEN,
                                x_min=-4,
                                x_max=4
                                )
        graph2 = self.get_graph(lambda x: x ** 2,
                                color=GREEN,
                                x_min=-4,
                                x_max=4
                                )
        graph3 = self.get_graph(lambda x: x ** 2 + 9,
                                color=GREEN,
                                x_min=-4,
                                x_max=4
                                )

        # Defining our dots for the roots of the equation
        p = Dot().move_to(self.coords_to_point(-3, 0))
        pback = Dot().move_to(self.coords_to_point(3, 0))

        p1 = Dot().move_to(self.coords_to_point(0, 0))
        p1back = Dot().move_to(self.coords_to_point(0, 0))

        # Playing everything in order
        self.play(ShowCreation(graph1), Write(p), Write(pback), Write(equation1))
        self.play(Write(root1), Write(root3), Write(describe1))
        self.wait(2)

        self.play(ReplacementTransform(graph1, graph2), ReplacementTransform(p, p1),
                  ReplacementTransform(pback, p1back), ReplacementTransform(equation1, equation2),
                  ReplacementTransform(root1, root2), ReplacementTransform(root3, root2),
                  ReplacementTransform(describe1, describe2), run_time=4)
        self.wait(2)
        self.remove(p, pback, p1, p1back, root2)
        self.play(ReplacementTransform(graph2, graph3), ReplacementTransform(equation2, equation3),
                  ReplacementTransform(describe2, describe3), run_time=4)

        ########################################################################
        # Creating an array of equations an including partial equations
        # equations = []
        # equations.append(self.get_graph(lambda x: x ** 2 - 6,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 - 5,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 - 4,
        #                        color=GREEN,
        #                        x_min=-4,
        #                        x_max=4
        #                        ))
        # equations.append(self.get_graph(lambda x: x ** 2 - 3,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 - 2,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 - 1,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 + 1,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 + 2,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 + 3,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 + 4,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 + 5,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        # equations.append(self.get_graph(lambda x: x ** 2 + 6,
        #                                 color=GREEN,
        #                                 x_min=-4,
        #                                 x_max=4
        #                                 ))
        #
        # # Defining arrays for dots
        # dots = [-2.4494, -2.2360, -2, -1.7320, -1.4142, -1, 0]
        # dots_back = [2.4494, 2.2360, 2, 1.7320, 1.4142, 1, 0]
        # # graph = self.get_graph(lambda x: x ** 2,
        # #                        color=GREEN,
        # #                        x_min=-4,
        # #                        x_max=4
        # #                        )
        # p = Dot().move_to(self.coords_to_point(dots[0], 0))
        # p2 = Dot().move_to(self.coords_to_point(dots_back[0], 0))
        # self.play(ShowCreation(equations[0]), Write(p), Write(p2))
        # self.wait()
        # # self.remove(equations[0])
        # for i in range(len(equations) - 1):
        #     self.remove(p, p2)
        #     # Here we try to define the points after each transform to create a uniform movement
        #     if i < len(equations)/2 and i+1 < len(dots):
        #         p = Dot().move_to(self.coords_to_point(dots[i], 0))
        #         pnext = Dot().move_to(self.coords_to_point(dots[i+1], 0))
        #         p2 = Dot().move_to(self.coords_to_point(dots_back[i], 0))
        #         p2next = Dot().move_to(self.coords_to_point(dots_back[i + 1], 0))
        #     self.play(ReplacementTransform(equations[i], equations[i+1]), ReplacementTransform(p, pnext), ReplacementTransform(p2, p2next), run_time=2)
        #     self.remove(p, pnext, p2, p2next)
        # self.play(ReplacementTransform(equations[len(equations)-1], equations[len(equations)-2]))
        ############################################################################


class Parabola3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # sphere = ParametricSurface(
        #     lambda u, v: np.array([
        #         u,
        #         v,
        #         -u**2 - v**2
        #     ]), v_min=-4, v_max=4, u_min=-4, u_max=4, checkerboard_colors=[RED_D, RED_A],
        #     resolution=(15, 32))

        below1 = ParametricFunction(
            lambda v: np.array([
                0,  # -v, -v**2, 0 gives horizontal perpendicularity
                -v,
                (-v)*(v) - 2  # This set up gives expected perpendicularity
            ]), color=RED, t_min=-4, t_max=4, )
        origin1 = ParametricFunction(
            lambda v: np.array([
                0,  # -v, -v**2, 0 gives horizontal perpendicularity
                -(v),
                (-v)*(v) # This set up gives expected perpendicularity
            ]), color=RED, t_min=-4, t_max=4, )
        above1 = ParametricFunction(
            lambda v: np.array([
                0,  # -v, -v**2, 0 gives horizontal perpendicularity
                -(v),
                (-v)*(v) + 2 # This set up gives expected perpendicularity
            ]), color=RED, t_min=-4, t_max=4, )

        below2 = ParametricFunction(
            lambda v: np.array([
                v,
                0,
                v**2 - 2
            ]), color=BLUE, t_min=-3, t_max=3,)
        origin2 = ParametricFunction(
            lambda v: np.array([
                v,
                0,
                v ** 2
            ]), color=BLUE, t_min=-3, t_max=3, )
        above2 = ParametricFunction(
            lambda v: np.array([
                v,
                0,
                v ** 2 + 2
            ]), color=BLUE, t_min=-3, t_max=3, )

        self.add(axes)
        ############################ Portion of Function3D
        self.set_camera_orientation(phi=80 * DEGREES, theta=5 * DEGREES, distance=1000)
        self.begin_ambient_camera_rotation(rate=0.4)
        self.play(ShowCreation(below2), ShowCreation(below1), ShowCreation(p))
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.wait(1)
        self.play(ReplacementTransform(below2, origin2), ReplacementTransform(below1, origin1))
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.wait(1)
        self.play(ReplacementTransform(origin2, above2), ReplacementTransform(origin1, above1))
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=0.4)
        ############################## Portion of CubicFunction
        # self.set_camera_orientation(phi=86 * DEGREES, theta=5 * DEGREES)
        # self.begin_ambient_camera_rotation(rate=0.4)
        # self.play(ShowCreation(cubic))
        self.wait(5)
        ############################## Portion of Hyperbola Function3D2


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -m --video_dir ~/Desktop/  "
    command_B = module_name + " " + "Parabola3D -p"
    os.system(command_A + command_B)
