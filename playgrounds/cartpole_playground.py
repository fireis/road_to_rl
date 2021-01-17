import gym

if __name__ == '__main__':

    env = gym.make('CartPole-v0')
    env.render()

    n_episodes = 1000

    for i in range(n_episodes):
        if i % 100 == 0:
            print(f"Starting episode {i} / {n_episodes}")
        env.reset()
        env.render()

        n_actions = 0
        # run episode
        while True:
            n_actions += 1
            action = env.action_space.sample()
            observation, reward, done, info =  env.step(action) # take a random action

            # check if the sim ended
            if done:
                break

    env.close()