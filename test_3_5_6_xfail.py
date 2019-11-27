import pytest

def test_succeed():
    if not True:
        pytest.xfail("failing configuration (but should work)")
    assert False

@pytest.mark.xfail
def test_not_succeed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False

# Изучите самостоятельно документацию про маркировку xfail. Найдите там параметр, который в случае неожиданного прохождения теста, помеченного как xfail, 
# отметит в отчете этот тест как упавший. Пометьте таким образом первый тест из этого тестового набора.

# Запустите полученные тесты. Обратите внимание на статус прогона тестов. Найдите последнюю строчку с итогами запуска, скопируйте текст между 
# символами == и отправьте его в качестве ответа на это задание. 