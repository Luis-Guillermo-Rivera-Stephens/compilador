def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_string = file.read()
        return json_string
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
