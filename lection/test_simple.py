import pytest
import time


@pytest.fixture()
def browser():
	"""
	dockstring - описание функции
	Фикстура возвращает браузер
	:return:
	"""
	time.sleep(1)


# можем скрыть фикстуру в маркер
@pytest.mark.usefixtures("browser")
def test_first():
	time.sleep(1)

# можем пропустить варнинг
@pytest.mark.filterwarnings("some")
def test_second(browser):
	time.sleep(1)

# указываем причину скипа теста
@pytest.mark.skip(reason="Этот тест еще не завершен TASK-123")
def test_third(browser):
	pytest.skip("Reason")
	time.sleep(1)

# да мы знаем что он падает, когда он перестанет падать будет проходить
@pytest.mark.xfail(reason="Причина", raises=(AssertionError, ZeroDivisionError))
def test_fourth():
	time.sleep(1)
	1 / 0


# можно найти место где возникает Ексепшен
@pytest.mark.xfail(reason="Причина")
def test_five():
	time.sleep(1)
	try:
		assert False
	except AssertionError:
		pytest.xfail(reason="Причина")


def test_six(browser):
	import random
	a = random.randint(0, 10)
	assert a > 5