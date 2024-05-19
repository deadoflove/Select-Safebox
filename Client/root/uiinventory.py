#within

class InventoryWindow(ui.ScriptWindow):

#search:

	def Close(self):
		self.Hide()
		
#Add:

		if app.SELECT_SAFEBOX:
			self.interface.CloseSelectSafebox()

#search

	def ClickMallButton(self):
		print "click_mall_button"
		net.SendChatPacket("/click_mall")

#replace

	def ClickMallButton(self):
		if app.SELECT_SAFEBOX:
			self.interface.OpenSelectSafebox()
		else:
			print "click_mall_button"
			net.SendChatPacket("/click_mall")