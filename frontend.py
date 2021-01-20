from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import main
from datetime import date

def gathered_today():
    string_to_display = "You gathered tons of shit :)"
    info_label["text"] = string_to_display

def earned_today():
    string_to_display = "You earned tons of shit :)"
    info_label["text"] = string_to_display

def add_gathered():
    add_meat = meat_count_var.get()
    add_caphra = caphra_count_var.get()
    add_gem = gem_count_var.get()
    add_sharp = sharp_count_var.get()
    add_hard = hard_count_var.get()
    add_time = time_count_var.get()
    print("added meat: ",add_meat)
    print("added caphras: ",add_caphra)
    print("added gem frags: ",add_gem)
    print("added sharps: ",add_sharp)
    print("added hards: ",add_hard)
    print("added time: ",add_time)
    main.gathering_data.insert({'meat': add_meat, 'caphras': add_caphra, 'gem_fragment': add_gem, 'sharp_shard': add_sharp, 'hard_shard': add_hard, 'gath_time': add_time, 'date': str(date.today())})

def change_prices():
    meat_price = meat_price_var.get()
    caphra_price = caphra_price_var.get()
    gem_price = gem_price_var.get()
    sharp_price = sharp_price_var.get()
    hard_price = hard_price_var.get()
    main.update_prices(meat_price, caphra_price, gem_price, sharp_price, hard_price)


# TODO Zrobić tak by wyświetlało ceny w Labelce po prawej
def check_prices():
    string_to_display = main.check_actual_prices()
    info_label["text"] = string_to_display

# TODO Zrobić tak by wyświetlało w tabeli gatherowane surowce iterując po ID lub dacie
def get_gathering_history():
    meats = [r['meat'] for r in main.gathering_data]
    database_display = main.gathering_data.all()
    database_label["text"] = meats

app = Tk()
app.title("BDO Meat Collector")
app.iconphoto(False, PhotoImage(file="images\\cleaver-icon.png"))
app.geometry("1050x550")
image = ImageTk.PhotoImage(Image.open("images\\gathering_database_background.png"))

tabs_control = ttk.Notebook(app)
tabs_control.pack(pady=15)

main_tab = Frame(tabs_control, width=1000, height=500)
alarm_tab = Frame(tabs_control, width=1000, height=500)
data_tab = Frame(tabs_control, width=1000, height=500)

main_tab.pack(expand=1, fill="both")
alarm_tab.pack(expand=1, fill="both")
data_tab.pack(expand=1, fill="both")

tabs_control.add(main_tab, text="Main")
tabs_control.add(alarm_tab, text="Alarm")
tabs_control.add(data_tab, text="Data")


filename = PhotoImage(file="images\\gathering_database_background.png")
main_label = Label(main_tab, image=filename)
main_label.place(x=0, y=0, relwidth=1, relheight=1)

outline_label = Label(main_label, bg="#90d6da")
outline_label.place(relx=0.01, rely=0.05, relwidth=0.7, relheight=0.92)
inside_label1 = Label(outline_label, bg="#eeeeee")
inside_label1.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99)
inside_label2 = Label(inside_label1, bg="#eeeeee")
inside_label2.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.98)


meat_count_var = IntVar()
caphra_count_var = IntVar()
gem_count_var = IntVar()
sharp_count_var = IntVar()
hard_count_var = IntVar()
time_count_var = IntVar()
gath_title_label = Label(inside_label2, text="Put your gathered stuff here!", relief=RAISED, width=29, bg="black", fg='#fff').grid(row=0, columnspan=2)
gath_meat_label = Label(inside_label2, text='Lamb Meat', relief=GROOVE, width=15).grid(row=1,column=0, padx=2, pady=2)
gath_caphra_label = Label(inside_label2, text='Caphra Stones', relief=GROOVE, width=15).grid(row=2, column=0, padx=2, pady=2)
gath_gem_label = Label(inside_label2, text='Gem Frags', relief=GROOVE, width=15).grid(row=3, column=0, padx=2, pady=2)
gath_sharp_label = Label(inside_label2, text='Sharp Shards', relief=GROOVE, width=15).grid(row=4, column=0, padx=2, pady=2)
gath_hard_label = Label(inside_label2, text='Hard Shards', relief=GROOVE, width=15).grid(row=5, column=0, padx=2, pady=2)
gath_time_label = Label(inside_label2, text='Time', relief=GROOVE, width=15).grid(row=6, column=0, padx=2, pady=2)
gath_meat_entry = Entry(inside_label2, textvariable=meat_count_var, relief=SUNKEN, width=15).grid(row=1, column=1, padx=2, pady=2)
gath_caphra_entry = Entry(inside_label2, textvariable=caphra_count_var, relief=SUNKEN, width=15).grid(row=2, column=1, padx=2, pady=2)
gath_gem_entry = Entry(inside_label2, textvariable=gem_count_var, relief=SUNKEN, width=15).grid(row=3, column=1, padx=2, pady=2)
gath_sharp_entry = Entry(inside_label2, textvariable=sharp_count_var, relief=SUNKEN, width=15).grid(row=4, column=1, padx=2, pady=2)
gath_hard_entry = Entry(inside_label2, textvariable=hard_count_var, relief=SUNKEN, width=15).grid(row=5, column=1, padx=2, pady=2)
gath_time_entry = Entry(inside_label2, textvariable=time_count_var, relief=SUNKEN, width=15).grid(row=6, column=1, padx=2, pady=2)
gath_add_button = Button(inside_label2, text="ADD", command=add_gathered, bg="black", fg='#fff').grid(row=7, columnspan=2)
var1 = IntVar()
time_check_box = Checkbutton(inside_label2, text="Get from timer?", variable=var1, bg="#eeeeee").grid(row=6, column=3)

spacer = Label(inside_label2, bg="#eeeeee").grid(row=8, columnspan=2)

meat_price_var = IntVar()
caphra_price_var = IntVar()
gem_price_var = IntVar()
sharp_price_var = IntVar()
hard_price_var = IntVar()
price_title_label = Label(inside_label2, text="Change the price of stuff here!", relief=RAISED, width=29, bg="black", fg='#fff').grid(row=9, columnspan=2)
price_meat_label = Label(inside_label2, text='Lamb Meat', relief=GROOVE, width=15).grid(row=10, column=0, padx=2, pady=2)
price_caphra_label = Label(inside_label2, text='Caphra Stones', relief=GROOVE, width=15).grid(row=11, column=0, padx=2, pady=2)
price_gem_label = Label(inside_label2, text='Gem Frags', relief=GROOVE, width=15).grid(row=12, column=0, padx=2, pady=2)
price_sharp_label = Label(inside_label2, text='Sharp Shards', relief=GROOVE, width=15).grid(row=13, column=0, padx=2, pady=2)
price_hard_label = Label(inside_label2, text='Hard Shards', relief=GROOVE, width=15).grid(row=14, column=0, padx=2, pady=2)
price_meat_entry = Entry(inside_label2, textvariable=meat_price_var, relief=SUNKEN, width=15).grid(row=10, column=1, padx=2, pady=2)
price_caphra_entry = Entry(inside_label2, textvariable=caphra_price_var, relief=SUNKEN, width=15).grid(row=11, column=1, padx=2, pady=2)
price_gem_entry = Entry(inside_label2, textvariable=gem_price_var, relief=SUNKEN, width=15).grid(row=12, column=1, padx=2, pady=2)
price_sharp_entry = Entry(inside_label2, textvariable=sharp_price_var, relief=SUNKEN, width=15).grid(row=13, column=1, padx=2, pady=2)
price_hard_entry = Entry(inside_label2, textvariable=hard_price_var, relief=SUNKEN, width=15).grid(row=14, column=1, padx=2, pady=2)
price_check_button = Button(inside_label2, text="CHECK ACTUAL", command=check_prices, bg="black", fg='#fff').grid(row=15, column=0)
price_add_button = Button(inside_label2, text="CHANGE", command=change_prices, bg="black", fg='#fff').grid(row=15, column=1)




info_label = Label(inside_label2, text="...", relief=RIDGE, font=10, bg="#fff")
info_label.place(relx=0.5, rely=0.01, relwidth=0.45, relheight=0.6)
gathered_today_button = Button(inside_label2, text="Gathered Today", command=gathered_today, bg="black", fg='#fff')
gathered_today_button.place(relx=0.5, rely=0.62, relwidth=0.2, relheight=0.1)
earned_today_button = Button(inside_label2, text="Earned Today", command=earned_today, bg="black", fg='#fff')
earned_today_button.place(relx=0.75, rely=0.62, relwidth=0.2, relheight=0.1)




data_label = Label(data_tab, image=filename)
data_label.place(x=0, y=0, relwidth=1, relheight=1)

outline_label = Label(data_label, bg="#90d6da")
outline_label.place(relx=0.01, rely=0.05, relwidth=0.7, relheight=0.92)
inside_label1 = Label(outline_label, bg="#eeeeee")
inside_label1.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99)
inside_label2 = Label(inside_label1, bg="#eeeeee")
inside_label2.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.98)

database_label = Label(inside_label2, text="Empty", relief=RIDGE, font=10, bg="#fff")
database_label.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.75)
get_database_button = Button(inside_label2, text="Get gathering history", command=get_gathering_history, bg="black", fg='#fff')
get_database_button.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)

app.mainloop()







# from tkinter import *
# from tkinter import messagebox
# top = Tk()
#
# C = Canvas(top, bg="blue", height=250, width=300)
# filename = PhotoImage(file = "C:\\Users\\Patryk Rak\\Desktop\\Programming Languages\\Python\\.Coding\\First Project\\gathering_database_background.png")
# background_label = Label(top, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# C.pack()
# top.mainloop()