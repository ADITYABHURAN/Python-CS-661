# Leap year check for Annie and Jane
annie_birth_year = 1996
jane_birth_year = 1999

if (annie_birth_year % 4 == 0 and (annie_birth_year % 100 != 0 or annie_birth_year % 400 == 0)):
    print("Annie was born in a leap year.")
elif (jane_birth_year % 4 == 0 and (jane_birth_year % 100 != 0 or jane_birth_year % 400 == 0)):
    print("Jane was born in a leap year.")
else:
    print("Neither was born in a leap year.")

# School canteen breakfast logic
sam_age = 10

if sam_age < 9:
    print("Sam gets milk porridge.")
elif 10 <= sam_age <= 14:
    print("Sam gets a sandwich.")
elif 15 <= sam_age <= 17:
    print("Sam gets a burger.")
else:
    print("Sam does not qualify for school breakfast.")
