
import matplotlib.pyplot as plt
import matplotlib.path as mplPath
import numpy as np
import pandas as pd
import ast

df = pd.read_csv("poly.txt", delimiter='\t')
print(len(df))

loc = [-21.992805, -42.255166]

for i in range(len(df)):
	row = df.iloc[[i]]
	polyid = int(row[row.columns[0]])
	print(polyid)
	coord = ast.literal_eval(list(row[row.columns[1]])[0])

	lon = coord[0:-2:2]
	lat = coord[1:-1:2]

	coord = [[b,a] for a,b in zip(lon, lat)]
	# print(len(x), len(y))
	# print(coord)
	plt.figure()
	plt.plot(lat,lon)
	plt.scatter(loc[0], loc[1])
	plt.show()

	bbPath = mplPath.Path(np.array(coord))
	print(bbPath.contains_point((loc[0], loc[1])))
