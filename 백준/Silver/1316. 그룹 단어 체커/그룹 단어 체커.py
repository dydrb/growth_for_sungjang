x = int(input())
group_word = x

for i in range(x) :
    word = input()
    for j in range(len(word)-1) :
        if word[j] == word[j+1] :
            continue
        
        elif word[j] in word[j+1:] :
            group_word -= 1
            break

print(group_word)