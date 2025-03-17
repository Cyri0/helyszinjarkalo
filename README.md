# Django Tutorial 4 Beginners

## Virtuális környezet
python -m venv [vkörny neve]
pl:
```console
python -m venv myvenv
myvenv\Scripts\activate
```
siker esetén a sor elején (myvenv)

## Django telepítése és új project
```console
pip install django
django-admin startproject [project név]
```
pl:
```console
django-admin startproject config
```
*ajánlott a külsőt átnevezni*
VAGY
```console
django-admin startproject config .
```
*és akkor helyben hozza létre*

## Alap adatbázis migrálása
```console
python manage.py migrate
```
Ez hozzáadja az alap 11 táblát a DB-hez.

## Admin felhasználó létrehozása
```console
python manage.py createsuperuser
```