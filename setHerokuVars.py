#!/usr/local/bin/python3
import os
import sys


def setVar(key, value,app_name):
  print(f'heroku config:set {key}={value} --app {app_name}')
  os.system(f'heroku config:set {key}={value} --app {app_name}')


def setVarsFromFile(filename,app_name):  
  if not os.path.exists(filename):
    print("No file found for: ",filename)
    return

  with open(filename) as f:
    lines = f.read().split('\n')
    print("Contents from ",filename,":")
    print("\n".join(lines))
    for line in lines:
      try:
        [key, value] = line.split('=')
        setVar(key, value,app_name)
      except:
        if line!="":
          print("skipping line:",line)

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 setHerokuVars.py NAME_OF_APP")
    exit(1)

  app_name = sys.argv[1]

  print(f'heroku config:set SPRING_PROPERTIES="$(cat secrets-heroku.properties)" "$@" --app {app_name}')
  os.system(f'heroku config:set SPRING_PROPERTIES="$(cat secrets-heroku.properties)" "$@" --app {app_name}')

  setVarsFromFile('javascript/.env.production',app_name)
  setVarsFromFile('javascript/.env.local',app_name)

if __name__=="__main__":
  main()
