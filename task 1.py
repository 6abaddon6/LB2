def analyze_log_file(log_file_path):
    response_codes = {}  # словник для зберігання кількості кодів

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 9:
                    # HTTP код зазвичай на 9-ій позиції (індекс 8)
                    try:
                        code = int(parts[8])
                        response_codes[code] = response_codes.get(code, 0) + 1
                    except ValueError:
                        # Якщо код не є числом — пропускаємо
                        continue
    except FileNotFoundError:
        print(f"[Помилка] Файл не знайдено: {log_file_path}")
    except IOError:
        print(f"[Помилка] Неможливо прочитати файл: {log_file_path}")

    return response_codes

results = analyze_log_file("apache_logs.txt")
print(results)
