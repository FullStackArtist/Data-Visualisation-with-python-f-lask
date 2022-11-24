import os
import sys

def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         val=(os.path.join(root, filename))
         result.append(os.path.abspath(val))
   return result

fpath=find_files(sys.argv[0],"C:")
for i in fpath:
    print(i)
