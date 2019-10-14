from __future__ import annotations
import G
from component import Component
import pyvmath as pm
import math


class Camera(Component):

    targetShowcaseIndex: int = -1
    targetTexture = None  # pyxie.texture
    camera = None  # pyxie.camera

    def init(self):
        self.camera = G.px.camera(self.go.name)
        self.camera.lockon = False
        pass

    def start(self):
        pass

    def render(self):
        if self.camera is None:
            return

        if self.targetShowcaseIndex >= 0:
            self.camera.shoot(G.SHOWCASES[self.targetShowcaseIndex], clearColor=True)

        if self.targetTexture is not None:
            self.camera.shoot(
                G.SHOWCASES[self.targetShowcaseIndex],
                target=self.targetTexture,
                clearColor=True,
            )
        pass

    def update(self):
        cam = self.camera
        rot = pm.normalize(
            pm.quat_rotation(0)
            * pm.quat_rotationZ(math.radians(self.transform.rotation.z))
            * pm.quat_rotationY(math.radians(self.transform.rotation.y))
            * pm.quat_rotationX(math.radians(self.transform.rotation.x))
        )
        cam.rotation = rot
        cam.position = self.transform.position
        pass
