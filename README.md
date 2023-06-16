# ApproveByPoll

[![wakatime](https://wakatime.com/badge/user/8fb54ab7-2914-4f28-b19d-d25e65f8e545/project/625fda84-ae65-4398-8d0f-c53903f1b04c.svg)](https://wakatime.com/badge/user/8fb54ab7-2914-4f28-b19d-d25e65f8e545/project/625fda84-ae65-4398-8d0f-c53903f1b04c)
[![actions](https://github.com/chitang233/ApproveByPoll/actions/workflows/docker-ci.yaml/badge.svg)](https://github.com/chitang233/ApproveByPoll/actions/workflows/docker-ci.yaml)

## Installation

Just install the required dependencies in `requirements.txt` in your favorite way.

Then run the bot with your bot token as an environment variable:

```shell
TOKEN=<YOUR_BOT_TOKEN_HERE> python3 main.py
```

Or use Docker instead:

```shell
docker run -d --name approvebypoll -e TOKEN=<YOUR_BOT_TOKEN_HERE> ghcr.io/chitang233/approvebypoll:latest
```
