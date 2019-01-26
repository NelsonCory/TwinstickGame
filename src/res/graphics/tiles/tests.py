import os

for file in os.listdir("."):
	print(file)
	print(os.path.basename(file).split("_"))
