# здесь расположим нашу функцию которая с помощью SSH соединения будет выполнять команду SQL

def SQL(command: str):
    """
    Функция для работы с БД через SSH

    Принимает на вход команду которую надо исполнить

    И возвращает результат
    """

    from SSH_DataBase_Framework import Setup, Set_Config
    from GenerateMeterData.Service.Config import path_to_data_base, IP_port, IP_address, user_password, user_login
    # Берем путь
    path = path_to_data_base
    # Задаем конфиги
    Set_Config(IP_address=IP_address, IP_port=IP_port, user_login=user_login, user_password=user_password)
    # Отправляем JSON в нужную нам API
    result = Setup(command=command, data_base_path=path)

    return result


def find_to_max_MeterId_in_MeterTable():
    """
    Функция для поиска максимального MeterId

    ВОЗВРАЩАЕТ СЛВОАРЬ - МАКСИСМАЛЬНОГО ЗНАЧЕНИЯ MeterId и соответсвеного ему DeviceIdx
    """
    # Формируем команду
    command = 'SELECT max(MeterId), DeviceIdx FROM MeterTable ;'
    # Запускаем ее
    result = SQL(command=command)

    # проверяем что заселектили не пустое значение
    if len(result) > 2:
        # Сначала очищаем ее от мусора
        result = result.strip('\\n')
        result = result.strip(' ')

        # После чего превращаем в словарь
        result = result.split('|')
        result = \
            {
                'MeterId': int(result[0]),
                'DeviceIdx': int(result[1])
            }

    else:
        result = \
            {
                'MeterId': 0,
                'DeviceIdx': 0
            }
    return result
