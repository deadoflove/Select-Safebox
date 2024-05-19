##add

if app.SELECT_SAFEBOX:
	import uiselectsafebox
	
#search:

		self.wndGuildBuilding = None

#add:

		if app.SELECT_SAFEBOX:
			self.wndSelectSafebox = None
			
#search:

		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.SetDragonSoulRefineWindow(self.wndDragonSoulRefine)
			self.wndDragonSoulRefine.SetInventoryWindows(self.wndInventory, self.wndDragonSoul)
			self.wndInventory.SetDragonSoulRefineWindow(self.wndDragonSoulRefine)
		
#add:
		
		if app.SELECT_SAFEBOX:
			self.wndSelectSafebox = uiselectsafebox.UiSelectSafebox()
			self.wndSelectSafebox.BindInterfaceClass(self)
			self.wndSelectSafebox.Hide()

#search:

		# ACCESSORY_REFINE_ADD_METIN_STONE
		if self.wndItemSelect:
			self.wndItemSelect.Destroy()
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE
		
#add:

		if app.SELECT_SAFEBOX:
			if self.wndSelectSafebox:
				self.wndSelectSafebox.Destroy()
				
#search:

		del self.wndItemSelect
		
#add:

		if app.SELECT_SAFEBOX:
			del self.wndSelectSafebox
			
#search

	def __HideWindows(self):
		
#add before:

	if app.SELECT_SAFEBOX:
		def OpenSelectSafebox(self):
			if False == player.IsObserverMode():
				if self.wndSelectSafebox:
					if self.wndSelectSafebox.IsShow():
						self.wndSelectSafebox.Close()
					else:
						self.wndSelectSafebox.Show()

		def CloseSelectSafebox(self):
			if self.wndSelectSafebox:
				self.wndSelectSafebox.Close()

#search

		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			hideWindows += self.wndDragonSoul,\
						self.wndDragonSoulRefine,

#add:

		if app.SELECT_SAFEBOX:
			if self.wndSelectSafebox:
				hideWindows += self.wndSelectSafebox,
