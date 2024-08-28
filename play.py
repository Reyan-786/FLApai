import numpy as np
from tensorflow.keras.models import load_model
from flappy_bird_env import FlappyBirdEnv
from dqn_agent import DQNAgent

def play_agent():
    # Initialize environment
    env = FlappyBirdEnv()

    # Initialize agent
    state_size = len(env._get_state())
    action_size = 2  # Assuming two actions: flap and do nothing
    agent = DQNAgent(state_size, action_size)

    # Load the trained model
    agent.model = load_model('flappy_bird_dqn_model.h5')

    state = env.reset()
    state = np.reshape(state, [1, state_size])
    done = False

    while not done:
        # Predict Q-values for the current state
        q_values = agent.model.predict(state)
        
        # Select the action with the highest Q-value
        action = np.argmax(q_values[0])
        
        # Apply action to the environment
        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])

        # Update state
        state = next_state

        # Render the environment (optional, comment out if not needed)
        env.render()

    env.close()

if __name__ == "__main__":
    while True : 
        play_agent()