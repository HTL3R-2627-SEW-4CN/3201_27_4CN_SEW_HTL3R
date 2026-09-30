"""
Dieses Modul beinhaltet Funktionen rund um Palindrome:
Wort-/Satz-Palindrome, Palindrom-Produkte, Dezimal-/Hex-Palindrome
Beispiel:
    >>> is_palindrom("Anna")
    True
"""

__author__ = "Darko Ljubobratovic"
__klasse__ = "4CN"
__example__ = "SEW4/01/F1"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "24.09.2026"
__version__ = "1.0.0"
__license__ = "GNU GPLv3"
__status__ = "Fertig"


def is_palindrom(s: str) -> bool:
    """
    Überprüft, ob der gegebene String ein Palindrom ist.
    Ein Palindrom ist ein Wort, das vorwärts und rückwärts gelesen dasselbe ist.

    :param s: Der zu überprüfende String.
    :return: True, wenn der String ein Palindrom ist, sonst False.
    Testbeispiele:
        >>> print(is_palindrom("Anna"))
        True
        >>> print(is_palindrom("Hello"))
        False
    """
    s = s.lower()
    return s == s[::-1]


def is_palindrom_sentence(s: str) -> bool:
    """
    Überprüft, ob der gegebene Satz ein Palindrom ist.
    Ein Palindrom ist ein Satz, der vorwärts und rückwärts gelesen dasselbe ist,
    wobei Leerzeichen und Satzzeichen ignoriert werden.

    :param s: Der zu überprüfende Satz.
    :return: True, wenn der Satz ein Palindrom ist, sonst False.
    Testbeispiele:
        >>> print(is_palindrom_sentence("Was it a car or a cat I saw?"))
        True
        >>> print(is_palindrom_sentence("Hello, World!"))
        False
    """
    s = "".join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]


def palindrom_product(x):
    """
    Ermittelt die größte Palindrom-Dezimalzahl kleiner als x,
    die das Produkt von zwei 3-stelligen Zahlen ist.

    :param x: Obere Grenze (exklusiv).
    :return: Größtes gefundenes Palindrom, 0 falls keines existiert.
    Testbeispiele:
        >>> palindrom_product(10**6)
        906609
        >>> palindrom_product(10000)
        0
    """
    highest = 0
    for i in range(999, 99, -1):
        if i * 999 <= highest:
            break
        for j in range(999, i - 1, -1):
            product = i * j
            if product <= highest:
                break
            if product < x and str(product) == str(product)[::-1]:
                highest = product
    return highest


def get_dec_hex_palindrom(x):
    """
    Ermittelt die größte Zahl kleiner als x, die sowohl im Dezimal-
    als auch im Hexadezimalsystem ein Palindrom ist.

    :param x: Obere Grenze (exklusiv)
    :return: Größte gefundene Zahl, 0 falls keine existiert
    Testbeispiele:
        >>> get_dec_hex_palindrom(1000)
        979
        >>> get_dec_hex_palindrom(10)
        9
        >>> get_dec_hex_palindrom(1)
        0
    """
    for i in range(x - 1, 0, -1):
        dec = str(i)
        hex = to_base(i, 16)
        if dec == dec[::-1] and hex == hex[::-1]:
            return i
    return 0


def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    Testbeispiele:
        >>> to_base(1234, 16)
        '4D2'
        >>> to_base(10, 2)
        '1010'
        >>> to_base(0, 16)
        '0'
        >>> to_base(10, 1)
        Traceback (most recent call last):
            ...
        ValueError: Base must be in range 2-36
    """
    numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base > len(numbers) or base < 2:
        raise ValueError("Base must be in range 2-36")
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = numbers[number % base] + result
        number //= base
    return result
