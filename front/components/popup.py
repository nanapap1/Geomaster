import subprocess

class Popup:

    @staticmethod
    def show(game):
        script = 'tell application "System Events" to return button returned of (display dialog "Вы уверены, что хотите пропустить задание?" buttons {"Нет", "Да"})'
        result = subprocess.check_output(['osascript', '-e', script], text=True)
        if result== "Да\n":
            return True
        return False

    @staticmethod
    def wrongauth():
        script = 'tell application "System Events" to return button returned of (display dialog "Проверьте учетные данные" buttons {"Ок"})'
        subprocess.call(['osascript', '-e', script])

    @staticmethod
    def unequal():
        script = 'tell application "System Events" to return button returned of (display dialog "Поля заполнены неккоректно" buttons {"Ок"})'
        subprocess.call(['osascript', '-e', script])

    @staticmethod
    def exists():
        script = 'tell application "System Events" to return button returned of (display dialog "Такой логин уже существует" buttons {"Ок"})'
        subprocess.call(['osascript', '-e', script])

    @staticmethod
    def error():
        script = 'tell application "System Events" to return button returned of (display dialog "Возникла ошибка. Попробуйте позже" buttons {"Ок"})'
        subprocess.call(['osascript', '-e', script])

    @staticmethod
    def wrongpass():
        script = 'tell application "System Events" to return button returned of (display dialog "Вы указали неверный пароль" buttons {"Ок"})'
        subprocess.call(['osascript', '-e', script])

    @staticmethod
    def add():
        script = 'tell application "System Events" to return button returned of (display dialog "Заполните все поля" buttons {"Ок"})'
        subprocess.call(['osascript', '-e', script])

    @staticmethod
    def fine():
        script = 'tell application "System Events" to return button returned of (display dialog "Пароль успешно изменен" buttons {"Ок"})'
        subprocess.call(['osascript', '-e', script])

