def binary_string_to_float(binary_str):
    """
    Преобразует строку двоичного представления float в десятичное число
    
    Args:
        binary_str: строка вида '0.101' или '101.101'
    
    Returns:
        float: десятичное число
    """
    # Разделяем на целую и дробную части
    if '.' in binary_str:
        integer_part, fractional_part = binary_str.split('.')
    else:
        integer_part = binary_str
        fractional_part = ''
    
    # Преобразуем целую часть
    integer_decimal = 0
    for i, bit in enumerate(integer_part[::-1]):
        if bit == '1':
            integer_decimal += 2 ** i
    
    # Преобразуем дробную часть
    fractional_decimal = 0.0
    for i, bit in enumerate(fractional_part, 1):
        if bit == '1':
            fractional_decimal += 2 ** (-i)
    
    return integer_decimal + fractional_decimal

def float_to_binary_string(number, max_fraction_bits=52):
    """
    Преобразует десятичное число в двоичную строку
    
    Args:
        number: десятичное число
        max_fraction_bits: максимальное количество бит дробной части
    
    Returns:
        str: двоичное представление
    """
    if number == 0:
        return "0.0"
    
    # Определяем знак
    sign = '-' if number < 0 else ''
    number = abs(number)
    
    # Отделяем целую и дробную части
    integer_part = int(number)
    fractional_part = number - integer_part
    
    # Преобразуем целую часть
    if integer_part == 0:
        integer_binary = "0"
    else:
        integer_binary = ""
        temp = integer_part
        while temp > 0:
            integer_binary = str(temp % 2) + integer_binary
            temp //= 2
    
    # Преобразуем дробную часть
    fractional_binary = ""
    temp_fraction = fractional_part
    bits_count = 0
    
    while temp_fraction > 0 and bits_count < max_fraction_bits:
        temp_fraction *= 2
        if temp_fraction >= 1:
            fractional_binary += "1"
            temp_fraction -= 1
        else:
            fractional_binary += "0"
        bits_count += 1
    
    # Если дробная часть не нулевая, добавляем точку
    if fractional_binary:
        return f"{sign}{integer_binary}.{fractional_binary}"
    else:
        return f"{sign}{integer_binary}.0"

