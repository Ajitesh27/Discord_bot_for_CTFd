# Discord_bot_for_CTFd

# ABSTRACT :
The purpose of the developed CTFd bot is to connect Discord server to CTFd
framework with a centralized system for real-time management of the competition
by the organizers. CTFd bot can monitor real-time solves, submissions and filter out
valid ones, sends notifications on each solves with beautiful and colorful embeds
with current rank and score of the person who solved with a timestamp in it. We
have a live scoreboard that notifies the participants and the organizers when there
is any change in the ranks.
The benefit of this bot is that it becomes much easier for the organizers to perform
all the most performed tasks with one command on Discord. This would reduce the
need to move to the CTFd web app. This would also help the participants to know
where they stand without having to go to the website
This product is a follow on to the CTFd platform. CTFd platform is a web application
to help organizers to easily manage and conduct Capture the Flag events. With the
existing CTFd framework, it is a paid web app, or it can be freely installed and hosted
on our own servers. We plan to make use of the Discord API to combine it with the
CTFd web application so that every task that an organizer and a participant would do
for a CTF, can now directly be done as a command to that bot on Discord.
# Steps to execute 
- Create a virtual environment
- Install latest postgres db and pgadmin
- Create a bot via Discord developer portal and place the token of the bot in config.yaml file
- Go to src folder 
- pip install -r requirements.txt (If some libraries are giving error, install them manually)
- python main.py (Now Bot is ready)
- To run commands use >>help
