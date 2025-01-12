# Итоговый проект по Python
---

## Запуск

### 1. Инициализация Airflow
Выполните следующую команду для инициализации Airflow:
```bash
docker compose -f docker-compose.init.yaml up
```

### 2. Поднятие сервисов Airflow, Postgres, MySQL
Чтобы запустить необходимые сервисы, выполните:
```bash
docker compose up
```
---

## Airflow Dags

### Вход в Airflow
Перейдите по адресу: [http://localhost:8080/](http://localhost:8080/).  
Учетные данные для входа:
- **Логин:** `admin`
- **Пароль:** `admin`

### Описание доступных DAG-ов

#### 1. **`1_Initial_Migration`**
- Запускается **один раз** при первом запуске для инициализации таблиц и данных.
- Функциональность:
  - Создание таблиц в Postgres и MySQL.
  - Загрузка первичных данных в Postgres.

#### 2. **`2_Transfer_Data_Postgres_to_MySQL`**
- Функциональность:
  - Репликация данных из Postgres в MySQL.
- **Настройка таблиц и полей для репликации**:
  - Содержится в файле `./airflow_dags/tables_to_replicate.yaml`.

#### 3.1 **`3.1_Create_MySQL_Vitrina_user_analytics`**
- Функциональность:
  - Создание пустой аналитической витрины `user_analytics`.

#### 3.2 **`3.2_Create_MySQL_Vitrina_product_performance`**
- Функциональность:
  - Создание пустой аналитической витрины `product_performance`.

#### 4.1 **`4.1_Populate_MySQL_Vitrina_user_analytics`**
- Функциональность:
  - Заполнение аналитической витрины `user_analytics` данными.
- Наполнение

| Поле | Описание |
| --- | --- |
| user_id,            | ID пользователя |
| first_name,         | Фамилия |
| last_name,          | Имя |
| email,              | Почта |
| phone,              | Номер телефона |
| registration_date,  | Дата регистрации |
| loyalty_status,     | Статус лояльности |
| total_orders,       | Кол-во заказов |
| total_spent         | Общая сумма трат |
- Применение
  - Анализ пользовательских метрик - тренды регистраций, статусов лояльности и т.д.

#### 4.2 **`4.2_Populate_MySQL_Vitrina_product_performance`**
- Функциональность:
  - Заполнение аналитической витрины `user_analytics` данными.
- Наполнение

| Поле | Описание |
| --- | --- |
| product_id          | ID товара |
| product_name        | Наименование |
| category_name       | Категория |
| total_sold_quantity | Кол-во проданных экземпляров |
| total_revenue       | Общая выручка |
| average_price       | Средняя цена |
| current_stock       | Кол-во в наличии |
- Применение
  - Анализ производительности продаж товаров, включая общую выручку, средние цены и наполнение склада.


---
