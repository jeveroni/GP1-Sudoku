#Soduko Gui Attempt 1!!!


#This imports tkinter, sets up a window and two frames within it
import tkinter
import tkinter.messagebox
import numpy as np
from tkinter import *

window = tkinter.Tk()
window.geometry("955x455")
window.resizable(0, 0)
window.title("Jev's Sudoku Solver")

left_frame = tkinter.Frame(window,height=455,width=455, background= 'black')
left_frame.place(x=0,y=0)
right_frame = tkinter.Frame(window,height=455,width=500,background='lightblue')
right_frame.place(x=455,y=0)

#Functions

#This function will replace the numbers inside of a cell in the sudoku
def replace(i,j,x):
    sudoku[i][j].delete(0,"end")
    sudoku[i][j].insert(0,x)
    



#This is just a test to see how to get numbers that i've placed on to the sudoku off of it 
    
#This will take whatever values you have placed onto the sudoku board and put them into the array for my backtracking
#code to solve
def set_up_board():
    for i in range(9):
        for j in range(9):
            number = (sudoku[i][j]).get()
            if len(number) != 0:
                board[i][j] = int(number)
            else:
                board[i][j] = 0
    check_elig()
    
def set_up_easy():
    for i in range(9):
        for j in range(9):
            sudoku[i][j].delete(0,'end')
            if easy[i][j] != 0:
                replace(i,j,easy[i][j])
    set_up_board()
    window.update()
    
def set_up_med():
    for i in range(9):
        for j in range(9):
            sudoku[i][j].delete(0,'end')
            if medium[i][j] != 0:
                replace(i,j,medium[i][j])
    set_up_board()
    window.update()
    
def set_up_hard():
    for i in range(9):
        for j in range(9):
            sudoku[i][j].delete(0,'end')
            if hard[i][j] != 0:
                replace(i,j,hard[i][j])
    set_up_board()
    window.update()
    
    
#This will check if the board is currently eligible to be solved using the fuctions already made for solving
#it takes the number out and acts like it's placing it on a normal run
def check_elig():
    for i in range(9):
        for j in range(9):
            if empty(i,j):
                ()
#                if the spot is empty it doesnt need to be checked for eligibility
            elif board[i][j] > 9 or board[i][j] < 1:
                tkinter.Label(right_frame,text = "Not Eligible").place(x=100,y=200, height=100,width=300)
                return
                
            else:
                temp = board[i][j]
                board[i][j] = 0
                if column(temp,i,j):
                    if row(temp,i,j):
                        if sec_solve(temp,i,j):
                            board[i][j] = temp
                            tkinter.Label(right_frame,text = "Eligible", bg='spring green').place(x=100,y=200, height=100,width=300)
                            
                        else:
                            tkinter.Label(right_frame,text = "Not Eligible", bg='red2').place(x=100,y=200, height=100,width=300)
                            board[i][j]=temp
                            return 
                    else:
                        tkinter.Label(right_frame,text = "Not Eligible",bg='red2').place(x=100,y=200, height=100,width=300)
                        board[i][j]=temp
                        return 
                
                else:
                    tkinter.Label(right_frame,text = "Not Eligible",bg='red2').place(x=100,y=200, height=100,width=300)
                    board[i][j]=temp
                    return 
        
    
    
        
#These are functions for the sudoku solver in project 2
def empty(x,y):
    if board[x][y] == 0:
        return True
    return False

def column(num,x,y):
    for i in range(9):
        if num == board[i][y]:
            return False
    return True
    
def row(num,x,y):
    for i in range(8):
        if num == board[x][i]:
            return False
    return True

def sec_solve(num,x,y):
    if x in range(0,3) and y in range(0,3):
        for i in range(0,3):
            for j in range(0,3):
                if num == board[i][j]:
                    return False
        return True
    
    if x in range(0,3) and y in range(3,6):
        for i in range(0,3):
            for j in range(3,6):
                if num == board[i][j]:
                    return False
        return True
    
    if x in range(0,3) and y in range(6,9):
        for i in range(0,3):
            for j in range(6,9):
                if num == board[i][j]:
                    return False
        return True
    
    if x in range(3,6) and y in range(0,3):
        for i in range(3,6):
            for j in range(0,3):
                if num == board[i][j]:
                    return False
        return True
    
    if x in range(3,6) and y in range(3,6):
        for i in range(3,6):
            for j in range(3,6):
                if num == board[i][j]:
                    return False
        return True
    
    if x in range(3,6) and y in range(6,9):
        for i in range(3,6):
            for j in range(6,9):
                if num == board[i][j]:
                    return False
        return True
    
    if x in range(6,9) and y in range(0,3):
        for i in range(6,9):
            for j in range(0,3):
                if num == board[i][j]:
                    return False
        return True
    
    if x in range(6,9) and y in range(3,6):
        for i in range(6,9):
            for j in range(3,6):
                if num == board[i][j]:
                    return False
        return True
    
    if x in range(6,9) and y in range(6,9):
        for i in range(6,9):
            for j in range(6,9):
                if num == board[i][j]:
                    return False
        return True
    
def slow_solve():
    zero = 0
    for i in range(9):
        for j in range(9):
            if(empty(i,j)):
                zero = zero + 1
    if zero == 0:
        return True
    
    for i in range(9):
        for j in range(9):
            if(empty(i,j)):
                x = i
                y = j
                break
        else: continue
        break
    
    for i in range(1,10):
        num = i
        replace(x,y,num)
        window.update()
        if(column(num,x,y)):
            if(row(num,x,y)):
                if(sec_solve(num,x,y)):
                    board[x][y] = num
                    if(slow_solve()):
                        return True
                    board[x][y] = 0
                else:
                    replace(x,y,'')
            else:
                replace(x,y,'')
        else:
            replace(x,y,'')
        window.update()
    return False       

def fast_solve():
    zero = 0
    for i in range(9):
        for j in range(9):
            if(empty(i,j)):
                zero = zero + 1
    if zero == 0:
        return True
    
    for i in range(9):
        for j in range(9):
            if(empty(i,j)):
                x = i
                y = j
                break
        else: continue
        break
    
    for i in range(1,10):
        num = i
        replace(x,y,num)
        if(column(num,x,y)):
            if(row(num,x,y)):
                if(sec_solve(num,x,y)):
                    board[x][y] = num
                    if(fast_solve()):
                        return True
                    board[x][y] = 0
    return False 


#This is the board which my program needs to be in the form of to solve
board = np.array([
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]])

easy = np.array([
    [7,0,0,3,0,9,0,8,0], 
    [0,3,9,8,0,7,2,4,0],
    [1,8,0,4,0,0,7,3,0],
    [0,0,8,0,0,5,0,0,7],
    [4,0,0,0,8,3,0,0,0],
    [0,5,6,0,0,0,8,1,0],
    [2,0,4,0,7,0,0,0,0],
    [0,1,0,5,0,0,0,2,4],
    [0,0,0,2,4,0,0,0,1]])
    
medium = np.array([
    [0,9,4,0,5,7,0,0,0], 
    [8,0,0,0,9,6,0,0,0],
    [3,0,0,0,8,4,1,9,0],
    [1,3,0,0,7,2,0,0,4],
    [0,4,0,8,0,0,0,0,7],
    [7,0,0,0,0,0,0,0,0],
    [0,7,0,0,0,8,0,6,0],
    [5,0,1,0,0,0,0,0,0],
    [2,0,0,0,0,5,0,7,8]])
    
hard = np.array([
    [0,0,4,8,6,0,0,3,0], 
    [0,0,1,0,0,0,0,9,0],
    [8,0,0,0,0,9,0,6,0],
    [5,0,0,2,0,6,0,0,1],
    [0,2,7,0,0,1,0,0,0],
    [0,0,0,0,4,3,0,0,6],
    [0,5,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,4,0,0],
    [0,0,0,4,0,0,0,1,5]])


    
#This sets up each of the entry boxes, and also stores them in the sudoku array in the same sort of storage as the board    
sudoku=[]
for i in range(0,9):
    entry_boxes=[]
    for j in range(0,9):
        box_name = tkinter.Entry(left_frame,font = "Helvetica 44 bold",justify="center")
        box_name.place(x=(50*j)+5,y=(50*i)+5,height=45,width=45)
#        j and i have been switched here so that it creates it box across then down instead of down and across 
        entry_boxes.append(box_name)
    sudoku.append(entry_boxes)

 

tkinter.Label(right_frame,text = "Hello! Welcome to Jev's Sudoku Solver, which solves sudoku's using backtracking technology!! Please either type in your values and press check eligibility to see if it can be worked out, then press solve to find your solution or pick one of the presets below! (Remember to press Check Eligibility before trying to solve)",bg="lightblue",wraplengt=475).place(x=0,y=0)
tkinter.Button(right_frame,text = 'Easy Board', command = set_up_easy).place(x=105,y=150,width=90)
tkinter.Button(right_frame,text = 'Medium Board', command = set_up_med).place(x=205,y=150,width=90)
tkinter.Button(right_frame,text = 'Hard Board', command = set_up_hard).place(x=305,y=150,width=90)
tkinter.Button(right_frame,text = "Check Eligibility", command = set_up_board).place(x=100,y=300,height=100,width=100)
tkinter.Button(right_frame,text = "Fast Solve!", command = fast_solve).place(x=200,y=300,height=100,width=100)
tkinter.Button(right_frame,text = "Slow Solve!",command = slow_solve).place(x=300,y=300,height=100,width=100)
tkinter.mainloop()