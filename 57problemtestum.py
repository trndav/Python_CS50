from um import count

def test_count_ok():
    assert count("um, this is ok, um, i guess") == 2
    assert count("Um?") == 1
    assert count("well, um..") == 1
    assert count("You do not need, um.. umbrela") == 1

def test_count_fail():
    assert count("Warum?") == 0
    assert count("This is yummy.") == 0
    assert count("Unagi beats everything.") == 0

if __name__ == "__main__":
    main()
