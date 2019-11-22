def test_input_text(expected_result, actual_result):
     assert expected_result == actual_result, (f"expected {expected_result}, got {actual_result}")

#"Let's count together! {}, then goes {}, and then {}".format("one", "two", "three") # using .format for message about extension 

#str1 = "one" # using f for message about extension
#str2 = "two"
#str3 = "third"
#(f"Let's count together! {str1}, then goes {str2}, and then {str3}")

test_input_text(8,11)

# Для закрепления материала реализуйте проверку самостоятельно. 
# Вам дана функция test_input_text,  которая принимает два значения: expected_result - ожидаемый результат, и actual_result - фактический результат. 
# Обратите внимание, input использовать не нужно!Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. 