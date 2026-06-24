ext = parent()

def onStart():

	# reset selection
	const = op("/project1/knob_ui/selection")
	seq = const.seq.const
	for chan in seq:
		chan.par.value = 0


	# recreate knob labels
	comp = op("knob1") 
	update_range = [1,17]
	scope = op("/project1/engine/noise1")
	run(f"{ext}.LabelKnob(args[0], args[1], args[2])", comp, update_range, scope, delayFrames=120)

	#recreate knob colors
	table = op("knob_settings")
	all_knobs = [knob.name for knob in parent().findChildren(tags=["knob"])]
	
	for knob in all_knobs:
		knob_color = [table[knob, "Knoblevelcolorr"], table[knob, "Knoblevelcolorg"], table[knob, "Knoblevelcolorb"]]
		ext.ChangeKnobColor(knob, knob_color)
	


	return

def onCreate():
	return

def onExit():
	# parent().StoreCurrentValues(param_name="Knoblevelcolorr")
	# parent().StoreCurrentValues(param_name="Knoblevelcolorg")
	# parent().StoreCurrentValues(param_name="Knoblevelcolorb")
	# parent().StoreCurrentValues(param_name="Mfthue")
	# parent().StoreCurrentValues(param_name="Bindparameterref")
	# parent().StoreCurrentValues(param_name="Value0")
	parameter_list = [param.val for param in op('knob_settings').row(0)[1:]]

	for param in parameter_list:
		for knob in parent().findChildren(tags=["knob"]):
			parent().StoreSettings(param, knob)
	return

def onFrameStart(frame):
	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return

	