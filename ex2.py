from pprint import pprint
def get_cats_info(path):
    list=[]
    try:
        with open(path, "r") as file:
            for line in file:
                data=line.strip().split(",")
                list.append({
                    "id":data[0],
                    "name":data[1],
                    "age":data[2]
                })
        return list
    except FileExistsError:
        print("Файл не знайдено")
    except Exception as e:
        print("Помилка: ",e)
pprint(get_cats_info("my_text.txt"))
