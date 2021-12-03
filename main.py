import tkinter.messagebox

import code_source
from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog


class minmakespan(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("MIN-MAKESPAN")
        w = 400  # width for the Tk root
        h = 300
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.titre = Label(self, text = "Choisissez le type d'instance :")
        self.rb1 = Button(self, text = "Instance Ip", command= self.display_Ip)
        self.rb2 = Button(self, text = "Instance Ir", command = self.display_Ir)
        self.titre.pack()
        self.rb1.pack()
        self.rb2.pack()

    def display_Ip(self):
        window2 = instance_Ip()
        window2.mainloop()
    def display_Ir(self):
        window3 = instance_Ir()
        window3.mainloop()

class instance_Ip(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Instance Ip")
        w = 400  # width for the Tk root
        h = 300
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.label = Label(self, text = "Choisissez un entier p :")
        self.label.pack()
        self.entree = Entry(self, width=30)
        self.entree.pack()
        self.submit = Button(self, text = "Valider", command = self.display_Ip)
        self.submit.pack()

    def display_Ip(self):
        try:
            pp = int(self.entree.get())
            M, D = code_source.generer_Ip(pp)
            res_lsa, res_lpt, res_rma = code_source.lsa(M, D), code_source.lpt(M, D), code_source.rma(M, D)
            b = max([max(D), sum(D)/len(D)])
            ratio_lsa = max(res_lsa) / b
            ratio_lpt = max(res_lpt) / b
            ratio_rma = max(res_rma) / b

            texte = "Borne inférieure ‘‘maximum’’ = " + str(max(D)) + "\n" + "Borne inférieure ‘‘moyenne’’ = " + \
                    str(sum(D)/len(D)) + "\n" + "Résultat LSA = " + str(max(res_lsa)) + \
                    "\n" + "ratio LSA = " + str(ratio_lsa) + "\n" + "Résultat LPT = " + str(max(res_lpt)) + "\n" + \
                    "ratio LPT = " + str(ratio_lpt) + "\n" + "Résultat RMA = " + str(max(res_rma)) + "\n" + \
                    "ratio RMA = " + str(ratio_rma)
            tkinter.messagebox.showinfo( "Résultats", texte)
            self.destroy()
        except ValueError:
            tkinter.messagebox.showerror( "Erreur", "Vous devez saisir un entier !" )
            self.destroy()

class instance_Ir(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Instance Ir")
        w = 400  # width for the Tk root
        h = 300
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.label1 = Label(self, text = "Choisissez un nombre de machines :")
        self.entree1 = Entry(self, width=30)
        self.label2 = Label(self, text = "Choisissez un nombre de tâches :")
        self.entree2 = Entry(self, width=30)
        self.label3 = Label(self, text = "Choisissez un nombre d'instances à générer :")
        self.entree3 = Entry(self, width=30)
        self.label4 = Label(self, text = "Choisissez une durée de tâche minimum :")
        self.entree4 = Entry(self, width=30)
        self.label5 = Label(self, text = "Choisissez une durée de tâche maximum :")
        self.entree5 = Entry(self, width=30)
        self.submit = Button(self, text = "Valider", command = self.display_Ir)
        self.label1.pack()
        self.entree1.pack()
        self.label2.pack()
        self.entree2.pack()
        self.label3.pack()
        self.entree3.pack()
        self.label4.pack()
        self.entree4.pack()
        self.label5.pack()
        self.entree5.pack()
        self.submit.pack()

    def display_Ir(self):
        try:
            m = int(self.entree1.get())
            n = int(self.entree2.get())
            k = int(self.entree3.get())
            dmin = int(self.entree4.get())
            dmax = int(self.entree5.get())
            instances = code_source.generer_Ir(m, n, k, dmin, dmax)
            somme_lsa, somme_lpt, somme_rma = 0, 0, 0
            for i in range(len(instances)):
                m, d = instances[i]
                res_lsa, res_lpt, res_rma = code_source.lsa(m, d), code_source.lpt(m, d), code_source.rma(m, d)
                b = max([max(d), sum(d)/len(d)])
                somme_lsa += max(res_lsa) / b
                somme_lpt += max(res_lpt) / b
                somme_rma += max(res_rma) / b

            texte = "ratio moyen LSA = " + str(somme_lsa/len(instances)) + "\n" + "ratio moyen LPT = " + \
                    str(somme_lpt/len(instances)) + "\n" +"ratio moyen RMA = " + str(somme_rma/len(instances))
            tkinter.messagebox.showinfo( "Résultats", texte)
            self.destroy()
        except ValueError:
            tkinter.messagebox.showerror( "Erreur", "Vous devez saisir un (des) entier(s) !" )


window = minmakespan()
window.mainloop()
