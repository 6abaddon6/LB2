import hashlib

def generate_file_hashes(*file_paths):
    hashes = {}  # словник для збереження хешів

    for path in file_paths:
        try:
            with open(path, 'rb') as f:
                file_data = f.read()
                sha256_hash = hashlib.sha256(file_data).hexdigest()
                hashes[path] = sha256_hash
        except FileNotFoundError:
            print(f"[Помилка] Файл не знайдено: {path}")
        except IOError:
            print(f"[Помилка] Помилка читання файлу: {path}")

    return hashes

results = generate_file_hashes("file1.txt", "image.jpg", "data.csv")
for path, hash_value in results.items():
    print(f"{path}: {hash_value}")
