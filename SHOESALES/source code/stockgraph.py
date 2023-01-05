import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('graph.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	
	for row in plots:
		x.append(row[1])
		y.append(int(row[3]))

f=plt.figure()
f.set_figwidth(10)
f.set_figheight(5)
plt.bar(x, y, color = 'g', width = 0.72, label = " SHOE UNITS")
plt.xlabel('SHOES BRAND NAME')
plt.ylabel('No. OF UNITS AVAILABLE')
plt.title('SHOE STOCK GRAPH')
plt.legend()
plt.show()