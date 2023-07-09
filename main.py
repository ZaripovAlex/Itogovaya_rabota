import db



class Counter():
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return True
        else:
            return False


class Animal:
    def __init__(self, type, name, commands, birthday):
        self.type = type
        self.name = name
        self.commands = commands
        self.birthday = birthday

    def to_dict(self):
        return [self.name, self.commands, self.birthday]


def add_record(table):
    while True:
        with Counter() as count:
            print("Введите данные для новой записи, разделенные пробелом:")
            data = input().split()

            if len(data) < 4:
                print("Недостаточно данных для создания записи.")
                if table == 1:
                    with Counter() as counter:
                        counter.add()
                    animal = Animal(type=data[0], name=data[1], commands=data[2], birthday=data[3])
                    animal_data = (animal.name, animal.commands, animal.birthday)
                    db.insert_record(table=table, data=animal_data)
                    print("Запись успешно добавлена")
                else:
                    print("Выбрана некорректная таблица")

                break


def show_main_menu():
    print("Выберите действие:")
    print("1. Добавить запись")
    print("2. Удалить запись")
    print("3. Просмотреть записи")
    print("4. Поиск")
    print("5. Выход")

    return int(input("Ваш выбор: "))


def show_tables_menu():
    print("Выберите таблицу:")
    print("1. Домашние животные")
    print("2. Животные фермы")
    return int(input("Ваш выбор: "))


def main():

    db.create_tables()
    while True:
        choice = show_main_menu()
        if choice == 1:
            while True:
                table_choice = show_tables_menu()
                if table_choice == 1:
                    add_record(1)
                if table_choice == 2:
                    add_record(2)
                    break

        if choice == 2:
            table = show_tables_menu()
            id = int(input("Введите номер записи для удаления: "))
            db.delete_record(table, id)
        if choice == 3:
            table = show_tables_menu()
            db.view_records(table)
        if choice == 4:
            table = show_tables_menu()
            term = input("Введите строку поиска: ")
            db.search_records(table, term)
        if choice == 5:
            break



if __name__ == '__main__':
    main()