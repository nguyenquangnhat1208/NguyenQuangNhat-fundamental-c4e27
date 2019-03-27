from matplotlib import pyplot

#1. prepare data
machine_counts = [18,4,2]

#2. prepare labels
machine_names = ["PC" , "MAC" , "LINUX"]

#3. draw pie
pyplot.pie(machine_counts, labels = machine_names, autopct="%.1f%%", shadow=True, explode=(0,0.1,0))
pyplot.axis("equal")
#4. show
pyplot.show()