# TODO: Implement train.pyfrom agent import Agent
from game import SnakeGameAI

def train():
    agent = Agent()
    game = SnakeGameAI()

    while True:
        state_old = agent.get_state(game)
        action = agent.get_action(state_old)
        reward, done, score = game.play_step(action)
        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, action, reward, state_new, done)
        agent.remember(state_old, action, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            print(f"Game: {agent.n_games} | Score: {score}")

if __name__ == '__main__':
    train()
