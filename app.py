import numpy as np
import random

# Environment parameters
GRID_SIZE = 10  # Change grid size to 16x16
ACTIONS = ['up', 'down', 'left', 'right']
ALPHA = 0.1   # Learning rate
GAMMA = 0.9   # Discount factor
EPSILON = 0.1  # Exploration rate

# Initialize Q-table
q_table = np.zeros((GRID_SIZE, GRID_SIZE, len(ACTIONS)))

# Reward function
def get_reward(state):
    if state == (GRID_SIZE - 1, GRID_SIZE - 1):  # Goal state
        return 10
    return -1  # Step penalty

# Get the next state given an action
def get_next_state(state, action):
    x, y = state
    if action == 'up' and x > 0:
        x -= 1
    elif action == 'down' and x < GRID_SIZE - 1:
        x += 1
    elif action == 'left' and y > 0:
        y -= 1
    elif action == 'right' and y < GRID_SIZE - 1:
        y += 1
    return (x, y)

# Choose an action using epsilon-greedy strategy
def choose_action(state):
    if random.uniform(0, 1) < EPSILON:  # Explore
        return random.choice(ACTIONS)
    else:  # Exploit
        x, y = state
        return ACTIONS[np.argmax(q_table[x, y])]

# Training
EPISODES = 1000
for episode in range(EPISODES):
    state = (0, 0)  # Start position
    while state != (GRID_SIZE - 1, GRID_SIZE - 1):  # Until goal is reached
        action = choose_action(state)
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)

        # Update Q-value using Q-learning formula
        x, y = state
        nx, ny = next_state
        action_index = ACTIONS.index(action)
        best_next_action = np.max(q_table[nx, ny])
        q_table[x, y, action_index] += ALPHA * (reward + GAMMA * best_next_action - q_table[x, y, action_index])

        state = next_state

# Testing the policy
def test_agent():
    state = (0, 0)
    steps = 0
    print("Agent's Path:")
    while state != (GRID_SIZE - 1, GRID_SIZE - 1):
        x, y = state
        action_index = np.argmax(q_table[x, y])
        action = ACTIONS[action_index]
        print(f"State: {state}, Action: {action}")
        state = get_next_state(state, action)
        steps += 1
    print(f"Goal reached in {steps} steps!")

# Test the trained agent
test_agent()
