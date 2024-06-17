def test_hello_world(capsys):
    from ..student_code import hello_world
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

def test_greet(capsys):
    from ..student_code import greet
    name = "Alice"
    greet(name)
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"

def test_print_full_name(capsys):
    from ..student_code import print_full_name
    first_name = "Alice"
    last_name = "Smith"
    print_full_name(first_name, last_name)
    captured = capsys.readouterr()
    assert captured.out == "Alice Smith\n"
