def is_creditable(age, salary):
    """
    #первый тест позитивный - если все данные валидны, результат позитивный
    >>> is_creditable(30, 40_000)
    True

    >>> is_creditable(20, 40_000)
    False

    >>> is_creditable(70, 40_000)
    False

    >>> is_creditable(30, 10_000)
    False
    """
    min_age = 21
    max_age = 60
    min_salary = 30_000

    #так делать не нужно
    #Alt + Insert - Что-то создать
    #Alt + Enter - Что-то поправить
    if min_age <= age <= max_age and salary >= min_salary:
        return True
    else:
        return False
