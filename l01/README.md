# Lista 1 - String matching

## Treść

### Zadanie 1
Przeanalizuj i zaimplementuj algorytmy wyszukiwania wzorca z wykorzystaniem automatów skończonych i Knutha-Morrisa-Pratta (opisane w książce: Cormen T.H., LeisersonCh.E., Rivest R.L.:Wprowadzenie do algorytmów, rozdział 34.3 i 34.4, ISBN 83-204-2144-6).

## Rozwiązanie

Rozwiązaniem tej listy zadań jest skrypt napisany w języku Python. Poniżej znajduje się instrukcja wraz z przykładowym użyciem.

### Instrukcja

Domyślnym algorytmem jest algorytm Knutha-Morrisa-Pratta. Aby skorzystać z wyszukiwania wzorca z wykorzystaniem automatów skończonych, należy podać alfabet.

#### Wymagane parametry:
  - `--text/-t` tekst
  - `--pattern/-p` pattern

#### Opcjonalne parametry:
  - `--alphabet/-a` Alfabet dla **Finite Automaton Matcher**
### Przykładowe użycie

#### KMP
```shell
$ python pattern_matcher.py -t "ąćąćąćąśśśćąćąćąćąćśśśćąćś" -p "ćąć"
Knuth-Morris-Pratt Matcher.
[1, 3, 10, 12, 14, 16, 22]
```

#### DFA
```shell
$ python pattern_matcher.py -t "\|\|\/\|/\ \\\ \\\ \/// //\|\|" -p "|" -a "\| /"
Finite Automaton Matcher.
[1, 3, 7, 25, 27]
```

#### Testy
```shell
$ ./tests.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
