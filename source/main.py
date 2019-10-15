import typing
import G


class Main(G.Component):

    cam = None  # components.Camera
    objects: typing.List[G.GameObject]

    def start(self):
        self.objects = list()

        cam = G.GameObject.Create("Camera Object").add_component(
            G.components.Camera(targetShowcaseIndex=0)
        )

        G.GameObject.Create("Ground").add_component(
            G.components.Quad(8, 8, "resources/images/Dirt-2290", (0, 1, 0))
        )

        for x in range(0, 5):
            for y in range(0, 5):
                pos = G.vec3(x - 2, 0, y - 2)
                o = G.GameObject.Create("Figure")

                o.transform.position = pos
                o.transform.rotation = G.vec3(0, 0, 0)
                o.transform.scale = G.vec3(1, 1, 1)

                figure = o.add_component(
                    G.components.Figure(
                        "Sapphiart/Sapphiart",
                        ["Sapphiart@idle", "Sapphiart@walk", "Sapphiart@running"],
                    )
                )
                figure.change_anim("Sapphiart@running")

                self.objects.append(o)

        # o1.add_component(source.autorot.AutoRot)
        cam.transform.position = G.vec3(0, 5, -10)
        cam.transform.rotation = G.vec3(-20, 180, 0)

        self.coroutines.start(self.co_start())

    def co_start(self):
        for o in self.objects:
            yield from self.coroutines.co_wait(1)
            o.kill()

    def update(self):
        pass
