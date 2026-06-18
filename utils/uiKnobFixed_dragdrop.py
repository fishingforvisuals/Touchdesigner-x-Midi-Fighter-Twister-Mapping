# callbacks for when associated Panel is being dropped on

def onHoverStartGetAccept(comp, info):
	"""
	Called when comp needs to know if dragItems are acceptable as a drop.

	Args:
		comp: the panel component being hovered over
		info: A dictionary containing all info about hover, including:
			dragItems: a list of objects being dragged over comp
			callbackPanel: the panel Component pointing to this callback DAT

	Returns:
		True if comp can receive dragItems
	"""
	#debug('\nonHoverStartGetAccept comp:', comp.path, '- info:\n', info)
	return True # accept what is being dragged

def onHoverEnd(comp, info):
	"""
	Called when dragItems leave comp's hover area.

	Args:
		comp: the panel component being hovered over
		info: A dictionary containing all info about hover, including:
			dragItems: a list of objects being dragged over comp
			callbackPanel: the panel Component pointing to this callback DAT
	"""
	#debug('\nonHoverEnd comp:', comp.path, '- info:\n', info)

def onDropGetResults(comp, info):
	"""
	Called when comp receives a drop of dragItems. This will only be called if
	onHoverStartGetAccept has returned True for these dragItems.

	Args:
		comp: the panel component being dropped on
		info: A dictionary containing all info about drop, including:
			dragItems: a list of objects being dropped on comp
			callbackPanel: the panel Component pointing to this callback DAT

	Returns:
		A dictionary of results with descriptive keys. Some possibilities:
			'droppedOn': the object receiving the drop
			'createdOPs': list of created ops in order of drag items
			'dropChoice': drop menu choice selected
			'modified': object modified by drop
	"""
	debug('\nonDropGetResults comp:', comp.path, '- info:\n', info)
	droppedOn = comp.path


	dropped_item = info.get("dragItems")[0]
	# print(dropped_item.name)
	# print(dropped_item.owner)
	target = op(dropped_item.owner)
	par_name = dropped_item.name
	target.pars(par_name)[0].mode = ParMode.BIND
	target.pars(par_name)[0].bindExpr = f"op('{droppedOn}').par.Value0"

	# create Label from bound parameters
	
	p = comp.par.Value0
	bound_par = p.bindReferences
	print(bound_par)

	p_exclude_list = ["midiFighterTwisterV2"] 

	# TODO: check the list creation again this throws errors
	bound_par_names = [
    x.name
    for x in bound_par
    if not any(ex in x.owner for ex in p_exclude_list)]
	print(bound_par_names)
	label = ""
	for name in bound_par_names:
		if label != "":
			label += ", "
		label += name
		
	comp.par.Widgetlabel = label
	
	# check all the other knobs for 

# callbacks for when associated Panel is being dragged

def onDragStartGetItems(comp, info):
	"""
	Called when information about dragged items is required.

	Args:
		comp: the panel clicked on to start drag
		info: A dictionary containing all info about drag
			callbackPanel: the panel Component pointing to this callback DAT

	Returns:
		A list of dragItems: [object1, object2, ...]
	"""
	dragItems = [comp] # drag the comp itself
	#debug('\nonDragStartGetItems comp:', comp.path, '- info:\n', info)
	return dragItems

def onDragEnd(comp, info):
	"""
	Called when a drag action ends.

	Args:
		comp: the panel clicked on to start drag
		info: A dictionary containing all info about drag, including:
			accepted: True if the drag was accepted, False if not
			dropResults: a dict of drop results. This is the return value of 
				onDropGetResults
			dragItems: the original dragItems for the drag
			callbackPanel: the panel Component pointing to this callback DAT
	"""
	#debug('\nonDragEnd comp:', comp.path, '- info:\n', info)
	
