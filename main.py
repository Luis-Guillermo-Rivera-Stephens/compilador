from read_json import read_json
from excel import escribir_en_excel
import lexer_file as lex
import yacc_file as yac

columnas = {}

def main():
    # Rutas fijas de los archivos
    archivo_json = "json.json"
    archivo_excel = "resultado.xlsx"

    try:
        # Leer el JSON
        contenido_json = read_json(archivo_json)
        
        resultado = yac.parser.parse(contenido_json, lexer=lex.lexer)
        universidad = resultado['university']

        print(f"\n\n\nName: {universidad['name']}")
        escribir_en_excel(archivo_excel, "A", universidad['name'])
        print(f"Location: {universidad['location']}")
        escribir_en_excel(archivo_excel, "B", universidad['location'])
        print("Students: ")
        
        for student in universidad['students']:
            print("="*133)
            print(f"\t- {student['name']} Age: {student['age']} Email: {student['email']}")
            escribir_en_excel(archivo_excel, "D", student['id'])
            escribir_en_excel(archivo_excel, "E", student['name'])
            escribir_en_excel(archivo_excel, "F", student['age'])
            escribir_en_excel(archivo_excel, "G", student['email'])
            escribir_en_excel(archivo_excel, "H", student['enrollment_status'])

            print(f"\t- Courses per student: ")
            for course in student['courses']:
                print(f"\t\t- {course['code']} | {course['name']} | {course['grade']}")
                escribir_en_excel(archivo_excel, "M", course['code'])
                escribir_en_excel(archivo_excel, "N", course['name'])
                escribir_en_excel(archivo_excel, "O", course['grade'])

            s_address = student['address']
            print(f"\t- Address: {s_address['city']} | {s_address['postal_code']} | {s_address['street']}")
            escribir_en_excel(archivo_excel, "I", s_address['street'])
            escribir_en_excel(archivo_excel, "J", s_address['city'])
            escribir_en_excel(archivo_excel, "K", s_address['postal_code'])

        print("="*133)

    except FileNotFoundError:
        print("Error: No se encontró alguno de los archivos")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()