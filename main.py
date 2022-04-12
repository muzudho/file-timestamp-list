import os
import glob
import re
import sys
from datetime import datetime

# 日本のWindows は "cp932" なので、Unicodeに変換
sys.stdout.reconfigure(encoding='utf-8')

# ディレクトリーを選んでください
while True:
    print("""Which directory?
Example: .""")

    path = input()
    os.chdir(path)

    # フィル名を一覧します
    print(f"""Current directory: {os.getcwd()}

Files
-----""")

    files = glob.glob("./*")

    # とりあえず一覧します
    for file in files:
        basename = os.path.basename(file)
        print(basename)

    print("""
Are you sure this is the right directory (y/n)?""")

    answer = input()

    if answer == "y":
        break
    else:
        print("Canceld")

# 表示します
print("""
Result
------""")

countOfSimulation = 0

for i, file in enumerate(files):
    basename = os.path.basename(file)

    tick = os.path.getctime(file)
    creation = datetime.fromtimestamp(tick).strftime('%Y-%m-%d')

    tick = os.path.getmtime(file)
    modified = datetime.fromtimestamp(tick).strftime('%Y-%m-%d')

    tick = os.path.getatime(file)
    access = datetime.fromtimestamp(tick).strftime('%Y-%m-%d')

    print(f"({i+1}) {basename} --> C[{creation}] M[{modified}] A[{access}]")
    countOfSimulation += 1

print(f"""
Created, Modified, Access.

Count of simulation = {countOfSimulation}""")
