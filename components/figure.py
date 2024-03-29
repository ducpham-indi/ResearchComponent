from __future__ import annotations
import G
import pyxie as px
import pyvmath as pm
from component import Component
import typing
import collections
import math


class Figure(Component):

    TRANSITION_TIME = 0.2
    transit_time: float = 0
    animations: typing.List[str]
    animation_indices: typing.Dict[str, int]

    current_animation_index = 0
    next_animation_index = 0

    __figure = None

    def __init__(self, path: str, animations: typing.List[str]):
        super().__init__()

        self.path = path
        self.animations = animations
        self.__figure = G.figure(path)
        self.animations = animations

        self.animations = animations.copy()
        self.animation_indices = dict()
        for i in range(0, len(self.animations)):
            self.animation_indices[self.animations[i]] = i
        self.current_animation_index = self.next_animation_index = 0

        fig = self.__figure
        fig.connectAnimator(px.ANIMETION_SLOT_A0, self.animations[0])
        self.transition_time = 0

    def start(self):
        G.SHOWCASES[0].add(self.__figure)
        self.update()

    def change_anim(self, anim_name):
        index = self.animation_indices.get(anim_name)
        if (
            index < 0
            or index == self.current_animation_index
            or index == self.next_animation_index
        ):
            return

        self.next_animation_index = index
        self.__figure.connectAnimator(px.ANIMETION_SLOT_A1, self.animations[index])
        self.transition_time = 0
        pass

    def update(self):
        self.__figure.step()
        self.__update_transform()
        self.__update_transition()
        pass

    def __update_transform(self):
        fig = self.__figure
        fig.rotation = self.transform.rotation
        fig.position = self.transform.position
        fig.scale = self.transform.scale
        pass

    def __update_transition(self):
        if self.current_animation_index == self.next_animation_index:
            return

        fig = self.__figure

        if self.transition_time >= self.TRANSITION_TIME:
            self.current_animation_index = self.next_animation_index
            fig.connectAnimator(
                px.ANIMETION_SLOT_A0, self.animations[self.current_animation_index]
            )
            self.__figure.connectAnimator(px.ANIMETION_SLOT_A1)
            return

        dt = G.DT
        self.transition_time += dt
        if self.transition_time > self.TRANSITION_TIME:
            self.transition_time = self.TRANSITION_TIME

        self.__figure.setBlendingWeight(
            px.ANIMETION_PART_A, self.transition_time / self.TRANSITION_TIME
        )
        pass

    def kill(self):
        G.SHOWCASES[0].remove(self.__figure)
        pass
