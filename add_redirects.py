import os

files = os.listdir('_rules')

for file_name in files:
    path = f'_rules/{file_name}'
    html_name = file_name.replace('.md', '.html')

    f = open(path, "r")
    contents = f.readlines()
    f.close()

    redirect_url = f'redirect_to: https://www.flake8rules.com/rules/{html_name}\n'
    contents.insert(1, redirect_url)

    f = open(path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
