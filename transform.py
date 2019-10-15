from __future__ import annotations
import G
import component
import pyvmath as pm
import math


class Transform(component.Component):

    position: pm.vec3
    rotation: pm.vec3
    scale: pm.vec3

    def __init__(self):
        super().__init__()
        self.position = pm.vec3(0, 0, 0)
        self.rotation = pm.vec3(0, 0, 0)
        self.scale = pm.vec3(1, 1, 1)

    def update(self):
        pass

    @property
    def calculated_quarternion(self) -> pm.vec4:
        rot = pm.normalize(
            pm.quat_rotation(0)
            * pm.quat_rotationZ(math.radians(self.rotation.z))
            * pm.quat_rotationY(math.radians(self.rotation.y))
            * pm.quat_rotationX(math.radians(self.rotation.x))
        )
        return rot
