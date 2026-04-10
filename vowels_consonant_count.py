n=input("Enter a word :")
vowel=0
cons=0

for char in n:
    if 'A' <= char <= 'Z':
        char=chr(ord(char)+32)

    if 'a'<= char <='z':
        if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
            vowel+=1
        else:
            cons+=1

print(f"number of vowels {vowel}")
print(f"number of consonant {cons}")