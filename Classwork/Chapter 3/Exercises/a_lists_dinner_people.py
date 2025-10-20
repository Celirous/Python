print('\n')

friend_names = ['james', 'frank', 'ciNDy', 'alice']
print(friend_names[0].title())
print(friend_names[1].title())
print(friend_names[2].title())
print(friend_names[3].title())

print('\n')


print(f'I have been friends with {friend_names[0].title()} for about 5 years now.')
print(f'I have been friends with {friend_names[3].title()} for about 5 years now.')

print('\n')

trans_mode = ['Bus', 'caR', 'subway system', 'bikes']

print(f"I really enjoy being on the {trans_mode[0]} on the weekdays")

print('\n')


fav_people = ['James Dean', 'Neal Patric Harris', 'Opra']
print(f'Hey there {fav_people[0]}, would you please attend tonight\'s get together? It will be hosted at my place later.')
print(f'Hey there {fav_people[1]}, would you please attend tonight\'s get together? It will be hosted at my place later.')
print(f'Hey there {fav_people[2]}, would you please attend tonight\'s get together? It will be hosted at my place later.')

print('\n')

print(f'As it turns out, {fav_people[2]}, cannot make it. What a shame')

print('\n')

fav_people.pop(2)
print(fav_people)

fav_people.append("Pewdiepie")
print(fav_people)

print('\n')

print(f'We have a replacement, please welcome {fav_people[2]} to the party')

print('\n')

print(f'Hey there {fav_people[0]}, would you please attend tonight\'s get together? It will be hosted at my place later.')
print(f'Hey there {fav_people[1]}, would you please attend tonight\'s get together? It will be hosted at my place later.')
print(f'Hey there {fav_people[2]}, would you please attend tonight\'s get together? It will be hosted at my place later.')

print('\n')

print("More guests will be joining us")

print('\n')

fav_people.insert(0, "Lucas Films")
fav_people.insert(2, "Jonathan")
fav_people.append("JRR Tolken")

print(f'Everyone who is coming tonight is going to be so happy')

print('\n')

print(f'Please wecome our guest for the evening; {fav_people[0]}. So glad to have you here')
print(f'Please wecome our guest for the evening; {fav_people[1]}. So glad to have you here')
print(f'Please wecome our guest for the evening; {fav_people[2]}. So glad to have you here')
print(f'Please wecome our guest for the evening; {fav_people[3]}. So glad to have you here')
print(f'Please wecome our guest for the evening; {fav_people[4]}. So glad to have you here')
print(f'Please wecome our guest for the evening; {fav_people[5]}. So glad to have you here')

print('\n')

print("Oh no, some guests cannot make it anymore")

print('\n')

person_leaving = fav_people.pop(5)
print(f'I am sorry to hear that you cannot make it anymore {person_leaving}')

print('\n')

print(fav_people)

print('\n')

del fav_people[0]
del fav_people[0]
del fav_people[0]
del fav_people[0]
del fav_people[0]

print(fav_people)

print('\n')

print(f'We are inviting {len(fav_people)} people for dinner')






