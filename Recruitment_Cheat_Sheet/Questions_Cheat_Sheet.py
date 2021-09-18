# 1. Co to jest GIL
"""Global interpreter lock, co robi i jak dokadnie dziala poczytajcie na necie"""
# 2. Co to jest MRO
"""Sposob dzidziczenia klas, Method Resolution Order.
In the nutshell chodzi o to, że gdy nasza klasa dziedziczy po paru innych a te inne jeszcze znowu po paru innych,
to interpreter będzie szedł rekurencyjnie do góry po klasach szukając jakiegos atrybutu albo metody az ją znajdzie.
Może nastąpić konflikt na zasadzie dziedziczenia krzyzowego Example(A(C,D), B(D,C)) to dostaniecie MRO error.
"""


# 3. Wyjaśnij jak działa MRO

class C:
    def printing(self):
        print("class C")


class D:
    def printing(self):
        print("class D")


class A(C, D):
    pass


class B:
    def printing(self):
        print("class B")


class Example(A, B):
    pass


print(f"\n{'*' * 30}\n MRO EXPLANATION")
klasa = Example()
klasa.printing()
print(f"\n{'*' * 30}\n")

# 4. Co to znaczy, że python jest jezykiem dynamicznie typowanym
"""Nie deklarujecie na starcie że zmienna to bedzie lista i przez dzialanie programu nic tam innego nie moze być.
lst na początku może być listą ale nic nie stoi na przeszkodzie, żeby był tam int czy string.
Nasze typowania co robimy lst:list = [] to jest tylko aluzja
"""

# 5. Czy int jest typem mutable czy immutable.
"""
Immutable, gdy zmieniamy inta to nie robimy append ani nic innego co go zmieni tylko new_int = int + 1 albo int += 1
"""

# 6. Różnica między tuplą a listą?
"""
Tuple definiujemy przed startem programu i jest ona immutable co oznacza ze interpreter przeznacza jakąś ilość ram,
i nie musi zostawiać sobie overheadu jak w przypadku listy.
Lista chyba zostawia sobie puste miejsce na wypadek appendow w ilości 2^n czyli macie 4 elementy w liscie to lista ma 
tam w srodku jeszcze 4 pola wolne. Macie 20 elemetow to macie tam wolnych do max 32 elemntow.
Append do listy to O(1) aaaaaale gdy traficie na koniec wolnych miejsc zaalokowanych przez interpreter to robi on:
nowa_lista = [copy(lista)] + [len(lista) * None] przez co jak niefortunnie traficie na kopie przy milionie elementow 
to macie duuupe :D
Dlatego też tworzenie list wielkich szybsze jest przy uzyciu list(iterator) niz robienie [item for item in iterator]
"""

# 7. Czy znasz bilbioteke collections?
"""TAK :D"""
# 8. Jakie moduły wymienisz z tej biblioteki?
"""
Frozen set, jest to niemutowalna wersja setu. To samo co set tylko raz deklarujeie i nie możecie zmieniac,
Named tuple, nie korzystalem nigdy, poczytajcie wiki,
Deque, double ended queue jest to implementacja pythonowa lined listy. Pamietajcie lista to jest CS(computer science)
to array. A prawdziwa lista czyli linked lista to jest wlasnie deque. Poznaliście to na bloku algorytmy i
struktury danych.
Counter, jest to takie cos co przeleci wam raz po danym iteratorze i policzy wystapienia wszystkiego np:
 - [1,2,3,1,2,3,1,2,1,1,1,2] > Counter(lst) = {1:6, 2:4, 3:2}. Tak, counter zwraca slownik
Default dict, taki dict ktory jak nie ma jakiejs zmiennej pod danej kluczem to wam zwroci default value zadeklarowana
Więcej grzechów nie pamietam
"""

# 9. Co to iterator?
"""To takie cos po czym mozemy przeiterowac :D Wszystko co ma zaimplementowane metody __iter__ i __next__"""


class Iterator:
    def __iter__(self):
        return "iterator object"

    def __next__(self):
        if "cos":
            raise StopIteration
        return "nastepny item"

    # 10. Co to jest context manager?


"""Takie coś co robi rzeczy przed kodem i rzeczy po kodzie lapiąc jeszcze wyjatki. 
Zaimplementowane metody __enter__ i __exit__"""


class CntxMngr:
    def __enter__(self):
        return self  # tu zwracamy dupa w > with COS as dupa:

    def __exit__(self, exc_type, exc_val, exc_tb):  # tutaj lapiemy wyjatki jesli sa to exc_cos nie bedzie None
        if any((exc_type, exc_val, exc_tb)):  # podwojne nawiasy bo any bierze iterator wiec dalem tuple, moglem liste
            # lapcie wyjatek
            return False  # gdy chcecie wywalic program tym exception, True jesli chcecie zdusic wyjatek(mozliwy anty pattern)
        # tu robcie cos na zakmniecie kodu


# 11. Jaka jest roznica miedzy try/except a context managerem?
"""W sumie rzadna, context manager to obiektowa implementacja try/except/finally. 
Jest na pewno czytelniej i mozecie to ponownie wykorzystac zamiast nakurwiac try/excepty"""

# 12. Co to jest decorator?
"""Takie coś co może dołożyć funkcjonalność do istniejącej funkcji przy użyciu @decorator nad daną funkckją"""


def decorator(func):
    def wrapper(*args, **kwargs):  # to jest po to żeby łapać argumenty funkcji udekorowanej
        # do something przed
        try:
            retval = func()
        except Exception as exc:
            print("dupa")
        finally:
            print("dupa finally")
        return retval

    return wrapper  # zwracamy funkcje bez wywolania


"""aaaalbo druga wersja dla mierzenia czasu"""
from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        tstart = time()
        retval = func()
        print(f"Elapsed time: {time() - tstart:0.4f}s")
        return retval

    return wrapper


# 13. Co to jest generator?
"""To takie coś co zna tylko aktualny stan i przepis na kolejny. Nie zajmujecie pamieci. Wolniejsze w obsludze niz lista
Lista duzo tracicie na starcie a potem siedzi w ramie i jest szybka.
Generator nie siedzi w ramie i procek zwraca wam na bierzaco on demand.
Generator dobry gdy chcecie wziac pare pierwszych elementow iteratora i olac nie zapychajac pamieci
Generator zly gdy chcecie iterowac pare razy po duzej strukturze
"""
def generator():
    start: int = 0
    while True:
        yield start
        start += 1

# 14. Czym sie rozni multiprocessing a multi threading albo asynchroniczne/asyncio
"""Multiprocessing to odpalacie pare rownoleglych procesow.
Asynchronicznie to znaczy ze wasz program idzie spac lub czeka i ma przestoj wtedy mozecie wypelnic luke innym zadaniem.
Multiprocessing dobry gdy macie jakies mocne obliczenia i nie macie przestojow.
Async dobry gdy macie duzo operacji czekajacych jak requesty do innych stron itp.
"""

# 15. Co to list comprhension lub olaboga lista skladana. To powie ten sam typ co zapyta o krotke xD
"""lst = [item for item in range(10)]"""
"""16. Macie inne typy comprehension jak: 
dict comprehension > dictio = {k:v for k,v in zip(range(10), range(11,21))},
set comprehension > {dupa for dupa in range(1_000_000)}
generator comprehension > (item for item in range(1_000_000)), tak, generatory tez tak mozecie skladac zamiast pisac 
yield
"""
# 17. Co oznacza slowko yield?
"""W sumie nie wiem jak to opisac :D w generatorze zwraca cos"""

# 18. Jest cos takiego o co nikt nie pyta i malo to wie, Consumer
def consumer(item):
    test = yield
"""Taki konstrukt jest podstawą asynchronicznosci ale jak to powiecie to juz beda przytakiwac.
Malo kto to zna. Wiec nie bedziecie musieli tlumaczyc jak z tego wynika async :D
"""
# 19. Jak mozna sledzic wycieki pamieci w pythonie?
"""Tracemalloc"""
# 20. Zarzadzanie pamiecia i weak ref. Tu juz #Senior
# 21. __slots__, pytanie do epamu. Totalna pierdola aaaale pytali #Senior
# 22. Zasada DRY-do not repeat yourself
# 23. Zasada YAGNI- you aint gonna need it, piz to co potrzebujesz teraz a nie bo sie przyda kiedys
# 24. Zasada KISS- keep it simple stupid- rob to glupio prosto
"""Ja wyznaje zasade ze prostota jest szczytem wyrafinowania ~DaVinci"""
# 25. CZy jak podajecie liste jako argument funkcji to podajecie przez wartosc czy referencje?
"""wszystko co mutable to podajecie jako referencje do obiektu w pamieci a co immutable jako wartosc"""
lst = [5]
def dupa(lista_d:list):
    lista_d.extend([1,2,3,4])
dupa(lst)
#lista bedzie miala teraz [5,1,2,3,4] polecam python tutor do tego przykladu
# 26. roznica miedzy threading a async?
"""threading to asynchronicznosc hardware a async to petla gevent polecam ten filmik:
https://www.youtube.com/watch?v=8aGhZQkoFbQ"""
# 27. Zadanie STX Next na juniora: Napiszcie komende string.split bez jej uzywania :D
############################## DOCKER #####################################3
# 1. Co to są layery w dockerze?
"""Jak skladacie sobie docker file to kazda linijka to nowy layer. 
Jezeli zmieni sie jakis wyzej w strukturze wszystkie nizej sa przebudowywane.
Chodzi tez zeby pisac jak najwiecej w jednym layerze dzieki temu zmniejszamy objetosc dockera.
W sumie nigdy nie musialem tego dokladnie wyjasniac wiec nie wiem jak to dziala ale to znaczy ze 
to wytlumaczenia wam wystarczy :D"""

# 2. Jak polaczyc system plikow komputera z dockerem/ Co to volumen
"""Opcja volume w dockerze pozwala na polaczenie systemu plikow hosta z kontenerem"""

# 3. Pytanie o to ze jak zamniesz dockera to tracisz pliki w srodku o ile nei sa polaczone volumenem
# 4. Porty w kontenerze, jak nie zrobisz forwarda to nic nie zobaczysz na zewnatrz co sie dzieje w srodku
# 5. Jak ograniczyc wielkosc dockera?
"""layery, inny image bazowy jak apline dalej nie wiem"""
# 6. Co lepsze, korzystac z image Python ofijalny czy samemu biuld skladac?
"""Podobno na rekrutacji uslyszalem raz ze skladac samemu z ubuntu np. bo jest lepiej zoptymalizowany ale chuj wie"""

################################## GIT #####################################
# 1. Jakie znacie flow w gicie? Tzn jak mozna prowadzic repo?
"""Poczytajcie o github flow i git flow. 5 min czytania ale na pewno mowili o tym na bloku git :D"""
# 2. Co to branch?
# 3. Co to merge
# 4. Co to rebase
# 5. Cherry pick?
# 6. Co to commit
# 7. Co to rollback

################################### AWS #########################################
# 1. Jakie znasz rzeczy w AWSIE?
"""EC2-virtualna maczyna, S3-zwykly dysk, RDS-system do bazy danych, Route53-modul do routingu, 
lambda-modul co dajecie tylko kod a on wam ten kod wykonuje na czyms, wieksza czesc SaaS (software as a service)"""
# 2. Co robiliście na AWS?
"""Probowaliscie przeniesc grida obliczeniowego on permise(czyli firma ma sobie stacjonarne serwery u siebie w budynku)
do clouda. Uzywaliscie stronki cloud craft do obliczania kosztow. Nic skomplikowanego, stworzyliscie VPC(siec wirtualna)
Maszyny on demand i wyjscie jakims tam modulem do polaczenia z vpn waszej firmy.
Uslyszycie na to AHA :D"""
#################################### MID/SENIOR #####################################
# 1. Zasady SOLID?
"""Poczytajcie w necie  o tutaj pytaja o ksiazkowa wiedze te stare pierdziele i nie liczcie ze pokazecie cos w praktyce :D
Ogolnie chodzi o to zeby budowac kod modulowy, ktorego zeby dodac funkcje nie trzeba zmieniac istniejacego tylko dodac nowy modul
"""
# 2. zasada high cohesion
"""Grupowanie kodu wg jego funkcjonalnosci. Np klasa czlowiek zeby nie miala metody kalkulator add bo to z dupy
Najlepsze pogrupowanie kodu wedlug wykonywanej czynosci
Srednie wg przynaleznosci do jakiegos modulu
Najgorsza grupujecie kod bo tak byl w repo ulozony."""

# 3. zasada low coupling
"""Chodzi o to zeby kod byl od siebie malo zalezny, jesli zmieniacie modul a to wymaga zmiany 10 innych to dupa.
Niski couplig to gdy zmiana w kodzie nie wywala innych rzeczy a wysoki gdy zmiana wywala wszystko inne"""

#################################### SENIORSKIE ######################################
# 1. Design patterny, wymiencie jakie znacie?
"""https://refactoring.guru/pl/design-patterns/python"""
# 2. O co chodzi w singleton
# 3. strategy pattern
# 4. Obserwator
# 5. Jakie patterny uzywaliscie?
"""Polecam proxy, latwo wytlumaczyc, strategy i wlasnie observer. #jebacSingletona"""
# 6. Pytanie moze pasc o wzorce architektoniczne, funkcjonalne i behawioralne ale to mowilem zawsze ze nie pamietam :D

################################### API #############################################
# 1. Jakie znacie metody restowe?
"""Get, post put, delete, patch i inne"""
# 2. wytlumaczcie roznice miedz post i put
"""sorki amigos ale tutaj ja tez nie do konca czuje ta roznice :D"""
# 3. Jakie znacie headery w rest
"""nie pamietam :D"""
# 4. Co to jest rest?
# 5. co to jest soap
# 6. co to jest xml
# 7. Ogolne zagadanie o jsona, JSON to ustalony format przekazywania danych w REST
# 8. Sposoby autentykacji
# 9. Autoryzacja vs Autentykacja
"""Tu sie gurbo wyjebalem :D Pamietam dostalem dobrego ziomka ktoremu nie dalo sie kitu ozenic :D"""
# 10. Co to cookies
# 11. Co to indepotency
"""Poczytajcie na necie :D ale post nie jest a put jest indepotent"""
# 12. Co to web serwer, lub asgi vs wsgi lub ogolnie gosc bedzie zagajac o ten topic
"""chodzi o to ze macie 3 stage jak zbudowany jest wasz serwer webowy
Mi sie udalo wylgac z tej odpowiedzi :D"""
# 13. Jakiego webserwera uzywaliscie?
"""Udalo mi sie ze nie pisalem nigdy w django i to lykneli wiec podalem web serwer FastAPI czyli gunicorn"""
# 14. Zadanie na zaprojektowanie jakiegos API
"""Dostaniecie jakies user story i macie do tego zapodac odpowiednie api
chodzi o to zeby do kazdej funkcjonalnosci dac odpowiedni typ requestu jak get post put patch"""
# 15. Jak powiecie ze tylko FastAPI uzywacie to badzcie ready na pytania o asynchronicznosc
"""Polecam wytlumaczenie z konferencji javascript https://www.youtube.com/watch?v=8aGhZQkoFbQ"""

####################################### SQL ##############################################
"""Ogolnie w chuj pytan o robienie operacji"""
# 1. Jakie znacie joiny?
"""Jezuuuuu, zawsze o to pytaja, cross join i inne pierdoly. poczytajcie na necie"""
# 2. Jak sprawdzicie czy wasze query jest wolne czy nie
"""Jest tam cos na to ale nie pamietam, chyba EXPLAIN"""
# 3. Primary key, foreign key o co biega
# 4. Beda wam kazac jakies wyimaginowane relacje tworzyc w glowie
# 5. #SENIOR:
"""Gdy postawicie pare baz danych zeby obsluzyc wiekszy ruch to jak zrobicie zeby do jednej bazy poszedl zapis
i sie spropagowal po reszcie a w tym czasie zeby z innej bazy ktos nie wzial danych i nie zrobil operacji
przyklad: bank i dane o kasie na koncie do jednej bazy wplywa wniosek o wyplate 100mln i usuwamy mu 100mln
ale druga baza jeszcze tego nie dostala a wplynal jej wniosek o wyplate 50mln a na koncie juz tyle nie ma
tylko ze druga baza nie jest swiadoma operacji na 100mln :D"""
# 6. Co to zasada acid
# 7. Roznica miedzy SQL a no-sql
"""Wkurzajace pytanie bo z baz relacyjnych to jest SQL a z no-sql jest 7 jak dokumentowa, key-value, graphowa itp.
Polecam filmik fireship na ten temat: https://www.youtube.com/watch?v=W2Z7fbCLSTw
Obejzycie i juz odpowiecie na wszystkie pytania NO-SQL"""
# wiecej nie pamietam bo ja dupa z baz jestem :D