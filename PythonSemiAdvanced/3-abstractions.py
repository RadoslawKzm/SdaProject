import dataclasses
from abc import ABC, abstractmethod
from typing import Dict, Optional


class KubekAbstrakcja(ABC):
    @abstractmethod
    def czy_jest_okragly(self) -> bool:
        """zaimplementuj ta funkcje"""

    @abstractmethod
    def czy_mozna_nalac(self) -> bool:
        """zaimplementuj czy mozna nalac"""

    @abstractmethod
    def czy_ma_ucho(self) -> bool:
        """zaimplementuj ucho"""


class TypowyKubek(KubekAbstrakcja):
    def czy_jest_okragly(self) -> bool:
        return True

    def czy_ma_ucho(self) -> bool:
        return True

    def czy_mozna_nalac(self) -> bool:
        return True


class KubekPikachu(KubekAbstrakcja):
    def czy_jest_okragly(self) -> bool:
        return True

    def czy_ma_ucho(self) -> bool:
        return True

    def czy_mozna_nalac(self) -> bool:
        return True


class RebelKubek(KubekAbstrakcja):
    def dupa(self):
        return True


def robot(*, kubek: KubekAbstrakcja) -> Dict[str, bool]:
    t1 = kubek.czy_ma_ucho()
    t2 = kubek.czy_mozna_nalac()
    t3 = kubek.czy_jest_okragly()
    return {"t1": t1, "t2": t2, "t3": t3}


if __name__ == '__main__':
    kubek1 = TypowyKubek()
    kubek2 = TypowyKubek()
    kubek3 = TypowyKubek()
    output1 = robot(kubek=kubek1)
    output2 = robot(kubek=kubek2)
    output3 = robot(kubek=kubek3)
    kubek_pikachu_1 = KubekPikachu()
    output4 = robot(kubek=kubek_pikachu_1)

    kubek_rebel = RebelKubek()
    output5 = robot(kubek=kubek_rebel)
