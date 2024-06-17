import student_code

def test_hello():
    assert student_code.hello_world() == "Hello World!"

def test_greet():
    name = "Alice"
    assert student_code.greet(name) == "Hello, Alice!"

def test_print_full_name(capsys):
    first_name = "Alice"
    last_name = "Smith"
    assert student_code.print_full_name(first_name, last_name) == "Alice Smith"
