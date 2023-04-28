import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def calculate_footprint():
    
    distance = float(distance_entry.get())
    electricity = float(electricity_entry.get())
    water = float(water_entry.get())
    waste = float(waste_entry.get())

    
    transportation_cf = distance * 0.16  
    electricity_cf = electricity * 0.5   
    water_cf = water * 0.25             
    waste_cf = waste * 0.2              

    total_cf = transportation_cf + electricity_cf + water_cf + waste_cf

    
    data = {'Category': ['Transportation', 'Electricity', 'Water', 'Waste'],
            'Usage': [distance, electricity, water, waste],
            'Carbon Footprint (kg CO2)': [transportation_cf, electricity_cf, water_cf, waste_cf]}
    df = pd.DataFrame(data)

    
    result_label.config(text="Your monthly carbon footprint is approximately {:.2f} kg CO2 equivalent.".format(total_cf))
    tips_label.config(text="Here are some tips to reduce your carbon footprint:")
    tips_list.delete(0, tk.END)
    if transportation_cf > 200:
        tips_list.insert(tk.END, "- Use public transportation, bike, or walk whenever possible.")
    if electricity_cf > 100:
        tips_list.insert(tk.END, "- Turn off lights and electronics when not in use and switch to energy-efficient appliances.")
    if water_cf > 190:
        tips_list.insert(tk.END, "- Fix leaky faucets, take shorter showers, and use a low-flow toilet.")
    if waste_cf > 100:
        tips_list.insert(tk.END, "- Reduce, reuse, and recycle as much as possible.")

    
    df.to_csv('carbon_footprint_results.csv', index=False)


root = tk.Tk()
root.title("Carbon Footprint Calculator")


distance_label = tk.Label(root, text="What is your average monthly transportation distance in kilometers?")
distance_label.pack()
distance_entry = tk.Entry(root)
distance_entry.pack()

electricity_label = tk.Label(root, text="What is your average monthly electricity usage in kilowatt-hours?")
electricity_label.pack()
electricity_entry = tk.Entry(root)
electricity_entry.pack()

water_label = tk.Label(root, text="What is your average monthly water usage in cubic meters?")
water_label.pack()
water_entry = tk.Entry(root)
water_entry.pack()

waste_label = tk.Label(root, text="What is your average monthly waste production in kilograms?")
waste_label.pack()
waste_entry = tk.Entry(root)
waste_entry.pack()


calc_button = tk.Button(root, text="Calculate", command=calculate_footprint)
calc_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()

tips_label = tk.Label(root, text="")
tips_label.pack()

tips_list = tk.Listbox(root)
tips_list.pack()


root.mainloop()
