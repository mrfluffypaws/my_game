"""Игра угадай число
Компьютер сам загадывает и сам угадывает число 
и находит число менее чем за 20 попыток
"""


import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """Какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    max_number = 100
    min_number = 0

    while True:
        count += 1
        predict_number = (max_number + min_number) // 2

        if predict_number == number:
            break  
        elif predict_number > number:
            max_number = predict_number - 1
        else:
            min_number = predict_number + 1
    

    return count

print('Run benchmarking for game_core_v3: ', end='')


if __name__ == '__main__':
    score_game(game_core_v3)