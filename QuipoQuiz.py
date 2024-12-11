# essayer de refaire quipo quizz en ma version

from tkinter import*

tk = Tk()
tk.geometry("1000x700+50+50")
tk.title("quipo quizz")
tk.config(bg="#77b5fE")
tk_frame=Frame(tk,width=900,height=610,bg="#1E90FF")
tk_frame.place(x=50,y=50)


def sujet_histoire():
    tk_hisoire_1 = Tk()
    tk_hisoire_1.geometry("1000x700+50+50")
    tk_hisoire_1.title("questions histoire")
    tk_hisoire_1.config(bg="white")
    annecdote_1_h = Label(tk_hisoire_1, text="Le Montenegro et le Japon on été en guerre pendant 101 ans .",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1_h.pack()

    def v_1_h ():
        v_M_P=Label(tk_hisoire_1,text="en effet les 2 pays avaient oublié de signer le traiter de paix.",font=("ghotique",25),bg="white",fg="green")
        v_M_P.place(x=50,y=300)


    def f_1_h():
        f_M_P=Label(tk_hisoire_1,text=" faux, les 2 pays avaient oublié de signer le traiter de paix.       ",font=("ghotique",25),bg="white",fg="red")
        f_M_P.place(x=50,y=300)

    v_1= Checkbutton(tk_hisoire_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_h)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_hisoire_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_h)
    f_1.place(x=550,y=50)




    suivant=Button(tk_hisoire_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_h)
    suivant.place(x=800,y=600)


def suivant_h():
    tk_histoire_2 = Tk()
    tk_histoire_2.geometry("1000x700+50+50")
    tk_histoire_2.title("questions histoire")
    tk_histoire_2.config(bg="white")
    annecdote_2_h= Label(tk_histoire_2, text="La première bombe tombée sur Berlin n'a tué personne, a part un éléphant .",font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2_h.pack()


    def v_2_h ():
        v_M_P=Label(tk_histoire_2,text="en effet, l'éléphant se trouvait dans le zoo de Berlin et la bombe lui est tombé dessus.     ",font=("ghotique",19),bg="white",fg="green")
        v_M_P.place(x=10,y=300)

    def f_2_h():
        f_M_P=Label(tk_histoire_2,text="faux,l'éléphant se trouvait dans le zoo de Berlin et la bombe lui est tombé dessus.    ",font=("ghotique",20),bg="white",fg="red")
        f_M_P.place(x=10,y=300)




    v_2=Checkbutton(tk_histoire_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_h)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_histoire_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_h)
    f_2.place(x=550,y=50)



#lister les differents themes(1er ligne)
histoire_theme=Button(tk_frame,text="Histoire",font=("ghotique",25),bg="white",fg="black",command= sujet_histoire)
histoire_theme.place(x=10,y=10)



#-------------------------------------------------------------------------------------------------------------------------------------------------


def sujet_maths():
    tk_maths_1 = Tk()
    tk_maths_1.geometry("1000x700+50+50")
    tk_maths_1.title("questions Maths")
    tk_maths_1.config(bg="white")
    annecdote_1 = Label(tk_maths_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_M ():
        v_Q_=Label(tk_maths_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_M():
        f_Q_=Label(tk_maths_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_maths_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_M)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_maths_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_M)
    f_1.place(x=550,y=50)



    suivant=Button(tk_maths_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_M)
    suivant.place(x=800,y=600)


def suivant_M():
    tk_maths_2 = Tk()
    tk_maths_2.geometry("1000x700+50+50")
    tk_maths_2.title("questions Maths")
    tk_maths_2.config(bg="white")
    annecdote_2= Label(tk_maths_2, text=" saisir texte.",font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()



    def v_2_M ():
        v_Q_=Label(tk_maths_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_M():
        f_Q_=Label(tk_maths_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_maths_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_M)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_maths_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_M)
    f_2.place(x=550,y=50)




maths_theme=Button(tk_frame,text=" maths ",font=("ghotique",25),bg="white",fg="black",command=sujet_maths)
maths_theme.place(x=200,y=10)






#--------------------------------------------------------------------------------------------------------------------------------



def sujet_culture_G():
    tk_culture_1 = Tk()
    tk_culture_1.geometry("1000x700+50+50")
    tk_culture_1.title("questions CG")
    tk_culture_1.config(bg="white")
    annecdote_1 = Label(tk_culture_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_CG():
        v_Q_=Label(tk_culture_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_CG():
        f_Q_=Label(tk_culture_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_culture_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_CG)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_culture_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_CG)
    f_1.place(x=550,y=50)



    suivant=Button(tk_culture_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_CG)
    suivant.place(x=800,y=600)




def suivant_CG():
    tk_maths_2 = Tk()
    tk_maths_2.geometry("1000x700+50+50")
    tk_maths_2.title("questions CG")
    tk_maths_2.config(bg="white")
    annecdote_2= Label(tk_maths_2, text=" saisir texte.",font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()



    def v_2_CG ():
        v_Q_=Label(tk_maths_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_CG():
        f_Q_=Label(tk_maths_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_maths_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_CG)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_maths_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_CG)
    f_2.place(x=550,y=50)



cultureG_theme=Button(tk_frame,text=" culture generale ",font=("ghotique",25),bg="white",fg="black",command=sujet_culture_G)
cultureG_theme.place(x=390,y=10)

#--------------------------------------------------------------------------------------------------------------------------------


def sujet_Anglais():
    tk_anglais_1 = Tk()
    tk_anglais_1.geometry("1000x700+50+50")
    tk_anglais_1.title("questions CG")
    tk_anglais_1.config(bg="white")
    annecdote_1 = Label(tk_anglais_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_A():
        v_Q_=Label(tk_anglais_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_A():
        f_Q_=Label(tk_anglais_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_anglais_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_A)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_anglais_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_A)
    f_1.place(x=550,y=50)



    suivant=Button(tk_anglais_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_A)
    suivant.place(x=800,y=600)

def suivant_A():
    tk_anglais_2 = Tk()
    tk_anglais_2.geometry("1000x700+50+50")
    tk_anglais_2.title("questions CG")
    tk_anglais_2.config(bg="white")
    annecdote_2 = Label(tk_anglais_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_A():
        v_Q_=Label(tk_anglais_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_A():
        f_Q_=Label(tk_anglais_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_anglais_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_A)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_anglais_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_A)
    f_2.place(x=550,y=50)



anglais_theme=Button(tk_frame,text=" Anglais ",font=("ghotique",25),bg="white",fg="black",command=sujet_Anglais)
anglais_theme.place(x=720,y=10)

#---------------------------------------------------------------------------------------------------------------------------------


def sujet_Francais():
    tk_fracais_1 = Tk()
    tk_fracais_1.geometry("1000x700+50+50")
    tk_fracais_1.title("questions CG")
    tk_fracais_1.config(bg="white")
    annecdote_1 = Label(tk_fracais_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_F():
        v_Q_=Label(tk_fracais_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_F():
        f_Q_=Label(tk_fracais_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_fracais_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_F)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_fracais_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_F)
    f_1.place(x=550,y=50)



    suivant=Button(tk_fracais_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_F)
    suivant.place(x=800,y=600)

def suivant_F():
    tk_fracais_2 = Tk()
    tk_fracais_2.geometry("1000x700+50+50")
    tk_fracais_2.title("questions CG")
    tk_fracais_2.config(bg="white")
    annecdote_2 = Label(tk_fracais_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_F():
        v_Q_=Label(tk_fracais_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_F():
        f_Q_=Label(tk_fracais_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_fracais_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_F)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_fracais_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_F)
    f_2.place(x=550,y=50)


#(2eme ligne)
francais_theme=Button(tk_frame,text="Français",font=("ghotique",25),bg="white",fg="black",command=sujet_Francais)
francais_theme.place(x=10,y=140)


#----------------------------------------------------------------------------------------------------------------------------

def sujet_auteur():
    tk_auteur_1 = Tk()
    tk_auteur_1.geometry("1000x700+50+50")
    tk_auteur_1.title("questions CG")
    tk_auteur_1.config(bg="white")
    annecdote_1 = Label(tk_auteur_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_a():
        v_Q_=Label(tk_auteur_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_a():
        f_Q_=Label(tk_auteur_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_auteur_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_a)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_auteur_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_a)
    f_1.place(x=550,y=50)



    suivant=Button(tk_auteur_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_a)
    suivant.place(x=800,y=600)

def suivant_a():
    tk_auteur_2 = Tk()
    tk_auteur_2.geometry("1000x700+50+50")
    tk_auteur_2.title("questions CG")
    tk_auteur_2.config(bg="white")
    annecdote_2 = Label(tk_auteur_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_a():
        v_Q_=Label(tk_auteur_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_a():
        f_Q_=Label(tk_auteur_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_auteur_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_a)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_auteur_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_a)
    f_2.place(x=550,y=50)


auteur_theme=Button(tk_frame,text=" auteur ",font=("ghotique",25),bg="white",fg="black",command=sujet_auteur)
auteur_theme.place(x=200,y=140)


#------------------------------------------------------------------------------------------------------------------------------

def sujet_cinematographie():
    tk_cinematographie_1 = Tk()
    tk_cinematographie_1.geometry("1000x700+50+50")
    tk_cinematographie_1.title("questions CG")
    tk_cinematographie_1.config(bg="white")
    annecdote_1 = Label(tk_cinematographie_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_c():
        v_Q_=Label(tk_cinematographie_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_c():
        f_Q_=Label(tk_cinematographie_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_cinematographie_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_c)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_cinematographie_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_c)
    f_1.place(x=550,y=50)



    suivant=Button(tk_cinematographie_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_a)
    suivant.place(x=800,y=600)

def suivant_c():
    tk_cinematographie_2 = Tk()
    tk_cinematographie_2.geometry("1000x700+50+50")
    tk_cinematographie_2.title("questions CG")
    tk_cinematographie_2.config(bg="white")
    annecdote_2 = Label(tk_cinematographie_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_c():
        v_Q_=Label(tk_cinematographie_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_c():
        f_Q_=Label(tk_cinematographie_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_cinematographie_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_c)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_cinematographie_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_c)
    f_2.place(x=550,y=50)


cinematographie_theme=Button(tk_frame,text=" cinematographie ",font=("ghotique",25),bg="white",fg="black",command=sujet_cinematographie)
cinematographie_theme.place(x=390,y=140)


#-------------------------------------------------------------------------------------------------------------------------------------------------------

def sujet_Animaux():
    tk_animaux_1 = Tk()
    tk_animaux_1.geometry("1000x700+50+50")
    tk_animaux_1.title("questions CG")
    tk_animaux_1.config(bg="white")
    annecdote_1 = Label(tk_animaux_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_an():
        v_Q_=Label(tk_animaux_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_an():
        f_Q_=Label(tk_animaux_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_animaux_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_an)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_animaux_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_an)
    f_1.place(x=550,y=50)



    suivant=Button(tk_animaux_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_a)
    suivant.place(x=800,y=600)

def suivant_an():
    tk_animaux_2 = Tk()
    tk_animaux_2.geometry("1000x700+50+50")
    tk_animaux_2.title("questions CG")
    tk_animaux_2.config(bg="white")
    annecdote_2 = Label(tk_animaux_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_an():
        v_Q_=Label(tk_animaux_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_an():
        f_Q_=Label(tk_animaux_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_animaux_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_an)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_animaux_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_an)
    f_2.place(x=550,y=50)



animaux_theme=Button(tk_frame,text=" animaux ",font=("ghotique",25),bg="white",fg="black",command=sujet_Animaux)
animaux_theme.place(x=720,y=140)

#-------------------------------------------------------------------------------------------------------------------------------



def sujet_Musique():
    tk_musique_1 = Tk()
    tk_musique_1.geometry("1000x700+50+50")
    tk_musique_1.title("questions CG")
    tk_musique_1.config(bg="white")
    annecdote_1 = Label(tk_musique_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_m():
        v_Q_=Label(tk_musique_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_m():
        f_Q_=Label(tk_musique_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_musique_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_m)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_musique_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_m)
    f_1.place(x=550,y=50)



    suivant=Button(tk_musique_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_m)
    suivant.place(x=800,y=600)

def suivant_m():
    tk_musique_2 = Tk()
    tk_musique_2.geometry("1000x700+50+50")
    tk_musique_2.title("questions CG")
    tk_musique_2.config(bg="white")
    annecdote_2 = Label(tk_musique_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_m():
        v_Q_=Label(tk_musique_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_m():
        f_Q_=Label(tk_musique_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_musique_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_m)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_musique_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_m)
    f_2.place(x=550,y=50)

#(3eme ligne)
musicien_theme=Button(tk_frame,text="musicien",font=("ghotique",25),bg="white",fg="black",command=sujet_Musique)
musicien_theme.place(x=10,y=270)

#-----------------------------------------------------------------------------------------------------------------------------

def sujet_sport():
    tk_sport_1 = Tk()
    tk_sport_1.geometry("1000x700+50+50")
    tk_sport_1.title("questions CG")
    tk_sport_1.config(bg="white")
    annecdote_1 = Label(tk_sport_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_s():
        v_Q_=Label(tk_sport_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_s():
        f_Q_=Label(tk_sport_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_sport_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_s)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_sport_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_s)
    f_1.place(x=550,y=50)



    suivant=Button(tk_sport_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_s)
    suivant.place(x=800,y=600)

def suivant_s():
    tk_sport_2 = Tk()
    tk_sport_2.geometry("1000x700+50+50")
    tk_sport_2.title("questions CG")
    tk_sport_2.config(bg="white")
    annecdote_2 = Label(tk_sport_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_m():
        v_Q_=Label(tk_sport_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_m():
        f_Q_=Label(tk_sport_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_sport_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_m)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_sport_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_m)
    f_2.place(x=550,y=50)



sport_theme=Button(tk_frame,text=" sport ",font=("ghotique",25),bg="white",fg="black",command=sujet_sport)
sport_theme.place(x=200,y=270)

#------------------------------------------------------------------------------------------------------------------------------

def sujet_techno():
    tk_techno_1 = Tk()
    tk_techno_1.geometry("1000x700+50+50")
    tk_techno_1.title("questions CG")
    tk_techno_1.config(bg="white")
    annecdote_1 = Label(tk_techno_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_t():
        v_Q_=Label(tk_techno_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_t():
        f_Q_=Label(tk_techno_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_techno_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_t)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_techno_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_t)
    f_1.place(x=550,y=50)



    suivant=Button(tk_techno_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_t)
    suivant.place(x=800,y=600)

def suivant_t():
    tk_techno_2 = Tk()
    tk_techno_2.geometry("1000x700+50+50")
    tk_techno_2.title("questions CG")
    tk_techno_2.config(bg="white")
    annecdote_2 = Label(tk_techno_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_t():
        v_Q_=Label(tk_techno_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_t():
        f_Q_=Label(tk_techno_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_techno_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_t)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_techno_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_t)
    f_2.place(x=550,y=50)


technologie_theme=Button(tk_frame,text=" technologie ",font=("ghotique",25),bg="white",fg="black",command=sujet_techno)
technologie_theme.place(x=390,y=270)
#------------------------------------------------------------------------------------------------------------------------------

def sujet_anime():
    tk_anime_1 = Tk()
    tk_anime_1.geometry("1000x700+50+50")
    tk_anime_1.title("questions CG")
    tk_anime_1.config(bg="white")
    annecdote_1 = Label(tk_anime_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_an():
        v_Q_=Label(tk_anime_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_an():
        f_Q_=Label(tk_anime_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_anime_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_an)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_anime_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_an)
    f_1.place(x=550,y=50)



    suivant=Button(tk_anime_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_an)
    suivant.place(x=800,y=600)

def suivant_an():
    tk_anime_2 = Tk()
    tk_anime_2.geometry("1000x700+50+50")
    tk_anime_2.title("questions CG")
    tk_anime_2.config(bg="white")
    annecdote_2 = Label(tk_anime_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_an():
        v_Q_=Label(tk_anime_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_an():
        f_Q_=Label(tk_anime_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_anime_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_an)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_anime_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_an)
    f_2.place(x=550,y=50)

anime_theme=Button(tk_frame,text=" animé ",font=("ghotique",25),bg="white",fg="black",command=sujet_anime)
anime_theme.place(x=650,y=270)

#------------------------------------------------------------------------------------------------------------------------------


def sujet_espagnol():
    tk_espagnol_1 = Tk()
    tk_espagnol_1.geometry("1000x700+50+50")
    tk_espagnol_1.title("questions CG")
    tk_espagnol_1.config(bg="white")
    annecdote_1 = Label(tk_espagnol_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_e():
        v_Q_=Label(tk_espagnol_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_e():
        f_Q_=Label(tk_espagnol_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_espagnol_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_e)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_espagnol_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_e)
    f_1.place(x=550,y=50)



    suivant=Button(tk_espagnol_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_e)
    suivant.place(x=800,y=600)

def suivant_e():
    tk_espagnol_2 = Tk()
    tk_espagnol_2.geometry("1000x700+50+50")
    tk_espagnol_2.title("questions CG")
    tk_espagnol_2.config(bg="white")
    annecdote_2 = Label(tk_espagnol_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_e():
        v_Q_=Label(tk_espagnol_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_e():
        f_Q_=Label(tk_espagnol_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_espagnol_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_e)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_espagnol_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_e)
    f_2.place(x=550,y=50)

#(4eme ligne)
espagnol_theme=Button(tk_frame,text="espagnol",font=("ghotique",25),bg="white",fg="black",command=sujet_espagnol)
espagnol_theme.place(x=10,y=400)
#------------------------------------------------------------------------------------------------------------------------------

def sujet_jeux():
    tk_jeux_1 = Tk()
    tk_jeux_1.geometry("1000x700+50+50")
    tk_jeux_1.title("questions CG")
    tk_jeux_1.config(bg="white")
    annecdote_1 = Label(tk_jeux_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_j():
        v_Q_=Label(tk_jeux_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_j():
        f_Q_=Label(tk_jeux_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_jeux_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_j)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_jeux_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_j)
    f_1.place(x=550,y=50)



    suivant=Button(tk_jeux_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_j)
    suivant.place(x=800,y=600)

def suivant_j():
    tk_jeux_2 = Tk()
    tk_jeux_2.geometry("1000x700+50+50")
    tk_jeux_2.title("questions CG")
    tk_jeux_2.config(bg="white")
    annecdote_2 = Label(tk_jeux_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_m():
        v_Q_=Label(tk_jeux_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_m():
        f_Q_=Label(tk_jeux_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_jeux_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_m)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_jeux_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_m)
    f_2.place(x=550,y=50)

jeux_theme=Button(tk_frame,text=" jeux ",font=("ghotique",25),bg="white",fg="black",command=sujet_jeux)
jeux_theme.place(x=200,y=400)
#------------------------------------------------------------------------------------------------------------------------------

def sujet_dinosaure():
    tk_dinosaure_1 = Tk()
    tk_dinosaure_1.geometry("1000x700+50+50")
    tk_dinosaure_1.title("questions CG")
    tk_dinosaure_1.config(bg="white")
    annecdote_1 = Label(tk_dinosaure_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_d():
        v_Q_=Label(tk_dinosaure_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_d():
        f_Q_=Label(tk_dinosaure_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_dinosaure_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_d)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_dinosaure_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_d)
    f_1.place(x=550,y=50)



    suivant=Button(tk_dinosaure_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_d)
    suivant.place(x=800,y=600)

def suivant_d():
    tk_dinosaure_2 = Tk()
    tk_dinosaure_2.geometry("1000x700+50+50")
    tk_dinosaure_2.title("questions CG")
    tk_dinosaure_2.config(bg="white")
    annecdote_2 = Label(tk_dinosaure_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_d():
        v_Q_=Label(tk_dinosaure_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_d():
        f_Q_=Label(tk_dinosaure_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_dinosaure_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_d)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_dinosaure_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_d)
    f_2.place(x=550,y=50)

dinosaure_theme=Button(tk_frame,text=" dinosaure ",font=("ghotique",25),bg="white",fg="black",command=sujet_dinosaure)
dinosaure_theme.place(x=360,y=400)
#------------------------------------------------------------------------------------------------------------------------------


def sujet_metl():
    tk_metl_1 = Tk()
    tk_metl_1.geometry("1000x700+50+50")
    tk_metl_1.title("questions CG")
    tk_metl_1.config(bg="white")
    annecdote_1 = Label(tk_metl_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_ml():
        v_Q_=Label(tk_metl_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_ml():
        f_Q_=Label(tk_metl_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_metl_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_ml)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_metl_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_ml)
    f_1.place(x=550,y=50)



    suivant=Button(tk_metl_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_ml)
    suivant.place(x=800,y=600)

def suivant_ml():
    tk_metl_2 = Tk()
    tk_metl_2.geometry("1000x700+50+50")
    tk_metl_2.title("questions CG")
    tk_metl_2.config(bg="white")
    annecdote_2 = Label(tk_metl_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_ml():
        v_Q_=Label(tk_metl_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_ml():
        f_Q_=Label(tk_metl_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_metl_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_ml)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_metl_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_ml)
    f_2.place(x=550,y=50)


mythe_legende_theme=Button(tk_frame,text=" mythe & legende ",font=("ghotique",25),bg="white",fg="black",command=sujet_metl)
mythe_legende_theme.place(x=600,y=400)
#------------------------------------------------------------------------------------------------------------------------------


def sujet_dessin_anime():
    tk_dessin_a_1 = Tk()
    tk_dessin_a_1.geometry("1000x700+50+50")
    tk_dessin_a_1.title("questions CG")
    tk_dessin_a_1.config(bg="white")
    annecdote_1 = Label(tk_dessin_a_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_da():
        v_Q_=Label(tk_dessin_a_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_da():
        f_Q_=Label(tk_dessin_a_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_dessin_a_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_da)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_dessin_a_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_da)
    f_1.place(x=550,y=50)



    suivant=Button(tk_dessin_a_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_da)
    suivant.place(x=800,y=600)

def suivant_da():
    tk_dessin_a_2 = Tk()
    tk_dessin_a_2.geometry("1000x700+50+50")
    tk_dessin_a_2.title("questions CG")
    tk_dessin_a_2.config(bg="white")
    annecdote_2 = Label(tk_dessin_a_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_da():
        v_Q_=Label(tk_dessin_a_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_da():
        f_Q_=Label(tk_dessin_a_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_dessin_a_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_da)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_dessin_a_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_da)
    f_2.place(x=550,y=50)

dessin_anime_theme=Button(tk_frame,text="dessin animé",font=("ghotique",25),bg="white",fg="black",command=sujet_dessin_anime)
dessin_anime_theme.place(x=10,y=530)



#------------------------------------------------------------------------------------------------------------------------------


def sujet_nature():
    tk_nature_1 = Tk()
    tk_nature_1.geometry("1000x700+50+50")
    tk_nature_1.title("questions CG")
    tk_nature_1.config(bg="white")
    annecdote_1 = Label(tk_nature_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_n():
        v_Q_=Label(tk_nature_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_n():
        f_Q_=Label(tk_nature_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_nature_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_n)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_nature_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_n)
    f_1.place(x=550,y=50)



    suivant=Button(tk_nature_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_a)
    suivant.place(x=800,y=600)

def suivant_n():
    tk_nature_2 = Tk()
    tk_nature_2.geometry("1000x700+50+50")
    tk_nature_2.title("questions CG")
    tk_nature_2.config(bg="white")
    annecdote_2 = Label(tk_nature_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_n():
        v_Q_=Label(tk_nature_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_n():
        f_Q_=Label(tk_nature_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_nature_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_n)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_nature_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_n)
    f_2.place(x=550,y=50)

nature_theme=Button(tk_frame,text=" nature ",font=("ghotique",25),bg="white",fg="black",command=sujet_nature)
nature_theme.place(x=270,y=530)
#------------------------------------------------------------------------------------------------------------------------------


def sujet_couleur():
    tk_couleur_1 = Tk()
    tk_couleur_1.geometry("1000x700+50+50")
    tk_couleur_1.title("questions CG")
    tk_couleur_1.config(bg="white")
    annecdote_1 = Label(tk_couleur_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_c():
        v_Q_=Label(tk_couleur_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_c():
        f_Q_=Label(tk_couleur_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_couleur_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_c)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_couleur_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_c)
    f_1.place(x=550,y=50)



    suivant=Button(tk_couleur_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_c)
    suivant.place(x=800,y=600)

def suivant_c():
    tk_couleur_2 = Tk()
    tk_couleur_2.geometry("1000x700+50+50")
    tk_couleur_2.title("questions CG")
    tk_couleur_2.config(bg="white")
    annecdote_2 = Label(tk_couleur_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_c():
        v_Q_=Label(tk_couleur_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_c():
        f_Q_=Label(tk_couleur_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_couleur_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_c)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_couleur_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_c)
    f_2.place(x=550,y=50)

couleur_theme=Button(tk_frame,text="couleur",font=("ghotique",25),bg="white",fg="black",command=sujet_couleur)
couleur_theme.place(x=450,y=530)
#------------------------------------------------------------------------------------------------------------------------------


def sujet_espace():
    tk_espace_1 = Tk()
    tk_espace_1.geometry("1000x700+50+50")
    tk_espace_1.title("questions CG")
    tk_espace_1.config(bg="white")
    annecdote_1 = Label(tk_espace_1, text="phrase a sasir",font=("ghotique", 25), bg="#77b5fE", fg="black")
    annecdote_1.pack()


    def v_1_e():
        v_Q_=Label(tk_espace_1,text="saisir texte.",font=("ghotique",25),bg="white",fg="green")
        v_Q_.place(x=50,y=300)

    def f_1_e():
        f_Q_=Label(tk_espace_1,text=" saisir texte  ",font=("ghotique",25),bg="white",fg="red")
        f_Q_.place(x=50,y=300)

    v_1=Checkbutton(tk_espace_1,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_1_e)
    v_1.place(x=400,y=50)
    f_1=Checkbutton(tk_espace_1,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_1_e)
    f_1.place(x=550,y=50)



    suivant=Button(tk_espace_1,text="suivant",font=("ghotique",25),bg="#77b5fE",fg="black",command=suivant_e)
    suivant.place(x=800,y=600)

def suivant_e ():
    tk_espace_2 = Tk()
    tk_espace_2.geometry("1000x700+50+50")
    tk_espace_2.title("questions CG")
    tk_espace_2.config(bg="white")
    annecdote_2 = Label(tk_espace_2, text=" saisir texte.", font=("ghotique", 22), bg="#77b5fE", fg="black")
    annecdote_2.pack()


    def v_2_e():
        v_Q_=Label(tk_espace_2,text="saisir texte     ",font=("ghotique",19),bg="white",fg="green")
        v_Q_.place(x=10,y=300)

    def f_2_e():
        f_Q_=Label(tk_espace_2,text="saisir texte    ",font=("ghotique",20),bg="white",fg="red")
        f_Q_.place(x=10,y=300)




    v_2=Checkbutton(tk_espace_2,text=" vrai ",font=("ghotique",25),bg="#77b5fE",fg="black",command=v_2_e)
    v_2.place(x=400,y=50)
    f_2=Checkbutton(tk_espace_2,text="faux",font=("ghotique",25),bg="#77b5fE",fg="black",command=f_2_e)
    f_2.place(x=550,y=50)

espace_theme=Button(tk_frame,text="espace",font=("ghotique",25),bg="white",fg="black",command=sujet_espace)
espace_theme.place(x=640,y=530)




tk.mainloop()
