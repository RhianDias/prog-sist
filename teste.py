import pyautogui
pyautogui.PAUSE = 0.7

#pyautogui.click
#pyautogui.write
#pyautogui.press
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://pt.wikipedia.org/wiki/Sport_Club_Corinthians_Paulista"
pyautogui.write(link)
pyautogui.press('enter')   
