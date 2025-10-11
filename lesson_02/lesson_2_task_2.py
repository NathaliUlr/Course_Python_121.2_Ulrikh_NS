def is_year_leap(year: int):
    return True if year % 4 == 0 else False


selected_year = 2025
result = is_year_leap(selected_year)
print(f"Год {selected_year}: {result}")
