#within

class ToolTip(ui.ThinBoard):

#search:

	def AlignHorizonalCenter(self):
		for child in self.childrenList:
			(x, y)=child.GetLocalPosition()
			child.SetPosition(self.toolTipWidth/2, y)

		self.ResizeToolTip()
		
#Add:

	def SetThinBoardSize(self, width, height = 12) :
		self.toolTipWidth = width 
		self.toolTipHeight = height

