import re
import os

html = open('index.html', encoding='utf-8').read()
match = re.search(r'<script type="text/babel">(.*?)</script>', html, re.DOTALL)
if match:
    jsx = match.group(1)
    with open('temp.jsx', 'w', encoding='utf-8') as f:
        f.write(jsx)
    print("Extracted jsx to temp.jsx")
else:
    print("Could not find babel script block")
