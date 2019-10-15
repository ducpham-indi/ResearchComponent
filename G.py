from typing import TYPE_CHECKING
from pyxie import *
from pyvmath import *
import pyxie.apputil.graphicsHelper as graphicHelper
from gameobject import GameObject
from component import Component
from scene import Scene
import pyxie as px

CAMERA = 1
ELAPSED_TIME = 0.03
DT = 0.03
SHOWCASES = list()
SCENE: Scene = None
