#!/usr/bin/env python3.7

message = input("Enter a message: ")

print("First Character:", message[0])
print("Last Character", message[-1])
print("Middle Character:", message[int(len(message) /2)])
print("Even Index Characters:", message[::2])
print("Odd Index Characters:", message[1::2])
print("Reversed Message:", message[::-1])