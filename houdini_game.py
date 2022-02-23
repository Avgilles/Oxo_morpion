import hou
import os
# from hutil.Qt import QtWidgets
from PySide2 import QtUiTools , QtWidgets


place = [
    {'tx': -3.25, 'ty': .5, 'tz': -3.25},
    {'tx': 0, 'ty': .5, 'tz': -3.25},
    {'tx': 3.25, 'ty': .5, 'tz': -3.25},
    {'tx': -3.25, 'ty': .5, 'tz': 0},
    {'tx': 0, 'ty': .5, 'tz': 0},
    {'tx': 3.25, 'ty': .5, 'tz': 0},
    {'tx': -3.25, 'ty': .5, 'tz': 3.25},
    {'tx': 0, 'ty': .5, 'tz': 3.25},
    {'tx': 3.25, 'ty': .5, 'tz': 3.25},
]

scriptPath = 'C:/Users/Gilles AVRAAM/Documents/houdini19.0/scripts'


class GamePlay:
    def __init__(self, name):
        super(GamePlay, self).__init__()
        self.obj_level = hou.node('obj')
        self.geoNode = self.obj_level.createNode('geo', str(name))

    def __str__(self):
        return f"Obj level : {self.obj_level.allChildren()}"

    def grid(self):
        grid = self.geoNode.createNode('grid', "ground")
        grid.setParms({'rows': 4, 'cols': 4})
        polywire = self.geoNode.createNode('polywire')

        merge = self.geoNode.createNode("merge")
        merge.setInput(0, polywire)
        polywire.setInput(0, grid)

        self.addBox(merge)

        outPut = self.geoNode.createNode("null", "OUTPUT")

        outPut.setInput(0, merge)
        self.geoNode.layoutChildren()

        outPut.setDisplayFlag(True)
        outPut.setRenderFlag(True)

    def addBox(self, parent):
        box = self.geoNode.createNode('box', 'test')
        box.setParms(place[8])
        parent.setInput(1, box)


class interface_Oxo:
    def __init__(self):
        super(interface_Oxo, self).__init__()
        self.gamePlay = GamePlay()

    def onCreateInterface(self):
        print("creating interface")
        self.scene_list.clear()

