# Домашка номер 14
***
## 1. Что я нового узнал?
 - модуль uuid-ossp для регенерация особого ключа 
    - скачать модуль командой: 
    ```CREATE EXTENSION IF NOT EXISTS "uuid-ossp";``` 
    - тип данных UUID для столбца:
    ```CREATE TABLE table_name (id UUID);```
    - при вставке данных:
    ```INSERT INTO table_name (id) VALUES (uuid_generate_v4());```

## Код SELECT из ДЗ
показал данные из трех таблиц (cars, manufactures, models):
```SELECT 
cars.name AS car_name, 
models.model AS car_model, 
manufactures.name AS car_manufacturer, 
models.year_of_issue as
production_year, 
models.price AS price
FROM cars
INNER JOIN manufactures ON (cars.manufacturer_uid = manufactures.id)
INNER JOIN models ON (cars.model_uid = models.id);```