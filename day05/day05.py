# https://adventofcode.com/2024/day/5

with open('input.txt') as f:
    [rules_raw, updates] = [data.splitlines() for data in f.read().split('\n\n')]

    rules = dict() # key_page must come before val_pages
    for rule in rules_raw:
        key, val = rule.split('|')
        if key in rules:
            rules[key].append(val)
        else:
            rules[key] = [val]

# Part One

def page_is_correct(i, page, pages):
    if page not in rules:
        return True
    for rule in rules[page]:
        if rule in pages[:i]:
            return False
    return True

def update_is_correct(pages):
    for i, page in enumerate(pages):
        if page_is_correct(i,page, pages):
            continue
        return False
    return True

sum = 0
for update in updates:
    pages = update.split(',')
    if update_is_correct(pages):
        sum += int(pages[len(pages) // 2])
print(sum)


# Part Two

def order_correctly(pages):
    for i, page in enumerate(pages):
        while i > 0:
            if not page_is_correct(i, page, pages):
                pages[i], pages[i-1] = pages[i-1], pages[i]
            i -= 1
    return pages

sum = 0
for update in updates:
    pages = update.split(',')
    if not update_is_correct(pages):
        pages = order_correctly(pages)
        sum += int(pages[len(pages) // 2])
print(sum)