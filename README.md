# Auction House - Dražby nemovitostí

## Úvod
Studentský projekt tříčlenné skupiny (origin git: https://github.com/LadisV/Auction_House_Team_One.git). Po úspěšné obhajobě projektu jsem se jej rozhodnul rozvíjet samostatně za účelem samostudia.
V týmu jsem měl na starosti back-end, primárně pak Users/Admins profily a postup pro tvorbu nových aukcí.

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

Projekt také využívá API od mapy.cz na bázi zobrazení mapy a vyhledání adresy nemovitosti.

## Postup pro zalogované uživatele ze skupiny práv "Admins" pro přidání aukce
1. Vytvořit záznam pro nemovitost.
2. Přiřadit záznamu typ nemovitosti.
3. Vytvořit samotnou aukci.
4. Přidat fotodokumentaci (obrázky) dle potřeby, buď ke konkrétní nemovitosti, nebo i k příslušné aukci.

- vše probíhá postupně a intuitivně bez nutnosti překlikávání

## Postup pro zalogované uživatele ze skupiny práv "Users" pro podání příhozu v aukci
1. V přednastavený datum a čas začátku aukce se uživateli zpřístupní možnost příhozu.
2. Uživatel vyplní políčko příhozu v minimální částce pro příhoz, která je uvedena v parametrech aukce. Toto minimum pro příhoz je automaticky kontrolováno.
3. Záznam o provedeném příhozu je zpřístupněn v historii přihazování i ostatním uživatelům. Z důvodu bezpečnosti jsou provedené příhozy vždy zobrazeny s anonymizovaným uživatelským jménem.
4. Pokud je příhoz proveden v době, kdy do konce aukce zbývá méně než pět minut, po příhozu je doba konce aukce nastavena na pět minut.
5. Po skončení aukce, tedy v posledních pěti minutách aukce není proveden žádný platný příhoz, výherce se vypíše a zároveň se aukce uloží do seznamu vyhraných aukcí daného uživatele. 

## Testování
Testy obsahují kontrolu registrace nového uživatele, testy formulářů a testy modelů.

```bash
# Spuštění testů
python manage.py test
```
