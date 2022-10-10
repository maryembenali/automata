# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:24:10 2022

@author: benmb
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:50:55 2022

@author: maryem
"""

from tkinter import *
from tkinter import ttk
import tkinter.font as font
from automata.fa.nfa import NFA
import ast
from PIL import ImageTk,Image
import graphviz


Letters_List=[]
Number_V=0
Number_S=0
Transitions_Dict = dict()
States=[]
Initial_state=[]
final_states=[]
transitions=""
Number_F_S=0
test=FALSE
list_S=list()
Text_Res=""
root = Tk()
root.geometry("650x550")
root.title('automata')
root.iconbitmap('assets/hypnose.ico')
img2=Image.open("assets/menu.png")
Automat_View_Path=ImageTk.PhotoImage(img2)
Label_img=ttk.Label(root,image=Automat_View_Path)
Label_img.place(x=0, y=0)

def menu():#first window function
    def help_page():#help window
        global my_img
        top=Toplevel()
        top.title('Transition help page')
        top.iconbitmap('assets/hypnose.ico')
        my_img=ImageTk.PhotoImage(Image.open("assets/akrem.png"))
        my_label=Label(top,image=my_img).pack()
    def vocab_page():#second window
        but1.destroy()
        but2.destroy()
        global Automat_View_Path
        Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/2.png"))
        Label_img=ttk.Label(root,image=Automat_View_Path)
        Label_img.place(x=0, y=0)
        Vocab_Sum = IntVar()
        global Number_Input
        Number_Input=Entry(root,textvariable=Vocab_Sum,highlightthickness=2)
        Number_Input.place(x=200,y=200)
        def next():
            def vocab_letters():#third window
                def save3():
                    Letters_List.append(Letter.get())
                    print(Letters_List)
                def cases_page():#forth window
                    Label_Vocab_1.destroy()
                    Letters_Input.destroy()
                    Button_Submit.destroy()
                    Button_Next2.destroy()
                    global Automat_View_Path
                    Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/4.png"))
                    Label_img=ttk.Label(root,image=Automat_View_Path)
                    Label_img.place(x=0, y=0)
                    States_Sum = IntVar()
                    def Save4():
                        global Number_S
                        Number_S=States_Sum.get()
                        for i1 in range (Number_S):
                            States.append('q'+str(i1))
                        print(Number_S)
                        print(States)
                    def Matrice_Page():#fifth window
                        def Save5():
                            global transitions
                            transitions=T_diction.get()
                            print("transtions as string =", transitions)
                            global Transitions_Dict
                            Transitions_Dict = ast.literal_eval(transitions)
                            print(type(Transitions_Dict))
                            print(Transitions_Dict)
                            
                        def Page_Intial():#sixth window
                            def Save6():
                                global Initial_state
                                Initial_state.append(State_In.get())
                                print(Initial_state)
                            def Save7():
                                global Number_F_S
                                Number_F_S=Num_S.get()
                                print(Number_F_S)
                            def Final_States_Page():#seventh window
                                def Save8():
                                    print("ty")
                                    final_states.append(State_String.get())
                                    print(final_states)
                                def Automat_Welcome_Page():#eightth window
                                    def Final_page():#last window
                                        def destruct():
                                            Label_img2.destroy()
                                            Label_Word.destroy()
                                            Word_Input.destroy()
                                            Button_View.destroy()
                                            Label_Res.destroy()
                                            Button_Submit00.destroy()
                                            
                                            
                                        destruct()
                                        global Automat_View_Path
                                        Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/automat.png"))
                                        Label_img=ttk.Label(root,image=Automat_View_Path)
                                        Label_img.place(x=0, y=0)
                                        f2 = graphviz.Digraph('pathway', filename='iteration',format="png",directory="assets/")
                                        f2.attr(rankdir='LR', size='8,5')
                                        nfa = NFA(states=set(States),input_symbols=set(Letters_List),transitions=Transitions_Dict,initial_state=Initial_state[0],final_states=set(final_states))
                                        lista=list(nfa.read_input_stepwise(Word_String.get()))
                                        new_list=list()
                                        for e in lista:
                                                new_list.append(list(e)[::-1])
                                        for i in range(len(new_list)-1):
                                            f2.attr('node', shape='circle')
                                            f2.edge(new_list[i][0], new_list[i+1][0],label=Word_String.get()[i]+"\n"+"step"+"{}".format(i+1))
                                        f2.view() 
                                        global finalimage
                                        finalimage=Image.open("assets/iteration.png")
                                        global finalimage2
                                        finalimage2=finalimage.resize((400,250),Image.ANTIALIAS)
                                        global  Automat_View_Path2
                                        Automat_View_Path2=ImageTk.PhotoImage(finalimage2)
                                        global Label_img3
                                        Label_img3=ttk.Label(root,image=Automat_View_Path2)
                                        Label_img3.place(x=100,y=140)
                                        global Button_new
                                        Button_new=Button(root,text='create a new automata',font=myFont3,command=redirect)
                                        Button_new.place(x=450,y=400)
                                        global Button_new_word
                                        Button_new_word=Button(root,text='try another word',font=myFont3,command=Automat_Welcome_Page)
                                        Button_new_word.place(x=450,y=450)

                                    def Verify_Word():
                                        global Text_Res
                                        nfa = NFA(states=set(States),input_symbols=set(Letters_List),transitions=Transitions_Dict,initial_state=Initial_state[0],final_states=set(final_states))
                                        if nfa.accepts_input(Word_String.get()):
                                            Text_Res='accepted'
                                            global Button_View
                                            Button_View=Button(root,text='click here to view iterations ',font=myFont3,command=Final_page)
                                            Button_View.place(x=150,y=350)
                                        else:
                                            Text_Res='rejected'
                                            
                                        print(Text_Res)
                                        myFont5 = font.Font(family='french script mt',size=17)
                                        global Label_Res
                                        Label_Res=Label(root,bg="#ffffff",fg="#106ea1",text=Text_Res,font=myFont5)
                                        Label_Res.place(x=50,y=350)
                                        
                                    def automat_draw():
                                        f = graphviz.Digraph('finite_state_machine', filename='auto',format="png",directory="assets/")
                                        f.attr(rankdir='LR', size='8,5')
                                        f.attr('node', shape='doublecircle')
                                        for F_state in final_states:
                                            f.node(F_state)
                                        f.attr('node', shape='circle')
                                        for start,Dic_State in Transitions_Dict.items():
                                            for k,v in Dic_State.items():
                                               for States_Destination in v:
                                                   f.edge(start, States_Destination, label=k)
                                                        
                                        f.view()
                                        global img
                                        img=Image.open("assets/auto.png")
                                        global img2
                                        img2=img.resize((350,220),Image.ANTIALIAS)
                                        global  Automat_View
                                        Automat_View=ImageTk.PhotoImage(img2)
                                        global Label_img2
                                        Label_img2=Label(root,image=Automat_View)
                                        Label_img2.place(x=280,y=20)
                                        
                                    Label_Add2.destroy()
                                    Label_Add21.destroy()
                                    Label_Add22.destroy()
                                    Label_Add23.destroy()
                                    Label_Add24.destroy()
                                    Label_Add25.destroy()
                                    Label_Add26.destroy()
                                    Label_f.destroy()
                                    I_Input0.destroy()
                                    Button_Sub.destroy()
                                    def redirect():
                                        global Letters_List
                                        global Initial_state
                                        global final_states
                                        global States
                                        States=[]
                                        Letters_List=[]
                                        Initial_state=[]
                                        final_states=[]
                                        vocab_page()
                                    global Automat_View_Path
                                    Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/automat.png"))
                                    Label_img=ttk.Label(root,image=Automat_View_Path)
                                    Label_img.place(x=0, y=0)
                                    automat_draw()
                                    myFont3 = font.Font(family='french script mt',size=16)
                                    Word_String = StringVar()
                                    global Label_Word
                                    Label_Word=Label(root,bg="#ffffff",text='verify if your automata accepts a word',font=('french script mt',16))
                                    Label_Word.place(x=20,y=220) 
                                    global Word_Input
                                    Word_Input=Entry(root,textvariable=Word_String)
                                    Word_Input.place(x=20,y=270)
                                    global Button_Submit00
                                    Button_Submit00=Button(root,text='Submit',font=myFont3,command=Verify_Word)
                                    Button_Submit00.place(x=150,y=250)
                                    global Button_new
                                    Button_new=Button(root,text='create a new automata',font=myFont3,command=redirect)
                                    Button_new.place(x=450,y=350)
                                    
                                    
                                def redirect5():
                                    Label_Add2.destroy()
                                    Label_Add21.destroy()
                                    Label_Add22.destroy()
                                    Label_Add23.destroy()
                                    Label_Add24.destroy()
                                    Label_Add25.destroy()
                                    Label_Add26.destroy()
                                    Label_f.destroy()
                                    I_Input0.destroy()
                                    Button_Submit00.destroy()
                                    Button_Sub.destroy()
                                    button_back3.destroy()
                                   
                                    global Initial_state
                                    global final_states
                                    Initial_state=[]
                                    final_states=[]
                                    Page_Intial()
                                    
                                Label_2.destroy()
                                I_Input.destroy()
                                Button_Submit33.destroy()
                                Label_3.destroy()
                                F_Sum_Input.destroy()
                                Button_Submit31.destroy()
                                Button_Next00.destroy()
                                global Automat_View_Path
                                Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/0.png"))
                                Label_img=ttk.Label(root,image=Automat_View_Path)
                                Label_img.place(x=0, y=0)
                                global Label_Add2
                                Label_Add2=Label(root,bg="#ffffff")
                                Label_Add2.grid(column=0,row=0)
                                global Label_Add21
                                Label_Add21=Label(root,bg="#ffffff")
                                Label_Add21.grid(column=0,row=1)
                                global Label_Add22
                                Label_Add22=Label(root,bg="#ffffff")
                                Label_Add22.grid(column=3,row=2)
                                global Label_Add23
                                Label_Add23=Label(root,bg="#ffffff")
                                Label_Add23.grid(column=3,row=3)
                                global Label_Add24
                                Label_Add24=Label(root,bg="#ffffff")
                                Label_Add24.grid(column=3,row=4)
                                global Label_Add25
                                Label_Add25=Label(root,bg="#ffffff")
                                Label_Add25.grid(column=0,row=5)
                                global Label_Add26
                                Label_Add26=Label(root,bg="#ffffff")
                                Label_Add26.grid(column=0,row=6)
                                
                                c=7
                                a=1
                                sf=Number_F_S 
                                State_String = StringVar()
                                while  sf!=0:
                                    global Label_f
                                    Label_f=Label(root,text='final state n°'+str(a),bg="#ffffff" ,font=('french script mt',16))
                                    Label_f.grid(column=0,row=c) 
                                    global I_Input0
                                    I_Input0=Entry(root,textvariable=State_String,highlightthickness=2)
                                    I_Input0.grid(row=c,column=1)
                                    global Button_Submit00
                                    Button_Submit00=Button(root,text='Submit',font=myFont3,command=Save8)
                                    Button_Submit00.grid(column=2,row=c)
                                    c=c+1
                                    a=a+1
                                    sf=sf-1
                                global  Button_Sub
                                Button_Sub=Button(root,text='Visualize your automate',command=Automat_Welcome_Page,height=0,width=0,font=myFont3)
                                Button_Sub.grid(column=2,row=c+1)
                                global button_back3
                                button_back3= Button(root,text='back',command=redirect5,font=myFont2)
                                button_back3.place(x=20,y=500)
                                
                            def redirect4():
                                button_back3.destroy()
                                Label_2.destroy()
                                I_Input.destroy()
                                Button_Submit33.destroy()
                                Label_3.destroy()
                                F_Sum_Input.destroy()
                                Button_Submit31.destroy()
                                Button_Next00.destroy()
                                global Initial_state
                                global final_states
                                
                                Initial_state=[]
                                final_states=[]
                                Matrice_Page()
                                
                            print("im tired")
                            T_Input.destroy()
                            Button_Next4.destroy()
                            Button_Submit3.destroy()
                            global Automat_View_Path
                            Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/0.png"))
                            Label_img=ttk.Label(root,image=Automat_View_Path)
                            Label_img.place(x=0, y=0)
                            global button_back3
                            button_back3= Button(root,text='back',command=redirect4,font=myFont2)
                            button_back3.place(x=20,y=500)
                            
                            global Label_2
                            Label_2=Label(root,text='type the initial state',bg="#ffffff" ,font=('french script mt',15))
                            Label_2.place(x=50,y=250)
                            State_In = StringVar()
                            global I_Input
                            I_Input=Entry(root,textvariable=State_In,highlightthickness=2)
                            I_Input.place(x=350,y=250)
                            global Button_Submit33
                            Button_Submit33=Button(root,text='Submit',height=0,width=0,font=myFont3,command=Save6)
                            Button_Submit33.place(x=500,y=250)
                            global Label_3
                            Label_3=Label(root,text='type the number of the final states',bg="#ffffff" ,font=('french script mt',15))
                            Label_3.place(x=50,y=350)
                            Num_S = IntVar() 
                            global F_Sum_Input
                            F_Sum_Input=Entry(root,textvariable=Num_S,highlightthickness=2)
                            F_Sum_Input.place(x=350,y=350)
                            global Button_Submit31
                            Button_Submit31=Button(root,text='Submit',height=0,width=0,font=myFont3,command=Save7)
                            Button_Submit31.place(x=500,y=350)
                            global Button_Next00
                            Button_Next00=Button(root,text='Next',height=0,width=0,font=myFont3,command=Final_States_Page)
                            Button_Next00.place(x=500,y=500)
                        
                        def redirect3():
                            Label_help.destroy()
                            T_Input.destroy()
                            manual.destroy()
                            Button_Submit3.destroy()
                            Button_Next4.destroy()
                            button_back2.destroy()
                            global States
                            States=[]
                            cases_page()
                            
                            
                        States_Sum_Input.destroy()
                        Button_Submit2.destroy()
                        Button_Next3.destroy()
                        global Automat_View_Path
                        Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/5.png"))
                        Label_img=ttk.Label(root,image=Automat_View_Path)
                        Label_img.place(x=0, y=0)
                        T_diction = StringVar()
                        global Label_help
                        Label_help=Label(root,text='Please click on the help button to show transitions manual' ,bg="#ffffff",font=('french script mt',15))
                        Label_help.place(x=50,y=170)
                        global T_Input
                        T_Input=Entry(root,width=90,textvariable=T_diction,highlightthickness=2)
                        T_Input.place(x=20,y=210)
                        myFont4 = font.Font(family='french script mt',size=17)
                        global manual
                        manual=Button(root,text='?',command=help_page,height=0,width=0,font=myFont3)
                        manual.place(x=565,y=200)
                        global Button_Submit3
                        Button_Submit3=Button(root,text='Submit',command=Save5,height=0,width=0,font=myFont3)
                        Button_Submit3.place(x=590,y=200)
                        global Button_Next4
                        Button_Next4=Button(root,text='Next',command=Page_Intial,height=0,width=0,font=myFont4)
                        Button_Next4.place(x=300,y=300)
                        print("GLG914")
                        global button_back2
                        button_back2= Button(root,text='back',command=redirect3,font=myFont2)
                        button_back2.place(x=20,y=500)
                      
                      
                        
                    def redirect1():
                        global States
                        States=[]
                        global Letters_List
                        Letters_List=[]
                        vocab_letters()
                        Button_back0.destroy()
                        Button_Submit2.destroy()
                        Button_Next3.destroy()
                        States_Sum_Input.destroy()
                        
                    myFont3 = font.Font(family='french script mt',size=15)
                    global States_Sum_Input
                    States_Sum_Input=Entry(root,textvariable=States_Sum,highlightthickness=2)
                    States_Sum_Input.place(x=10,y=200)
                    global Button_Submit2
                    Button_Submit2=Button(root,text='Submit',font=myFont3,command=Save4)#height=0,width=0,font=myFont3)
                    Button_Submit2.place(x=250,y=190)
                    global Button_Next3
                    Button_Next3=Button(root,text='Next',width=6,font=myFont3,command=Matrice_Page)
                    Button_Next3.place(x=250,y=300)
                    global Button_back0
                    Button_back0=Button(root,text='back',width=6,font=myFont3,command=redirect1)
                    Button_back0.place(x=20,y=500)
                    print("FLG")
                Letter=StringVar()
                print(Number_V)
                global Letters_List
                j=Number_V
                i=9 
                n=0
                Label_Add=Label(root,bg="#ffffff").grid(column=1,row=0)
                Label_Add=Label(root,bg="#ffffff").grid(column=2,row=1)
                Label_Add=Label(root,bg="#ffffff").grid(column=3,row=2)
                Label_Add=Label(root,bg="#ffffff").grid(column=4,row=3)
                Label_Add=Label(root,bg="#ffffff").grid(column=1,row=4)
                Label_Add=Label(root,bg="#ffffff").grid(column=1,row=5)
                Label_Add=Label(root,bg="#ffffff").grid(column=4,row=6)
                Label_Add=Label(root,bg="#ffffff").grid(column=4,row=7)
                Label_Add=Label(root,bg="#ffffff").grid(column=9,row=8)
                def redirect0():
                    global Letters_List
                    Letters_List=[]
                    vocab_page()
                    
                while j != 0 :
                    global Label_Vocab_1
                    Label_Vocab_1=Label(root,text='element number'+' '+str(n+1),bg="#ffffff" ,font=('french script mt',20))
                    Label_Vocab_1.grid(column=0,row=i)
                    global Letters_Input 
                    Letters_Input=Entry(root,textvariable=Letter,highlightthickness=2)
                    Letters_Input.grid(column=3,row=i)
                    global Button_Submit
                    myFont3 = font.Font(family='french script mt',size=15)
                    Button_Submit=Button(root,text='Submit',bg="#ffffff",command=save3,height=0,width=0,font=myFont3)
                    Button_Submit.grid(column=5,row=i)
                    n=n+1
                    j=j-1
                    i=i+1
                global Button_Next2
                Label_Add=Label(root,bg="#ffffff").grid(column=9,row=i)
                Button_Next2=Button(root,text='Next',bg="#ffffff",command=cases_page,height=0,width=6,font=myFont3)
                Button_Next2.grid(column=8,row=i+2)
                
                global Button_back
                Label_Add=Label(root,bg="#ffffff").grid(column=9,row=i+3)
                Button_back=Button(root,text='back',bg="#ffffff",command=redirect0,height=0,width=6,font=myFont3)
                Button_back.grid(column=8,row=i+4)
            def save1():
                global Number_V 
                Number_V=Vocab_Sum.get()
                print(Number_V)
            save1()
            Button_Next.destroy()
            Number_Input.destroy()
            global Automat_View_Path
            Automat_View_Path=ImageTk.PhotoImage(Image.open("assets/3.png"))
            Label_img=ttk.Label(root,image=Automat_View_Path)
            Label_img.place(x=0, y=0)
            vocab_letters()
            
            
        myFont2 = font.Font(family='french script mt',size=17)
        global Button_Next
        Button_Next=Button(root,text='Next',font=myFont2,width=5,command=next)
        Button_Next.place(x=290,y=340)
    
    myFont = font.Font(family='french script mt',size=22)
    myFont2 = font.Font(family='french script mt',size=15,weight="bold")
    global but1
    but1= Button(root,text='Start',command=vocab_page,height=1,width=9,font=myFont,bg="#c0deef")
    but1.place(x=429, y=274)
    global but2
    but2= Button(root,text='?',command=vocab_page,height=0,width=13,font=myFont2,bg="#f2f2f2",fg='#c3c3c3')
    but2.place(x=427, y=351)
  
    
    
menu()
root.mainloop()