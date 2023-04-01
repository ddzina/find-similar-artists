# Поиск похожих артистов на данного

## Установка и запуск

### Клонирование репозитория

Клонируйте репозиторий в удобную папку и перейдите в нее:

```
git clone https://github.com/ddzina/find-similar-artists.git
```

### Anaconda environment

Создайте и активируйте виртуальное окружение:

```
conda create -n name
conda activate name
```

Установите pip: 

```
conda install pip
```

### Venv

Создайте и активируйте виртуальное окружение:

```
python -m venv name
source name/bin/activate (Linux)
venv\Scripts\activate.bat (Windows)
```

Установите зависимости:

```
pip install -r requirements.txt
```

### Запуск

Запустите приложение:

```
python main.py
```

# Описание проделанной работы:
Для определения похожих артистов был использован метод коллаборативной фильтрации.
* Сначала формируется словарь из пользователей и значений scrobbles для каждого артиста.
* Scrobbles интерпретируются как мера интереса к артисту: больше - лучше.
* Получив на вход имя артиста, ищем "самого преданного" фаната - пользователя с наибольшим scrobbles для данного артиста.
* Затем находим схожих пользователей, используя меру близости - косинусное расстояние между векторами scrobbles.
* Умножаем значение scrobbles на меру для каждого пользователя, чтобы более похожие пользователи сильнее влияли на результат.
* Далее для всех артистов считаем сумму данных произведений (откалиброванных мер) и делим на сумму мер для выбранных пользователей,
тем самым нормируя значения коэффицентов релевантости для артистов.
* Сортируем артистов по убыванию данного коэффицента и получаем наиболее похожих артистов на введенного. Profit!

# Описание файлов в проекте
* collaboration.ipynb - "черновик", файл, в котором писался и тестировался код
* funcs.py - файл с основными функциями, реализующими всю логику
* main.py - исполняемый файл

# Пример работы программы
https://drive.google.com/file/d/17o4n46WMeFN5y6myjgm8G2Fb-KmV2xYa/view?usp=share_link
