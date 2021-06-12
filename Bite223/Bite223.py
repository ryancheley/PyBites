
def _helper(permission_string: str) -> int:
    permission_score = 0
    if permission_string == 'r':
        permission_score += 4
    elif permission_string == 'w':
        permission_score += 2
    elif permission_string == 'x':
        permission_score += 1
    return permission_score


def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
       its octal representation.

       In Unix you have user, group and other permissions,
       each can have read (r), write (w), and execute (x)
       permissions expressed by r, w and x.

       Each has a number:
       r = 4
       w = 2
       x = 1

       So this leads to the following input/ outputs examples:
       rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
       rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
       r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """
    user_permissions = rwx[0:3]
    output_permission_string_user = 0
    group_permissions = rwx[3:6]
    output_permission_string_group = 0
    other_permissions = rwx[6:9]
    output_permission_string_other = 0


    for u in user_permissions:
        output_permission_string_user += _helper(u)
    for g in group_permissions:
        output_permission_string_group += _helper(g)
    for o in other_permissions:
        output_permission_string_other += _helper(o)
    output_permission_string = str(output_permission_string_user) + str(output_permission_string_group) + str(output_permission_string_other)

    return output_permission_string


# ('-----x-w-', '012'), ('-----x-wx', '013'), ('-----xr--', '014')

input_string = '-----x-w-'

test = get_octal_from_file_permission(input_string)
print(test)