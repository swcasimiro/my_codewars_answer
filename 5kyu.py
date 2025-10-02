
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
def first_non_repeating_letter(s):
    lst = [i for i in s if s.lower().count(i.lower()) == 1]

    if len(lst) > 0:
        return lst[0]

    else:
        return ""