alpha=str(input())
if(alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u' or alpha == 'A'
       or alpha == 'E' or alpha == 'I' or alpha == 'O' or alpha == 'U'):
    print("vowel")
elif(alpha>='a' and alpha<='z')or(alpha>='A' and alpha<='Z'):
    print("Consonant")
else:
    print("invalid")
