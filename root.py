import time, os, os.path
import G
import gameloader
import components
import source.main
import source.autorot

G.window(True, 480, 640)

# TODO: CHANGE MAIN HERE, WE NOT USING IT AT ALL
o2 = gameloader.load_scripts("/source/", "main", "main.py")

# should work tbh
# scene = loadscene()

# init the showcases
for i in range(0, 8):
    G.SHOWCASES.append(G.showcase("3dcase"))
# showcase2D = G.px.showcase("2dcase")

gameobjects = set()

o1 = G.GameObject("Camera Object")
cam = o1.add_component(components.Camera)
o2 = G.GameObject("Gameplay object")
main = o2.add_component(source.main.Main)
main.setup(cam)

o3 = G.GameObject("Figure")
figure = o3.add_component(
    components.Figure,
    "Sapphiart/Sapphiart",
    ["Sapphiart@idle", "Sapphiart@walk", "Sapphiart@running"],
)
figure.change_anim("Sapphiart@running")

o3.transform.position = G.vec3(0, 0, 0)
o3.transform.rotation = G.vec3(0, 0, 0)

# o1.add_component(source.autorot.AutoRot)
o1.transform.position = G.vec3(0, 5, -10)
o1.transform.rotation = G.vec3(-20, 180, 0)

gameobjects.add(o1)
gameobjects.add(o2)
gameobjects.add(o3)

while True:

    G.DT = G.ELAPSED_TIME = G.getElapsedTime()

    moveVector = G.vec3(0.0, 0.0, 0.0)

    touch = G.singleTouch()
    if touch is not None:
        if touch["is_pressed"]:
            print("ASDASDSD")
        moveVector = G.vec3(
            touch["cur_x"] - touch["org_x"], 0, -(touch["cur_y"] - touch["org_y"])
        )
        moveVector = G.vec3(cam.camera.viewInverseMatrix * moveVector)

    for go in gameobjects:
        go.start()  # start inactivated components

    for go in gameobjects:
        go.update()  # update the components

    for go in gameobjects:
        go.try_render_camera()  # render the camera components

    G.swap()
