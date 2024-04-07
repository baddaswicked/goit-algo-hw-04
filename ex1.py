def total_salary(path):
    try:
        with open(path,"r") as file:
            lst=[]
            for line in file:
                name,salary=line.split(",")
                lst.append(int(salary))

        return (sum(lst), sum(lst)//len(lst))
    except FileExistsError:
        print("Файл не знайдено")
    except Exception as e:
        print("Помилка: ",e)
# print(total_salary("my_text.txt"))
total, average = total_salary("my_text1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")






