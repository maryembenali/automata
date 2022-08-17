#where in this tooltip for additional help# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:14:39 2022

@author: maryem
"""

from tkinter import *
from tkinter import ttk
import tkinter.font as font
from automata.fa.dfa import DFA
import json
from PIL import ImageTk,Image
import graphviz
from automata.fa.nfa import NFA
import automata.base.exceptions as exceptions



root = Tk()
root.minsize(height=550,width=650)
root.title('automate generator')
Letters_List=[]
Number_V=0
Number_S=0
Transitions_Dict = dict()
States=[]
Initial_state=[]
final_states=[]
transitions=""
Number_F_S=0
Aut_Type=True

def menu():
    
    
    def vocab_page():
        print(Aut_Type)
        Frame_Menu.destroy()
        Frame_Vocab=ttk.Frame(root, padding=5)
        Frame_Vocab.grid()
        Vocab_Sum = IntVar()
        Label_Welcome_vocab=ttk.Label(Frame_Vocab,text='start by defining the number of elements of your automate" s vocabulary' ,font=('Arial',15)).grid(column=0,row=0)
        Label_Vocab_1=ttk.Label(Frame_Vocab,text='number of automates" vocabulary elements:' ,font=('Arial',10)).grid(column=0,row=1)
        Number_Input=Entry(Frame_Vocab,textvariable=Vocab_Sum).grid(row=1,column=1)
        
        

       
        def vocab_letters():
            Frame_Letters=ttk.Frame(root, padding=5)
            Frame_Letters.grid()
            Letter=StringVar()
            print(Number_V)
            global Letters_List
        
            def cases_page():
                Frame_Letters.destroy()
                Frame_cases=ttk.Frame(root, padding=5)
                Frame_cases.grid()
                States_Sum = IntVar()
                def Save4():
                    global Number_S
                    Number_S=States_Sum.get()
                    for i1 in range (Number_S):
                        States.append('q'+str(i1))
                    print(Number_S)
                    print(States)
                
                def Matrice_Page():
                     
                    def Save5():
                        global transitions
                        transitions=T_diction.get()
                        print("transtions as string =", transitions)
                        global Transitions_Dict
                        Transitions_Dict = json.loads(transitions)
                        print(type(Transitions_Dict))
                        print(Transitions_Dict)
                    def Page_Intial():
                        Frame_transitions.destroy()
                        Frame_I=ttk.Frame(root, padding=5)
                        Frame_I.grid()
                        def Save6():
                            global Initial_state
                            Initial_state.append(State_In.get())
                            print(Initial_state)
                        def Save7():
                            global Number_F_S
                            Number_F_S=Num_S.get()
                            print(Number_F_S)
                        def Final_States_Page():
                            Frame_I.destroy()
                            Frame_F=ttk.Frame(root, padding=5)
                            Frame_F.grid()
                            
                            def Save8():
                                final_states.append(State_String.get())
                                print(final_states)
                            def Automat_Welcome_Page():
                                Transitions_Dict = json.loads(transitions)
                                type(Transitions_Dict)
                                print(Transitions_Dict)
                                def automat_draw():
                                    f = graphviz.Digraph('finite_state_machine', filename='auto',format="png",directory="assets/")
                                    f.attr(rankdir='LR', size='8,5')
                                    f.attr('node', shape='doublecircle')
                                    for F_state in final_states:
                                        f.node(F_state)
                                    f.attr('node', shape='circle')
                                    for start,Dic_State in Transitions_Dict.items():
                                        for k,v in Dic_State.items():
                                            f.edge(start, v, label=k)
                                    f.view()
                                    global img
                                    img=Image.open("assets/auto.png")
                                    global img2
                                    img2=img.resize((300,150),Image.ANTIALIAS)
                                    global  Automat_View
                                    Automat_View=ImageTk.PhotoImage(img2)
                                    Label_img=ttk.Label(Frame_A,image=Automat_View).grid(column=2,row=0)
                                    #image_A=PhotoImage(file ="assets/auto.png")
                                    #Label_img=ttk.Label(Frame_A,image = image_A)
                                    
                                    
                                def Verify_Word():
                                    nfa = NFA(states=set(States),input_symbols=set(Letters_List),transitions=Transitions_Dict,initial_state=Initial_state[0],final_states=set(final_states))
                                    if nfa.accepts_input(Word_String.get()):
                                        print('accepted')
                                    else:
                                        print('rejected')
                                    #DFA.read_input_stepwise(self, Word_String.get())
                                        
                                Frame_F.destroy()   
                                Frame_A=ttk.Frame(root, padding=5)
                                Frame_A.grid()
                                if (Aut_Type):
                                    automat_draw()
                                Word_String = StringVar()
                                Label_Word=ttk.Label(Frame_A,text='verify if your automata accepts a word' ,font=('Arial',10)).grid(column=1,row=2) 
                                Word_Input=Entry(Frame_A,textvariable=Word_String).grid(row=4,column=1)
                                Button_Submit00=ttk.Button(Frame_A,text='Submit',command=Verify_Word).grid(column=2,row=4)
                                
                               
                                    
                                        
                                        
                            c=0
                            sf=Number_F_S 
                            State_String = StringVar()
                            while  sf!=0:
                                Label_2=ttk.Label(Frame_F,text='final state n°'+str(c) ,font=('Arial',10)).grid(column=0,row=c) 
                                
                                I_Input=Entry(Frame_F,textvariable=State_String).grid(row=c,column=1)
                                Button_Submit00=ttk.Button(Frame_F,text='Submit',command=Save8).grid(column=2,row=c)
                                c=c+1
                                sf=sf-1
                            Button_Sub=ttk.Button(Frame_F,text='Visualize your automate',command=Automat_Welcome_Page).grid(column=2,row=c+1)

                            
                            
                            
                        Label_2=ttk.Label(Frame_I,text='type the name of the initial state' ,font=('Arial',10)).grid(column=0,row=0) 
                        State_In = StringVar()
                        I_Input=Entry(Frame_I,textvariable=State_In).grid(row=0,column=1)
                        Button_Submit33=ttk.Button(Frame_I,text='Submit',command=Save6).grid(column=2,row=0)
                        Label_3=ttk.Label(Frame_I,text='type the number of the final states' ,font=('Arial',10)).grid(column=0,row=1) 
                        Num_S = IntVar() 
                        F_Sum_Input=Entry(Frame_I,textvariable=Num_S).grid(row=1,column=1)
                        Button_Submit31=ttk.Button(Frame_I,text='Submit',command=Save7).grid(column=2,row=1)
                        Button_Next4=ttk.Button(Frame_I,text='Next',command=Final_States_Page).grid(column=2,row=3)
                        
                        #deterministic example
                        #{"q0": {"a": "q1"}, "q1": {"a": "q1", "b": "q2"},"q2": {"b": "q0"}}
                        #without any other quotes double or single
                        
                        
                    Frame_cases.destroy()
                    Frame_transitions=ttk.Frame(root, padding=5)
                    Frame_transitions.grid()
                    T_diction = StringVar()
                    Label_1=ttk.Label(Frame_transitions,text='type the transitions in a dictionary' ,font=('Arial',10)).grid(column=0,row=0) 
                    T_Input=Entry(Frame_transitions,textvariable=T_diction).grid(row=0,column=1)
                    Button_Submit3=ttk.Button(Frame_transitions,text='Submit',command=Save5).grid(column=1,row=2)
                    Button_Next4=ttk.Button(Frame_transitions,text='Next',command=Page_Intial).grid(column=1,row=3)
                     
                  
                Label_Cases_1=ttk.Label(Frame_cases,text='number of states' ,font=('Arial',10)).grid(column=0,row=0) 
                States_Sum_Input=Entry(Frame_cases,textvariable=States_Sum).grid(row=0,column=1)
                Button_Submit2=ttk.Button(Frame_cases,text='Submit1',command=Save4).grid(column=2,row=2)
                Button_Next3=ttk.Button(Frame_cases,text='Next',command=Matrice_Page).grid(column=2,row=3)

                
            def save3():
                Letters_List.append(Letter.get())
                print(Letters_List)
             
                
                
            j=Number_V
            i=0   
            while j != 0 :
                Label_Vocab_1=ttk.Label(Frame_Letters,text='element number'+str(i) ,font=('Arial',10)).grid(column=0,row=i) 
                Letters_Input=Entry(Frame_Letters,textvariable=Letter).grid(row=i,column=1)
                Button_Submit=ttk.Button(Frame_Letters,text='Submit',command=save3).grid(column=2,row=i)
                j=j-1
                i=i+1
            
            Button_Next2=ttk.Button(Frame_Letters,text='Next',command=cases_page).grid(column=2,row=i+1)
    
        
            
        def back():
            Frame_Vocab.destroy()
            menu()
        def next():
            def save1():
                global Number_V 
                Number_V=Vocab_Sum.get()
                print(Number_V)
            save1()    
            Frame_Vocab.destroy()
            vocab_letters()
            
        Button_Back=ttk.Button(Frame_Vocab,text='Back',command=back).grid(column=0,row=5)
        Button_Next=ttk.Button(Frame_Vocab,text='Next',command=next).grid(column=0,row=6)    
            
    def check_changed():
        global Aut_Type
        if (checkbox_var1.get()=="deterministic"):
            Aut_Type=True
       
            
            
    def check_changed2():
        global Aut_Type
        if (checkbox_var2.get()=="non-deterministic"):
            Aut_Type=False
            
        
    Frame_Menu=ttk.Frame(root, padding=5)
    Frame_Menu.grid()    
    Label_Welcome=ttk.Label(Frame_Menu,text='welcome to automate generator',font=('Script',25)).grid(column=0,row=0)
    Label_Start=ttk.Label(Frame_Menu,text='click on continue to start creating your automate',font=('Script',25)).grid(column=0,row=1)
    checkbox_var1 = StringVar()
    checkbox_var2 = StringVar()
    Label_T=ttk.Label(Frame_Menu,text='your finite automate is',font=('Arial',25)).grid(column=0,row=2)
    checkbox1 = ttk.Checkbutton(Frame_Menu, text='deterministic', command=check_changed,variable=checkbox_var1, onvalue='non-deterministic', offvalue='non-deterministic').grid(column=1,row=2)
    checkbox2 = ttk.Checkbutton(Frame_Menu, text='non-deterministic', command=check_changed2,variable=checkbox_var2, onvalue='non-deterministic', offvalue='deterministic').grid(column=2,row=2)
    Button_Start=ttk.Button(Frame_Menu,text='Continue',command=vocab_page).grid(column=0,row=3)

menu()
root.mainloop()