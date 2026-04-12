env_file_content = """
# Настройки базы данных
DB_HOST=192.168.1.100
DB_PORT=5432
DB_USER=admin

# Настройки кэша
REDIS_HOST=10.0.0.5

# Прочее
DEBUG=True
"""

# Список параметров, которые ОБЯЗАТЕЛЬНО должны быть в конфиге для запуска:
required_keys = ["DB_HOST", "DB_USER", "DB_PASSWORD", "SECRET_KEY"]

# ==================================MAIN======================================
def check_required_keys(file_content, required_keys):
    cleaned_lines = [
        line
        for line in file_content.splitlines()
        if line.strip() and not line.startswith("#")
    ]  # Очищаем файл от мусора и складываем в список

    clean_lst = []
    for elements in cleaned_lines:
        result = elements.split("=")
        clean_lst.append(result[0].strip())  # Достаем ключи до знака "="
    missing_keys = set(required_keys) - set(clean_lst)    # Проверяем недостающие и кладем в список
    return missing_keys

def main():
    result = check_required_keys(env_file_content, required_keys)
    if result:
        print(
            "Ошибка валидации! В конфиге отсутствуют обязательные параметры:",
            *result,
            sep="\n- "
        )
    else:
        print("Конфиг валиден. Приложение готово к запуску!")

if __name__ == "__main__":
    main()  #запуск функции
"end"