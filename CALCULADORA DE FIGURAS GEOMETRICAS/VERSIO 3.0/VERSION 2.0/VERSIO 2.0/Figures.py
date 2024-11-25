import math

def rectangleArea(height, weight):
    """Calcula el área del rectangulo"""
    return height * weight

def triangleArea(base, height):
    """Calcula el área del triangulo"""
    return (base * height) / 2

def squareArea(side):
    """Calcula el área de un Cuadrado"""
    return math.pow(side, 2)

def circleArea(radius):
    """Calcula el área del circulo"""
    return math.pi * math.pow(radius, 2)

def pentagonArea(perimeter, apotema):
    """Calcula el área del Pentagono"""
    return (perimeter * apotema) / 2

def trapezeArea(maxBase, minBase, height):
    """Calcula el área del Trapecio"""
    return ((maxBase + minBase) * height) / 2

def romboidwArea(base, height):
    """Calcula el área del Romboide"""
    return base * height

def diamondArea(maxDiagonal, minDiagonal):
    """Calcula el área del Rombo"""
    return (maxDiagonal * minDiagonal) / 2
