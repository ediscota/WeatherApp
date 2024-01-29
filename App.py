
from tkinter import messagebox
import requests
import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap


#Richiesta API e selezione dei campi di intersesse dal .Json
def get_weather(city):
    #richiesta API
    API_key="6a7ff6dafa1f1111180105e74898207f"
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    
    #Gestione errori
    if res.status_code == 404:
        messagebox.showerror("Error", "City not found") 
        return None
    
    weather = res.json() #conversione in json
    
    #seleziona i campi di tuo interesse nel .json
    icon_id= weather['weather'][0]['icon']
    temperature = weather['main']['temp'] -273.15 
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    
    #l'icona la prendi dall'url, non dal json
    icon_url= f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)
    
    
#funzione associata al Button nella GUI, chiama get_weather con parametro la
#entry che scrivi, e aggiorna le icone e i campi    
def search():
    city= city_entry.get()
    result= get_weather(city)
    if result is None:
        return
    
    icon_url, temperature, description, city, country= result
    
    location_label.configure(text=f"{city},{country}")
    
    image = Image.open(requests.get(icon_url, stream=True).raw) #prendi l'icona del meteo dall'URL
    icon = ImageTk.PhotoImage(image) #conversione a formato immagine
    icon_label.configure(image=icon)
    icon_label.image = icon         #aggiorna la icon label a quella appena presa dall'url
    
    temperature_label.configure(text= f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")  #aggiorna temperature e description a quelle corrispondenti per la città
    


#Creazione GUI
root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

city_entry= ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

search_button = ttkbootstrap.Button(root, text="Search", command= search, bootstyle="warning" )
search_button.pack(pady=10)
 
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack()

icon_label = tk.Label(root, font="Helvetica, 25")
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()

