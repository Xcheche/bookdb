from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox


root = Tk()  # main window
root.title("My Books Database Application")  # window title
root.configure(bg="lightblue")  # window background
root.geometry("850x500")  # window size
root.resizable(width=False, height=False)  # blocking resize
# label and entry widgets
# title label
title_label = ttk.Label(
    root, text="Title", background="lightblue", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=24, textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)
# author label
author_label = ttk.Label(
    root, text="Author", background="lightblue", font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root, width=24, textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

# isbn label
isbn_label = ttk.Label(
    root, text="ISBN", background="lightblue", font=("TkDefaultFont", 14))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width=24, textvariable=isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)
# add button to input into database
add_btn = Button(root, text="Add Book", bg="blue",
                 fg="white", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=6, sticky=W)
# listbox to show records from database
list_box = Listbox(root, width=40, height=16,
                   font="helvetica 13", bg="lightgrey")
list_box.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)

# scrollbar to enable scrolling

scrollbar = Scrollbar(root)
scrollbar.grid(row=1, column=8, rowspan=14, sticky=W)
# binding
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)
# modify button
modify_btn = Button(root, text="Modify Record", bg="purple",
                    fg="white", font="helvetica 10 bold", command="")
modify_btn.grid(row=15, column=4)
# delete button
delete_btn = Button(root, text="Delete Record", bg="red",
                    fg="white", font="helvetica 10 bold", command="")
delete_btn.grid(row=15, column=5)

# view button
view_btn = Button(root, text="View All Records", bg="black",
                  fg="white", font="helvetica 10 bold", command="")
view_btn.grid(row=15, column=1)
# clear button
clear_btn = Button(root, text="Clear Screen", bg="maroon",
                   fg="white", font="helvetica 10 bold", command="")
clear_btn.grid(row=15, column=2)

# exit button
exit_btn = Button(root, text="Exit Application", bg="blue",
                  fg="white", font="helvetica 10 bold", command="")
exit_btn.grid(row=15, column=3)


root.mainloop()  # main loop
