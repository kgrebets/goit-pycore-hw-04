def total(path):
    try:
        salaries = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    salary = float(parts[1])
                    salaries.append(salary)
                else:
                    raise Exception("Not valid data in file")
            
            total = sum(salaries)
            average = total / len(salaries)
            return (total, average)
        
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

path = r"d:\Projects\Neoversity\home task 4\data_01.txt"
(total, average) = total(path)
if total != None and average != None:
    print(f"Загальна сума заробітної плати: {total}\nСередня заробітна плата: {average}")
