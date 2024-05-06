import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if city:
        try:
            api_key = '2fa73590fd8b5a4c6e68098ad5625395'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            data = response.json()
            temperature = data['main']['temp']
            if temperature_format.get() == 'Celsius':
                temp_label.config(text=f'Temperature: {temperature} °C')
            elif temperature_format.get() == 'Fahrenheit':
                temp_label.config(text=f'Temperature: {temperature * 9/5 + 32} °F')
        except Exception as e:
            messagebox.showerror('ERROR', f'An error occurred: {e}')
    else:
        messagebox.showwarning('Caution', 'Please enter a city name')

root = tk.Tk()
root.title('Swiss Sunrise')
root.geometry('700x700')

header_label = tk.Label(root, text='Swiss Sunrise', font=('Times New Roman', 18))
header_label.pack(pady=10)

city_frame = tk.Frame(root)
city_frame.pack()

city_entry = tk.Entry(city_frame, font=('Times New Roman', 14))
city_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(city_frame, text='Search', command=get_weather, font=('Times New Roman', 14))
search_button.pack(side=tk.LEFT, padx=5)

temperature_format = tk.StringVar()
temperature_format.set('Celsius')
format_dropdown = tk.OptionMenu(root, temperature_format, 'Celsius', 'Fahrenheit')
format_dropdown.pack(pady=10)

temp_label = tk.Label(root, text='Temperature: ', font=('Times New Roman', 16))
temp_label.pack(pady=10)

root.mainloop()
