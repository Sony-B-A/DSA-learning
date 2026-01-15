main_list = ["Sony", "Aishu", "Varha", "Punya", "Amruta", "Akshara"]
def classify(l):
    l1 = []
    l2 = []
    for word in l:
        if(word.startswith("a") or word.startswith("A")):
            l1.append(word)
        else:
            l2.append(word)
    return l1, l2

start_with_A, start_with_other_than_A = classify(main_list)

print(f"Words that starts with A/a:\n{start_with_A}\nWords that starts withe any alphabet but a/A:\n{start_with_other_than_A}")