import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
from tkinter.scrolledtext import ScrolledText
import json

class Home_Page:
    def __init__(self, root):
        root.title("Home Page")
        icon_path = 'images/live_wire_logo.png'
        icon_image = PhotoImage(file=icon_path)
        root.call('wm', 'iconphoto', root._w, icon_image)
        root.geometry('600x500')
        root.resizable(False, False)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        self.mainframe = ttk.Frame(root, relief=RAISED)
        self.mainframe.grid(row=0, column=0, sticky=(N, S, E, W))

        self.style = ThemedStyle()
        self.style.theme_use("clam")
        
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
            
        root.bind('<Return>', self.press_button)
    
    def heirarchy_page(self, *args):
        self.mainframe.grid_remove()
        Heirarchy_Page(root)
        
    def events_page(self, *args):
        self.mainframe.grid_remove()
        Events_Page(root)
        
    def images_page(self, *args):
        self.mainframe.grid_remove()
        Images_Page(root)
        
    def how_to_use(self, *args):
        with open('documents/heirarchy.txt') as f:
            content = f.read()
        messagebox.showinfo("How to use", content)
        with open('documents/events.txt') as f:
            content = f.read()
        messagebox.showinfo("How to use", content)
        
    def press_button(self, event):
        current_focus = root.focus_get()
        if isinstance(current_focus, ttk.Button):
            current_focus.invoke()
        return 'break'
    
    def go_back(self, *args):
        self.subframe.grid_remove()
        Home_Page(root)

    def clear_scr(self):
        for child in self.subframe.winfo_children():
            child.grid_remove()
            
class Heirarchy_Page(Home_Page):
    def __init__(self, root):
        super().__init__(root)
        root.title("Heirarchy Page")
        self.heirarchy_btn.configure(text="Teachers", command=self.show_teacher_coordinator, width=15)
        self.events_btn.configure(text="Conveners", command=self.show_conveners, width=15)
        self.images_btn.configure(text="Teams", command=self.show_teams, width=15)
        self.go_back_btn = ttk.Button(self.subframe, text = "Back", command = self.go_back, width=15)
        self.go_back_btn.grid(pady=10)
        self.quit_btn.grid_remove()
        self.use_btn.grid_remove()
        self.msg = StringVar()
        root.bind("<Escape>", self.go_back)
        
    def show_teacher_coordinator(self, *args):
        self.clear_scr()
        root.title("Teachers")
        with open('live_wire_team/teachers.json') as f:
            teacher = json.load(f)
        if teacher:
            message = teacher
        else:
            message = "This list is empty"
        
        msg = Message(self.subframe, text=message, font=("Helvetica", 16), width=200)
        msg.grid(padx=180, pady=10)
        self.add_team_btn = ttk.Button(self.subframe, text='Add', command=self.add_teacher_coordinator)
        self.add_team_btn.grid(pady=5)
        self.remove_team_btn = ttk.Button(self.subframe, text='Remove', command=self.remove_teacher)
        self.remove_team_btn.grid(pady=5)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.step_back)
        self.step_back_btn.grid(pady=5)
        root.bind("<Escape>", self.step_back)
    
    def add_teacher_coordinator(self):
        self.clear_scr()
        root.title("Adding Teacher")
        self.teacher_lbl = ttk.Label(self.subframe, text="Teacher", background="#DAD7D7", width=12)
        self.teacher_lbl.grid(row=0, column=0, padx=10, pady=5)
        self.teacher_insert = ttk.Entry(self.subframe, width=40)
        self.teacher_insert.grid(row=0, column=2, sticky=E, padx=80)
        self.done_btn = ttk.Button(self.subframe, text="Add", command=self.save_teachers_data)
        self.done_btn.grid(row=1, column=2, padx=10, pady=10)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.show_teacher_coordinator)
        self.step_back_btn.grid(row=1, pady=10)
        self.display_msg = Message(self.subframe, text="", width=250, font=("Helvetica", 12))
        self.display_msg.grid(column=2, padx=20)
        self.teacher_insert.focus()
        root.bind("<Escape>", self.show_teacher_coordinator)
    
    def save_teachers_data(self, *args):
        if self.teacher_insert.get() != "":
            teacher = ""
            try:
                with open('live_wire_team/teachers.json', 'r') as f:
                    content = json.load(f)    
            except:
                pass
            teacher = self.teacher_insert.get()
            with open('live_wire_team/teachers.json', 'w') as f:
                json.dump(teacher, f)
            self.teacher_insert.delete(0, END)
            self.display_msg.configure(text='Data has been added')
    
    def remove_teacher(self):
        self.add_teacher_coordinator()
        root.title("Removing Teacher")
        self.done_btn.configure(text="Remove", command=self.delete_teacher)
        self.step_back_btn.configure(command=self.show_teacher_coordinator)
        root.bind("<Escape>", self.show_teacher_coordinator)
        
    def delete_teacher(self, *args):
        if self.teacher_insert.get() != "":
            with open("live_wire_team/teachers.json") as f:
                content = json.load(f)
            if self.teacher_insert.get() == content:
                content=""
                with open("live_wire_team/teachers.json", 'w') as f:
                    json.dump(content, f)
                self.display_msg.configure(text="Data successfully deleted")
            else:
                self.display_msg.configure(text="Data not found in list")    
            self.teacher_insert.delete(0, END)
            
    def show_conveners(self, *args):
        self.clear_scr()
        root.title("Conveners")
        convener_list = []
        with open('live_wire_team/conveners.json') as f:
            convener_list = json.load(f)
        if convener_list:
            message = ""
            for i, item in enumerate(convener_list):
                message += str(i+1) + '. ' + item + '\n'
        else:
            message = "This list is empty"
        
        msg = Message(self.subframe, text=message, font=("Helvetica", 16), width=200)
        msg.grid(padx=180, pady=10)
        self.add_team_btn = ttk.Button(self.subframe, text='Add', command=self.add_conveners)
        self.add_team_btn.grid(pady=5)
        self.remove_team_btn = ttk.Button(self.subframe, text='Remove', command=self.remove_convener)
        self.remove_team_btn.grid(pady=5)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.step_back)
        self.step_back_btn.grid(pady=5)
        root.bind("<Escape>", self.step_back)
        
    def add_conveners(self):
        self.add_teacher_coordinator()
        root.title("Adding Convener")
        self.teacher_lbl.configure(text="Convener")
        self.done_btn = ttk.Button(self.subframe, text="Add", command=self.save_conveners_data)
        self.done_btn.grid(row=1, column=2, padx=10, pady=10)
        self.step_back_btn.configure(command=self.show_conveners)
        root.bind("<Escape>", self.show_conveners)
    
    def save_conveners_data(self, *args):
        if self.teacher_insert.get() != "":
            convener_list = []
            try:
                with open('live_wire_team/conveners.json', 'r') as f:
                    convener_list = json.load(f)    
            except:
                pass
            convener_list.append(self.teacher_insert.get())
            with open('live_wire_team/conveners.json', 'w') as f:
                json.dump(convener_list, f)
            self.teacher_insert.delete(0, END)
            self.display_msg.configure(text='Data has been added')
            
    def remove_convener(self):
        self.add_conveners()
        root.title("Removing Convener")
        self.done_btn.configure(text="Remove", command=self.delete_convener)
        self.step_back_btn.configure(command=self.show_conveners)
        root.bind("<Escape>", self.show_conveners)
        
    def delete_convener(self, *args):
        if self.teacher_insert.get() != "":
            content = []
            with open("live_wire_team/conveners.json") as f:
                content = json.load(f)
            if self.teacher_insert.get() in content:
                content.remove(self.teacher_insert.get())
                with open("live_wire_team/conveners.json", 'w') as f:
                    json.dump(content, f)
                    self.display_msg.configure(text="Data successfully deleted")
            else:
                self.display_msg.configure(text="Data not found in list")    
            self.teacher_insert.delete(0, END)
    
    def show_teams(self, *args):
        root.title("Select Team")
        self.team_names = ['event', 'creative', 'technical', 'database', 'photography']
        self.clear_scr()
        for number in range(5):
            self.event_btn = ttk.Button(self.subframe, text=self.team_names[number].title(), width=15, command= self.make_command_function(number))
            self.event_btn.grid(padx=200, pady=10)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command=self.step_back)
        self.step_back_btn.grid(pady=10)
        root.bind("<Escape>", self.step_back)
        
    def make_command_function(self, index):
        def command_function():
            self.show_team_member_list(index)
        return command_function
    
    def show_team_member_list(self, index, *args):
        self.clear_scr()
        self.field_name=['Event Management', 'Creative', 'Technical', 'Database', 'Photography']
        head_files=['event_head.json', 'creative_head.json', 'technical_head.json', 'database_head.json', 'photography_head.json']
        team_files=['event_team.json', 'creative_team.json', 'technical_team.json', 'database_team.json', 'photography_team.json']
        root.title(f"{self.field_name[index]} Team")
        head_name = ""
        team_members=[]
        temp = index
         
        head_lbl = ttk.Label(self.subframe, text=f"{self.field_name[index]} head", width=28)
        head_lbl.grid(row=0, column=0, padx=10, pady=5)
        head_lbl = ttk.Label(self.subframe, width=28, background='white')
        head_lbl.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        with open(f"live_wire_team/{head_files[index]}") as f:
            head_name = json.load(f)
        if head_name:
            head_lbl.configure(text=head_name.title())
        else:
            head_lbl.configure(text="")
        head_lbl = ttk.Label(self.subframe, text=f"{self.field_name[index]} team", width=28)
        head_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=N)
        with open(f"live_wire_team/{team_files[index]}") as f:
            team_members = json.load(f)
        names_list_txt = ScrolledText(self.subframe , width=35, height=10, background='white')
        names_list_txt.grid(row=1, column=1, padx=10, pady=5)
        for index,member in enumerate(team_members):
            names_list_txt.insert(END, str(index+1) + ". " + member + "\n")
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = self.show_teams)
        self.step_back_btn.grid(row=2, pady=10)
        self.add_team_btn = ttk.Button(self.subframe, text='Add', command=lambda: self.add_team(temp))
        self.add_team_btn.grid(row=2, column=1, sticky=E, padx=20)
        self.remove_team_btn = ttk.Button(self.subframe, text='Remove', command=lambda: self.remove_team(temp))
        self.remove_team_btn.grid(row=2, column=1, sticky=W, padx=20)
        root.bind("<Escape>", self.show_teams)
    
    def add_team(self, index, *args):
        self.clear_scr()
        root.title(f"Adding {self.team_names[index].title()} Team")
        self.head_lbl = ttk.Label(self.subframe, text=f"{self.field_name[index]} Head", background="#DAD7D7", width=28)
        self.head_lbl.grid(row=0, column=0, padx=10, pady=5)
        self.get_head = ttk.Entry(self.subframe, width=40)
        self.get_head.grid(row=0, column=1)
        self.team_lbl = ttk.Label(self.subframe, text=f"{self.field_name[index]} Team", background="#DAD7D7", width=28)
        self.team_lbl.grid(row=1, column=0, padx=15, pady=5, sticky=N)
        self.get_team = Text(self.subframe, width=35, height=12)
        self.get_team.grid(row=1, column=1, columnspan=2, pady=5, sticky=E, padx=10)
        self.done_btn = ttk.Button(self.subframe, text="Add", command=lambda: 
            self.save_team(self.get_head.get(), self.get_team.get("1.0", 'end-1c'), self.team_names[index],
                                   self.get_head, self.get_team))
        self.done_btn.grid(row=2, column=1, padx=10, sticky=E)
        self.step_back_btn = ttk.Button(self.subframe, text = "Back", command = lambda: self.show_team_member_list(index))
        self.step_back_btn.grid(row=2)
        self.display_msg = Message(self.subframe, text="", width=250, font=("Helvetica", 12))
        self.display_msg.grid(column=1, sticky=W)
        root.bind("<Escape>", lambda event: self.show_team_member_list(index))
        
    def save_team(self, head_data, team_data, name, head_space, team_space,*args):
        if head_data != "":
            new_head = head_data
            with open(f'live_wire_team/{name}_head.json', 'w') as f:
                json.dump(new_head, f)
            head_space.delete(0, END)
            self.display_msg.configure(text='Data has been added')
            
        if team_data != "":
            member_list = []
            try:
                with open(f'live_wire_team/{name}_head.json') as f:
                    member_list = json.load(f)    
            except:
                pass
            data = team_data
            data.strip()
            lines = data.split('\n')
            for line in lines:
                if line != "":
                    member_list.append(line)
            with open(f'live_wire_team/{name}_team.json', 'w') as f:
                json.dump(sorted(member_list), f)
            team_space.delete("1.0", END)
            self.display_msg.configure(text='Data has been added')
            
    def remove_team(self, index, *args):
        self.add_team(index)
        root.title(f"Removing {self.team_names[index].title()} Team")
        self.get_team.grid_remove()
        self.get_head = ttk.Entry(self.subframe, width=50)
        self.get_head.grid(row=0, column=1)
        self.get_team = ttk.Entry(self.subframe, width=50)
        self.get_team.grid(row=1, column=1)
        self.done_btn.configure(text="Remove", command=lambda: 
            self.delete_team(self.get_head.get(), self.get_team.get(), self.team_names[index],
                                   self.get_head, self.get_team))
        self.done_btn.grid_configure(sticky=(N,E,S,W))
    
    def delete_team(self, head_data, team_data, name, head_space, team_space,*args):
        if head_data != "":
            with open(f'live_wire_team/{name}_head.json') as f:
                content = json.load(f)
            if content == head_data:
                with open(f'live_wire_team/{name}_head.json', 'w') as f:
                    json.dump("", f)
                self.display_msg.configure(text="Data sucessfully removed")
            else:
                self.display_msg.configure(text="Data not found in list")
            head_space.delete(0, END)
            
        if team_data != "":
            with open(f'live_wire_team/{name}_team.json') as f:
                content = json.load(f)
            if team_data in content:
                content.remove(self.get_event_team.get())
                with open(f'live_wire_team/{name}_team.json', 'w') as f:
                    json.dump(content, f)
                self.display_msg.configure(text="Data sucessfully removed")
            else:
                self.display_msg.configure(text="Data not found in list")
            team_space.delete(0, END)
        
    def step_back(self, *args):
        self.clear_scr()
        self.step_back_btn.grid_remove()
        Heirarchy_Page(root)
    
class Events_Page(Home_Page):
    def __init__(self, root):
        super().__init__(root)
        self.clear_scr()
        events_list=[]
        ttk.Label(self.subframe, text="List of Events", font=("Helvetica", 16)).grid(row=0, column=0, sticky=N)
        self.list_of_events = Listbox(self.subframe, height=15, width=40)
        self.list_of_events.grid(row=0, column=1, padx=50)
        try:
            with open("events/event_names.json") as f:
                events_list = json.load(f)
        except:
            pass
        for index,event in enumerate(events_list):
            self.list_of_events.insert(END, event.title())
            if index%2==0:
                self.list_of_events.itemconfigure(index, background='#f0f0ff')
        self.delete_event_btn = ttk.Button(self.subframe, text = "Delete Event", command = self.delete_event)
        self.delete_event_btn.grid(row=1, column=0 , pady=5, sticky=W, padx=15)
        self.open_event_btn = ttk.Button(self.subframe, text="Open Event Details", command=self.display_event)
        self.open_event_btn.grid(row=1, column=1, padx=15, pady=5, sticky=E)
        self.create_event_btn = ttk.Button(self.subframe, text="Create New Event", command=self.create_event)
        self.create_event_btn.grid(row=1, column=1, pady=5, padx=40, sticky=W)
        self.go_back_btn = ttk.Button(self.subframe, text = "Back", command = self.go_back)
        self.go_back_btn.grid(row=2, column=1 , padx=30, pady=5, sticky=W)
        
        root.bind("<Escape>", self.go_back)
        
    def delete_event(self):
        with open("events/event_names.json") as f:
            events_list = json.load(f)
        try:
            selected_item = self.list_of_events.get(self.list_of_events.curselection())
            if selected_item in events_list:
                events_list.remove(selected_item)
            with open("events/event_names.json", 'w') as f:
                json.dump(events_list ,f)
            os.remove(f"events/{selected_item}.json")
            self.step_back()
        except:
            pass
        
    def display_event(self):
        selected_item = ""
        try:
            self.selected_item = self.list_of_events.get(self.list_of_events.curselection())
            with open(f'events/{self.selected_item}.json') as f:
                content = json.load(f)
            new_root = Tk()
            new_root.title(selected_item)
            
            self.menu_bar = Menu(new_root)
            new_root.config(menu=self.menu_bar)
            self.file_menu = Menu(self.menu_bar, tearoff=0)
            self.menu_bar.add_cascade(label="File", menu=self.file_menu)
            self.file_menu.add_command(label="Save", command=self.update_event)
            self.menu_bar.config(font=("Arial", 26))
            
            self.display_content = ScrolledText(new_root)
            self.display_content.insert(END, content)
            self.display_content.grid(row=0, column=0, sticky=(N,S,E,W))
            new_root.rowconfigure(0, weight=1)
            new_root.columnconfigure(0, weight=1)
            new_root.mainloop()
        except:
            pass
        
    def update_event(self):
        content=self.display_content.get(1.0, END)
        with open(f'events/{self.selected_item}.json', 'w') as f:
            json.dump(content, f)
        pass
    
    def create_event(self):
        self.clear_scr()
        self.event_name_lbl = ttk.Label(self.subframe, text="Event Name", width=20)
        self.event_name_lbl.grid(row=0, column=0)
        self.get_event_name = ttk.Entry(self.subframe, width=40)
        self.get_event_name.grid(row=0, column=1, sticky=W)
        self.event_name_lbl = ttk.Label(self.subframe, text="Event Details", width=20)
        self.event_name_lbl.grid(row=1, column=0, sticky=N, pady=10)
        self.get_event_details = Text(self.subframe, width=37, height=13)
        self.get_event_details.grid(row=1, column=1, pady=10)
        self.create_event_btn = ttk.Button(self.subframe, text="Done", command=self.save_event_data)
        self.create_event_btn.grid(row=2, column=1, padx=50)
        self.go_back_btn = ttk.Button(self.subframe, text = "Back", command = self.step_back)
        self.go_back_btn.grid(row=2, column=0, padx=50, sticky=W)
        self.display_msg = ttk.Label(self.subframe, text="", font=("Helvetica", 16))
        self.display_msg.grid(column=1, sticky=W, pady=5, padx=40)
        
        root.bind("<Escape>", self.step_back)
        self.get_event_details.bind("<Control-v>", self.paste_text)
                
    def save_event_data(self):
        events_list = []
        if self.get_event_name.get() != "" and self.get_event_details.get(1.0, END) == "":
            self.display_msg.configure(text="Enter event details first")
                
        if self.get_event_details.get(1.0, END) != "" and self.get_event_name.get() == "":
            self.display_msg.configure(text="Enter event name first")
            
        if self.get_event_details.get(1.0, END) != "" and self.get_event_name.get() != "":
            try:
                with open("events/event_names.json") as f:
                    events_list = json.load(f)
            except:
                pass
            if self.get_event_name.get not in events_list:
                events_list.append(self.get_event_name.get().title())
            with open("events/event_names.json", 'w') as f:
                json.dump(events_list, f)
            with open(f"events/{self.get_event_name.get()}.json", 'w') as f:
                json.dump(self.get_event_details.get(1.0, END), f)
            self.display_msg.configure(text="Event details saved")
        
    def paste_text(self,event):
        event.widget.insert(INSERT, root.clipboard_get())
        
    def step_back(self, *args):
        self.clear_scr()
        Events_Page(root)
     
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
        self.use_btn.grid_remove()
        
    def go_back(self, *args):
        self.subframe.grid_remove()
        Home_Page(root)
        
if __name__ == '__main__':
    root = Tk()
    Home_Page(root)
    root.mainloop()
