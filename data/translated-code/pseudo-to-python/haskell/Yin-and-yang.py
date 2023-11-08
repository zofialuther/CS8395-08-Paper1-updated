from diagrams import *
from diagrams.backends import Cairo

def yinyang():
    perim = arc(0, 360) * scale(1/2)
  
    torus = circle(1/3) * fc(black) + circle(1) * fc(white)
  
    xform = translateY(-1/4) * scale(1/4)
  
    base = rect(1/2, 1) * fc(white) + rect(1/2, 1) * fc(black)
  
    result = lw(0) * (perim + lw(0.003) + torus + xform + torus + xform(-1) + clipBy(perim, base))
  
    return result

def main():
    yinYangDiagram = yinyang()
  
    result = defaultMain(pad(1.1, beside(2, -1, yinYangDiagram, scale(1/4, yinYangDiagram))))
  
    return result