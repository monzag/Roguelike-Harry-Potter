import time
import csv


def get_score_list(points):
    date = time.strftime("%Y-%m-%d-%H:%M")
    print("Winner!! You have ", points, 'points!')
    name = input("What is your name? ")
    lista = [name, str(date),  str(points)]
    scorelist = ' | '.join(lista)

    return scorelist


def add_result_to_scorelist(scorelist):
    '''Create ranking list '''
    with open('highscore.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([scorelist])


def get_points(element):
    return float(element[-1])


def display_scorelist():
    with open('highscore.csv') as csv:
        from_file = csv.readlines()
        splitted = [line.split(' | ') for line in from_file]
        ranking = [(line[0], line[1], (line[2]).strip()) for line in splitted]

    sorted_ranking = sorted(ranking, key=get_points)
    for item in sorted_ranking:
        print(item)


# ranking = get_score_list(points)
# add_result_to_scorelist(ranking)
# display_scorelist()