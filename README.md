<h2>Всем привет, это Андрей <img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h2>
</h2> 

<h3>Вы находитесь на странице моего проекта по тестовому заданию Stripe</h3> 

Перед Вами тестовое задание, суть заключается в знакомстве с платежной системой Stripe. 
В качестве базовой части задание необходимо было реализовать простой сервер с одной html страничкой, 
который общается со Stripe и создает платёжные формы для товаров.
Я пошел чуть дальше, добавив 2 html странички). 
На главной отображается весь список товаров, с возможностью добавить их в заказ,
далее на старнице заказа можно изменить количество товара и нажать кнопочку купить,
которая перекинет пользователя на форму оплаты Stripe.
Большинство процессов добавления/изменения товаров в заказ реализовано через AJAX.
С целью упрощения в данном проекте реализована одна сущность заказа, без авторизации.
В работе необходимо было использовать Django, что и было сделано.

## Технологии:

<details><summary>Подробнее</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)

[![Stripe](https://img.shields.io/badge/Stripe-8.4-blue?logo=Stripe)](https://stripe.com/)

**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v5.0.2-blue?logo=Django)](https://www.djangoproject.com/)


**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)

**Фронт:**

![Static Badge](https://img.shields.io/badge/Bootstrap-5.2.0-blue?logo=Bootstrap&logoColor=blue)
![Static Badge](https://img.shields.io/badge/Jquery-3.6.1-blue?logo=jquery&logoColor=blue)

**CI/CD:**


[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?logo=gunicorn)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)


</details>

## Запуск:

<details><summary>Подробнее</summary>


В первую очeредь для удосбва тестирования проект запущен на удаленном сервере и доступен по адресу:
`http://78.141.242.95/`

Доступ в админ панель:
`http://78.141.242.95/admin/`

Учетные данные для входа:
````
Username: adm
Password: adm
````


<details><summary>Локальный запуск: Docker Compose/PostgreSQL</summary>

1. Клонируйте репозиторий с GitHub:
   ```bash
   git clone git@github.com:AFrantsevich/test_task_stripe.git
   ```
   
2. В корневой директории проекта создайте файл .env для примера в директории находится [.env_example](.env_example). 
В случае отсутсвия данных, оставьте файл пустым. Главное что бы файл физически присутсвовал в директории.


3. Из корневой директории проекта выполните команду:
   ```bash
   docker-compose up -d --build 
   ```
   Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу `http://localhost`.
   

4. Доступ в админ панель:
   `http://localhost/admin/`
   
   Учетные данные для входа:
   ````
   Username: adm
   Password: adm
   ````

5. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
   ```bash
   docker compose -f docker-compose.yml down
   ```
   Если также необходимо удалить тома базы данных, статики и медиа:
   ```bash
   docker compose -f docker-compose.yml down -v
   ```
</details>

<details><summary>Локальный запуск: Django/SQLite3</summary>

1. Клонируйте репозиторий с GitHub:
   ```bash
   git clone git@github.com:AFrantsevich/test_task_stripe.git
   ```

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```
   
3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
   ```bash
   python -m pip install --upgrade pip && pip install -r requirements.txt
   ```

4. В корневой директории проекта создайте файл .env для примера в директории находится [.env_example](.env_example). 
В случае отсутсвия данных, оставьте файл пустым. Главное что бы файл физически присутсвовал в директории.


5. Примените миграции, наполните БД тестовыми данными, создайте суперюзера, запустите приложение:
   ```bash
   python tree_menu/manage.py migrate && \
   python tree_menu/manage.py load_data 15 454 6423 && \
   python tree_menu/manage.py create_superuser && \
   python tree_menu/manage.py runserver
   ```
   Сервер запустится локально по адресу `http://127.0.0.1:8000/`


6. Остановить приложение можно комбинацией клавиш Ctl-C.
</details>