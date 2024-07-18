# DZ № 13.1
Задание 1
Создайте классы 
Category
 и 
Product
.

Для класса 
Category
 определите следующие свойства:

название,
описание,
товары.
Для класса 
Product
:

название,
описание,
цена,
количество в наличии.
Для каждого поля используйте наиболее подходящий тип данных на ваше усмотрение, но обратите внимание, что цена может быть указана с копейками, а количество лучше измерять в штуках.

#атрибуты
 
#типы_данных
 
#создание_класса
 
#class

Задание 2
Для двух классов, которые были реализованы в задании 1, добавьте инициализацию так, чтобы каждый параметр был передан в инициализацию объекта и сохранен. А также для класса 
Category
 добавьте два атрибута, в которых будут храниться общее количество категорий и общее количество уникальных продуктов, не учитывая количество в наличии.

#__init__
 
#конструктор_класса
 
#self

Задание 3
Напишите тесты для классов, которые проверяют:

корректность инициализации объектов класса 
Category
,
корректность инициализации объектов класса 
Product
,
подсчет количества продуктов,
подсчет количества категорий.
#pytest
 
#assert
 
#fixtures
# Критерии
Создали классы и описали их инициализацию со всеми свойствами.
Объекты продуктов хранятся в соответствующем атрибуте объекта категории.
Результат выполнения всего задания залили на GitHub и сдали в виде ссылки на репозиторий.
Все написанные тесты выполняются без ошибок.
