import csv
import datetime
import os

# Global data storage
member_data = {}
role_data = {Professional Engineer [], Design Engineer [], Test Engineer []}
wages = {Professional Engineer 25, Design Engineer 65, Test Engineer 100}

# ...

def save_csv(filename)
    try
        with open(filename, 'w', newline='') as csvfile
            fieldnames = ['Name', 'Clock In Time', 'Clock Out Time', 'Role', 'Shift Duration', 'Wages Owed']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for name, data in member_data.items()
                row = {'Name' name,
                       'Clock In Time' data.get('clock_in', ''),
                       'Clock Out Time' data.get('clock_out', ''),
                       'Role' data.get('role', ''),
                       'Shift Duration' data.get('shift_duration', ''),
                       'Wages Owed' data.get('owed_wages', '')}
                writer.writerow(row)
        print(fData successfully saved to {filename}.)
    except Exception as e
        print(fAn error occurred while trying to save to {filename} {e})

def load_csv(filename)
    if not os.path.exists(filename)
        print(fThe file {filename} does not exist.)
        return

    try
        with open(filename, 'r', newline='') as csvfile
            reader = csv.DictReader(csvfile)
            for row in reader
                name = row['Name']
                member_data[name] = {'clock_in' datetime.datetime.fromisoformat(row['Clock In Time']) if row['Clock In Time'] else None,
                                     'clock_out' datetime.datetime.fromisoformat(row['Clock Out Time']) if row['Clock Out Time'] else None,
                                     'role' row['Role'],
                                     'shift_duration' datetime.timedelta(seconds=float(row['Shift Duration'].total_seconds())) if row['Shift Duration'] else None,
                                     'owed_wages' float(row['Wages Owed']) if row['Wages Owed'] else None}
        print(fData successfully loaded from {filename}.)
    except Exception as e
        print(fAn error occurred while trying to read {filename} {e})

# ...

def clock_in()
    # User input and text formatting
    name = input(Enter your first and last name )
    name = name.title()
    role = input(Choose your role (Professional Engineer, Design Engineer, Test Engineer) )

    # Clock-in time and data storage
    now = datetime.datetime.now()
    member_data[name] = {clock_in now, role role}

def clock_out()
    name = input(Enter your first and last name )
    name = name.title()

    # Calculate shift duration and wages
    now = datetime.datetime.now()
    shift_duration = now - member_data[name][clock_in]
    owed_wages = shift_duration.total_seconds()  3600  wages[member_data[name][role]]

    # Update data storage
    member_data[name][clock_out] = now
    member_data[name][shift_duration] = shift_duration
    member_data[name][owed_wages] = owed_wages

def clock_out_all()
    for name in member_data
        if clock_out not in member_data[name]
            now = datetime.datetime.now()
            shift_duration = now - member_data[name][clock_in]
            owed_wages = shift_duration.total_seconds()  3600  wages[member_data[name][role]]
            member_data[name][clock_out] = now
            member_data[name][shift_duration] = shift_duration
            member_data[name][owed_wages] = owed_wages

def clock_in_check()
    for name, data in member_data.items()
        if clock_out not in data
            print(f{name} is clocked in as {data['role']}.)

def sum_wages()
    total_wages = 0
    for name, data in member_data.items()
        if owed_wages in data
            total_wages += data[owed_wages]
    print(fTotal wages owed {total_wages})

# Initial prompt for new or existing payroll
new_payroll = input(New Payroll (yn) )

if new_payroll.lower() == 'n'
    csv_file = input(Enter the CSV file to load )
    load_csv(csv_file)

while True
    action = input(What would you like to do (For full list of options, type 'show_opt') )

    if action == clock_in
        clock_in()
    elif action == clock_out
        clock_out()
    elif action == show_opt
        print(Available options clock_in, clock_out, clock_out_all, clock_in_check, sum_wages)
    elif action == clock_out_all
        clock_out_all()
    elif action == clock_in_check
        clock_in_check()
    elif action == sum_wages
        sum_wages()
    elif action == quit
        save_csv(csv_file if new_payroll.lower() == 'n' else input(Enter the new CSV file name ))
        break



import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def gui_clock_in()
    name = name_entry.get()
    name = name.title()
    role = role_combo.get()
    now = datetime.datetime.now()
    member_data[name] = {clock_in now, role role}

def gui_clock_out()
    name = name_entry.get()
    name = name.title()
    now = datetime.datetime.now()
    shift_duration = now - member_data[name][clock_in]
    owed_wages = shift_duration.total_seconds()  3600  wages[member_data[name][role]]
    member_data[name][clock_out] = now
    member_data[name][shift_duration] = shift_duration
    member_data[name][owed_wages] = owed_wages

def gui_clock_out_all()
    clock_out_all()

def gui_clock_in_check()
    clock_in_check()

def gui_sum_wages()
    sum_wages()

def load_csv_file()
    file_path = filedialog.askopenfilename()
    load_csv(file_path)

def save_csv_file()
    file_path = filedialog.asksaveasfilename(defaultextension=.csv)
    save_csv(file_path)

# Tkinter Setup
root = tk.Tk()
root.title(Payroll)

# Widgets
name_label = tk.Label(root, text=Name)
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

role_label = tk.Label(root, text=Role)
role_label.grid(row=1, column=0)
role_combo = ttk.Combobox(root, values=list(wages.keys()))
role_combo.grid(row=1, column=1)

clock_in_button = tk.Button(root, text=Clock In, command=gui_clock_in)
clock_in_button.grid(row=2, column=0)

clock_out_button = tk.Button(root, text=Clock Out, command=gui_clock_out)
clock_out_button.grid(row=2, column=1)

clock_out_all_button = tk.Button(root, text=Clock Out All, command=gui_clock_out_all)
clock_out_all_button.grid(row=3, column=0)

clock_in_check_button = tk.Button(root, text=Clock In Check, command=gui_clock_in_check)
clock_in_check_button.grid(row=3, column=1)

sum_wages_button = tk.Button(root, text=Sum Wages, command=gui_sum_wages)
sum_wages_button.grid(row=4, column=0)

load_csv_button = tk.Button(root, text=Load CSV, command=load_csv_file)
load_csv_button.grid(row=5, column=0)

save_csv_button = tk.Button(root, text=Save CSV, command=save_csv_file)
save_csv_button.grid(row=5, column=1)

root.mainloop()

