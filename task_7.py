import random
import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_experiments):
    result = np.zeros((2,11))

    result[0,:] = range (2,12+1)
    
    for _ in range(num_experiments):
        # Generate random throws
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        sum = first_dice + second_dice
        result[1, sum-2] += 1

    return result


# Number of experiments
num_experiments = 10_000_000

# Execution of the simulation
experiment = monte_carlo_simulation(num_experiments)
print(f"For {num_experiments} number of experiments results are:")
experiment[1,:] = experiment[1,:]/num_experiments*100
print(experiment)


fig, ax = plt.subplots()
xd = ax.bar(experiment[0,:],experiment[1,:])
ax.bar_label(xd, experiment[1,:])

plt.show()