import pandas as pd
import numpy as np
from math import ceil
from collections import namedtuple
from copy import deepcopy
from random import randint

Raffle_Tickets = namedtuple('Raffle_Tickets', ['name', 'ticket_numbers', 'tickets'])

df = pd.read_excel (r'/Users/ryan/Documents/python-files/8th  Hero Points.xlsx')
df = df[df['Available Points'] >0]
df.reset_index(inplace=True, drop=True)
tickets = []
for i in df['Available Points'] / 10:
    tickets.append(ceil(i))

df['Tickets'] = tickets
total_number_of_tickets = sum(df['Tickets'])
ticket_number_start = 1000000
ticket_number_list = []
for i in range(ticket_number_start, ticket_number_start+total_number_of_tickets):
    ticket_number_list.append(i)
assigned_ticket_number_list = deepcopy(ticket_number_list)
df = df.reindex(np.random.permutation(df.index))

# Assign the tickets to the students
raffle_list = []
for student in range(df.shape[0]):
    student_ticket_list = []
    for i in range(df.loc[student].Tickets):
        assigned_ticket_number = randint(0, len(assigned_ticket_number_list)-1)
        student_ticket_list.append(assigned_ticket_number_list[assigned_ticket_number])
        assigned_ticket_number_list.pop(assigned_ticket_number)
    raffle_list.append(Raffle_Tickets(df.loc[student].Name, student_ticket_list, len(student_ticket_list)))

# Randomly draw ticket
selected_tickets = []
for i in range(25):
    selected_ticket_number_index = randint(0, len(ticket_number_list) - 1)
    selected_ticket_number = ticket_number_list[selected_ticket_number_index]
    for r in raffle_list:
        if selected_ticket_number in r.ticket_numbers:
            ticket_number_list = [x for x in ticket_number_list if x not in r.ticket_numbers]
    selected_tickets.append(selected_ticket_number)


# Find the winners:
winners_list=[]
for r in raffle_list:
    for t in r.ticket_numbers:
        student_winning_list = []
        if t in selected_tickets:
            student_winning_list.append(t)
            winners_list.append((Raffle_Tickets(r.name, student_winning_list, len(student_winning_list))))


def ticket_count(winner):
    for r in raffle_list:
        if r.name == winner:
            return r.tickets


with open('/Users/ryan/PyBites/Raffle/winners_new.txt', 'w+') as f:
    for winner in winners_list:
        tickets = ticket_count(winner.name)
        percent_chance_of_winning = tickets / total_number_of_tickets * 100
        percent_chance_of_winning_string = "{:.2f}".format(percent_chance_of_winning)
        f.write(f'{winner.name} with winning ticket {winner.ticket_numbers[0]}. They had {tickets} tickets and a {percent_chance_of_winning_string}% chance of winning.\n')