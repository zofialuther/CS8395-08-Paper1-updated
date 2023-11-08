from diagrams import *
from diagrams.backends import Cairo, CmdLine

def eqTriangle(fc, lw):
  return eqTriangle(fc=black, lw=0)

def reduce(t):
  return t | t

def iterate(reduce, triangle):
  return reduce(triangle)

def main(sierpinski):
  return defaultMain(sierpinski[7])