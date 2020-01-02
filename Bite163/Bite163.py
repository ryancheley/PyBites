import packaging

other_old_reqs = """
twilio==6.23.1
urllib3==1.21.1
Werkzeug==0.12.1
WTForms==1.19.0
"""
other_new_reqs = """
twilio==6.3.0
urllib3==1.21.1
Werkzeug==0.14.1
WTForms==2.1
"""

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    differences = []
    old_reqs_list = old_reqs.split()
    new_reqs_list = new_reqs.split()
    for i in range(len(old_reqs_list)):
        # if tuple(old_reqs_list[i].split('==')[1].split('.')) < tuple(new_reqs_list[i].split('==')[1].split('.')):
        o_major, o_minor, *o_hf = tuple(old_reqs_list[i].split('==')[1].split('.'))
        n_major, n_minor, *n_hf = tuple(new_reqs_list[i].split('==')[1].split('.'))
        if int(n_major) > int(o_major):
            differences.append(old_reqs_list[i].split('==')[0])
        if int(n_major) == int(o_major) and int(n_minor) > int(o_minor):
            differences.append(old_reqs_list[i].split('==')[0])
        if int(n_major) == int(o_major) and int(n_minor) == int(o_minor) and n_hf > o_hf:
            differences.append(old_reqs_list[i].split('==')[0])

    return differences


c = changed_dependencies(other_old_reqs, other_new_reqs)
print(c)