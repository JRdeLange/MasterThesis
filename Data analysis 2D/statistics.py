import json

def test():
    with open("exps/20_boids7/exp_analysis_20_boids7.txt") as f:
        data = json.load(f)

    print(data["total_nr_of_clusters"])
