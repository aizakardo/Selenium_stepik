def test_input_text(expected_result, actual_result):
     assert expected_result == actual_result, (f"expected {expected_result}, got {actual_result}")
     #return "expected" + expected_result + ", got" + actual_result


#"Let's count together! {}, then goes {}, and then {}".format("one", "two", "three") # using .format for message about extension 

#str1 = "one" # using f for message about extension
#str2 = "two"
#str3 = "third"
#(f"Let's count together! {str1}, then goes {str2}, and then {str3}")

test_input_text(8,11)