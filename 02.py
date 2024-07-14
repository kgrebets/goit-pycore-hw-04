def get_cats_info(path):
    try:
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    id, name, age_str = parts
                    age = int(age_str)
                    cats_info.append({"id": id, "name": name, "age": age})
                else:
                    raise Exception("Not valid data in file")
        return cats_info
          
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

path = r"d:\Projects\Neoversity\home task 4\data_02.txt"
cats = get_cats_info(path)
if cats != None:
    for cat in cats:
        print(cat)