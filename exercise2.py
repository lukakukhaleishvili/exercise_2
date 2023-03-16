n = int(input("enetr number: "))
given_words = input()
def func(words):
    for words in range(n):

        words = list(given_words)
        i = len(words) -1
        while not (i<0 or words[i] < words[i+1] ):
            i-=1

        if i<=0:
            print("no answer")

        j = len(words)-1
        while words[j] <= words[i-1]:
            j-=1

        words[i-1] , words[j] =  words[j],  words[i-1]

        words[i:] = words[len(words)-1:i-1:-1]

    return "".join(words)

print(func(given_words))