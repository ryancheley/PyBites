import re


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    code_text_original = re.findall(r'(<code\b[^>]*>(.*?)<\/code>)', org_text.replace('\n', ' '), re.DOTALL)
    for i, c in enumerate(re.finditer(r'<code\b[^>]*>(.*?)<\/code>', trans_text)):
        trans_text = trans_text.replace(c.group(), code_text_original[i][0])

    pre_text_original = re.findall(r'(<pre\b[^>]*>(.*?)<\/pre>)', org_text, re.DOTALL)
    for j, p in enumerate(re.finditer(r'<pre\b[^>]*>(.*?)<\/pre>', trans_text)):
        trans_text = trans_text.replace(p.group(), pre_text_original[j][0])
    return trans_text
