"""Unit converter: temperature, length, weight."""

TEMP_UNITS = ['celsius', 'fahrenheit', 'kelvin']
LENGTH_UNITS = ['meters', 'kilometers', 'miles', 'feet']
WEIGHT_UNITS = ['kg', 'grams', 'pounds', 'ounces']


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def fahrenheit_to_kelvin(f):
    """Convert Fahrenheit to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius."""
    return k - 273.15


def kelvin_to_fahrenheit(k):
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between celsius, fahrenheit and kelvin."""
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'kelvin':
            return celsius_to_kelvin(value)
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'kelvin':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return kelvin_to_celsius(value)
        elif to_unit == 'fahrenheit':
            return kelvin_to_fahrenheit(value)
    return None


def meters_to_km(m):
    """Convert meters to kilometers."""
    return m / 1000


def meters_to_miles(m):
    """Convert meters to miles."""
    return m * 0.000621371


def meters_to_feet(m):
    """Convert meters to feet."""
    return m * 3.28084


def convert_length(value, from_unit, to_unit):
    """Convert length between meters, kilometers, miles and feet."""
    conversions = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.344,
        'feet': 0.3048
    }
    if from_unit not in conversions or to_unit not in conversions:
        return None
    value_in_meters = value * conversions[from_unit]
    return value_in_meters / conversions[to_unit]


def convert_weight(value, from_unit, to_unit):
    """Convert weight between kg, grams, pounds and ounces."""
    conversions = {
        'kg': 1,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    if from_unit not in conversions or to_unit not in conversions:
        return None
    value_in_kg = value * conversions[from_unit]
    return value_in_kg / conversions[to_unit]


def print_result(value, from_unit, to_unit, result):
    """Print formatted conversion result."""
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")


if __name__ == '__main__':
    print("=== Unit Converter ===")

    print("\n-- Temperature --")
    print_result(
        100, 'celsius', 'fahrenheit',
        convert_temperature(100, 'celsius', 'fahrenheit')
    )
    print_result(
        0, 'celsius', 'kelvin',
        convert_temperature(0, 'celsius', 'kelvin')
    )

    print("\n-- Length --")
    print_result(
        1000, 'meters', 'kilometers',
        convert_length(1000, 'meters', 'kilometers')
    )
    print_result(
        1, 'miles', 'kilometers',
        convert_length(1, 'miles', 'kilometers')
    )

    print("\n-- Weight --")
    print_result(
        1, 'kg', 'pounds',
        convert_weight(1, 'kg', 'pounds')
    )
    print_result(
        500, 'grams', 'pounds',
        convert_weight(500, 'grams', 'pounds')
    )
