
import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    """
    return len(word) >= length


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a period.
    """
    phrase = phrase.strip()
    if not phrase:
        return ""
    sentence = phrase[0].upper() + phrase[1:]
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car.fuel == 0, "Default car fuel should be 0"
    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Fuel should be set correctly"


if __name__ == "__main__":
    run_tests()
    doctest.testmod()

