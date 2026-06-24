ext = op('/project1/midiFighterTwisterV2')

def onValueChange(channel, sampleIndex, val, prev):
	knob_list = ext.GetSelectedKnobs()
	focus_color_op = op("/project1/knob_ui/focus_knobcolor")
	focus_color_rgb = [color.eval() for color in focus_color_op.chans()]
	
	for knob in knob_list:
		ext.ChangeKnobColor(knob, focus_color_rgb)

	return
	