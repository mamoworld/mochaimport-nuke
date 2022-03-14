import nuke
import nuke.rotopaint as rp

def getLayersAsList(curves):
    return getLayersAsListHelper(curves.rootLayer,[curves.rootLayer])

def getLayersAsListHelper(layer, list):
    for i in layer:
        x = i.getAttributes()  
        if isinstance(i, nuke.rotopaint.Shape):
            list.append(i)
        if isinstance(i, nuke.rotopaint.Stroke):
            list.append(i) 
        if isinstance(i, nuke.rotopaint.Layer):
            list.append(i)
            getLayersAsListHelper(i, list)
    return list


def layerListToLayerNameList(layerList):
    return map(lambda x: x.name,layerList)
