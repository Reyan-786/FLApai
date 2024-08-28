import numpy as np
from flappy_bird_env import FlappyBirdEnv
from dqn_agent import DQNAgent

def train_agent():
    # Initialize environment and agent
    env = FlappyBirdEnv()
    state_size = len(env._get_state())
    action_size = 2  
    agent = DQNAgent(state_size, action_size)

    # Training parameters
    episodes = 3
    batch_size = 32

    for e in range(episodes):
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        for time in range(500):
            # No visualization, so commenting out render
            # env.render()

            action = agent.act(state)
            next_state, reward, done = env.step(action)
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                print(f"Episode: {e}/{episodes}, Score: {time}, Epsilon: {agent.epsilon:.2}")
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)

    # Save the trained model
    agent.model.save('flappy_bird_dqn_model.h5')
    env.close()

if __name__ == "__main__":
    train_agent()
