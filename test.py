import pronotepy
from pronotepy.ent import ile_de_france
from datetime import date
from datetime import datetime
import schedule
import time
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_WEBHOOKS_PRONOTE = os.getenv("DISCORD_WEBHOOKS_PRONOTE")
ENT_USERNAME = os.getenv("ENT_USERNAME")
ENT_PASSWORD = os.getenv("ENT_PASSWORD")

client = pronotepy.Client('https://0910626l.index-education.net/pronote/eleve.html',
                        username=ENT_USERNAME,
                        password=ENT_PASSWORD,
                        ent=ile_de_france)
if not client.logged_in:
    exit(1)

new_average = client.periods[0].overall_average

new_grades_list = []
for period in client.periods:
    for grade in period.grades:
        grade_dict = {
            'grade': grade.grade,
            'average': grade.average,
            'coefficient': grade.coefficient,
            'comment': grade.comment,
            'date': grade.date,
            'default_out_of': grade.default_out_of,
            'id': grade.id,
            'is_bonus': grade.is_bonus,
            'is_optional': grade.is_optionnal,
            'is_out_of_20': grade.is_out_of_20,
            'max': grade.max,
            'min': grade.min,
            'out_of': grade.out_of,
            'period_id': grade.period.id,
            'period_name': grade.period.name,
            'subject_id': grade.subject.id,
            'subject_groups': grade.subject.groups,
            'subject_name': grade.subject.name,
            }
        new_grades_list.append(grade_dict)

print(new_grades_list)