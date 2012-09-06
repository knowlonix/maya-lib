# Maya Deformer Node Skeleton Base
# Dan Knowlton 2012
# Based on sample deformers from the Autodesk Maya devkit (yTwistNode.py)

import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

# TODO change the nodeName
kPluginNodeTypeName = "nodeName"

# Todo change the nodeName to above and the ID number to be unique.
nodeNameId = OpenMaya.MTypeId(0x8702)

class nodeName(OpenMayaMPx.MPxDeformerNode):
	"""
	The deformer node structure.
	"""

	def __init__(self):
		OpenMayaMPx.MPxDeformerNode.__init__(self)

	def deform(self, dataBlock, geomIter, matrix, multiIndex):
		"""
		The main deform method. Main structure will be to update the vertex 
		positions in the passed in geomIter object.
		"""

		# Get the envelope value. This value is attached to every deformer node
		# and is a scale 0-1 of the deformer's influence on the base geometry.
		envelope = OpenMayaMPx.cvar.MPxDeformerNode_envelope
		envelopeHandle = dataBlock.inputValue(envelope)
		envelopeValue = envelopeHandle.asFloat()

		# Loop over the provided geometry and make any changes to the vertex
		# positions.
		while not geomIter.isDone():
			# Get the point location in object space.
			point = geomIter.position()

			# TODO transform the point to new deformed location. Remember to 
			# multiply in the envelope value.

			# Set the point's new position.
			geomIter.setPosition(point)

			geomIter.next()

def nodeCreator():
	# TODO change this node name
	return OpenMayaMPx.asMPxPtr(nodeName)

def nodeInitializer():
	# Initialize the node attributes



