import pyautogui
import pyperclip as clip
import time

def main():
	time.sleep(5)
	with open('input.txt', 'r') as f:
		for line in f:
			for word in line.split(' '):
				clip.copy(word)
				pyautogui.hotkey('ctrl','v')
				pyautogui.press('enter')
	


if __name__ == '__main__':
	main()
