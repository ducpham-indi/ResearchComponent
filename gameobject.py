from __future__ import annotations
import typing
from component import *


class GameObject:
    components: typing.Set

    def __init__(self, name):
        self.components = set()
        pass

    def add_component(self, component_type, *params):
        if not issubclass(component_type, Component):
            return

        component = component_type(self, *params)
        self.components.add(component)
        pass
