"""
Dieses Modul beinhaltet die McCarthy-91-Funktion.
Beispiel:
    >>> M(50)
    91
"""

__author__ = "Darko Ljubobratovic"
__klasse__ = "4CN"
__example__ = "SEW4/01/F3"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "30.09.2026"
__version__ = "1.0.0"
__license__ = "GNU GPLv3"
__status__ = "Fertig"

from time import time


def M(n: int) -> int:
    """
    McCarthy-91-Funktion.

    :param n: ganze Zahl
    :return: M(M(n + 11)) wenn n <= 100, sonst n - 10
    Testbeispiele:
        >>> M(50)
        91
        >>> M(100)
        91
        >>> M(150)
        140
    """
    if n <= 100:
        return M(M(n + 11))
    return n - 10


if __name__ == "__main__":
    t0 = time()
    m_list = []
    for i in range(200):
        m_list.append(M(i))

    m_dict = {}
    for n in range(200):
        m_dict[n] = M(n)

    t1 = time()

    print(m_list)
    print(m_dict)
    print(f"Dauer: {t1 - t0:.6f} s")
    print("Bemerkenswert: Bis 101 ist es immer 91, danach steigt es immer um 1")
