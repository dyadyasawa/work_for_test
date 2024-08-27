# work_for_test

Платформа-торговой сети электроники

Создано веб-приложение с API-интерфейсом и админ-панелью.
Привязана база данных (фикстуры для моделей присутствуют).


Реализована иерархическая структура из трех уровней:

 - Производитель (Manufacturer)
 - Оптовик (Wholesaler)
 - Розничный продавец (Seller)

Для каждого звена струкруры прописана отдельная модель содержащая поля:

 - Название
 - Легкое описание
 - Email
 - Cтрана
 - Город
 - Улица
 - Номер дома
 - Поставщики (для Производителя - это нечто просто обозначенное словом, а для Оптовика и Розничного 
              продавца - это ссылки на существующие модели)
 - Задолженность (Присутствует только в модели Производителя, тоже просто цифра)
 - Кредиторы (Ссылка на модель, в которой зафиксировано, кто, кому и сколько должен. Тип связи: многие ко многим) 

Приложения:
 - Производители (manufacturers)
    - Модель: Производитель (Manufacturer)
    - Модель: Товар (Product)  # для примера, ссылается только на Производителя

 - Оптовики (wholesaler)  # забыл добавить 's для множественного числа
    - Модель: Оптовик (Wholesaler)
   
 - Продавцы (sellers)
    - Модель: Продавец (Seller)
   
 - Кредиторы (creditors)
    - Модель: Кредитор (Creditor)
   
 - Пользователи (users)
    - Модель (User)

Реализован CRUD для всех моделей.(+)

Права доступа:
 - Не авторизованный пользователь может только зарегистрироваться(создать пользователя, при этом
   введенный пароль хэшируется) и залогиниться.(+)
 - Авторизованный пользователь может все просматривать и создавать, но не может редактировать и удалять.(+)
 - Суперюзер может все.(+)

Для моделей: Производитель (Manufacturer), Оптовик (Wholesaler) и Продавец (Seller) добавлена возможность фильтрации
по определенной стране.(+)

Только аутентифицированные пользователи имеют доступ к API.(+)

Реализовано документирование (swagger, redoc).(+)
