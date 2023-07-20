import csv
import datetime

def read_car_data(filename):
    cars = []
    with open(filename, newline='') as file:
        csv_reader = csv.reader(file)

        try:
            header = next(csv_reader)
            if header != ['numeris', 'gamintojas', 'modelis', 'metai']:
                raise ValueError("Invalid header format in the CSV file.")
        except StopIteration:
            raise ValueError("CSV file is empty or does not have a header row.")

        for row in csv_reader:
            if len(row) != 4:
                print(f"Invalid row format: {row}. Skipping this row.")
                continue

            numeris, gamintojas, modelis, metai = row
            metai = int(metai)
            car = {'numeris': numeris, 'gamintojas': gamintojas, 'modelis': modelis, 'metai': metai}
            cars.append(car)

    return cars

def find_manufacturers_with_more_than_one_car(cars):
    manufacturers = [car['gamintojas'] for car in cars]
    return set(manufacturer for manufacturer in manufacturers if manufacturers.count(manufacturer) > 1)

def find_cars_by_manufacturer(cars, selected_manufacturer):
    return [car for car in cars if car['gamintojas'] == selected_manufacturer]

def find_older_than_10_years(cars):
    current_year = datetime.datetime.now().year
    return [car for car in cars if current_year - car['metai'] > 10]

def write_cars_to_file(cars, filename):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['numeris', 'gamintojas', 'modelis', 'metai']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cars)

filename = "autoparkas.csv"
cars = read_car_data(filename)

# 1. Raskite, kurių gamintojų automobilių yra daugiau nei vienas, ekrane atspausdinkite gamintojų pavadinimus.
# (Atspausdinkite ir kiekį - NEBŪTINA)
multiple_cars_manufacturers = find_manufacturers_with_more_than_one_car(cars)
print("Manufacturers with more than one car:", multiple_cars_manufacturers)
print('-------------------------------------------------------------')

# 2. Sudarykite visų pasirinkto gamintojo (pvz.: „Volvo“) automobilių sąrašą, ekrane atspausdinkite
# automobilio valstybinį numerį, modelį, bei pagaminimo metus.
# Jei tokio automobilio sąraše nėra atspausdinkite pranešimą - "Tokio gamintojo automobilių sąraše nėra".
selected_manufacturer = "Volkswagen"
selected_manufacturer_cars = find_cars_by_manufacturer(cars, selected_manufacturer)
if selected_manufacturer_cars:
    print(f"Cars of {selected_manufacturer}:")
    for car in selected_manufacturer_cars:
        print(f"Numeris: {car['numeris']}, Modelis: {car['modelis']}, Metai: {car['metai']}")
else:
    print(f"Cars of {selected_manufacturer} not found.")
print('-------------------------------------------------------------')

# 3. Sudarykite sąrašą, senesnių nei 10 metų, į failą „Senienos.csv“ surašykite visus jų duomenis.
older_than_10_years = find_older_than_10_years(cars)
if older_than_10_years:
    write_cars_to_file(older_than_10_years, "Senienos.csv")
else:
    print("Senesnių nei 10 metų automobilių sąraše nėra.")
