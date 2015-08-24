# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:25:12 2015

@author: Simon
"""

# select a dice image at random using Tkinter
# tested with Python24     vegaseat      23dec2006
import tkinter as tk  # use tk namespace for Tkinter items
import random
def create_dice():
    """
    create the dice canvas list as dice[0] to dice[6]
    """
    dice = []
    dice.append(draw_dice('dot0'))   # empty
    dice.append(draw_dice('dot5'))   # center dot --> 1
    dice.append(draw_dice('dot4', 'dot6'))
    dice.append(draw_dice('dot3', 'dot5', 'dot7'))
    dice.append(draw_dice('dot1', 'dot3', 'dot7', 'dot9'))
    dice.append(draw_dice('dot1', 'dot3', 'dot5', 'dot7', 'dot9'))
    dice.append(draw_dice('dot1', 'dot3', 'dot4', 'dot6', 'dot7', 'dot9'))
    return dice
def draw_dice(*arg):
    """
    draws the 7 different dice dots on the canvas
    """
    w = 20
    h = 20
    c = tk.Canvas(root, width=w+3, height=h+3, bg='yellow')
    # set the dot specs
    x = 2
    y = 2
    r = 5
    if 'dot1' in arg:
        dot1 = c.create_oval(x, y, x+r, y+r, fill='black')
    x = w/2
    x = 18
    if 'dot3' in arg:
        dot3 = c.create_oval(x, y, x+r, y+r, fill='black')
    x = 2
    y = h/2
    if 'dot4' in arg:
        dot4 = c.create_oval(x, y, x+r, y+r, fill='black')
    x = w/2
    if 'dot5' in arg:
        dot5 = c.create_oval(x, y, x+r, y+r, fill='black')
    x = 18
    if 'dot6' in arg:
        dot6 = c.create_oval(x, y, x+r, y+r, fill='black')
    x = 2
    y = 18
    if 'dot7' in arg:
        dot7 = c.create_oval(x, y, x+r, y+r, fill='black')
    x = w/2
    x = 18
    if 'dot9' in arg:
        dot9 = c.create_oval(x, y, x+r, y+r, fill='black')
    if 'dot0' in arg:
        pass
    return c
def click():
    """
    display a randomly selected dice value
    """
    # start with a time delay of 100 ms and increase it as the dice rolls
    t = 100
    stop = random.randint(13, 18)
    for x in range(stop):
        dice_index = x%6 + 1
        root.title(str(dice_index))  # test
        dice_list[dice_index].grid(row=1, column=0, pady=5)
        root.update()
        if x == stop-1:
            # final result available via var1.get()
            var1.set(str(x%6 + 1))
            break
        root.after(t, dice_list[dice_index].grid_forget())
        t += 25
    
# create the window form
root = tk.Tk()
# StringVar() updates result label automatically
var1 = tk.StringVar()
# set initial value
var1.set("")
# create the result label
result = tk.Label(root, textvariable=var1, fg='red')
result.grid(row=3, column=0, columnspan=3)
dice_list = create_dice()
# start with an empty canvas
dice_list[0].grid(row=1, column=0, pady=5)
button1 = tk.Button(root, text="Press me", command=click)
button1.grid(row=2, column=0, pady=3)
# start of program event loop
root.mainloop()