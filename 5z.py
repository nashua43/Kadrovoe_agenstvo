"""
Кадровое агентство
Простая программа для управления базой данных соискателей
"""

applicants = []


def load_data():
    """Загружает данные из файла в программу"""
    global applicants
    print("Пытаюсь загрузить данные из файла...")

    try:
        with open("applicants.txt", "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

        applicants = []
        for line in lines[1:]:  # пропускаем заголовок
            parts = line.split(";")
            if len(parts) >= 12:
                applicants.append({
                    "id": int(parts[0]), "last_name": parts[1], "first_name": parts[2],
                    "patronymic": parts[3], "gender": parts[4], "birth_year": int(parts[5]),
                    "birth_month": int(parts[6]), "birth_day": int(parts[7]), "specialty": parts[8],
                    "experience": float(parts[9]), "languages": parts[10], "expected_salary": int(parts[11])
                })

        print(f"Успешно загружено {len(applicants)} записей")
    except:
        print("Ошибка при загрузке файла. Создаю тестовые данные...")
        create_test_data()


def save_data():
    """Сохраняет данные из программы в файл"""
    print("Сохраняю данные в файл...")

    try:
        with open("applicants.txt", "w", encoding="utf-8") as file:
            file.write("id;фамилия;имя;отчество;пол;год;месяц;день;специальность;стаж;языки;оклад\n")
            for a in applicants:
                file.write(f"{a['id']};{a['last_name']};{a['first_name']};{a['patronymic']};")
                file.write(f"{a['gender']};{a['birth_year']};{a['birth_month']};{a['birth_day']};")
                file.write(f"{a['specialty']};{a['experience']};{a['languages']};{a['expected_salary']}\n")

        print("Данные успешно сохранены!")
    except:
        print("Ошибка при сохранении файла")


def create_test_data():
    """Создает 25 тестовых записей для демонстрации"""
    global applicants

    test_records = [
        [1, "Иванов", "Иван", "Иванович", "М", 1990, 5, 15, "Программист", 5.5, "Английский", 120000],
        [2, "Петрова", "Анна", "Сергеевна", "Ж", 1988, 3, 22, "Программист", 7.0, "Английский, Немецкий", 150000],
        [3, "Сидоров", "Алексей", "Петрович", "М", 1995, 8, 10, "Дизайнер", 3.0, "Английский", 90000],
        [4, "Кузнецова", "Елена", "Владимировна", "Ж", 1992, 11, 30, "Дизайнер", 4.5, "Английский, Французский",
         110000],
        [5, "Смирнов", "Дмитрий", "Александрович", "М", 1985, 2, 14, "Менеджер", 10.0, "Английский", 140000],
        [6, "Волкова", "Ольга", "Игоревна", "Ж", 1990, 7, 18, "Менеджер", 8.5, "Английский, Испанский", 130000],
        [7, "Васильева", "Мария", "Андреевна", "Ж", 1993, 4, 25, "Аналитик", 4.0, "Английский", 100000],
        [8, "Федоров", "Андрей", "Николаевич", "М", 1991, 12, 3, "Аналитик", 5.0, "Английский, Китайский", 115000],
        [9, "Новиков", "Павел", "Олегович", "М", 1994, 1, 8, "Дизайнер", 3.5, "Английский", 85000],
        [10, "Андреева", "Юлия", "Павловна", "Ж", 1996, 10, 12, "Дизайнер", 2.0, "Английский, Итальянский", 75000],
        [11, "Козлов", "Максим", "Сергеевич", "М", 1992, 3, 19, "Тестировщик", 4.5, "Английский", 80000],
        [12, "Лебедева", "Ирина", "Анатольевна", "Ж", 1988, 8, 21, "Тестировщик", 6.0, "Английский, Французский",
         95000],
        [13, "Семенов", "Артем", "Владимирович", "М", 1986, 2, 28, "Программист", 8.0, "Английский", 160000],
        [14, "Павлов", "Кирилл", "Игоревич", "М", 1993, 7, 14, "Маркетолог", 4.0, "Английский", 85000],
        [15, "Абрамов", "Виктор", "Степанович", "М", 1978, 4, 2, "Водитель", 15.0, "-", 60000],
        [16, "Александрова", "Галина", "Петровна", "Ж", 1980, 11, 15, "Водитель", 12.0, "-", 55000],
        [17, "Борисов", "Игорь", "Васильевич", "М", 1995, 6, 30, "Курьер", 2.0, "-", 40000],
        [18, "Антонов", "Михаил", "Юрьевич", "М", 1989, 10, 8, "Администратор", 9.0, "Английский", 110000],
        [19, "Яковлев", "Роман", "Аркадьевич", "М", 1987, 3, 17, "Программист", 8.5, "Английский", 145000],
        [20, "Морозов", "Сергей", "Викторович", "М", 1990, 9, 5, "Менеджер", 6.0, "Английский", 95000],
        [21, "Тихонова", "Екатерина", "Романовна", "Ж", 1992, 12, 24, "Администратор", 6.5, "Английский, Польский",
         105000],
        [22, "Григорьева", "Светлана", "Олеговна", "Ж", 1991, 9, 26, "Маркетолог", 5.5, "Английский, Немецкий", 95000],
        [23, "Данилова", "Людмила", "Алексеевна", "Ж", 1998, 2, 11, "Курьер", 1.0, "-", 35000],
        [24, "Егорова", "Наталья", "Викторовна", "Ж", 1990, 5, 7, "Программист", 5.5, "Английский, Испанский", 140000],
        [25, "Попов", "Александр", "Дмитриевич", "М", 1993, 11, 19, "Аналитик", 7.5, "Английский, Немецкий", 135000]
    ]

    applicants = []
    for record in test_records:
        applicants.append({
            "id": record[0], "last_name": record[1], "first_name": record[2], "patronymic": record[3],
            "gender": record[4], "birth_year": record[5], "birth_month": record[6], "birth_day": record[7],
            "specialty": record[8], "experience": record[9], "languages": record[10], "expected_salary": record[11]
        })

    print(f"Создано {len(applicants)} тестовых записей")
    save_data()


def show_all():
    """Показывает всех соискателей в базе"""
    if not applicants:
        print("База данных пуста!")
        return

    print("\n" + "=" * 120)
    print("ВСЕ СОИСКАТЕЛИ В БАЗЕ ДАННЫХ")
    print("=" * 120)

    print(
        f"{'ID':<4} {'ФИО':<30} {'Пол':<4} {'Дата рождения':<12} {'Специальность':<20} {'Стаж':<6} {'Языки':<20} {'Оклад':<10}")
    print("-" * 120)

    for a in applicants:
        date = f"{a['birth_day']:02d}.{a['birth_month']:02d}.{a['birth_year']}"
        name = f"{a['last_name']} {a['first_name'][0]}.{a['patronymic'][0]}."
        print(
            f"{a['id']:<4} {name:<30} {a['gender']:<4} {date:<12} {a['specialty']:<20} {a['experience']:<6.1f} {a['languages']:<20} {a['expected_salary']:<10}")

    print("=" * 120)
    print(f"Всего записей: {len(applicants)}")


def shaker_sort(data, key1, dir1, key2=None, dir2=False, key3=None, dir3=False):
    """Шейкерная сортировка"""
    if len(data) <= 1:
        return data.copy()

    arr = data.copy()
    n = len(arr)
    swapped = True
    left, right = 0, n - 1

    while swapped:
        swapped = False
        for i in range(left, right):
            if compare(arr[i], arr[i + 1], key1, dir1, key2, dir2, key3, dir3):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        right -= 1
        for i in range(right - 1, left - 1, -1):
            if compare(arr[i], arr[i + 1], key1, dir1, key2, dir2, key3, dir3):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        left += 1

    return arr


def compare(a, b, k1, d1, k2=None, d2=False, k3=None, d3=False):
    """Сравнение для сортировки"""
    if a[k1] != b[k1]:
        return (a[k1] > b[k1]) if not d1 else (a[k1] < b[k1])
    if k2 and a[k2] != b[k2]:
        return (a[k2] > b[k2]) if not d2 else (a[k2] < b[k2])
    if k3 and a[k3] != b[k3]:
        return (a[k3] > b[k3]) if not d3 else (a[k3] < b[k3])
    return False


def report_1():
    """Отчет 1: полный список, отсортированный по специальности и фамилии"""
    print("\n" + "=" * 60)
    print("ОТЧЕТ 1: ПОЛНЫЙ СПИСОК СОИСКАТЕЛЕЙ")
    print("=" * 60)
    print("Сортировка: специальность (А-Я), фамилия (А-Я)")

    sorted_list = shaker_sort(applicants, "specialty", False, "last_name", False)

    if not sorted_list:
        print("Нет данных для отображения")
        return

    print("\n" + "=" * 120)
    print("ОТСОРТИРОВАННЫЙ СПИСОК")
    print("=" * 120)

    print(f"{'ID':<4} {'ФИО':<30} {'Пол':<4} {'Специальность':<20} {'Стаж':<6} {'Оклад':<10}")
    print("-" * 120)

    for a in sorted_list:
        name = f"{a['last_name']} {a['first_name'][0]}.{a['patronymic'][0]}."
        print(
            f"{a['id']:<4} {name:<30} {a['gender']:<4} {a['specialty']:<20} {a['experience']:<6.1f} {a['expected_salary']:<10}")

    print("=" * 120)
    print(f"Всего записей: {len(sorted_list)}")


def report_2():
    """Отчет 2: соискатели заданной специальности"""
    print("\n" + "=" * 60)
    print("ОТЧЕТ 2: СОИСКАТЕЛИ ПО СПЕЦИАЛЬНОСТИ")
    print("=" * 60)
    print("Сортировка: стаж (больше->меньше), пол (М->Ж), фамилия (А-Я)")

    specialties = sorted(set(a["specialty"] for a in applicants))

    if not specialties:
        print("В базе нет записей")
        return

    print("\nДоступные специальности:")
    for i, spec in enumerate(specialties, 1):
        print(f"{i}. {spec}")

    choice = get_choice("\nВведите номер специальности (или 0 для отмены): ", 0, len(specialties))
    if choice == 0:
        print("Операция отменена.")
        return

    spec = specialties[choice - 1]
    filtered = [a for a in applicants if a["specialty"] == spec]

    if not filtered:
        print(f"\nНет соискателей со специальностью '{spec}'")
        return

    sorted_list = shaker_sort(filtered, "experience", True, "gender", True, "last_name", False)

    print(f"\n" + "=" * 120)
    print(f"СОИСКАТЕЛИ СПЕЦИАЛЬНОСТИ: {spec.upper()}")
    print("=" * 120)

    print(f"{'ID':<4} {'ФИО':<30} {'Пол':<4} {'Стаж':<6} {'Языки':<20} {'Оклад':<10}")
    print("-" * 120)

    for a in sorted_list:
        name = f"{a['last_name']} {a['first_name'][0]}.{a['patronymic'][0]}."
        print(
            f"{a['id']:<4} {name:<30} {a['gender']:<4} {a['experience']:<6.1f} {a['languages']:<20} {a['expected_salary']:<10}")

    print("=" * 120)
    print(f"Найдено записей: {len(sorted_list)}")


def report_3():
    """Отчет 3: соискатели с окладом в заданном диапазоне"""
    print("\n" + "=" * 60)
    print("ОТЧЕТ 3: СОИСКАТЕЛИ ПО ДИАПАЗОНУ ОКЛАДА")
    print("=" * 60)
    print("Сортировка: оклад (больше->меньше), фамилия (А-Я)")

    min_s = get_int("Введите минимальный оклад (или 0 для отмены): ", 0)
    if min_s == 0:
        print("Операция отменена.")
        return

    max_s = get_int("Введите максимальный оклад: ", min_s)
    if max_s == 0:
        print("Операция отменена.")
        return

    filtered = [a for a in applicants if min_s <= a["expected_salary"] <= max_s]

    if not filtered:
        print(f"\nНет соискателей с окладом от {min_s} до {max_s}")
        return

    sorted_list = shaker_sort(filtered, "expected_salary", True, "last_name", False)

    print(f"\n" + "=" * 120)
    print(f"СОИСКАТЕЛИ С ОКЛАДОМ ОТ {min_s} ДО {max_s}")
    print("=" * 120)

    print(f"{'ID':<4} {'ФИО':<30} {'Пол':<4} {'Специальность':<20} {'Стаж':<6} {'Оклад':<10}")
    print("-" * 120)

    for a in sorted_list:
        name = f"{a['last_name']} {a['first_name'][0]}.{a['patronymic'][0]}."
        print(
            f"{a['id']:<4} {name:<30} {a['gender']:<4} {a['specialty']:<20} {a['experience']:<6.1f} {a['expected_salary']:<10}")

    print("=" * 120)
    print(f"Найдено записей: {len(sorted_list)}")


def get_choice(prompt, min_val, max_val):
    """Получение выбора пользователя"""
    while True:
        try:
            val = int(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"Введите число от {min_val} до {max_val}")
        except ValueError:
            print("Ошибка ввода! Введите число.")


def get_int(prompt, min_val=0):
    """Получение целого числа (без максимального ограничения)"""
    while True:
        try:
            val = int(input(prompt).strip())
            if val >= min_val:
                return val
            print(f"Введите число не менее {min_val}")
        except ValueError:
            print("Ошибка ввода! Введите целое число.")


def get_float(prompt, min_val=0, max_val=60):
    """Получение дробного числа"""
    while True:
        try:
            val = float(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"Введите число от {min_val} до {max_val}")
        except ValueError:
            print("Ошибка ввода! Введите число.")


def validate_name(name):
    """Проверка имени, фамилии, отчества"""
    return bool(name) and all(c.isalpha() or c == '-' for c in name)


def validate_day(day, month, year):
    """Проверка корректности дня с учетом месяца и года"""
    days_in_month = [31, 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
                     31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= day <= days_in_month[month - 1]


def add_applicant():
    """Добавляет нового соискателя в базу"""
    print("\n" + "=" * 60)
    print("ДОБАВЛЕНИЕ НОВОГО СОИСКАТЕЛЯ")
    print("=" * 60)

    new_id = max((a["id"] for a in applicants), default=0) + 1
    print(f"ID нового соискателя: {new_id}")
    print("\nЗаполните данные о соискателе:")
    print("=" * 40)

    # Ввод данных с проверками
    while True:
        last_name = input("Фамилия: ").strip()
        if validate_name(last_name):
            break
        print("Фамилия должна содержать только буквы и дефисы! Попробуйте еще раз.")

    while True:
        first_name = input("Имя: ").strip()
        if validate_name(first_name):
            break
        print("Имя должно содержать только буквы и дефисы! Попробуйте еще раз.")

    while True:
        patronymic = input("Отчество: ").strip()
        if validate_name(patronymic):
            break
        print("Отчество должно содержать только буквы и дефисы! Попробуйте еще раз.")

    while True:
        gender = input("Пол (М или Ж): ").strip().upper()
        if gender in ["М", "Ж"]:
            break
        print("Пол должен быть 'М' или 'Ж' Попробуйте еще раз.!")

    # Год рождения с ограничением 1900-2024
    birth_year = get_int("Год рождения (1900-2024): ", 1900)
    while birth_year > 2024:
        print("Год рождения не может быть больше 2024! Попробуйте еще раз.")
        birth_year = get_int("Год рождения (1900-2024): ", 1900)

    # Месяц рождения с ограничением 1-12
    birth_month = get_int("Месяц рождения (1-12): ", 1)
    while birth_month > 12:
        print("Месяц рождения не может быть больше 12! Попробуйте еще раз.")
        birth_month = get_int("Месяц рождения (1-12): ", 1)

    # День рождения с проверкой корректности
    while True:
        birth_day = get_int("День рождения (1-31): ", 1)
        while birth_day > 31:
            print("День рождения не может быть больше 31! Попробуйте еще раз.")
            birth_day = get_int("День рождения (1-31): ", 1)

        if validate_day(birth_day, birth_month, birth_year):
            break
        print("Такого дня нет в указанном месяце и году! Попробуйте еще раз.")

    specialty = input("Специальность: ").strip()
    while not specialty:
        print("Специальность не может быть пустой! Попробуйте еще раз.")
        specialty = input("Специальность: ").strip()

    # Стаж с ограничением 0-60
    experience = get_float("Стаж работы (лет, 0-60): ", 0, 60)

    languages = input("Иностранные языки (через запятую, Enter если нет): ").strip() or "-"

    # Оклад без максимального ограничения, только минимум 10000
    salary = get_int("Ожидаемый оклад (руб., минимум 10000): ", 10000)

    # Создаем новую запись
    applicants.append({
        "id": new_id, "last_name": last_name, "first_name": first_name,
        "patronymic": patronymic, "gender": gender, "birth_year": birth_year,
        "birth_month": birth_month, "birth_day": birth_day, "specialty": specialty,
        "experience": experience, "languages": languages, "expected_salary": salary
    })

    print("\n" + "=" * 60)
    print(f"Соискатель {last_name} {first_name} {patronymic} успешно добавлен!")
    print(f"Его ID: {new_id}")
    print("=" * 60)


def delete_applicant():
    """Удаляет соискателя по ID"""
    if not applicants:
        print("База данных пуста!")
        return

    print("\n" + "=" * 60)
    print("УДАЛЕНИЕ СОИСКАТЕЛЯ")
    print("=" * 60)

    show_all()

    try:
        id_to_delete = int(input("\nВведите ID соискателя для удаления (или 0 для отмены): ").strip())
        if id_to_delete == 0:
            print("Операция отменена.")
            return
        if id_to_delete < 1:
            print("ID должен быть положительным числом!")
            return
    except:
        print("Ошибка ввода!")
        return

    # Ищем соискателя
    for i, a in enumerate(applicants):
        if a["id"] == id_to_delete:
            print(f"\nВы хотите удалить соискателя:")
            print(f"ID: {a['id']}, ФИО: {a['last_name']} {a['first_name']} {a['patronymic']}")
            print(f"Специальность: {a['specialty']}")

            confirm = input("\nУдалить? (да/нет): ").strip().lower()
            if confirm in ["да", "д", "yes", "y"]:
                applicants.pop(i)
                print("Соискатель удален!")
            else:
                print("Удаление отменено.")
            return

    print(f"Соискатель с ID {id_to_delete} не найден!")


def edit_applicant():
    """Редактирует данные существующего соискателя"""
    if not applicants:
        print("База данных пуста!")
        return

    print("\n" + "=" * 60)
    print("РЕДАКТИРОВАНИЕ ДАННЫХ СОИСКАТЕЛЯ")
    print("=" * 60)

    show_all()

    try:
        id_to_edit = int(input("\nВведите ID соискателя для редактирования (или 0 для отмены): ").strip())
        if id_to_edit == 0:
            print("Редактирование отменено.")
            return
        if id_to_edit < 1:
            print("ID должен быть положительным числом!")
            return
    except:
        print("Ошибка ввода!")
        return

    # Ищем соискателя
    applicant = None
    for a in applicants:
        if a["id"] == id_to_edit:
            applicant = a
            break

    if not applicant:
        print(f"Соискатель с ID {id_to_edit} не найден! Попробуйте еще раз.")
        return

    # Показываем текущие данные
    print(f"\nТекущие данные соискателя ID {id_to_edit}:")
    print(f"1. Фамилия: {applicant['last_name']}")
    print(f"2. Имя: {applicant['first_name']}")
    print(f"3. Отчество: {applicant['patronymic']}")
    print(f"4. Пол: {applicant['gender']}")
    print(f"5. Дата рождения: {applicant['birth_day']:02d}.{applicant['birth_month']:02d}.{applicant['birth_year']}")
    print(f"6. Специальность: {applicant['specialty']}")
    print(f"7. Стаж: {applicant['experience']}")
    print(f"8. Языки: {applicant['languages']}")
    print(f"9. Оклад: {applicant['expected_salary']}")

    try:
        choice = int(input("\nВыберите поле для редактирования (1-9, 0 - отмена): ").strip())
        if choice == 0:
            print("Редактирование отменено.")
            return
        if choice < 1 or choice > 9:
            print("Неверный выбор! Введите число от 1 до 9.")
            return
    except:
        print("Ошибка ввода!")
        return

    # Редактирование выбранного поля
    if choice == 1:
        while True:
            new_val = input("Новая фамилия: ").strip()
            if validate_name(new_val):
                applicant['last_name'] = new_val
                break
            print("Фамилия должна содержать только буквы и дефисы! Попробуйте еще раз.")

    elif choice == 2:
        while True:
            new_val = input("Новое имя: ").strip()
            if validate_name(new_val):
                applicant['first_name'] = new_val
                break
            print("Имя должно содержать только буквы и дефисы! Попробуйте еще раз.")

    elif choice == 3:
        while True:
            new_val = input("Новое отчество: ").strip()
            if validate_name(new_val):
                applicant['patronymic'] = new_val
                break
            print("Отчество должно содержать только буквы и дефисы! Попробуйте еще раз.")

    elif choice == 4:
        while True:
            new_val = input("Пол (М или Ж): ").strip().upper()
            if new_val in ["М", "Ж"]:
                applicant['gender'] = new_val
                break
            print("Пол должен быть 'М' или 'Ж'! Попробуйте еще раз.")

    elif choice == 5:
        applicant['birth_year'] = get_int("Год рождения: ", 1900)
        while applicant['birth_year'] > 2024:
            print("Год рождения не может быть больше 2024! Попробуйте еще раз.")
            applicant['birth_year'] = get_int("Год рождения: ", 1900)

        applicant['birth_month'] = get_int("Месяц рождения: ", 1)
        while applicant['birth_month'] > 12:
            print("Месяц рождения не может быть больше 12! Попробуйте еще раз.")
            applicant['birth_month'] = get_int("Месяц рождения: ", 1)

        while True:
            applicant['birth_day'] = get_int("День рождения: ", 1)
            while applicant['birth_day'] > 31:
                print("День рождения не может быть больше 31! Попробуйте еще раз.")
                applicant['birth_day'] = get_int("День рождения: ", 1)

            if validate_day(applicant['birth_day'], applicant['birth_month'], applicant['birth_year']):
                break
            print("Такого дня нет в указанном месяце и году! Попробуйте еще раз.")

    elif choice == 6:
        new_val = input("Специальность: ").strip()
        while not new_val:
            print("Специальность не может быть пустой! Попробуйте еще раз.")
            new_val = input("Специальность: ").strip()
        applicant['specialty'] = new_val

    elif choice == 7:
        applicant['experience'] = get_float("Стаж работы (0-60): ", 0, 60)

    elif choice == 8:
        new_val = input("Языки: ").strip()
        applicant['languages'] = new_val or "-"

    elif choice == 9:
        applicant['expected_salary'] = get_int("Оклад (минимум 10000): ", 10000)

    print(f"\nДанные соискателя ID {id_to_edit} успешно обновлены!")


def main_menu():
    """Главное меню программы"""
    print("\n" + "=" * 60)
    print("КАДРОВОЕ АГЕНТСТВО - ГЛАВНОЕ МЕНЮ")
    print("=" * 60)

    load_data()

    while True:
        print("\n" + "=" * 60)
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("=" * 60)
        print("1. Показать всех соискателей")
        print("2. Отчет 1: Полный список (специальность, фамилия)")
        print("3. Отчет 2: По специальности (стаж, пол, фамилия)")
        print("4. Отчет 3: По диапазону оклада (оклад, фамилия)")
        print("5. Добавить нового соискателя")
        print("6. Редактировать данные соискателя")
        print("7. Удалить соискателя")
        print("8. Сохранить данные")
        print("0. Выйти из программы")
        print("=" * 60)

        choice = input("Ваш выбор (0-8): ").strip()

        if choice == "0":
            save_choice = input("Сохранить изменения перед выходом? (да/нет): ").lower()
            if save_choice in ["да", "д", "yes", "y"]:
                save_data()
            print("Спасибо за использование программы! До свидания!")
            break

        actions = {
            "1": show_all, "2": report_1, "3": report_2, "4": report_3,
            "5": add_applicant, "6": edit_applicant, "7": delete_applicant, "8": save_data
        }

        if choice in actions:
            actions[choice]()
        else:
            print("Неверный выбор! Введите число от 0 до 8.")

        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    print("Добро пожаловать в программу 'Кадровое агентство'!")
    main_menu()