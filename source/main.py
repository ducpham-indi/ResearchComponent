import typing
import G
from .sapphi import Sapphi


class Main(G.Component):

    cam = None  # components.Camera
    objects: typing.List[G.GameObject]

    def start(self):
        self.objects = list()

        cam = G.GameObject("Camera Object")
        cam = cam.add_component(G.components.Camera(targetShowcaseIndex=0))
        cam.transform.position = G.vec3(0, 5, -10)
        cam.transform.rotation = G.vec3(-20, 180, 0)

        ground = G.GameObject("Ground")
        ground = ground.add_component(
            G.components.Quad(8, 8, "resources/images/Dirt-2290")
        )

        for x in range(0, 5):
            for y in range(0, 5):
                pos = G.vec3(x - 2, 0, y - 2)

                fig = G.GameObject("fig").add_component(Sapphi())
                fig.transform.position = pos
                fig.transform.rotation = G.vec3(0, 0, 0)
                fig.transform.scale = G.vec3(1, 1, 1)
                self.objects.append(fig.go)

        self.coroutines.start(self.co_start())

    def co_start(self):
        for o in self.objects:
            yield from self.coroutines.co_wait(1)
            o.kill()

    def update(self):
        pass
