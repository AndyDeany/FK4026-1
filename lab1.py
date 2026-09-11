"""
Lab 1: temperaturkonvertering
"""
def fahrenheit_to_celsius(temperature_fahrenheit):
    """Konvertera den givna temperaturen från Fahrenheit till Celcius."""
    return (temperature_fahrenheit - 32) * 5/9


def celsius_to_fahrenheit(temperature_celcius):
    """Konvertera den givna temperaturen från Celcius till Fahrenheit."""
    return (temperature_celcius * 9 / 5) + 32


def convert_temperature(temperature, scale):
    """Konvertera °F/°C till den andra."""
    if scale == "F":
        return fahrenheit_to_celsius(temperature)
    elif scale == "C":
        return celsius_to_fahrenheit(temperature)
    else:
        raise ValueError(f"Ogiltig temperaturenhet: '{scale}'")


def get_temperature_from_user():
    try:
        return int(input())
    except ValueError:
        print("Ogiltig temperatur värde - måste vara ett tal.")


TEMPERATURE_SCALES = {
    # Förkortning: Fullt namn
    "F": "Fahrenheit",
    "C": "Celsius",
}


def main():
    print("Välkommen till Temperature Converter!")
    while True:
        print("Vilken temperaturenhet vill du omvandla från?")
        print("Svara 'F' för Fahrenheit och 'C' för Celcius, eller 'q' för att avsluta programmet:")
        answer = input()

        if answer == "q":
            print("Tack för att du använde Temperature Converter!")
            return

        input_scale = answer.upper()  # Gör input till versaler för att underlätta jämförelser
        if input_scale not in TEMPERATURE_SCALES.keys():
            print(f"Ditt svar '{answer}' är inte en godkänd enhet. Försök igen.")
            continue

        output_scale = {"F": "C", "C": "F"}[input_scale]    # Vi konvertera bara mellan °F/°C för nu

        print(f"Ange en temperatur i {TEMPERATURE_SCALES[input_scale]}: ")
        input_temperature = get_temperature_from_user()
        converted_temperature = convert_temperature(input_temperature, input_scale)
        print(f"{TEMPERATURE_SCALES[output_scale]}: {converted_temperature}\n")


if __name__ == "__main__":
    main()