
class Building:
    total = 0  # Атрибут для отслеживания количества созданных объектов

    def __init__(self):
        Building.total += 1  # Увеличиваю атрибут total при создании объекта

    def __str__(self):
        return f"Объект {Building.total}"  # Переопределяю метод __str__ для удобного вывода объектов

# Создаю 40 объектов класса Building
buildings = [Building() for _ in range(40)]

# Вывожу все объекты на экран
for i, building in enumerate(buildings):
    print(f"{i+1}. {building}")  # для удобства вывел номер объекта и сам объект