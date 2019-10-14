from __future__ import annotations
import G
import component
import pyvmath as pm


class Transform(component.Component):

    position: pm.vec3
    rotation: pm.vec3
    scale: pm.vec3

    def init(self):
        self.position = pm.vec3(0, 0, 0)
        self.rotation = pm.vec3(0, 0, 0)
        self.scale = pm.vec3(0, 0, 0)
        pass

    def update(self):
        pass
