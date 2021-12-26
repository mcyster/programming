#!/usr/bin/python
import turtle

pen = turtle.Turtle()
pen.up()
pen.backward(100)
pen.down()


def flake_side(angle, length):
  pen.left(angle)
  pen.forward(length)
  if length > 1:
    flake_point(angle, length / 3)
  else:
    pen.forward(length)
  pen.forward(length)
  pen.right(angle)


def flake_point(angle, length):
  flake_side(angle, length)
  pen.right(180 - angle)
  flake_side(angle, length)
  pen.right(180 + angle)

for i in range(4):
  flake_point(60, 90)
  pen.right(90)
