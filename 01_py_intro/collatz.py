"""
Dieses Modul beinhaltet Funktionen rund um die Collatz-Folge:
einzelner Schritt, rekursive Folge, längste Folge bis n.
Bonus: verallgemeinerter Faktor p statt 3.
Beispiel:
    >>> collatz(6)
    3
"""

__author__ = "Darko Ljubobratovic"
__example__ = "SEW4/01/F"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "30.09.2026"
__version__ = "1.0.0"
__license__ = "GNU GPLv3"
__status__ = "Entwicklung"

from typing import List, Tuple


def collatz(n):
    """
    Berechnet den nächsten Wert der Collatz-Folge.

    :param n: aktuelle Zahl (n > 0)
    :return: n // 2 wenn n gerade, sonst 3 * n + 1
    Testbeispiele:
        >>> collatz(6)
        3
        >>> collatz(7)
        22
    """
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    return n


def collatz_sequence(number: int) -> List[int]:
    """
    Liefert rekursiv die Collatz-Folge ab number (endet mit 4, 2, 1).

    :param number: Startzahl
    :return: Collatz Zahlenfolge, resultierend aus number
    Testbeispiele:
        >>> collatz_sequence(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> collatz_sequence(1)
        [1]
    """
    if number == 1:
        return [1]
    return [number] + collatz_sequence(collatz(number))


def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
    Sucht die längste Collatz-Folge mit Startwert <= n.

    :param n: größter Startwert
    :return: Startwert und Länge der längsten Collatz Zahlenfolge
    Testbeispiele:
        >>> longest_collatz_sequence(100)
        (97, 119)
        >>> longest_collatz_sequence(10)
        (9, 20)
    """
    erg_start = 1
    erg_len = 1
    for i in range(1, n + 1):
        length = len(collatz_sequence(i))
        if length > erg_len:
            erg_len = length
            erg_start = i
    return (erg_start, erg_len)
