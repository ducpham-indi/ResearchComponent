from component import Component
import G
import components


class Main(Component):

    cam = None  # components.Camera

    def start(self):
        print("HELLO WORLD!")

        cam = G.GameObject.Create("Camera Object").add_component(
            components.Camera(targetShowcaseIndex=0)
        )

        G.GameObject.Create("Ground").add_component(
            components.Quad(8, 8, "resources/images/Dirt-2290", (0, 1, 0))
        )

        for x in range(0, 5):
            for y in range(0, 5):
                pos = G.vec3(x - 2, 0, y - 2)
                o = G.GameObject.Create("Figure")
                o.add_component(
                    components.Quad(8, 8, "resources/images/Dirt-2290", (0, 1, 0))
                )
                figure = o.add_component(
                    components.Figure(
                        "Sapphiart/Sapphiart",
                        ["Sapphiart@idle", "Sapphiart@walk", "Sapphiart@running"],
                    )
                )

                figure.change_anim("Sapphiart@running")

                figure.transform.position = pos
                figure.transform.rotation = G.vec3(0, 0, 0)
                figure.transform.scale = G.vec3(1, 1, 1)

        # o1.add_component(source.autorot.AutoRot)
        cam.transform.position = G.vec3(0, 5, -10)
        cam.transform.rotation = G.vec3(-20, 180, 0)

        print("OBJECT CREATION COMPLETED")

        pass

    def update(self):
        pass
