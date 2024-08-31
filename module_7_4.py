
team1 = 'Мастера кода '
team2 = 'Волшебники данных'
class CodeMasters_and_DataWizards:
    def __init__(self, team1_num, team2_num):
        self.team1_num = team1_num
        self.team2_num = team2_num
        print('В команте %s участников: %s' % (team1,team1_num))
        print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

CodeMasters_and_DataWizards(5, 6)

class Tasks(CodeMasters_and_DataWizards):
        def __init__(self, score_1, score_2):
            self.score_1 = score_1
            self.score_2 = score_2
            team1_time = 1552.512
            team2_time = 2153.31451
            challenge_result = "Результат битвы: победа команды"
            tasks_total = 82
            time_avg = 350.4
            print("Команда {0} решила задач:{1}!".format(team2,score_2))
            print("{0} решили задачи за {1} с !".format(team2, team1_time))
            print(f'Команды решили {score_1} и {score_2} задачи')
            print(f'"Результат битвы: победа команды {team1}!')
            print(f"Сегодня было решено {tasks_total} задачи, в среднем по {time_avg } секунды на задачу!.")
Tasks(40, 42)


