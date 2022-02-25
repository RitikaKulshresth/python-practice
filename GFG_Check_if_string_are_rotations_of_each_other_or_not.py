def check_if_strings_are_rotations_of_each_other_or_not(s1,s2):
    comb_str=''
    s=s1*2

    if len(s1)!=len(s2):
        return False

    if s2 in s:
        return True
    else:
        return False


s1='mightandmagic'
s2='andmagicmigth'
print(check_if_strings_are_rotations_of_each_other_or_not(s1,s2)) 