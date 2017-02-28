def l2d(f):

	line = f.readlines()

	keys = line[0].split()
	values = line[1].split()

	d = {}

	i = 0

	while i < len(keys):
		d[keys[i]] = int(values[i])
		i = i +1
	return d