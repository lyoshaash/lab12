import tkinter as tk
from tkinter import messagebox
from my_calculator_package.calculations import calculate_volume, calculate_heat_power
from my_calculator_package.docx_saver import save_results_to_docx

def create_gui():
    root = tk.Tk()
    root.title("Калькулятор тепловой мощности")
    root.geometry("400x400")

    def calculate_and_display():
        length = float(length_entry.get())
        width = float(width_entry.get())
        height = float(height_entry.get())
        num_apartments = float(num_apartments_entry.get() or 1)
        num_floors = float(num_floors_entry.get() or 1)

        volume = calculate_volume(length, width, height, num_apartments, num_floors)
        volume_label.config(text=f"Объем помещения: {volume:.2f} куб. м")

        heat_power = calculate_heat_power(volume)
        heat_power_label.config(text=f"Тепловая мощность для обогрева помещения: {heat_power:.2f} кВт")

    def save_results():
        length = float(length_entry.get())
        width = float(width_entry.get())
        height = float(height_entry.get())
        num_apartments = float(num_apartments_entry.get() or 1)
        num_floors = float(num_floors_entry.get() or 1)

        volume = calculate_volume(length, width, height, num_apartments, num_floors)
        heat_power = calculate_heat_power(volume)

        save_results_to_docx(length, width, height, num_apartments, num_floors, volume, heat_power)
        messagebox.showinfo("Сохранение", "Результаты успешно сохранены в файл 'Результаты расчетов.docx'")

    length_label = tk.Label(root, text="Длина комнаты:")
    length_label.pack()
    length_entry = tk.Entry(root)
    length_entry.pack()

    width_label = tk.Label(root, text="Ширина комнаты:")
    width_label.pack()
    width_entry = tk.Entry(root)
    width_entry.pack()

    height_label = tk.Label(root, text="Высота комнаты:")
    height_label.pack()
    height_entry = tk.Entry(root)
    height_entry.pack()

    num_apartments_label = tk.Label(root, text="Количество квартир (необязательно):")
    num_apartments_label.pack()
    num_apartments_entry = tk.Entry(root)
    num_apartments_entry.pack()

    num_floors_label = tk.Label(root, text="Количество этажей (необязательно):")
    num_floors_label.pack()
    num_floors_entry = tk.Entry(root)
    num_floors_entry.pack()

    calculate_button = tk.Button(root, text="Рассчитать", command=calculate_and_display)
    calculate_button.pack()

    save_button = tk.Button(root, text="Сохранить в DOCX", command=save_results)
    save_button.pack()

    volume_label = tk.Label(root, text="")
    volume_label.pack()

    heat_power_label = tk.Label(root, text="")
    heat_power_label.pack()

    root.mainloop()
