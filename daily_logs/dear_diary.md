# Description

This file is meant to be my daily log of activities. I hope this helps me keep the study on track, as it adds some accountability to the process.

## Day 0 - 2020/12/30

During my Udacity nanodegree on Machine Learning, I've used pygame in a reinforcement learning project. As this can help this study, I've searched a little bit if there are any significant projects available in this area. I found the following links:

* <https://github.com/ntasfi/PyGame-Learning-Environment>: seems to be pretty straightforward, containing a decent amount of old games. My main concern about this is the lack of updates since 2019, and it has not been tested on python > 2.7, which indicates its age;
* <https://github.com/mgbellemare/Arcade-Learning-Environment>: this is the project in which the PLE was inspired. It seems to be mostly in C++, but has a Python interface;
* <https://github.com/openai/gym>: this is my favorite so far. As with CARLA, this one I've known and wanted to try for years. I think I'll need to do some tinkering to define how complex it is to implement something in this platform, as it seems to be robust, being used in many cool projects, but this may come with an overhead.

Now that I've done a bit of research, I think it's time to get my hands dirty, so I'll start tinkering with OpenAI Gym.

### OpenAI Gym Installation

It seems that this distro is available directly at conda, so I'll take the path of least resistance here:

```shell
conda install -c conda-forge gym
```

To test the installation, I've executed the code for a random agent, available in [this link](https://github.com/openai/gym/blob/master/examples/agents/random_agent.py). Additionally, to help me kwwping track, I've created the **OpenAIGym - Intro** notebook.

### Useful Links - Learning Paths

* <https://spinningup.openai.com/en/latest/spinningup/rl_intro.html>: the OpenAI team has a free course on RL. It seems to start simple, and I think it makes sense for me to take a look after diving into chapter 3 of the AI book, as I want a good classical introduction.

## Day 1 - 2021/01/01

* Started reading chapter 3 from the book. Read sections 3.1 and 3.2.

## Day 2 - 2021/01/02

* Read section 3.3.

## Day 3 - 2021/01/03

* Found a cool project to test agents, <https://www.pommerman.com/>. This is something for the somewhat far future, but seems good to keep anyway.

## Day 4 - 2021/01/05

* I found a course on RL in [Coursera](https://www.coursera.org/learn/fundamentals-of-reinforcement-learning/home/welcome) and, although my plan was to follow the AI book for a broader start, I've decided to check if the course is any good to begin with. So I've taken the three initial lessons.

## Days 5 - 8 - 2021/01/09

* Finished Week 1 from [Coursera RL Course](https://www.coursera.org/learn/fundamentals-of-reinforcement-learning/home/welcome).

## Day 9 - 2021/01/10

* Written the recap and started Week 2.

### Recap

In my study so far, I've seen almost the same subject from two distinct perspectives: classical agents and reinforcement learning. The concepts that I've studied in the classical agent section allowed agents to search and choose between a given set of options to achieve a final goal. On the reinforcement learning side, I've studied the basics of creating a policy to select an action given a set of rewards or estimates of rewards. We can consider that both approaches solve the same bigger problem, but the details are quite distinct. The classical agent approach assumes that we know the outputs for each action, while the reinforcement learning approach assumes that we learn the effects of our efforts as we experiment with them.

As my goal is to experiment with hands-on projects, specifically in the reinforcement learning side, the Coursera specialization seems to be the most adequate for my current moment.

## Day 10 - 2021/01/17

* Ok, I forgot to commit during the past week. But I finished Week 2 of the [Coursera RL Course](https://www.coursera.org/learn/fundamentals-of-reinforcement-learning/home/welcome);
* I think I'm going to reset my day counter to be more fair;
* Today I've played a bit with OpenAi Gym, as I want to apply the course concepts to the environments in the Gym. Hence I need to understand the gym structure;
* I've played with the [Cart Pole](https://gym.openai.com/docs/) example from the openai gym. Then I've tried to implement a simple MDP agent, but I achieved only a small progress. [This lib](https://github.com/BlackHC/mdp) may be helpful in the future.

## Day 11 - 2021/01/18

* I realised there was still one additional assignement on week 2, so I finished it today.
  
## Day 12 - 2021/01/21

* Started the Week 3 of the course and started my new physical notebook as this tends to help me really understand the concepts.

## Day 13 - 2021/01/22

* Advanced on week 3.

## Day 14 - 2021/01/23

* Finished week 3! Only one more left to go in this course.
  
## Day 15 - 2021/01/25

* Almost done with the classes of teh fourth week! Excited for the lab in the week. 

## Days 16 - 19 - 2021/01/26 - 2021/01/29

* Finished week 4, with the exception of the programming challenge.