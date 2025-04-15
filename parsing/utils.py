def clean_number(parsed_data: str) -> str:
    number = ""

    for char in parsed_data:
        if char.isdigit() or char in '.,':
            number += char

    return number.replace(',', '.')


