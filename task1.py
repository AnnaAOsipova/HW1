# Задание 1.
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
# и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess


def Check_search(command:str, text:str):

    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, encoding='UTF-8')
        if result.returncode==0:
            return text in result.stdout
    except subprocess.SubprocessError:
        return False

if __name__ == "__main__":
    command = "echo 'Some text to be searched'"
    text = "be"
    print(Check_search(command, text))
