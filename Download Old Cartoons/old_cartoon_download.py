from tkinter import *
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


main_window = Tk()

#labels
Label(main_window, text="Enter cartoon name").grid(row=0, column=0)

#text input
cartoon = Entry(main_window, width=80, borderwidth= 3)
cartoon.grid(row=0, column=1)

# checkbutton for ep or movies or both
var = StringVar()
var.set(" ")
ep = Radiobutton(main_window, text="Episodes", variable=var, value="episodes").grid(row=1, column=0)
mov = Radiobutton(main_window, text="Movies", variable=var, value="movies")
mov.grid(row=1, column=1)
both = Radiobutton(main_window, text="Both", variable=var, value=" ")
both.grid(row=1, column=2)


# automation script with user input
def click_button():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome() 
    driver.maximize_window()
    driver.get("https://raretoonshindi.in/")

    search_btn = driver.find_element(by=By.XPATH, value="//*[@id='header']/div[1]/div/div/div/div[2]/div/span")
    search_btn.click()

    search_bar = driver.find_element(by=By.XPATH, value="//*[@id='header']/div[1]/div/div/div/div[2]/div/div/form/input")
    search_bar.send_keys(cartoon.get() + " " + var.get(), Keys.ENTER)
    main_window.destroy()
    while(True):
        pass

#button
Button(main_window, text="Go!", width=20, bg="red", command=click_button).grid(row=2, column=1)

main_window.mainloop()
