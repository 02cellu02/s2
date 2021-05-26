#pathlib
from pathlib import Path
path=Path("ecommerce")
print(path.exists())
#path1=Path("email")
#path1.mkdir() to create a directory
#path1.rmdir() to remove a directory
path1=Path()
for i in (path1.glob('*.py')):#search all py files in s2 folder#('*')gives all files
    print(i)

for i in (path1.glob('*')):
    print(i)
    