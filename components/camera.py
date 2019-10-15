from __future__ import annotations
import G
from component import Component
import pyvmath as pm
import math


class Camera(Component):

    targetShowcaseIndex: int = 0
    targetTexture = None  # pyxie.texture
    camera = None  # pyxie.camera

    def __init__(self, targetShowcaseIndex: int):
        super().__init__()
        self.targetShowcaseIndex = targetShowcaseIndex

    def awake(self):
        self.camera = G.px.camera(self.go.name)
        self.camera.lockon = False
        pass

    def render(self):
        if self.camera is None:
            return

        if self.targetShowcaseIndex >= 0:
            self.camera.shoot(G.SHOWCASES[self.targetShowcaseIndex], clearColor=False)

        if self.targetTexture is not None:
            self.camera.shoot(
                G.SHOWCASES[self.targetShowcaseIndex],
                target=self.targetTexture,
                clearColor=False,
            )
        pass

    def update(self):
        cam = self.camera
        cam.rotation = self.transform.calculated_quarternion
        cam.position = self.transform.position
        pass
