import requests
import tkinter as tk
import datetime

response = requests.get("http://api.covid19api.com/summary")

def search(country):
    # method 2 do something in search method to account for those cases
    for index in response.json()["Countries"]:
        if index['Country'].lower() == country.lower():
            return index
    return {}

# print(search('kdsfksjfkjs'))
today = datetime.date.today()
window = tk.Tk()
window.geometry("800x400")
window.title("Covid-19 Stats for {}".format(today.strftime("%Y-%m-%d")))

country_entry = tk.Entry(window)
country_entry.place(relx=0.30, rely=0.14)

def btn_press(country):
    # method 1: modify country variable before passing into search
    info = search(country)
    if info:
        new_confirmed = info['NewConfirmed']
        total_confirmed = info['TotalConfirmed']
        new_deaths = info['NewDeaths']
        total_deaths = info['TotalDeaths']
        new_recovered = info['NewRecovered']
        total_recovered = info['TotalRecovered']

        new_confirmed_label = tk.Label(window, text="New confirmed: " +str(new_confirmed), fg='black')
        new_confirmed_label.place(relx=0.30, rely=0.34)
        total_confimed_label = tk.Label(window, text="Total confirmed:" +str(total_confirmed), fg='black')
        total_confimed_label.place(relx=0.30, rely=0.40)
        new_deaths_label = tk.Label(window, text="New deaths: " + str(new_deaths), fg='black')
        new_deaths_label.place(relx=0.30, rely=0.46)
        total_deaths_label = tk.Label(window, text="Total deaths:" + str(total_deaths), fg='black')
        total_deaths_label.place(relx=0.30, rely=0.52)
        new_recovered_label = tk.Label(window, text="New recovered: " + str(new_recovered), fg='black')
        new_recovered_label.place(relx=0.30, rely=0.58)
        total_recovered_label = tk.Label(window, text="Total recovered:" + str(total_recovered), fg='black')
        total_recovered_label.place(relx=0.30, rely=0.64)

        # destroy label after some time
        new_confirmed_label.after(6000, new_confirmed_label.destroy)
        total_confimed_label.after(6000, total_confimed_label.destroy)
        new_deaths_label.after(6000, new_deaths_label.destroy)
        total_deaths_label.after(6000, total_deaths_label.destroy)
        new_recovered_label.after(6000, new_recovered_label.destroy)
        total_recovered_label.after(6000, total_recovered_label.destroy)
    else:
        # country does not exist => what should we do?
        error_label = tk.Label(window, text="No such country exists", fg="black")
        error_label.place(relx=0.30, rely=0.30)
        error_label.after(6000, error_label.destroy)


search_btn = tk.Button(window, text="Search for a country", width=30, relief="sunken",
                       command=lambda: btn_press(country_entry.get()))
search_btn.place(relx=0.30, rely=0.24)

window.mainloop()