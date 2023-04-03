import os

for directory in os.listdir("./"):
	if not directory[-1] == "y":
		for config in os.listdir("./" + directory):
			os.mkdir("./" + directory + "/" + config + "/2D_rec_10_total_boids_slower")
			for file in os.listdir("./" + directory + "/" + config):
				if os.path.isfile("./" + directory + "/" + config + "/" + file):
					os.rename("./" + directory + "/" + config + "/" + file, "./" + directory + "/" + config + "/2D_rec_10_total_boids_slower/" + file)