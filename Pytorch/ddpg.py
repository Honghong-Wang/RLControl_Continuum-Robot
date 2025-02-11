import sys
sys.path.append('../Reinforcement Learning')

# import gym
# import random
import torch
print(torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))
import pickle
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
from ddpg_agent import Agent
from env import continuumEnv
import time
import math

env = continuumEnv()
env.seed(10)
agent = Agent(state_size=4, action_size=3, random_seed=10)

# %%
def ddpg(n_episodes=1500, max_t=750, print_every=25):
    global scores
    global avg_reward_list
    scores_deque = deque(maxlen=print_every)
    scores = []
    avg_reward_list = []
    counter = 0
    for i_episode in range(1, n_episodes+1):
        state = env.reset()
        agent.reset()
        score = 0
        if i_episode % print_every == 0:
            print('\n')
            print("Initial Position is",state[0:2])
            print("===============================================================")
            print("Target Position is",state[2:4])
            print("===============================================================")
            print("Initial Kappas are ",[env.kappa1,env.kappa2,env.kappa3])
            print("===============================================================")
            print("Goal Kappas are ",[env.target_k1,env.target_k2,env.target_k3])
            print("===============================================================")
            time.sleep(2)
        
        for t in range(max_t):
            action = agent.act(state)
            # next_state, reward, done, _ = env.step_minus_euclidean_square(action) # -e^2
            next_state, reward, done, _ = env.step_error_comparison(action) # reward is -1.00 or -0.50 or 1.00
            # next_state, reward, done, _ = env.step_minus_weighted_euclidean(action) # -0.7*e
            # next_state, reward, done, _ = env.step_distance_based(action) # reward is du-1 - du
            agent.step(state, action, reward, next_state, done) 
            state = next_state
            # # Uncomment below!!!!
            # print("Episode Number {0} and {1}th action".format(i_episode,t))
            # print("Goal Position",state[2:4])
            # # print("Previous Error: {0}, Error: {1}, Current State: {2}".format(env.previous_error, env.error, prev_state)) # for step_1
            # print("Error: {0}, Current State: {1}".format(math.sqrt(-1*reward), state)) # for step_2
            # print("Action: {0},  Kappas {1}".format(action, [env.kappa1,env.kappa2,env.kappa3]))
            # print("Reward is ", reward)
            # print("{0} times robot reached to the target".format(counter))
            # print("Avg Reward is {0}, Episodic Reward is {1}".format(np.mean(scores),score))
            # print("--------------------------------------------------------------------------------")
            score += reward
            if done:
                counter += 1
                break 
        scores_deque.append(score)
        scores.append(score)
        # Mean of 100 episodes
        avg_reward_list.append(np.mean(scores[-100:]))
        print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)), end="")
        torch.save(agent.actor_local.state_dict(), 'experiment/checkpoint_actor.pth')
        torch.save(agent.critic_local.state_dict(), 'experiment/checkpoint_critic.pth')
            
    return scores

scores = ddpg()

# %% Result
plt.subplot(1, 2, 1)
plt.plot(np.arange(1, len(scores)+1), scores)
plt.ylabel('Reward')
plt.xlabel('Episode #')
with open('experiment/scores.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(scores, f, pickle.HIGHEST_PROTOCOL)

plt.subplot(1, 2, 2)
plt.plot(np.arange(1, len(avg_reward_list)+1), avg_reward_list)
plt.ylabel('Average Reward')
plt.xlabel('Episode #')
plt.show()
with open('experiment/avg_reward_list.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(avg_reward_list, f, pickle.HIGHEST_PROTOCOL)

