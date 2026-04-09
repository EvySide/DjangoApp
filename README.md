# DjangoApp

### 1. Клонируйте репозиторий 
```
git clone https://github.com/EvySide/DjangoApp.git
cd DjangoFirstApp
```

### 2. Создайте виртуальное окружение и его активируйте
```
python -m venv djevenv
.\djevenv\Scripts\activate
```

### 3. Установите зависимости
```
pip install -r requirements.txt
```

### 4. Примените миграции db
```
cd storeinventory\
python manage.py migrate
```

### 5. Запустите сервер
```
python manage.py runserver
```

