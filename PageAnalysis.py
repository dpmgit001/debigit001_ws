import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import filedialog as fd

def analyse():
  print("Analysing page...") 

root = tk.Tk()

top_frame = ttk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X)

bottom_frame = ttk.Frame(root)
bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True) 

favorite1_btn = ttk.Button(top_frame, text="Favorite 1", command=lambda: load_url("https://www.google.com"))
favorite1_btn.pack(side=tk.LEFT)

favorite2_btn = ttk.Button(top_frame, text="Favorite 2", command=lambda: load_url("https://www.youtube.com"))
favorite2_btn.pack(side=tk.LEFT)

analyse_btn = ttk.Button(top_frame, text="Analyse", state=tk.DISABLED, command=analyse)
analyse_btn.pack(side=tk.LEFT)

browser = tk.Text(bottom_frame)
browser.pack(fill=tk.BOTH, expand=True)

def load_url(url):
  analyse_btn.config(state=tk.DISABLED)
  
  webbrowser.open(url)
  browser.insert(tk.END, webbrowser.open(url).read())
  
  analyse_btn.config(state=tk.NORMAL)



root.mainloop()