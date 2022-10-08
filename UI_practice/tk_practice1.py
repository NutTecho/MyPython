import os
from tkinter import Tk ,ttk , Button ,Menu , messagebox , BooleanVar,IntVar ,StringVar, DoubleVar 
def getname():
    theme_path = os.path.dirname(__file__)
    main_path = os.path.join(theme_path,"Azure","azure.tcl")
    print(main_path)
    return main_path

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = BooleanVar()
        self.var_1 = BooleanVar(value=True)
        self.var_2 = BooleanVar()
        self.var_3 = IntVar(value=2)
        self.var_4 = StringVar(value=self.option_menu_list[1])
        self.var_5 = DoubleVar(value=75.0)
        self.var_6 = StringVar()
        self.var_7 = StringVar()

        self.set_button()
        self.set_entry()
        self.set_checkbox()
        self.set_combo()

    def print(self, objtext, x):
        print(objtext, x)
        print()
    
    def com1(self,object):
        # self.var_6.set("hello")
        print(self.var_7)

    def comboClick(self,object):
        # if self.var_7.get()=='Friday':
        #     label1=Label(root,text = 'Yes! that''s Friday').pack(pady = 10)
        # else:
        #     label1=Label(root,text = d1.get()).pack(pady = 10)
        self.var_6.set(self.var_7.get())

    def set_button(self):
        self.button_frame0 = ttk.LabelFrame(self, text="Entry", padding=(20, 10))
        self.button_frame0.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew" )

        self.accentbutton = ttk.Button(self.button_frame0, text="Accent button", style="Accent.TButton",
            command=lambda: self.print("Accent button: ", "pressed") )
        self.accentbutton.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.accbut1 = ttk.Button(self.button_frame0, text="Accent button", style="Accent.TButton")
        self.accbut1.bind("<Button-1>", self.com1)
        self.accbut1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

    def set_entry(self):
        self.Frame2 = ttk.LabelFrame(self,text = "Frame2")
        self.Frame2.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew" )
        
        self.ent1 = ttk.Entry(self.Frame2,textvariable=self.var_6)
        self.ent1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.ent2 = ttk.Entry(self.Frame2)
        self.ent2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.ent3 = ttk.Entry(self.Frame2)
        self.ent3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

    def set_checkbox(self):
        self.Frame3 = ttk.LabelFrame(self,text="Frame3")
        self.Frame3.grid(row=2, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew" )

        self.check_1 = ttk.Checkbutton(self.Frame3, text="Unchecked" ,variable=self.var_0)
        self.check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.lb1 = ttk.Label(self.Frame3,textvariable=self.var_6)
        self.lb1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

    def set_combo(self):
        self.Frame4 = ttk.LabelFrame(self,text="Frame4")
        self.Frame4.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew" )
        # for index,value in enumerate(self.combo_list):
        self.combobox = ttk.Combobox(self.Frame4, values=self.combo_list,textvariable=self.var_7)
        self.combobox.current(0)
        self.combobox.bind("<<ComboboxSelected>>", self.comboClick)
        self.combobox.grid(row=2, column=0, padx=5, pady=10, sticky="ew")




def main():
    gui = Tk()
    gui.geometry("450x500")
    gui.option_add("*Font",",15")
   
    # Pack a big frame so, it behaves like the window background
    big_frame = App(gui)
    big_frame.pack(fill="both", expand=True)

    # Set the initial theme
    gui.tk.call("source", getname())
    gui.tk.call("set_theme", "dark")

    def change_theme():
        # NOTE: The theme's real name is azure-<mode>
        if gui.tk.call("ttk::style", "theme", "use") == "azure-dark":
            # Set light theme
            gui.tk.call("set_theme", "light")
        else:
            # Set dark theme
            gui.tk.call("set_theme", "dark")

    button = ttk.Button(big_frame, text="Change theme!", command=change_theme ,style="Accent.TButton")
    button.grid()

    #  minimun size not less than geometry setting
    gui.update()
    gui.minsize(gui.winfo_width(), gui.winfo_height())
    x_cordinate = int((gui.winfo_screenwidth() / 2) - (gui.winfo_width() / 2))
    y_cordinate = int((gui.winfo_screenheight() / 2) - (gui.winfo_height() / 2))
    gui.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))
 
    gui.mainloop()



if __name__ == "__main__":
    main()
    # getname()