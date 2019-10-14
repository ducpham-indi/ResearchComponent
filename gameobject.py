from __future__ import annotations
from typing import TypeVar
import typing
import component as comp

# import G
import components
import transform

T = TypeVar("T")


class GameObject:

    __components: typing.Set
    __camera = None
    transform: transform.Transform = None

    def __init__(self, name: str):
        self.__components = set()
        self.__started = False
        self.name = name
        self.transform = self.add_component(transform.Transform)
        self.transform.transform = self.transform
        pass

    def add_component(self, T, *params) -> T:
        if not issubclass(T, comp.Component):
            return None

        component = T(self, *params)
        self.__components.add(component)

        if T == components.Camera:
            self.__camera = component

        return component

    def start(self):
        for co in self.__components:
            co._start()

    def update(self):
        for co in self.__components:
            co._update()

    def try_render_camera(self):
        if self.__camera is None:
            return

        cam: components.Camera = self.__camera
        cam.render()
