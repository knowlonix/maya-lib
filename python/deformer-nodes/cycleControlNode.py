import math, sys

import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeTypeName = "cycleControlNode"

cycleControlNodeId = OpenMaya.MTypeId(0x8733)

# Node definition
class cycleControlNode(OpenMayaMPx.MPxNode):
    # class variables
    inputCurve_ = OpenMaya.MObject()


    # constructor
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
    # deform
    def compute(self, plug, dataBlock):
                
# creator
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( cycleControlNode() )

# initializer
def nodeInitializer():
    # angle
    nAttr = OpenMaya.MFnNumericAttribute()
    tAttr = OpenMaya.MFnTypedAttribute()

    curveCycleNode.time_ = nAttr.create( "time", "t", OpenMaya.MFnNumericData.kDouble, 0.0 )
    nAttr.setKeyable(True)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setWritable(True)

    curveCycleNode.inputCurve_ = tAttr.create("inputCurve", "ic", OpenMaya.MFnData.kNurbsCurve)
    nAttr.setKeyable(True)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setWritable(True)

    curveCycleNode.maxSquash_ = nAttr.create("maxSquash", "sq", OpenMaya.MFnNumericData.kDouble, 1.0 )
    nAttr.setKeyable(True)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setWritable(True)

    curveCycleNode.maxStretch_ = nAttr.create("maxStretch", "st", OpenMaya.MFnNumericData.kDouble, 1.0 )
    nAttr.setKeyable(True)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setWritable(True)

    curveCycleNode.minHeight_ = nAttr.create("minHeight", "mh", OpenMaya.MFnNumericData.kDouble, 0.0 )
    nAttr.setKeyable(True)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setWritable(True)

    curveCycleNode.averageVertical_ = nAttr.create("averageVertical", "av", OpenMaya.MFnNumericData.kDouble, 1.0 )
    nAttr.setKeyable(True)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setWritable(True)

    curveCycleNode.timesOnGround_ = tAttr.create("timesOnGround")






    # add attribute
    try:
        cycleControlNode.addAttribute( cycleControlNode.angle )
        yTwistNodeFloor.attributeAffects( curveCycleNode.angle, outputGeom )
    except:
        sys.stderr.write( "Failed to create attributes of %s node\n", kPluginNodeTypeName )
    
# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Dan Knowlton", "0.1.0")
    try:
        mplugin.registerNode( kPluginNodeTypeName, cycleControlNodeId, nodeCreator, nodeInitializer )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % kPluginNodeTypeName )

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( cycleControlNodeId )
    except:
        sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )
        
