import sys

def run_script(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    exec(code)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь к файлу .dfs.")
    else:
        run_script(sys.argv[1])
