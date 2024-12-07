# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.

import subprocess
import string


def Check_search(command:str, text:str, mode:str = 'words'):

    try:
        result = subprocess.run(command.split(), text=True, capture_output=True, encoding='UTF-8')
        if result.returncode==0:
            if mode == 'words':
                words = result.stdout.translate(str.maketrans('', '', string.punctuation)).split()
                return text in words
            elif mode == 'substring':
                return text in result.stdout
        return False
    except subprocess.SubprocessError:
        return False

if __name__ == "__main__":
    command = "echo 'Some text to be searched'"
    text = "be"
    mode = 'words'
    print(Check_search(command, text, mode))
    command = "echo 'Some text to be searched'"
    text = "be"
    mode = 'substring'
    print(Check_search(command, text, mode))