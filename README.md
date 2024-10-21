# Auction House - Dražby nemovitostí

## Popis projektu
Tento projekt je webová aplikace pro aukční dům postavená na frameworku Django. Umožňuje uživatelům (dle přiřazených práv) přidávat a spravovat aukce, podávat nabídky a spravovat svůj účet. Aukční dům je určen pouze pro uživatele s českým občanstvím.

## Instalace
```bash
# Instalace závislostí
pip install -r requirements.txt
```

```bash
# Migrace databáze
python manage.py migrate
```
![ER Diagram](/other_files/ER_diagram.png)

```bash
# Spuštění serveru
python manage.py runserver
```

## Požadavky
Python 3.10+

Django 5.1.1

## Použití
Aukce jsou rozdělené do tří sekcí - domy, byty a pozemky. Při registraci je nový uživatel automaticky zařazen do skupiny práv "Users", což mu umožňuje účastnit se aukcí a spravovat svůj účet. Pokud je registrovaný uživatel následně zařazen do skupiny práv "Admins", pak se účastnit aukcí nesmí, ale může aukce přidávat a spravovat. Z důvodu bezpečnosti jsou provedené příhozy vždy anonymizované.

Pro úspěšnou registraci je (z důvodů opatření proti praní špinavých peněz) potřeba uvést i údaje dokladu totožnosti (občanský průkaz či pas). Doklad je následně automaticky ověřen v databázi neplatných dokladů (https://aplikace.mvcr.cz/neplatne-doklady/).

Projekt také využívá API od mapy.cz.

## Postup pro uživatele ze skupiny práv "Admins" pro přidání aukce
1. Vytvořit záznam pro nemovitost.
2. Přiřadit záznamu typ nemovitosti.
3. Vytvořit samotnou aukci.
4. Přidat fotodokumentaci (obrázky) dle potřeby, buď ke konkrétní nemovitosti, nebo i k příslušné aukci.

## Testování
Testy obsahují kontrolu registrace nového uživatele, testy formulářů a testy modelů.

## Dražba
Po zpřístupnění dražby uživatelé přihazují. Pokud je čas menší než 5 minut po příhozu se nastaví zase na 5 minut.

Po ukončení dražby se vypíše výherce a dražba se uloží do jeho vyhraných aukcí.
```bash
# Spuštění testů
python manage.py test
```
