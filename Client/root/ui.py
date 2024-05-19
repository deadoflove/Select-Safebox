#within

class Button(Window):

#search:

		self.ToolTipText = None

#Add:

		self.showtooltipevent = None
		self.showtooltiparg = None
		self.hidetooltipevent = None
		self.hidetooltiparg = None

#search:

	def ShowToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Show()

#Add:

		if self.showtooltipevent:
			apply(self.showtooltipevent, self.showtooltiparg)

#search

	def HideToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Hide()

#Add

		if self.hidetooltipevent:
			apply(self.hidetooltipevent, self.hidetooltiparg)

	def SetShowToolTipEvent(self, func, *args):
		self.showtooltipevent = func
		self.showtooltiparg = args

	def SetHideToolTipEvent(self, func, *args):
		self.hidetooltipevent = func
		self.hidetooltiparg = args





