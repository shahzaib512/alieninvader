# import random
# import matplotlib.pyplot as plt

# def roll_dice():
#     return random.randint(1, 8) + random.randint(1, 8)

# def simulate_rolls(num_rolls):
#     rolls = [roll_dice() for _ in range(num_rolls)]
#     return rolls

# def visualize_results(rolls):
#     frequencies = [0] * 16
#     for roll in rolls:
#         frequencies[roll] += 1
    
#     x = range(2, 17)
#     y = frequencies[2:]
    
#     plt.bar(x, y)
#     plt.xlabel('Sum of Dice')
#     plt.ylabel('Frequency')
#     plt.title('Simulation Results - Rolling Two Eight-Sided Dice')
#     plt.show()

# # Simulation with 1,000 rolls
# rolls = simulate_rolls(1000)
# visualize_results(rolls)


# import random
# import matplotlib.pyplot as plt

# def roll_dice():
#     return random.randint(1, 8) + random.randint(1, 8)

# def simulate_rolls(num_rolls):
#     rolls = [roll_dice() for _ in range(num_rolls)]
#     return rolls

# def visualize_results(rolls):
#     frequencies = [0] * 16
#     for roll in rolls:
#         frequencies[roll] += 1
    
#     x = range(2, 17)
#     y = frequencies[2:]
    
#     plt.bar(x, y)
#     plt.xlabel('Sum of Dice')
#     plt.ylabel('Frequency')
#     plt.title('Simulation Results - Rolling Two Eight-Sided Dice')
#     plt.show()

# # Simulation with 1,000 rolls
# rolls = simulate_rolls(1000)
# visualize_results(rolls)

# import random
# import matplotlib.pyplot as plt

# def roll_dice():
#     return random.randint(1, 8) + random.randint(1, 8)

# def simulate_rolls(num_rolls):
#     rolls = [roll_dice() for _ in range(num_rolls)]
#     return rolls

# def visualize_results(rolls):
#     frequencies = [0] * 16
#     [frequencies[roll] := frequencies[roll] + 1 for roll in rolls]
    
#     x = range(2, 17)
#     y = frequencies[2:]
    
#     plt.bar(x, y)
#     plt.xlabel('Sum of Dice')
#     plt.ylabel('Frequency')
#     plt.title('Simulation Results - Rolling Two Eight-Sided Dice')
#     plt.show()

# # Simulation with 1,000 rolls
# rolls = simulate_rolls(1000)
# visualize_results(rolls)

# import random
# import matplotlib.pyplot as plt

# def roll_die():
#     return random.randint(1, 6)

# def simulate_rolls(num_rolls):
#     rolls = [roll_die() for _ in range(num_rolls)]
#     return rolls

# def visualize_die_rolls(rolls):
#     unique_rolls = list(set(rolls))
#     frequencies = [rolls.count(roll) for roll in unique_rolls]

#     plt.bar(unique_rolls, frequencies)
#     plt.xlabel('Die Face')
#     plt.ylabel('Frequency')
#     plt.title('Die-Rolling Visualization')
#     plt.show()

# # Simulation with 1,000 rolls
# rolls = simulate_rolls(1000)
# visualize_die_rolls(rolls)

# import random
# import plotly.graph_objects as go

# def random_walk(steps):
#     positions = [0]  # Starting position at 0

#     for _ in range(steps):
#         movement = random.choice([-1, 1])  # Randomly select -1 (left) or 1 (right)
#         new_position = positions[-1] + movement
#         positions.append(new_position)

#     return positions

# # Random walk with 100 steps
# steps = 100
# positions = random_walk(steps)

# # Create a scatter plot using Plotly
# fig = go.Figure(data=go.Scatter(x=list(range(steps + 1)), y=positions, mode='lines+markers'))
# fig.update_layout(title='Random Walk Visualization', xaxis_title='Steps', yaxis_title='Position')
# fig.show()

# import random
# import plotly.graph_objects as go

# def random_walk(steps):
#     positions = [0] # starting position at 0

#     for _ in range(steps):
#         movement = random.choice([-1, 1]) # Randomly selected -1 (left) or 1 (right)
#         new_position = positions[-1] + movement
#         positions.append(new_position)

#     return positions

# # Random walk with 100 steps
# steps = 100
# positions = random_walk(steps)

# # Create a scatter plot using plotly.
# fig = go.Figure(data=go.Scatter(x=list(range(steps +1)), y = positions, mode='lines+markers'))
# fig.update_layout(title = 'Random Walk Visualization', xaxis_title = 'Step', yaxis_title = 'Position')
# fig.show()
