from __future__ import annotations
from typing import TypeVar
from typing import TYPE_CHECKING

import typing
import component as comp
import components
import transform
import G

if TYPE_CHECKING:
    T = TypeVar("T")


class GameObject:

    __components: typing.Set
    __camera = None
    transform: transform.Transform = None
    __dead: False

    @staticmethod
    def Create(name):
        go = GameObject(name)
        G.SCENE.add_gameobject(go)
        return go

    def __init__(self, name: str):
        self.__components = set()
        self.__started = False
        self.name = name
        self.transform = self.add_component(transform.Transform())
        self.transform.transform = self.transform
        self.__dead = False
        pass

    def add_component(self, component: T) -> T:
        t = type(component)
        if not issubclass(t, comp.Component):
            return None

        if t == components.Camera:
            self.__camera = component

        self.__components.add(component)
        component.go = self
        component.transform = self.transform

        return component

    def add_component_type(self, T, *params) -> T:
        if not issubclass(T, comp.Component):
            return None

        component = T(self, *params)
        self.__components.add(component)

        if T == components.Camera:
            self.__camera = component

        return component

    def awake(self):
        for co in self.__components:
            co._awake()

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

    def kill(self):
        if self.__dead:
            return
        self.__dead = True
        for co in self.__components:
            co._kill()
        del self

    @property
    def dead(self):
        return self.__dead
