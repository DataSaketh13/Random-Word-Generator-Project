


from tkinter import *
import random
root = Tk()
root.title("Random Word Generator")
root.geometry("500x500")

label_series = Label(root)




def random_letter():
    
    alpha_list = ["A", B", C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    random_no = random.randint(1, 26)
    random_alpha_1 = alpha_list[random_no]
    
    random_no_2 = random.randint(1, 26)
    random_alpha_2 = alpha_list[random_no_2]
    
    random_no_3 = random.randint(1, 26)
    random_alpha_3 = alpha_list[random_no_3]
    
    random_no_4 = random.randint(1, 26)
    random_alpha_4 = alpha_list[random_no_4]
    
    random_no_5 = random.randint(1, 26)
    random_alpha_5 = alpha_list[random_no_5]
     
    

    label_series["text"] = random_alpha_1, random_alpha_2, random_alpha_3, random_alpha_4, random_alpha_5

btn1 = Button(root, text="Generate Random Word  ", command=random_letter)
btn1.place(relx=0.5, rely=0.4, anchor = CENTER)
label_series.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()