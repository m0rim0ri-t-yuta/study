import matplotlib.pyplot as plt

test_result = [{82, 65},
               {45, 60},
               {56, 58},
               {78, 67},
               {50, 48},
               {96, 88},
               {64, 80},
               {72, 87}]

#Extract x and y values
x_vals = []
y_vals = []
for s in test_result:
    x,y = list(s)
    x_vals.append(x)
    y_vals.append(y)

#Create scater plot
plt.figure(figsize = (6,6))
plt.scatter(x_vals,y_vals, color='blue')

#Annoate each point
for x,y in zip(x_vals, y_vals):
    plt.annotate(f'({x},{y})', (x,y), textcoords = "offset points", xytext=(5,5), ha='center')

#Add labels and grid
plt.xlim(0,100)
plt.ylim(0,100)
plt.xlabel('x')
plt.xlabel('y')
plt.grid(True)
plt.show()


