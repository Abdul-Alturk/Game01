from itertools import count
import json
import random
import time
import tkinter as tk
from tkinter import ttk

with open('score.json', 'r') as json_file:
    python_Daten = json.load(json_file)

######## variables ########
N0 = python_Daten['The last choices'][9]
N1 = python_Daten['The last choices'][8]
N2 = python_Daten['The last choices'][7]
N3 = python_Daten['The last choices'][6]
N4 = python_Daten['The last choices'][5]
N5 = python_Daten['The last choices'][4]
N6 = python_Daten['The last choices'][3]
N7 = python_Daten['The last choices'][2]
N8 = python_Daten['The last choices'][1]
N9 = python_Daten['The last choices'][0]

black_percent_Int = (python_Daten['The last choices'].count('BLACK')/10)*100
red_percent_Int = (python_Daten['The last choices'].count('RED')/10)*100

######## functions ########

def update_progress_bars():
    black_percent_Int.set((python_Daten['The last choices'].count('BLACK') / 10) * 100)
    red_percent_Int.set((python_Daten['The last choices'].count('RED') / 10) * 100)
    progress_BLACK['value'] = black_percent_Int.get()
    progress_RED['value'] = red_percent_Int.get()
    window.after(1000, update_progress_bars)

    black_percent_Int.set(f"{(python_Daten['The last choices'].count('BLACK') / 10) * 100}%")
    red_percent_Int.set(f"{(python_Daten['The last choices'].count('RED') / 10) * 100}%")

def update_blackAndRed_percent():
    black_percent = f"{(python_Daten['The last choices'].count('BLACK')/10)*100}%"
    red_percent = f"{(python_Daten['The last choices'].count('RED')/10)*100}%"
    black_percent_Int.set(black_percent)
    red_percent_Int.set(red_percent)

def update_last_choices_labels():
    color0.config(bg=N9)
    color1.config(bg=N8)
    color2.config(bg=N7)
    color3.config(bg=N6)
    color4.config(bg=N5)
    color5.config(bg=N4)
    color6.config(bg=N3)
    color7.config(bg=N2)
    color8.config(bg=N1)
    color9.config(bg=N0)

def dealer_choice():
    return random.choice(['BLACK', 'RED'])

def high_score_function():
    if player_score_Int.get() > python_Daten['highScore']:
        python_Daten['highScore'] = player_score_Int.get()
        high_score_string.set(player_score_Int.get())

def check_black():
    global player_score_Int, N0, N1, N2, N3, N4, N5, N6, N7, N8, N9
    the_dealer_choice = dealer_choice()
    # print(the_dealer_choice)
    with open('score.json', 'w') as json_file:
        json.dump(python_Daten, json_file, indent=4)
    if (python_Daten['The last choices'].count('RED') + python_Daten['The last choices'].count('BLACK')) != 10:
        python_Daten['The last choices'].append(the_dealer_choice)
    else:
        python_Daten['The last choices'].pop(0)
        python_Daten['The last choices'].append(the_dealer_choice)
        N0, N1, N2, N3, N4, N5, N6, N7, N8, N9 = python_Daten['The last choices']
        update_last_choices_labels()
        update_blackAndRed_percent()
        update_progress_bars()
        

    black_percent = (python_Daten['The last choices'].count('BLACK')/10)*100
    with open('score.json', 'w') as json_file:
        json.dump(python_Daten, json_file, indent=4)
    # time.sleep(0.5)
    if the_dealer_choice == 'BLACK':
        player_score_Int.set(player_score_Int.get() + 1)
    else:
        high_score_function()
        player_score_Int.set(0)


def check_red():
    global player_score_Int, N0, N1, N2, N3, N4, N5, N6, N7, N8, N9
    the_dealer_choice = dealer_choice()
    # print(the_dealer_choice)
    if (python_Daten['The last choices'].count('RED') + python_Daten['The last choices'].count('BLACK')) != 10:
        python_Daten['The last choices'].append(the_dealer_choice)
    else:
        python_Daten['The last choices'].pop(0)
        python_Daten['The last choices'].append(the_dealer_choice)
        N0, N1, N2, N3, N4, N5, N6, N7, N8, N9 = python_Daten['The last choices']
        update_last_choices_labels()
        update_blackAndRed_percent()
        update_progress_bars()

    with open('score.json', 'w') as json_file:
        json.dump(python_Daten, json_file, indent=4)
    # time.sleep(0.5)
    if the_dealer_choice == 'RED':
        player_score_Int.set(player_score_Int.get() + 1)
    else:
        high_score_function()
        player_score_Int.set(0)


window = tk.Tk()
window.title('Luck Game')
window.geometry('500x500')

####### Frame 1 #######

frame1 = tk.Frame(master=window)

player_name = tk.Label(master=frame1, text="Good Luck!", font=("Ravie", 30, "bold"))
your_score = tk.Label(master=frame1, text="Your score: ", font=("Rupee", 20, "bold"))
player_score_Int = tk.IntVar()
player_score = tk.Label(master=frame1, textvariable=player_score_Int, font=("Rupee", 20, "bold"), anchor="w")

player_name.pack()
your_score.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
player_score.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

frame1.pack(pady=10)

####### Frame 2 #######

frame2 = tk.Frame(master=window)

black_button = tk.Button(master=frame2, text="BLACK", command= check_black, font=("Stencil", 30, "bold"), bg="black", fg="white", width=True)
red_button = tk.Button(master=frame2, text="RED", command= check_red, font=("Stencil", 30, "bold"), bg="red", fg="white", width=True)

black_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
red_button.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)


frame2.pack(expand=True, fill=tk.BOTH)

####### Frame 3 #######

frame3 = tk.Frame(master=window)

frame3_1 = tk.Frame(master=frame3)
frame3_2 = tk.Frame(master=frame3)
frame3_3 = tk.Frame(master=frame3)

progress_BLACK = ttk.Progressbar(frame3_2, orient="horizontal", length=200, value=black_percent_Int, maximum=100)
progress_RED = ttk.Progressbar(frame3_2, orient="horizontal", length=200, value=red_percent_Int, maximum=100)
black_percent_Int = tk.IntVar(value=f'{black_percent_Int}%')
red_percent_Int = tk.IntVar(value=f'{red_percent_Int}%')
black_label = tk.Label(master=frame3_3, textvariable= black_percent_Int, font=("Rupee", 10))
red_label = tk.Label(master=frame3_1, textvariable= red_percent_Int, font=("Rupee", 10))

black_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
red_label.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
progress_RED.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
progress_BLACK.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

frame3_1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
frame3_2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
frame3_3.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)


frame3.pack(pady=10)

####### Frame 4 #######
frame4main = tk.Frame(master=window)

frame4sample = tk.Frame(master=frame4main)
last_choices = tk.Label(master=frame4sample, text="Last color: ", font=("Stencil", 20))
last_choices.pack()
frame4sample.pack(side=tk.LEFT)


frame4 = tk.Frame(master=frame4main)

color0 = tk.Label(master=frame4, bg=N0, width=3, height=True)
color1 = tk.Label(master=frame4, bg=N1, width=3, height=True)
color2 = tk.Label(master=frame4, bg=N2, width=3, height=True)
color3 = tk.Label(master=frame4, bg=N3, width=3, height=True)
color4 = tk.Label(master=frame4, bg=N4, width=3, height=True)
color5 = tk.Label(master=frame4, bg=N5, width=3, height=True)
color6 = tk.Label(master=frame4, bg=N6, width=3, height=True)
color7 = tk.Label(master=frame4, bg=N7, width=3, height=True)
color8 = tk.Label(master=frame4, bg=N8, width=3, height=True)
color9 = tk.Label(master=frame4, bg=N9, width=3, height=True)

frame4.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
frame4.rowconfigure(0, weight=1)


color0.grid(row=0, column=0, sticky='nswe', padx=1)
color1.grid(row=0, column=1, sticky='nswe', padx=1)
color2.grid(row=0, column=2, sticky='nswe', padx=1)
color3.grid(row=0, column=3, sticky='nswe', padx=1)
color4.grid(row=0, column=4, sticky='nswe', padx=1)
color5.grid(row=0, column=5, sticky='nswe', padx=1)
color6.grid(row=0, column=6, sticky='nswe', padx=1)
color7.grid(row=0, column=7, sticky='nswe', padx=1)
color8.grid(row=0, column=8, sticky='nswe', padx=1)
color9.grid(row=0, column=9, sticky='nswe', padx=1)

frame4.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

frame4main.pack()

####### Frame 5 #######

frame5 = tk.Frame(master=window)

high_score_label = tk.Label(master=frame5, text="High score: ", font=("Stencil", 30),fg="green")
high_score_string = tk.StringVar(value=python_Daten['highScore'])
high_score = tk.Label(master=frame5, textvariable=high_score_string, font=("Stencil", 30), fg="green")

high_score_label.pack(side=tk.LEFT)
high_score.pack(side=tk.LEFT)

frame5.pack(side=tk.BOTTOM,pady=10)



window.mainloop()

with open('score.json', 'w') as json_file:
    json.dump(python_Daten, json_file, indent=4)