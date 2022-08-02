from dataclasses import dataclass

import pytest


@pytest.mark.fast
def test_with_param():
	pass

# кей - валью в скобках []
# @pytest.mark.parametrize("browser, user",
#                          [
# 	                         pytest.param("firefox", 1, id="Firefox with first user"),
# 	                         pytest.param("chrome", 2, id="Chrome with second user"),
# 	                                        marks=[pytest.mark.xfail(reason="Why")])
# 						 ]
#                          )

def test_with_param2(browser, user):
	pass


@pytest.mark.parametrize("browser", ["Chrome", "Firefox"])
@pytest.mark.parametrize("user", [1, 2], ids=["First user", "Second user"])
def test_with_param_again(browser, user):
	pass


@pytest.fixture(params=["Chrome", "Firefox"])
def browser(request):
	return request.param + " from fixture"

@pytest.fixture(params=[])
def prepare_user(request):
	if not hasattr(request, "param"):
		raise ValueError("Параметризуй фикстуру!")

def test_with_parametrized_fixture(browser):
	pass

@pytest.mark.parametrize("prepare_user", [1, 2, 3], indirect=True)
def test_with_user(prepare_user):
	pass


# параметризация фикстуры browser только для хрома при помощи indirect - твердо и четко
@pytest.mark.parametrize("browser", ["Chrome"], indirect=True)
def test_with_parametrized_fixture_only_chrome(browser):
	assert browser in ["Chrome from fixture", "Firefox from fixture"]




chrome = pytest.mark.parametrize("browser", ["Chrome"], indirect=True)


# вторая версия - параметризация фикстуры browser только для хрома
@chrome
def test_with_parametrized_fixture_only_chrome(browser):
	assert browser in ["Chrome from fixture", "Firefox from fixture"]




@pytest.mark.parametrize("value", {1, 2, 4, 8, 3, 4, 5, 5, 5, 5})
def test_order(value):
	pass

@dataclass
class User:
	id: int
	name: str
	age: int
	description: str

	def __repr__(self):
		return f"<{self.id} {self.name}>"


user1 = User(id=1, name="Mario", age=32, description="something " * 10)
user2 = User(id=2, name="Wario", age=62, description="else " * 10)


def get_user_name(user):
	return user.name


#@pytest.mark.parametrize("user", [user1, user2], ids=get_user_name)
@pytest.mark.parametrize("user", [user1, user2], ids=repr)
def test_testov(user):
	pass