def calculate_volume(length, width, height, num_apartments=1, num_floors=1):
    return length * width * height * num_apartments * num_floors

def calculate_heat_power(volume):
    return volume * 0.07
