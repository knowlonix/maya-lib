import math, sys

import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeTypeName = "curveCycleNode"

curveCycleNodeId = OpenMaya.MTypeId(0x8743)

# Node definition
class curveCycleNode(OpenMayaMPx.MPxNode):
    # class variables
    time_ = OpenMaya.MObject()
    inputCurve_ = OpenMaya.MObject()
    timesOnGround_ = OpenMaya.MObject()
    outputKnotX_ = OpenMaya.MObject()
    outputKnotY_ = OpenMaya.MObject()
    outputKnotZ_ = OpenMaya.MObject()
    outputKnot_ = OpenMaya.MObject()

    # constructor
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
    # deform
    def compute(self, plug, dataBlock):
        return 1
                
# creator
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( curveCycleNode() )

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

    curveCycleNode.timesOnGround_ = nAttr.create("timesOnGround", "tg", OpenMaya.MFnNumericData.kFloat, 0.0)
    nAttr.setKeyable(True)
    nAttr.setStorable(True)
    nAttr.setReadable(True)
    nAttr.setWritable(True)
    nAttr.setArray(True)
    nAttr.setUsesArrayDataBuilder(True)

    # Set up the location outputKnot
    curveCycleNode.outputKnotX_ = nAttr.create("outKnotX", "okx", OpenMaya.MFnNumericData.kFloat, 0)
    curveCycleNode.outputKnotY_ = nAttr.create("outKnotY", "oky", OpenMaya.MFnNumericData.kFloat, 0)
    curveCycleNode.outputKnotZ_ = nAttr.create("outKnotZ", "okz", OpenMaya.MFnNumericData.kFloat, 0)
    curveCycleNode.outputKnot_ = nAttr.create("outputKnot", "ok", curveCycleNode.outputKnotX_, curveCycleNode.outputKnotY_, curveCycleNode.outputKnotZ_)
    nAttr.setKeyable(False)
    nAttr.setStorable(False)
    nAttr.setReadable(True)
    nAttr.setWritable(False)

    # add attribute
    try:
        curveCycleNode.addAttribute( curveCycleNode.time_ )
        curveCycleNode.addAttribute( curveCycleNode.inputCurve_ )
        curveCycleNode.addAttribute( curveCycleNode.timesOnGround_ )
        curveCycleNode.addAttribute( curveCycleNode.outputKnot_ )
        curveCycleNode.attributeAffects( curveCycleNode.time_, curveCycleNode.outputKnot_ )
        curveCycleNode.attributeAffects( curveCycleNode.inputCurve_, curveCycleNode.outputKnot_ )
        curveCycleNode.attributeAffects( curveCycleNode.timesOnGround_, curveCycleNode.outputKnot_ )
    except:
        sys.stderr.write( "Failed to create attributes of %s node\n", kPluginNodeTypeName )
    
# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Dan Knowlton", "0.1.0")
    try:
        mplugin.registerNode( kPluginNodeTypeName, curveCycleNodeId, nodeCreator, nodeInitializer )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % kPluginNodeTypeName )

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( curveCycleNodeId )
    except:
        sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )
        