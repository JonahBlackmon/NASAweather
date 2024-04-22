import customtkinter 
from data import *
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry('500x350')
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill='both',expand=True)
title = customtkinter.CTkLabel(master=frame, text='Current Weather on Mars', font=("Mars Weather Data", 24))
title.pack(pady = 12, padx = 10)
tDay = customtkinter.CTkLabel(master=frame, text=f'Current Terrestrial Date: {currentDay}', font = ("Roboto", 16))
tDay.pack(pady = 6, padx = 5)
sol = customtkinter.CTkLabel(master=frame, text=f'Current Mars Sol: {recentSol}', font = ("Roboto", 16))
sol.pack(pady = 6, padx = 5)
minT = customtkinter.CTkLabel(master=frame, text=f'Lowest Temp Today: {recentMin}', font = ("Roboto", 16))
minT.pack(pady = 6, padx = 5)
maxT = customtkinter.CTkLabel(master=frame, text=f'Highest Temp Tody: {recentMax}', font = ("Roboto", 16))
maxT.pack(pady = 6, padx = 5)


root.mainloop()









'''
pygame.init()
screen = pygame.display.set_mode([1710,1040])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.display.flip()
pygame.quit()
'''
