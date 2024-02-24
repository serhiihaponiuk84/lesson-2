star = "* "
whitespaces = "  "
border = "- "
side = "| "

print("а)")
stars_count = 8
whitespaces_count = 0
border_count = stars_count + whitespaces_count + 2
for i in range(border_count):
    if i == 0 or i == border_count - 1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            print(star, end="")
        print(side, end="")
        whitespaces_count += 1
        stars_count -= 1
    print()
print()

print("б)")
stars_count= 1
whitespaces_count = 7
border_count = stars_count + whitespaces_count + 2
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(side, end="")
        whitespaces_count -= 1
        stars_count += 1
    print()
print()

print("в)")
stars_count = 9
whitespaces_count = 0
border_count = stars_count + whitespaces_count + 2
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            print(star, end="")
        if stars_count > 0:
            stars_count -= 2
            whitespaces_count += 1
        for j in range(whitespaces_count - 1):
            print(whitespaces, end="")
        print(side, end="")
    print()
print()

# производная из варианта "д"
print("г)")
stars_count = 9
whitespaces_count = 0
border_count = stars_count + whitespaces_count + 2
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            if i < border_count // 2:
                print(whitespaces, end="")
            else:
                print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(side, end="")
        if i < border_count // 2:
            stars_count -= 2
            whitespaces_count += 1
        else:
            stars_count += 2
            whitespaces_count -= 1
    print()
print()

# производная из варианта "д"
print("г)")
stars_count = 9
whitespaces_count = 0
border_count = stars_count + whitespaces_count + 2
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            if i >= border_count // 2:
                print(star, end="")
            else:
                print(whitespaces, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(side, end="")
        if i < border_count // 2:
            stars_count -= 2
            whitespaces_count += 1
        else:
            stars_count += 2
            whitespaces_count -= 1
    print()
print()

print("д)")
stars_count = 9
whitespaces_count = 0
border_count = stars_count + whitespaces_count + 2
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(side, end="")
        if i < border_count // 2:
            stars_count -= 2
            whitespaces_count += 1
        else:
            stars_count += 2
            whitespaces_count -= 1
    print()
print()

print("е)")
stars_count = 1
whitespaces_count = 7
border_count = 11
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            if j < (border_count // 2 - 1):
                print(star, end="")
        print(side, end="")
        if (i < border_count // 2):
            stars_count += 1
            whitespaces_count -= 2
        else:
            stars_count -= 1
            whitespaces_count += 2
    print()
print()

# производная из варианта "е"
print("ж)")
stars_count = 1
whitespaces_count = 7
border_count = 11
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            if j < (border_count // 2 - 1):
                print(whitespaces, end="")
        print(side, end="")
        if (i < border_count // 2):
            stars_count += 1
            whitespaces_count -= 2
        else:
            stars_count -= 1
            whitespaces_count += 2
    print()
print()

# производная из варианта "е"
print("з)")
stars_count = 1
whitespaces_count = 7
border_count = 11
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(stars_count):
            if j < (border_count // 2 - 1):
                print(whitespaces, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
                print(star, end="")
        print(side, end="")
        if (i < border_count // 2):
            stars_count += 1
            whitespaces_count -= 2
        else:
            stars_count -= 1
            whitespaces_count += 2
    print()
print()

print("и)")
stars_count = 8
whitespaces_count = 0
border_count = stars_count + whitespaces_count + 2
for i in range(border_count):
    if i == 0 or i == border_count - 1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(stars_count):
            print(star, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        print(side, end="")
        whitespaces_count += 1
        stars_count -= 1
    print()
print()

print("к)")
stars_count = 1
whitespaces_count = 8
border_count = stars_count + whitespaces_count + 2
for i in range(border_count):
    if i == 0 or i == border_count -1:
        for j in range(border_count):
            print(border, end="")
    else:
        print(side, end="")
        for j in range(whitespaces_count):
            print(whitespaces, end="")
        for j in range(stars_count):
            print(star, end="")
        print(side, end="")
        whitespaces_count -= 1
        stars_count += 1
    print()
print()
