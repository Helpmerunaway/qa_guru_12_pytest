# Аргументы запуска. Собираем фикстуры, марки, и другую полезную информацию:

### список тестов
--co

pytest --co

### вхождение подстроки из имени тестов
-k

pytest -k "simple"

для запуска выбранных тестов, например:
pytest -k "(homework and mobile) or simple" --co ./

### маркеры
pytest --markers

### фикстуры используемые в проекте

pytest --fixtures

tmpdir

### поиск самых долгих тестов и самые долгие предусловия

pytest --durations=10

### делает наш лог читаемым (например выводит переменную )

pytest -l 

### план запуска - тесты + фикстуры (сетап + тирдаун)

pytest --setup-plan

### Параметризация. На тесте, на фикстуре. Переопределение параметров

pytest.mark.parametrize