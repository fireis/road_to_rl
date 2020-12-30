# Description

This file is meant to be my daily log of activities. I hope this helps me keep the study on track, as it adds some accountability to the process.

## Day 1 - 2020/12/30

During my Udacity nanodegree on Machine Learning, I've used pygame in a reinforcement learning project. As this can help this study, I've searched a little bit if there are any significant projects available in this area. I found the following links:

* <https://github.com/ntasfi/PyGame-Learning-Environment>: seems to be pretty straightforward, containing a decent amount of old games. My main concern about this is the lack of updates since 2019, and it has not been tested on python > 2.7, which indicates its age;
* <https://github.com/mgbellemare/Arcade-Learning-Environment>: this is the project in which the PLE was inspired. It seems to be mostly in C++, but has a Python interface;
* <https://github.com/openai/gym>: this is my favorite so far. As with CARLA, this one I've known and wanted to try for years. I think I'll need to do some tinkering to define how complex it is to implement something in this platform, as it seems to be robust, being used in many cool projects, but this may come with an overhead.

Now that I've done a bit of research, I think it's time to get my hands dirty, so I'll start tinkering with OpenAI Gym.

## OpenAI Gym Installation
It seems that this distro is available directly at conda, so I'll take the path of least resistance here:

```shell
conda install -c conda-forge gym
```

To test the installation, I've executed the code for a random agent, available in [this link](https://github.com/openai/gym/blob/master/examples/agents/random_agent.py). Additionally, to help me kwwping track, I've created the **OpenAIGym - Intro** notebook.

## Useful Links - Learning Paths

* <https://spinningup.openai.com/en/latest/spinningup/rl_intro.html>: the OpenAI team has a free course on RL. It seems to start simple, and I think it makes sense for me to take a look after diving into chapter 3 of the AI book, as I want a good classical introduction.