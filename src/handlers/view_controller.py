from databases import task_database, audit_database, team_database
from discord import Embed
from collections import Counter
from config import score

import discord
import math

def challenges():
    challs = task_database.find_all_visible_task()
    categorys = [chall.category for chall in challs]
    groups = {}

    for category in categorys:
        groups[category] = []
    
    for chall in challs:
        groups[chall.category].append(chall)
    
    solves = Counter(audit_database.number_of_solves())
    data = '```py\n'
    
    for category in groups:
        data += f'├── [{category}]\n'
        count = 0
        length = len(groups[category])

        for chall in groups[category]:
            value = max(score.minimal, int(math.ceil((((score.minimal - score.maximal) / (score.decay ** 2)) * (max(solves[chall.id]-1, 0) ** 2)) + score.maximal)))
            data += f'│   ├── [{chall.name}][{value}]\n' if (count < length-1) else f'│   └── [{chall.name}][{value}]\n'
            count += 1

    data += '```'
    card = Embed(title='Challenges', description=data, color=discord.Color.blue())
    card.add_field(name='Jump to detail with', value='```>>challenges-info name```')

    return card

def challenges_info(name):
    chall = task_database.find_visible_task(name)
    solve = Counter(audit_database.number_of_solves())[chall.id]
    value = max(score.minimal, int(math.ceil((((score.minimal - score.maximal) / (score.decay ** 2)) * (max(solve-1, 0) ** 2)) + score.maximal)))

    data = f'```md\n{chall.description}```'
    card = Embed(title=chall.name, description=data, url=chall.files, color=discord.Color.blue())
    card.add_field(name='Category', value=chall.category, inline=True)
    card.add_field(name='Solves', value=solve , inline=True)
    card.add_field(name='Scores', value=value , inline=True)
    
    blood = audit_database.firstblood(chall.id)
    if blood != None:
        team = team_database.find_team_data(blood.team_id)
        card.add_field(name='Firstblood', value=f':drop_of_blood: {team.name}', inline=False)

    return card

def scoreboard_before_freeze():
    audits = audit_database.audit_before_freeze()
    solves = Counter(audit_database.number_of_solves())
    challs = [audit.task_id for audit in audits]
    values = {}
    for chall in challs:
        values[chall] = max(score.minimal, int(math.ceil((((score.minimal - score.maximal) / (score.decay ** 2)) * (max(solves[chall]-1, 0) ** 2)) + score.maximal)))
    
    scoreboard = {}
    for audit in audits:
        if audit.team_id in scoreboard.keys():
            scoreboard[audit.team_id] += values[audit.task_id]
        else:
            scoreboard[audit.team_id] = values[audit.task_id]
    
    sorted_scoreboard = dict(sorted(scoreboard.items(), key=lambda item: item[1]))
    count = 1
    data = ''
    for x in sorted_scoreboard:
        if count > 10:
            break
        team = team_database.find_team_data(x)
        data += f'{count}|{team.name}|{sorted_scoreboard[x]}|{audit_database.number_of_solves_team(x)}\n'
    
    file = open("C:\\Users\Prajna\Desktop\XAMPP1\htdocs\GUI\scoreboard.txt", "w")
    file.write("%s" %(data))

    file.close()
    card = "Scoreboard Updated"
    return card


    
    
        

