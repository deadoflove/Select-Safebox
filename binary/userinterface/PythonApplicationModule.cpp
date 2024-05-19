// 1) Search: search at the end 

}

// 2) before its end make a new line and paste:

#ifdef ENABLE_SELECT_SAFEBOX
	PyModule_AddIntConstant(poModule, "SELECT_SAFEBOX", true);
#else
	PyModule_AddIntConstant(poModule, "SELECT_SAFEBOX", false);
#endif


// Example:

#ifdef ENABLE_SELECT_SAFEBOX
	PyModule_AddIntConstant(poModule, "SELECT_SAFEBOX", true);
#else
	PyModule_AddIntConstant(poModule, "SELECT_SAFEBOX", false);
#endif

}