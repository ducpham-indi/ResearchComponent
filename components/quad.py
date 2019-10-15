from __future__ import annotations
import G
from component import Component


class Quad(Component):

    __quad: G.editableFigure

    def __init__(self, width: float, height: float, path: str, normal=(0, 1, 0)):
        super().__init__()
        self.__quad = G.graphicHelper.createSprite(
            width, height, texture=path, normal=normal
        )

    def update(self):
        quad = self.__quad
        quad.rotation = self.transform.rotation
        quad.position = self.transform.position
        quad.scale = self.transform.scale
        pass

    def start(self):
        self.update()
        G.SHOWCASES[0].add(self.__quad)

    def kill(self):
        G.SHOWCASES[0].remove(self.__quad)
