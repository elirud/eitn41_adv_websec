from math import sqrt, floor, ceil
from random import randint
from statistics import mean
from statistics import stdev

c_val = int(input("Please enter how many keys (c): "))
u_val = int(input("Please enter the power of 2 for amount of bins (u): "))
k_val = int(input("Please enter size of key (k): "))
wanted_width = int(input("Please enter confidence intervall width: "))

num_bins = 2 ** u_val
sim_throws = []
ci_width = None
i = 0

while True:
    finished_keys = []
    num_of_throws = 0
    bins = [0] * num_bins
    while len(finished_keys) < c_val:
        rand = randint(0, num_bins - 1)
        bins[rand] += 1
        if rand not in finished_keys:
            if bins[rand] == k_val:
                finished_keys.append(rand)

        num_of_throws += 1

    i += 1
    print(f"--------Simulation {i}--------")
    print("Finished keys:", len(finished_keys))
    print("Number of throws:", num_of_throws)
    print("----------------------------")
    sim_throws.append(num_of_throws)

    if i > 2:
        sim_mean = mean(sim_throws)
        lower_bound = floor(sim_mean - 3.66 * (stdev(sim_throws) / sqrt(i)))
        upper_bound = ceil(sim_mean + 3.66 * (stdev(sim_throws) / sqrt(i)))
        ci_width = upper_bound - lower_bound
        print(ci_width)

        if ci_width <= wanted_width:
            break



print("########Simulations done!########")
print(f"Mean throws to get {c_val} amount of keys: {sim_mean}")
print("Confidence intervall lower bound:", lower_bound)
print("Confidence intervall upper bound:", upper_bound)
print("Confidence intervall width:", ci_width)
print("#################################")

