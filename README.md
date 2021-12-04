[![Build Status](https://app.travis-ci.com/VsevolodOn/PTLab2.svg?branch=master)](https://app.travis-ci.com/kpdvstu/PTLab2)
# Лабораторная №2 по дисциплине "Технологии программирования"

**Цели работы:**
1. Познакомиться c моделью MVC, ее сущностью и основными фреймворками на ее основе.
2. Разобраться с сущностями «модель», «контроллер», «представление», их функциональным назначением.
3. Получить навыки разработки веб-приложений с использованием MVC-фреймворков, написания модульных тестов к ним и интеграции приложений в конвейер CI / CD;
4. Получить навыки управления автоматизированным тестированием и разворачиванием программного обеспечения, расположенного в системе Git, с помощью инструмента Travis CI.


**Постановка задачи:**

Требуется разработать web приложение с использованием модели MVC, фреймворка Django, реализующее функцию магазина товаров для сада. С возможностью непрерывной интеграции и непрерывного развертывания на Heroku с использованием Travis CI.


**Описание:**

В магазине имеется определенное количество товара каждого 
вида. После покупки количество товара уменьшается. Если 
количество товара уменьшилось более чем в два раза, его цена 
возрастает на 20%.

**Входные данные:**

* Товар, количество товара, ФИО, адрес


**Окно товара:**

![image](https://user-images.githubusercontent.com/92991750/144700435-46838478-b97e-4b96-94a7-71596945900c.png)


**Окно покупки:**

![image](https://user-images.githubusercontent.com/92991750/144700451-4ecf0ab2-84b1-45dc-b5d2-4e6a9ff249de.png)


**Изменение цены:**

![image](https://user-images.githubusercontent.com/92991750/144700463-fdd1b838-835d-4637-831f-976ee64752fa.png)


**Вывод:**

В результате выполнения лабораторной работы был разработан проект с использованием MVC, реализовано автоматическое развертывание.

