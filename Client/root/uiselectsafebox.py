__author__		= 'DeadOfLove'
__date__		= '2024-19-05'
__name__		= 'Select Safebox'
__version__		= '1.0'
import ui, net, uiToolTip, uiScriptLocale, wndMgr

class UiSelectSafebox(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.buttontooltip = None
		self.ShowButtonToolTip = False

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()
		ui.ScriptWindow.Show(self)

	def BindInterfaceClass(self, interface):
		self.interface = interface

	def __LoadWindow(self):
		try:	
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/selectsafeboxddialog.py")
		except:
			import exception
			exception.Abort("UiSelectSafebox.__LoadScript.LoadObject")
		try:
			self.BoardTitle = self.GetChild("titlebar")
			self.SafeboxButton = self.GetChild("safebox_button")
			self.MallButton = self.GetChild("mall_button")
		except:
			import exception
			exception.Abort("UiSelectSafebox.__LoadScript.LoadObject")
			
		self.BoardTitle.SetCloseEvent(ui.__mem_func__(self.Close))
		self.SafeboxButton.SetEvent(ui.__mem_func__(self.__ClickSafeboxButton))
		self.MallButton.SetEvent(ui.__mem_func__(self.__ClickMallButton))

		self.buttontooltip = uiToolTip.ToolTip()
		self.buttontooltip.ClearToolTip()
		self.SafeboxButton.SetShowToolTipEvent(ui.__mem_func__(self.OverInToolTipButton), uiScriptLocale.SELECT_SAFEBOX_DEC2)
		self.SafeboxButton.SetHideToolTipEvent(ui.__mem_func__(self.OverOutToolTipButton))
		self.MallButton.SetShowToolTipEvent(ui.__mem_func__(self.OverInToolTipButton), uiScriptLocale.MALL_TITLE)
		self.MallButton.SetHideToolTipEvent(ui.__mem_func__(self.OverOutToolTipButton))

	def OverInToolTipButton(self, arg):
		arglen = len(str(arg))
		pos_x, pos_y = wndMgr.GetMousePosition()

		self.buttontooltip.ClearToolTip()
		self.buttontooltip.SetThinBoardSize(6 * arglen)
		self.buttontooltip.SetToolTipPosition(pos_x + 20, pos_y + 55)
		self.buttontooltip.AppendTextLine(arg, 0xffffffff)
		self.buttontooltip.Show()
		self.ShowButtonToolTip = True

	def OverOutToolTipButton(self):
		self.buttontooltip.Hide()
		self.ShowButtonToolTip = False

	def ButtonToolTipProgress(self) :
		if self.ShowButtonToolTip :
			pos_x, pos_y = wndMgr.GetMousePosition()
			self.buttontooltip.SetToolTipPosition(pos_x + 50, pos_y + 50)

	def __ClickSafeboxButton(self):
		net.SendChatPacket("/click_safebox")
		self.Close()

	def __ClickMallButton(self):
		net.SendChatPacket("/click_mall")
		self.Close()

	def Destroy(self):
		self.interface = None
		if self.buttontooltip:
			self.buttontooltip.Hide()
			self.ShowButtonToolTip = False

	def Close(self):
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True

