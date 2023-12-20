import pronotepy
from pronotepy.ent import ile_de_france
from datetime import date
from datetime import datetime
import time
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_WEBHOOKS_PRONOTE = os.getenv("DISCORD_WEBHOOKS_PRONOTE")
ENT_USERNAME = os.getenv("ENT_USERNAME")
ENT_PASSWORD = os.getenv("ENT_PASSWORD")
ENT = os.getenv("ENT")
path = 'new/pronote/'
path =''

def date_encoder(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def envoyer_message_webhook(contenu):
    data = {
        'content': contenu
    }
    response = requests.post(DISCORD_WEBHOOKS_PRONOTE, json=data)
    if response.status_code == 204:
        print(f'{datetime.now().strftime("%H:%M")} : Send')
    else:
        print(f"Échec de l'envoi du message. Code d'état : {response.status_code}")

def refresh(send):
    try :
        client = pronotepy.Client('https://0910626l.index-education.net/pronote/eleve.html',
                            username=ENT_USERNAME,
                            password=ENT_PASSWORD,
                            ent=globals().get(ENT)) #ile_de_france
        if not client.logged_in:
            exit(1)

        if send == 1:
            with open(path + 'grades.txt', 'r') as file:
                prev_grades = json.load(file)

            with open(path + 'average.txt', 'r') as file:
                prev_average = json.load(file)

        new_average = client.periods[0].overall_average

        new_grades_list = []
        for period in client.periods:
            for grade in period.grades:
                obj = grade.date
                gooddate = obj.isoformat()
                grade_dict = {
                    'grade': grade.grade,
                    'average': grade.average,
                    'coefficient': grade.coefficient,
                    'comment': grade.comment,
                    'date': gooddate,
                    'default_out_of': grade.default_out_of,
                    # 'id': grade.id,
                    'is_bonus': grade.is_bonus,
                    'is_optional': grade.is_optionnal,
                    'is_out_of_20': grade.is_out_of_20,
                    'max': grade.max,
                    'min': grade.min,
                    'out_of': grade.out_of,
                    # 'period_id': grade.period.id,
                    'period_name': grade.period.name,
                    # 'subject_id': grade.subject.id,
                    'subject_groups': grade.subject.groups,
                    'subject_name': grade.subject.name,
                    }
                new_grades_list.append(grade_dict)
        if send == 1:
            if len(new_grades_list) != len(prev_grades):
                changes = 0
                while len(new_grades_list) != len(prev_grades):
                    prev_grades.append('tmp')
                for i,old in zip(new_grades_list, prev_grades):
                    
                    if i != old:
                        changes+=1           
                    if changes == 1:
                        content = f"""**{i['subject_name']}** : {i['comment']}
                        {datetime.strptime(str(i['date']), "%Y-%m-%d").strftime("%d %B %Y")}
                        **{i['grade']}/{i['out_of']}** | Coef : {i['coefficient']}
                        Moy : **{i['average']}/{i['out_of']}**
                        :arrow_up_small: : {i['max']}/{i['out_of']} | :arrow_down_small: : {i['min']}/{i['out_of']}

                        Moy G : {new_average}({float(new_average)-float(prev_average)})
                        """
                        print('content: ', content)
                        envoyer_message_webhook(content)
            else:
                print(f'{datetime.now().strftime("%H:%M")} : No change')

        ################
        with open(path + 'grades.txt', 'w') as file:
            json.dump(new_grades_list, file, indent=2, default=date_encoder)

        with open(path + 'average.txt', 'w') as file:
            json.dump(new_average, file, indent=2)

        return 1
    except Exception as e:
        return e


# schedule.every(20).minutes.do(refresh)
# print('refresh: 20')
# while True:
#     schedule.run_pending()
#     time.sleep(1)


status = 0
while status != 1:
    status = refresh(send = 0)
    if status != 1 :
        print(status)
        envoyer_message_webhook(status)
        time.sleep(2*60)

min = 20
print('refresh rate: ', 20)
while True:
    status = 0
    while status != 1:
        status = refresh(send = 1)
        if status != 1 :
            print(status)
            envoyer_message_webhook(status)
            time.sleep(2*60)

    time.sleep(min*60)

### debug
# refresh(send=1)