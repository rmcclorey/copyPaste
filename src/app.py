import pyautogui
import pyperclip as clip
import time
import tkinter as tk
from tkinter import ttk

def copyPaste():
	for i in range(5, 0, -1):
		otptTimer.set(i)
		root.update_idletasks()
		time.sleep(1)
	otptTimer.set('Pasting!')
	root.update_idletasks()
	for word in inptField.get("1.0", "end-1c").split(' '):
		clip.copy(word)
		pyautogui.hotkey('ctrl','v')
		pyautogui.press('enter')
	
def main():
	inptField.pack()
	button.pack()
	otpt.pack()
	root.mainloop()
	


root = tk.Tk()
root.title("Copy/Paste automation")
inpt = tk.StringVar()
inptField = tk.Text(root)
otptTimer = tk.StringVar()
otptTimer.set(5)
button = ttk.Button(root, text="Paste!", command=copyPaste)
otpt = ttk.Label(root, textvariable=otptTimer)

if __name__ == '__main__':
	main()
