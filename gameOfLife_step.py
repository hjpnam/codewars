import numpy as np

def next_gen(cells):
	data = np.asarray(cells, dtype='int')
	new_values = np.copy(data)
	results = np.copy(data)
	padded = np.pad(new_values,(1,1),'constant',constant_values=0)
	for j in range(1,len(data)+1):
		for i in range(1,len(data[0])+1):
			check = surroundCheck(padded[j-1:j+2,i-1:i+2])
			if padded[j][i] == 1:
				if check < 2 or check > 3: results[j-1][i-1] = 0
				else: results[j-1][i-1] = 1
			elif check == 3: results[j-1][i-1] = 1
	
	return results.tolist()
	
def surroundCheck(cells):
	data = np.copy(np.asarray(cells))
	data[1][1] = 0
	live = np.count_nonzero(data)
	return live
