"""

\d
\w
+
?

"""

import re

# strin = "test 123_du1pa+test"
# output_1 = re.sub(r"[ _+]", "", strin)
# output_2 = re.findall(r"[dupa]", strin)
# compiled_regex = re.compile(r"[dupa]")
# output_3 = re.findall(compiled_regex, strin)
# output_4 = re.match(r"d", strin)
# output_5 = re.search(r"dupa", strin)

# st: set = set()
#
# with open("7-RegEx_example", "r") as file:
#     for line in file:
#         if text := re.findall(r"(?<=\* Cell {13}: )\w+", line):
#             st.add(text[0].strip())

with open("7-RegEx_example2", encoding='cp850') as file:
    line = file.readline()
    users = re.split(r"(?={\"gender)", line)[1:]
    for user in users:
        email = re.split(r"[.@]", re.findall(r"(?<=\"email\":\")[a-zA-z.@]*", user)[0])

        print("pass")
