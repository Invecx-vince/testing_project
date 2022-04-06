import os

if __name__ == '__main__':
  cmd = 'python -m unittest discover -v -p scenario*.py'
  os.system(cmd)