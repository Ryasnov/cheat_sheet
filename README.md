# Интернет-магазин "Шпаргалка"<br>документация


### Оглавление:

1. [Структура проекта](#структура-проекта)
2. [Основные сведения](#основные-сведения)
4. [Инструкция по запуску проекта](#инструкция-по-запуску-проекта)

## Структура проекта

```python
README.md
demo.py
devices.csv
docker-compose.yaml
Dockerfile
queries.sql
requirements.txt
shopapp-products-fixtures.json
mysite
│   db.sqlite3
│   manage.py
│   shopapp-products-fixtures.json
│   shopapp-products-fixtures.xml
│   shopapp.fixtures.json
├───blogapp
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   templates
│       └───blogapp
│               articles_list.html
│               base.html
├───blogapp_new
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   sitemap.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   └───templates
│       └───blogapp_new
│               article_detail.html
│               article_list.html
│               base.html
├───locale
│   ├───en
│   │   └───LC_MESSAGES
│   │           django.mo
│   │           django.po
│   └───ru
│       └───LC_MESSAGES
│               django.mo
│               django.po
├───myapiapp
│       admin.py
│       apps.py
│       models.py
│       serializers.py
│       tests.py
│       urls.py
│       views.py
│       __init__.py
├───myauth
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   ├───management
│   │   └───commands
│   │           bind_user.py
│   └───templates
│       └───myauth
│               about-me.html
│               base.html
│               login.html
│               profile_form.html
│               profile_update_form.html
│               register.html
│               users-list.html
│               user_detail.html
│               user_detail_form.html
├───mysite
│       asgi.py
│       settings.py
│       sitemaps.py
│       urls.py
│       wsgi.py
│       __init__.py
├───requestdataapp
│   │   admin.py
│   │   apps.py
│   │   exceptions.py
│   │   forms.py
│   │   middlewares.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   └───templates
│       └───requestdataapp
│               base.html
│               file-upload.html
│               request-query-params.html
│               user-bio-form.html
├───shopapp
│   │   admin.py
│   │   admin_mixins.py
│   │   apps.py
│   │   common.py
│   │   forms.py
│   │   models.py
│   │   prodicts-fixtures.json
│   │   serializers.py
│   │   sitemap.py
│   │   tests.py
│   │   urls.py
│   │   utils.py
│   │   views.py
│   │   __init__.py
│   ├───fixtures
│   │       orders-fixture.json
│   │       products-fixture.json
│   │       users-fixture.json
│   ├───management
│   │   └───commands
│   │           agg.py
│   │           bulk_actions.py
│   │           create_order.py
│   │           create_products.py
│   │           selecting_fields.py
│   │           update_order.py
│   └───templates
│       ├───admin
│       │       csv_form.html
│       └───shopapp
│               base.html
│               create-order.html
│               create-product.html
│               groups_list.html
│               order_confirm_delete.html
│               order_detail.html
│               order_form.html
│               order_list.html
│               order_update_form.html
│               product-details.html
│               products_changelist.html
│               products_list.html
│               product_confirm_delete.html
│               product_form.html
│               product_update_form.html
│               shop_index.html
│               user_orders_list.html
└───uploads
    ├───orders
    ├───products
    └───users
```

## Основные сведения

&nbsp;&nbsp;&nbsp;Данный проект представляет собой шпаргалку по написанию интернет-магазина для личного пользования.
В проекте реализована система регистрации пользователей с возможностью смены аватаров
Проект предусматривает группы пользователей: продавцы и покупатели. Продавцы могут размещать товары с изображениями и описанием.
Покупатели могут оформлять заказы. 
Незарегистрированные пользователи могут просматривать товары

&nbsp;&nbsp;&nbsp;Backend разработан на языке программирования **Python 3.11**, с использованием фреймворков **Django версии 4.2**, **DjangoRestFramework версии 3.15**, в качестве базы данных используется СУБД **SQLite 3**


## Инструкция по запуску проекта


1. Скачайте проект командой *git clone*: `git clone <адрес Git-репозитория>`

2. Измените значение **SECRET_KEY** в файле **megano/.env**: `SECRET_KEY='<ваше значение>'`

3. Запустите приложение Docker Desktop

4. Соберите прoект коммандой `docker-compose build <название приложения>`

5. Запустите проект коммандой `docker-compose up <название приложения>`

