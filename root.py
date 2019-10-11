import time, os, os.path
import gameloader
import G
from components.ground import Ground

G.px.window(True, 480, 640)

# TODO: CHANGE MAIN HERE, WE NOT USING IT AT ALL
main = gameloader.load_scripts("/source/", "main", "main.py")

# should work tbh
# scene = loadscene()


go = G.GameObject("Test gameobject")
go.add_component(Ground, 1, 2, 3)


while True:
    # try:
    # except:  # noqa
    #     # pdb.set_trace()
    #     print(traceback.format_exc())

    G.px.singleTouch()
    G.px.swap()
