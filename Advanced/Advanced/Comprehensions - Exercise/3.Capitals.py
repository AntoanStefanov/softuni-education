countries = input().split(', ')
capitals = input().split(', ')

zipped_data = list(zip(countries, capitals))


dict_comprehension = {country: capital for country,
                      capital in zipped_data}


{print(f'{country} -> {capital}')
 for country, capital in dict_comprehension.items()}
