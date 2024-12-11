# Reinforcement Learning Grid Environment with Docker
Overview
This project implements a basic reinforcement learning algorithm using Q-Learning to teach an agent how to navigate a grid-based environment. The agent starts at (0, 0) and learns to reach the goal state at (9, 9) through trial and error, using rewards and penalties. The environment is highly customizable, allowing changes to grid size, learning parameters, and exploration strategies. By the end of training, the agent optimizes its path to minimize steps and maximize rewards, demonstrating a learned policy in action.

To make the project easily accessible, it is fully containerized with Docker. This ensures a consistent runtime environment and eliminates dependency issues. With a prebuilt image available on Docker Hub, you can quickly pull and run the project without any setup. For advanced users, the Dockerfile enables customization and local builds for experimenting with different configurations. Docker makes deploying, sharing, and scaling the project seamless, enhancing its usability across platforms. 

Features
Q-Learning Implementation: A basic reinforcement learning algorithm to train the agent.
Customizable Environment: Grid size, actions, and learning parameters are easily adjustable.
Path Visualization: The agent's path to the goal is displayed after training.
Dockerized Setup: Pre-configured for easy deployment using Docker.

How It Works
Training
The agent is trained over a series of episodes using Q-Learning, updating the Q-table based on the rewards received for its actions. The key parameters include:

Grid Size: 10x10 (can be modified via the GRID_SIZE constant).
Actions: ['up', 'down', 'left', 'right'].
Learning Rate (α): 0.1
Discount Factor (γ): 0.9
Exploration Rate (ε): 0.1
Episodes: 1000
Testing
After training, the agent demonstrates its learned policy by navigating to the goal, with the path and steps displayed in the console.

Docker link
https://hub.docker.com/repository/docker/eyuel136/reinforcement_grid_env/general
