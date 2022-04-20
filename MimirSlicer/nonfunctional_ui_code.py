import tkinter as tk

import wx

app = wx.App()
frame = wx.Frame(parent=None, title='Hello World')
frame.Show()
app.MainLoop()

class ContentViewAccessible(wx.Accessible):

    def GetRole(self, childId):
        return (wx.ACC_OK, wx.ROLE_SYSTEM_DOCUMENT)

    def GetDescription(self, childId):
        return (wx.ACC_OK, "Document Page")


class ContentViewCtrl(wx.TextCtrl):

    def __init__(self, *args, **kwargs):
        super().__init__()
        super().Create(
            *args,
            style=wx.TE_READONLY
            | wx.TE_MULTILINE
            | wx.TE_RICH2
            | wx.TE_AUTO_URL
            | wx.TE_NOHIDESEL,
            **kwargs,
        )
        self.SetAccessible(ContentViewAccessible(self))




class main_window(wx.Frame):
    def init(self):
        wx.Frame.init(self, parent=None, title="Test", name="test") # The name attribute here is used so that when the app starts, screen reader does not read the word "frame". In this case and environment, it has no effect.
        panel=wx.Panel(self)
        test_input=wx.TextCtrl(panel, name="Enter some text here!")
        # or you could comment the line above and uncomment the two lines below. The result is the same. In third case, if you initialize element with the blank string, no success then as well.
        # test_input=wx.TextCtrl(panel)
        # test_input.SetName("Enter some text here!")
        ok_button=wx.Button(panel, label="OK!") # the label for the button will work, however when tabbing or shift+tabbing to the text field, nothing will work.
        self.Show()

main_window()
app.MainLoop()



# window = tk.Tk()

# frame_a = tk.Frame()
# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()

# frame_b = tk.Frame()
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()

# # Swap the order of `frame_a` and `frame_b`
# frame_b.pack()
# frame_a.pack()

# window.mainloop()


# root = tk.Tk()
# root.geometry("350x300")
# root.configure(bg="ghost white")
# root.title("Project Mimir - Print Slicer")

# tk.Label(root, text="Project Mimir", font="arial 20 bold", bg="white smoke").pack()


# root.mainloop()