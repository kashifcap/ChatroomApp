from tkinter import *


class ChatApplication():
    def __init__(self):
        self.chatroom_size = '800x600+250+100'
        self.chatroom_title = 'Chatroom'
        self.backgroungcolor = 'pink'
        self.chatbox_size = (90, 25)
        self.messagebox_width = 70
        self.send_button_background_color = 'cyan'
        self.send_button_foreground_color = 'black'
    

    def send_messages_to_server(self):
        message = self.messagebox.get()
        self.chatbox.insert(END, str('ME : ' + message))
        self.messagebox.delete(0, END)


    def chat_screen(self):
        self.root = Tk()
        self.root.geometry(self.chatroom_size)
        self.root.title(self.chatroom_title)
        self.root.config(bg = self.backgroungcolor)

        self.chatbox = Listbox(self.root, height = self.chatbox_size[1], width = self.chatbox_size[0])
        self.chatbox.grid(row = 0, column = 0, padx = (35,20), pady = 30, columnspan = 3)

        self.messagebox = Entry(self.root, width = self.messagebox_width)
        self.messagebox.grid(row = 1, column = 0, columnspan = 2, padx = (35, 0))

        self.send_button = Button(self.root, text = 'Send',
                                         bg = self.send_button_background_color,
                                         fg = self.send_button_foreground_color,
                                         command = self.send_messages_to_server)
        self.send_button.grid(row = 1, column = 2)

        print('Before mainloop')
        self.root.mainloop()
        print('After mainloop')
    


if __name__ == "__main__":
    chat_app = ChatApplication()
    chat_app.chat_screen()