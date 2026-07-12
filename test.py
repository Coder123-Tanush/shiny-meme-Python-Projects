import tkinter as tk
import random
window = tk.Tk()
window.title("Laptop Store")
window.geometry("650x650+100+100")
window.configure(bg = "linen")

specs = ['Brand', 'Model', 'CPU', 'Speed', 'RAM', 'Storage', 'Screen Size', 'Price']
laptop = dict.fromkeys(specs)


def append_s(name):
    return name + 's'

def laptop_options():
    laptops_list = []
    for _ in range(46080):
        new_laptop = {}
        for spec in specs:
            key = spec
            value = random.choice(master_dict[spec + 's'])
            new_laptop[key] = value
        laptops_list.append(new_laptop)  # append a new dictionary for each laptop
    return laptops_list


def save_selected():
    selected = []

    if user_brand.get() != "None":
        selected.append(f"laptop['Brand'] == '{user_brand.get()}'")
    if user_model.get() != "None":
        selected.append(f"laptop['Model'] == '{user_model.get()}'")
    if user_cpu.get() != "None":
        selected.append(f"laptop['CPU'] == '{user_cpu.get()}'")
    if user_speed.get() != "None":
        selected.append(f"laptop['Speed'] == '{user_speed.get()}'")
    if user_ram.get() != "None":
        selected.append(f"laptop['RAM'] == '{user_ram.get()}'")
    if user_storage.get() != "None":
        selected.append(f"laptop['Storage'] == '{user_storage.get()}'")
    if user_ss.get() != "None":
        selected.append(f"laptop['Screen Size'] == '{user_ss.get()}'")
    if user_price.get() != "None":
        selected.append(f"laptop['Price'] == '{user_price.get()}'")

    query = " and ".join(selected)

    laptops_list = laptop_options()
    if query:
        filt_laptops = [laptop for laptop in laptops_list if eval(query)]
        '''
        filt_laptops = []
    for laptop in laptops_list:
        if eval(query): # basically the query won't append to "filt_laptops" list if the specification is not included in the master dict; for eg if user specifies google brand
        filt_laptops.append(laptop)
    '''
    else:
        filt_laptops = laptops_list

    tk.Label(window, text=str((len(filt_laptops))) + ' laptop(s) met your preference (Displaying 1-10)', bg="linen", fg="black", font=('Times New Roman', 13)).grid(row = (len(master_dict))+1, column = 1, sticky=tk.NSEW, columnspan = 8)

    col = 0
    for spec in specs:
        tk.Label(window, text=spec, font=('Times New Roman', 15, 'bold'), bg="linen", fg="black").grid(row=len(master_dict) + 2, column=col, padx=10, pady=10, sticky=tk.W)
        col += 1

    row = len(master_dict) + 3 
    for laptop in filt_laptops[0:10:1]:
        col = 0
        for spec in specs:
            value = laptop[spec]
            tk.Label(window, text=value, bg="linen", fg="black", font=('Times New Roman', 15)).grid(row=row, column=col, padx=10, pady=10, sticky=tk.W)
            col += 1
        row += 1


specs_new = list(map(append_s, specs)) # map is basically like for loop, but you can do it in a single line

master_dict = dict.fromkeys(specs_new)
master_dict = {
    'Brands': ['Dell', 'Asus', 'Acer', 'Lenovo', 'HP'],
    'Models': ['AAA', 'BBB', 'CCC', 'DDD'],
    'CPUs': ['Intel i5', 'Intel i7', 'AMD Ryzen'],
    'Speeds': ['2 GHz', '3 GHz', '3.15 GHz', '3.8 GHz'],
    'RAMs': ['8 GB', '16 GB', '24 GB'],
    'Storages': ['128 GB', '256 GB', '512 GB', '1 TB'],
    'Screen Sizes': ['9 in', '13.3 in', '15 in', '17 in'],
    'Prices': ['₹40000', '₹65000', '₹90000', '₹100000']
}


row = 0
for i in specs:
    tk.Label(window, text = i, bg="linen", fg="black", font=('Times New Roman', 15, 'bold')).grid(row = row, column = 0, padx=10, pady=10, sticky=tk.NSEW)
    row += 1

user_brand = tk.StringVar()
user_brand.set("None")
tk.OptionMenu(window, user_brand, *master_dict['Brands']).grid(column = 1, row = 0, padx = 10, pady = 10, sticky = tk.NSEW)

user_model = tk.StringVar()
user_model.set("None")
tk.OptionMenu(window, user_model, *master_dict['Models']).grid(column = 1, row = 1, padx = 10, pady = 10, sticky = tk.NSEW)

user_cpu = tk.StringVar()
user_cpu.set("None")
tk.OptionMenu(window, user_cpu, *master_dict['CPUs']).grid(column = 1, row = 2, padx = 10, pady = 10, sticky = tk.NSEW)

user_speed = tk.StringVar()
user_speed.set("None")
tk.OptionMenu(window, user_speed, *master_dict['Speeds']).grid(column = 1, row = 3, padx = 10, pady = 10, sticky = tk.NSEW)

user_ram = tk.StringVar()
user_ram.set("None")
tk.OptionMenu(window, user_ram, *master_dict['RAMs']).grid(column = 1, row = 4, padx = 10, pady = 10, sticky = tk.NSEW)

user_storage = tk.StringVar()
user_storage.set("None")
tk.OptionMenu(window, user_storage, *master_dict['Storages']).grid(column = 1, row = 5, padx = 10, pady = 10, sticky = tk.NSEW)

user_ss = tk.StringVar()
user_ss.set("None")
tk.OptionMenu(window, user_ss, *master_dict['Screen Sizes']).grid(column = 1, row = 6, padx = 10, pady = 10, sticky = tk.NSEW)

user_price = tk.StringVar()
user_price.set("None")
tk.OptionMenu(window, user_price, *master_dict['Prices']).grid(column = 1, row = 7, padx = 10, pady = 10, sticky = tk.NSEW)

tk.Button(window, text = "Submit", command = save_selected, bg="wheat", fg="black", font=('Times New Roman', 15, 'bold')).grid(row = len(specs), column = 0, columnspan = 2, pady = 20)

window.mainloop()