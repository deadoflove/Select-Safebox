import uiScriptLocale
WND_WIDTH = 250
WND_HEIGTH = 130
window = { "name" : "SelectSafebotdDialog", "style" : ("movable", "float",), 
	"x" : (SCREEN_WIDTH/2) - (WND_WIDTH/2),
	"y" : (SCREEN_HEIGHT/2) - (WND_HEIGTH/2),
	"width" : WND_WIDTH, "height" : WND_HEIGTH,
	"children" :
	(
		{ "name" : "board", "type" : "board", "x" : 0, "y" : 0, "width" : WND_WIDTH, "height" : WND_HEIGTH,
			"children" :
			(
				{ "name" : "titlebar", "type" : "titlebar", "style" : ("attach",), "x" : 8, "y" : 8, "width" : WND_WIDTH-16, "color" : "red",
					"children" :
					(
						{ "name" : "TitleName", "type" : "text", "x" : (WND_WIDTH-16)/2, "y" : 3, "text" : uiScriptLocale.SELECT_SAFEBOX_DEC, "text_horizontal_align":"center" },
					),
				},
				{ "name" : "Desc", "type" : "text", "x" : WND_WIDTH/2, "y" : WND_HEIGTH/3+3, "text" : uiScriptLocale.SELECT_SAFEBOX_DEC, "text_horizontal_align":"center" },
				{ "name" : "safebox_button", "type" : "button", "x" : WND_WIDTH/2 - 61 - 5, "y" : WND_HEIGTH/2 +10, "text" : uiScriptLocale.SAFE_TITLE,
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{ "name" : "mall_button", "type" : "button", "x" : WND_WIDTH/2 + 5, "y" : WND_HEIGTH/2+10, "text" : uiScriptLocale.SAFE_TITLE,
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}
