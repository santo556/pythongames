import tkinter as tk
class Game(tk.Frame):
    def __init__(self, master):
        super(self, Game).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self,bg='#aaaaff', width=self.width, height=self.height)
        self.canvas.pack()
        self.pack()
if __name__ == '_main_':
    root = tk.Tk()
    root.title('Janela do Game!')
    game = Game(root)
    # Essa linha é só para abrir a janela, é a chamada a instãncia do Game.
    game.mainloop()



