#!/usr/bin/python3
import os
p = input("Path to addforward.py:\n")
os.system('gcc wrap_cmd.c -o addforward -DSCRIPTPATH=\\"%s\\"'%p)

p = input("Path to listforwards.py:\n")
os.system('gcc wrap_cmd.c -o listforwards -DSCRIPTPATH=\\"%s\\"'%p)

p = input("Path to removeforward.py:\n")
os.system('gcc wrap_cmd.c -o removeforward -DSCRIPTPATH=\\"%s\\"'%p)
