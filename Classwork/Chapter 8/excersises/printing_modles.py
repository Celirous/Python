print('\n') 

from printing_functions import build_profile, make_car

user_profile = build_profile(    'marie', 'curie',
    location='paris',
    field='chemistry',
    discoveries=['radioactivity', 'polonium', 'radium'],
    awards=['Nobel Prize in Physics', 'Nobel Prize in Chemistry'])
print("User profile:")
print(f"\t{user_profile}")

print('\n')

car = make_car(
    'mercadies', 
    "C63",
    color='silver',
    tire_pressure="2.2 bar"
)
print("car info:")
print(f'\t{car}')

print('\n')
