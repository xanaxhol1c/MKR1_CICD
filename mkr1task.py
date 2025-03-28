def read_population_data(filename):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    country = parts[0].strip()
                    try:
                        area = float(parts[1].strip())
                        population = int(parts[2].strip())
                        data.append((country, area, population))
                    except ValueError:
                        print(f"Reading error on: {line}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return data

if __name__ == "__main__":
    filename = input("Enter file name: ")
    population_data = read_population_data(filename)
    



