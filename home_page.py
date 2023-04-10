from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
from tkinter.scrolledtext import ScrolledText
import json

class Home_Page:
    def __init__(self, root):
        root.title("Live Wire Official Application")
        icon_path = 'images/live_wire_logo.png'
        icon_image = PhotoImage(file=icon_path)
        root.call('wm', 'iconphoto', root._w, icon_image)
        root.geometry('600x500')
        root.resizable(False, False)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        # root.option_add('*tearOff', FALSE)
        self.mainframe = ttk.Frame(root, relief=RAISED)
        self.mainframe.grid(row=0, column=0, sticky=(N, S, E, W))
        
        # self.menubar = Menu(root)
        # root.config(menu=self.menubar)
        
        # self.mode_menu = Menu(self.menubar)
        # self.menubar.add_cascade(label="Mode", menu=self.mode_menu)
        # self.mode_menu.add_command(label='Sky Theme', command=self.change_theme)
        
        # Create an instance of ttk Style
        self.style = ThemedStyle()
        # Configure the theme with style
        # self.style.theme_use("clam")

        self.club_logo = PhotoImage(file='images/bigger_club_logo.png')
        self.club_label = Label(self.mainframe, image=self.club_logo, background="#dcdad5")
        self.club_label.grid(row=0, column=0, sticky=N, padx=50, pady=25)

        self.clg_logo = PhotoImage(file='images/clg_logo.png')
        self.clg_label = Label(self.mainframe, image=self.clg_logo, background="#dcdad5")
        self.clg_label.grid(row=0, column=2, sticky=N, pady=20, padx=50)

        self.subframe = ttk.Frame(self.mainframe, relief=RIDGE, borderwidth=10)
        self.subframe.grid(row=1, column=0, columnspan=3, sticky=(N,E,S,W), padx=40)
        
        self.heirarchy_btn = ttk.Button(self.subframe, text="Heirarchy", command=self.heirarchy_page, width=15)
        self.heirarchy_btn.grid(pady=20)

        self.events_btn = ttk.Button(self.subframe, text="Events", command=self.events_page, width=15)
        self.events_btn.grid()

        self.images_btn = ttk.Button(self.subframe, text="Images", command=self.images_page, width=15)
        self.images_btn.grid()
        
        self.use_btn = ttk.Button(self.subframe, text="How to use", command=self.how_to_use, width=15)
        self.use_btn.grid()
        
        self.mode_btn = ttk.Button(self.subframe, text="Cream Theme", command=self.change_theme, width=15)
        self.light_mode = True
        self.mode_btn.grid()
                
        self.quit_btn = ttk.Button(self.subframe, text="Quit", command=lambda: root.quit(), width=15)
        self.quit_btn.grid()
        
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.rowconfigure(3, weight=1)
        self.mainframe.columnconfigure(3, weight=1)
        
        for child in self.subframe.winfo_children():
            child.grid_configure(padx=210, pady=10)
    
    def heirarchy_page(self, *args):
        self.mainframe.grid_remove()
        Heirarchy_Page(root)
        
    def events_page(self, *args):
        self.mainframe.grid_remove()
        Events_Page(root)
        
    def images_page(self, *args):
        self.mainframe.grid_remove()
        Images_Page(root)
        
    def how_to_use(self):
        with open('members/how_to_use.txt') as f:
            content = f.read()
        messagebox.showinfo("How to use", content)
        
    def change_theme(self):
        if self.light_mode:
            self.style.theme_use("itft1")
            self.mode_btn.configure(text="Sky Theme")
            self.club_label.configure(background="#daeffd")
            self.clg_label.configure(background="#daeffd")
            self.light_mode = False
        
        else:
            self.style.theme_use("clam")
            self.mode_btn.configure(text="Cream Theme")
            self.club_label.configure(background="#dcdad5")
            self.clg_label.configure(background="#dcdad5")
            self.light_mode = True
        
    def go_back(self, *args):
        self.subframe.grid_remove()
        Home_Page(root)

    def clear_scr(self):
        for child in self.subframe.winfo_children():
            child.grid_remove()
            
class Heirarchy_Page(Home_Page):
    def __init__(self, root):
        super().__init__(root)
        self.heirarchy_btn.configure(text="Conveners", command=self.show_conveners, width=15)
        self.events_btn.configure(text="Team Heads", command=self.show_heads, width=15)
        self.images_btn.configure(text="Active Members", command=self.show_active_members, width=15)
        self.edit_btn = ttk.Button(self.subframe, text="Edit", command=self.edit_list, width=15)
        self.edit_btn.grid(pady=10)
        self.go_back_btn = ttk.Button(self.subframe, text = "Back", command = self.go_back, width=15)
        self.go_back_btn.grid(pady=10)
        self.quit_btn.grid_remove()
        self.use_btn.grid_remove()
        # self.mode_btn.grid_forget()
        self.msg = StringVar()
    
    def show_conveners(self):
        self.clear_scr()
        convener_list = []
        with open('members/conveners.json') as f:
            convener_list = json.load(f)
        if convener_list:
            message = ""
            for i, item in enumerate(convener_list):
                message += str(i+1) + '. ' + item + '\n'
        
        else:
            message = "This list is empty"
        
        msg = Message(self.subframe, text=message, font=("Helvetica", 16), width=200)
        msg.grid(padx=160)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.step_back)
        self.step_back_btn.grid(pady=10)
    
    def show_heads(self):
        self.clear_scr()
        heads_list = {}
        text_widget = ScrolledText(self.subframe, width=40, height=10,background='#afafaf')
        with open('members/team_heads.json') as f:
            heads_list = json.load(f)
        if heads_list:
            count=1
            for team, name in heads_list.items():
                text_widget.insert(END, str(count) + '. ' + team + ' : ' + name + "\n")
                count = count+1
        else:
            text_widget.insert(END,"This list is empty")
            
        text_widget.grid(padx=80)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.step_back)
        self.step_back_btn.grid(pady=10)
    
    def show_active_members(self):
        self.clear_scr()
        member_list = []
        text_widget = ScrolledText(self.subframe, width=40, height=10, background='#afafaf')

        with open('members/active_members.json') as f:
            member_list = json.load(f)
        if member_list:
            # Loop through the list and add each item to the widget
            for item in sorted(member_list):
                text_widget.insert(END, item + "\n")
        else:
            text_widget.insert(END,"This list is empty")
        text_widget.grid(padx=80)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.step_back)
        self.step_back_btn.grid(pady=10)

        
    def edit_list(self):
        for child in self.subframe.winfo_children():
            child.grid_remove()
        self.add_btn = ttk.Button(self.subframe, text="Add", command=self.add_members)
        self.add_btn.grid(padx=215)
        self.remove_btn = ttk.Button(self.subframe, text="Remove", command=self.remove_members)
        self.remove_btn.grid(pady=10)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.step_back)
        self.step_back_btn.grid(pady=10)
    
        
    def add_members(self):
        for child in self.subframe.winfo_children():
            child.grid_remove()
        self.conv_lbl = ttk.Label(self.subframe, text="Conveners", background="#DAD7D7", width=12)
        self.conv_lbl.grid(row=0, column=0, padx=10)
        self.conv_insert = ttk.Entry(self.subframe, width=40)
        self.conv_insert.grid(row=0, column=1)
        self.done_btn = ttk.Button(self.subframe, text="Add", command=self.save_data)
        self.done_btn.grid(row=0, column=2, padx=10)
        self.title_lbl = ttk.Label(self.subframe, text="Team Name", background="#DAD7D7", width=12)
        self.title_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.get_team = ttk.Entry(self.subframe)
        self.get_team.grid(row=1, column=1, sticky=W)
        self.name_lbl = ttk.Label(self.subframe, text="Head Name", background="#DAD7D7", width=12)
        self.name_lbl.grid(row=1, column=1, pady=10, sticky=E)
        self.get_name = ttk.Entry(self.subframe)
        self.get_name.grid(row=1, column=2, padx=10)
        self.members_lbl = ttk.Label(self.subframe, text="Active Members", background="#DAD7D7")
        self.members_lbl.grid(row=2, column=0, padx=10)
        self.get_members = Entry(self.subframe, width=30)
        self.get_members.grid(row=2, column=1, padx=10, pady=15)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.step_back)
        self.step_back_btn.grid(column=1 ,pady=10)
        self.display_msg = Message(self.subframe, textvariable=self.msg, width=250, font=("Helvetica", 12))
        self.display_msg.grid(column=1, padx=20)
        
        root.bind("<Return>", self.save_data)
    
    def remove_members(self):
        self.add_members()
        self.display_msg.grid_remove()
        self.done_btn.configure(text="Remove", command = self.delete_data)
        self.reboot_btn = ttk.Button(self.subframe, text = "Clear All Data", command = self.clear_all_data)
        self.reboot_btn.grid(column=1 ,pady=10)
        self.display_msg = Message(self.subframe, textvariable=self.msg, width=250, font=("Helvetica", 12))
        self.display_msg.grid(column=1, padx=20)
        root.bind("<Return>", self.delete_data)
        
    def delete_data(self, *args):
        if self.conv_insert.get != "":
            convener_list = []
            try:
                with open('members/conveners.json', 'r') as f:
                    convener_list = json.load(f)
            except:
                pass
            if self.conv_insert.get() in convener_list:
                convener_list.remove(self.conv_insert.get())
                with open('members/conveners.json', 'w') as f:
                    json.dump(convener_list, f)
                self.msg.set("Data is successfully deleted.")
            else:
                self.msg.set(f"\"{self.conv_insert.get()}\" was not found in list")
            self.conv_insert.delete(0,END)
        
        if self.get_team.get() != "" :
            team_heads_list = {}
            try:
                with open('members/team_heads.json', 'r') as f:
                    team_heads_list = json.load(f)
            except:
                pass
            if self.get_team.get() in team_heads_list:
                del team_heads_list[self.get_team.get()]
                with open('members/team_heads.json', 'w') as f:
                    json.dump(team_heads_list, f)
                self.msg.set("Data is successfully deleted.")
            else:
                self.msg.set(f"\"{self.get_team.get()}\" was not found in list")
            self.get_team.delete(0,END)
            self.get_name.delete(0,END)
        
        if self.get_members.get() != "":
            member_list = []
            try:
                with open('members/active_members.json', 'r') as f:
                    member_list = json.load(f)
            except:
                pass
            if self.get_members.get() in member_list:
                member_list.remove(self.get_members.get())
                with open('members/conveners.json', 'w') as f:
                    json.dump(member_list, f)
                self.msg.set("Data is successfully deleted.")
            else:
                self.msg.set(f"\"{self.get_members.get()}\" was not found in list")
            self.get_members.delete(0,END)
            
    def clear_all_data(self):
        convener_list = []
        with open('members/conveners.json', 'w') as f:
            json.dump(convener_list, f)
            
        team_heads = {}
        with open('members/team_heads.json', 'w') as f:
            json.dump(team_heads, f)
            
        members_list = []
        with open('members/active_members.json', 'w') as f:
            json.dump(members_list, f)
            
        self.msg.set("All data has been cleared")
    
    def step_back(self):
        for child in self.subframe.winfo_children():
            child.grid_remove()
        self.step_back_btn.grid_remove()
        Heirarchy_Page(root)
    
    def save_data(self, *args):
        if self.conv_insert.get() != "":
            convener_list = []
            try:
                with open('members/conveners.json', 'r') as f:
                    convener_list = json.load(f)    
            except:
                pass
            convener_list.append(self.conv_insert.get())
            with open('members/conveners.json', 'w') as f:
                json.dump(convener_list, f)
            self.conv_insert.delete(0, END)
            self.msg.set("Data has been added")
        
        if self.get_name.get() != "" and self.get_team.get() != "":
            team_heads = {}
            try:
                with open('members/team_heads.json', 'r') as f:
                    team_heads = json.load(f)
            except:
                pass
            team_heads[self.get_team.get()] = self.get_name.get()
            with open('members/team_heads.json', 'w') as f:
                json.dump(team_heads, f)
            self.get_team.delete(0, END)
            self.get_name.delete(0,END)
            self.msg.set("Data has been added")
        
        if self.get_members.get() != "":
            active_member_list = []
            try:
                with open('members/active_members.json', 'r') as f:
                    active_member_list = json.load(f)
            except FileNotFoundError:
                pass
            active_member_list.append(self.get_members.get())
            with open('members/active_members.json', 'w') as f:
                json.dump(active_member_list, f)
            self.get_members.delete(0, END)
            self.msg.set("Data has been added")
    
class Events_Page(Home_Page):
    def __init__(self, root):
        super().__init__(root)
        self.heirarchy_btn.destroy()
        self.events_btn.destroy()
        self.images_btn.destroy()
        self.quit_btn.destroy()
        self.mode_btn.destroy()
        self.use_btn.destroy()
        self.list_of_events = Listbox(self.subframe, height=15, width=30)
        self.list_of_events.grid(padx=150)
        self.list_of_events.insert(END, "This section is under work")
        self.create_event_btn = ttk.Button(self.subframe, text="Create Event", command=self.create_event)
        self.create_event_btn.grid(pady=10)
        self.go_back_btn = ttk.Button(self.subframe, text = "Back", command = self.go_back)
        self.go_back_btn.grid()
        
    def create_event(self):
        pass
        
    def go_back(self, *args):
        self.subframe.grid_remove()
        Home_Page(root)
     
            
class Images_Page(Home_Page):
    def __init__(self, root):
        super().__init__(root)
        self.heirarchy_btn.destroy()
        self.events_btn.destroy()
        self.images_btn.destroy()
        ttk.Label(self.subframe, text="This Page is Empty").grid(padx=200)
        self.go_back_btn = ttk.Button(self.subframe, text = "Back", command = self.go_back)
        self.go_back_btn.grid(pady=10)
        self.quit_btn.grid_remove()
        self.mode_btn.grid_remove()
        self.use_btn.grid_remove()
        
    def go_back(self, *args):
        self.subframe.grid_remove()
        Home_Page(root)
        
if __name__ == '__main__':
    root = Tk()    
    style = ThemedStyle()
    style.theme_use("clam")
    Home_Page(root)
    root.mainloop()
