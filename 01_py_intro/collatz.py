"""
Dieses Modul beinhaltet Funktionen rund um die Collatz-Folge:
einzelner Schritt, rekursive Folge, längste Folge bis n.
Bonus: verallgemeinerter Faktor p statt 3.
Beispiel:
    >>> collatz(6)
    3
"""

__author__ = "Darko Ljubobratovic"
__klasse__ = "4CN"
__example__ = "SEW4/01/F2"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "30.09.2026"
__version__ = "1.0.0"
__license__ = "GNU GPLv3"
__status__ = "Fertig"

from typing import List, Tuple


def collatz(n: int, p: int = 3) -> int:
    """
    Berechnet den nächsten Wert der Collatz-Folge.

    :param n: aktuelle Zahl (n > 0)
    :param p: Faktor für ungerade Zahlen (Default 3)
    :return: n // 2 wenn n gerade, sonst p * n + 1
    Testbeispiele:
        >>> collatz(6)
        3
        >>> collatz(7)
        22
        >>> collatz(7, 5)
        36
    """
    if n % 2 == 0:
        return n // 2
    return n * p + 1


def collatz_sequence(number: int, p: int = 3) -> List[int]:
    """
    Liefert rekursiv die Collatz-Folge ab number (endet mit 4, 2, 1).

    :param number: Startzahl
    :param p: Faktor für ungerade Zahlen (Default 3)
    :return: Collatz Zahlenfolge, resultierend aus number
    Testbeispiele:
        >>> collatz_sequence(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> collatz_sequence(1)
        [1]
        >>> collatz_sequence(5, 1)
        [5, 6, 3, 4, 2, 1]
    """
    if number == 1:
        return [1]
    return [number] + collatz_sequence(collatz(number, p), p)


def longest_collatz_sequence(n: int, p: int = 3) -> Tuple[int, int]:
    """
    Sucht die längste Collatz-Folge mit Startwert <= n.

    :param n: größter Startwert
    :param p: Faktor für ungerade Zahlen (Default 3)
    :return: Startwert und Länge der längsten Collatz Zahlenfolge
    Testbeispiele:
        >>> longest_collatz_sequence(100)
        (97, 119)
        >>> longest_collatz_sequence(10)
        (9, 20)
        >>> longest_collatz_sequence(10, 1)
        (9, 8)
    """
    erg_start = 1
    erg_len = 1
    for i in range(1, n + 1):
        length = len(collatz_sequence(i, p))
        if length > erg_len:
            erg_len = length
            erg_start = i
    return (erg_start, erg_len)


def main() -> None:
    try:
        longest_collatz_sequence(13, 5)
    except (RecursionError):
        print("RecursionError: 1 wird nicht erreicht")


if __name__ == "__main__":
    main()
