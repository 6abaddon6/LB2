import re

def filter_ips(input_file_path, output_file_path):
    ip_counts = {}

    try:
        with open(input_file_path, 'r') as infile:
            for line in infile:
                # Знаходимо IP-адресу на початку рядка
                match = re.match(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
                if match:
                    ip = match.group(1)
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1

        # Запис результатів у файл
        with open(output_file_path, 'w') as outfile:
            for ip, count in ip_counts.items():
                outfile.write(f"{ip} - {count}\n")

    except FileNotFoundError:
        print(f"[Помилка] Файл не знайдено: {input_file_path}")
    except IOError as e:
        print(f"[Помилка] Помилка читання/запису: {e}")

filter_ips("apache_logs.txt", "output_ips.txt")
