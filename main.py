# import tkinter
from tkinter import *
import tkinter.messagebox

# créer la fenêtre
window = Tk()

# titre de la fenêtre
window.title("Shoguntoto To-do App")

# widget pour la liste et le scroll
frame_task = Frame(window)
frame_task.pack()

# créer la liste des tâches
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

# créer la bar de scroll si trop de tâche
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)


# fonction entrer une tâche
def entertask():
    # Nouvelle page pour saisir le texte
    input_text = ""

    def add():
        text_input: str = entry_task.get(1.0, "end-1c")
        if text_input == "":
            tkinter.messagebox.showwarning(title="Attention !", message="Entrer votre tâche")
        else:
            listbox_task.insert(END, text_input)
            # fermer la fenêtre
            root1.destroy()

    root1 = Tk()
    root1.title("Ajout de tâche")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Ajouter la tâche", command=add)
    button_temp.pack()
    root1.mainloop()


# fonction pour supprimer une tâche
def deletetask():
    # selectionner l'item "selected" et le supprimer
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])


# fonction pour compléter une tâche
def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    # mettre l'élément sélectionné dans une variable
    temp_marked = listbox_task.get(marked)
    # le mettre à jour
    temp_marked = temp_marked + " ✔"
    # enlever la tâche sans la mark et remettre la tâche avec la mark
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


# widget pour le bouton
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)
delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)
mark_button = Button(window, text="Mark as completed ", width=50, command=markcompleted)
mark_button.pack(pady=3)

# boucle pour la fenêtre
window.mainloop()
