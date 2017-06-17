from foneticaBR import foneticaBR
from buscabr import buscaBR

chaveRoberto = foneticaBR()
chavebr = buscaBR()

texto = 'JOSSEPH ARCADIANO DA CRUZ'
print chaveRoberto.chavefonetica(texto)
print chavebr.chaveBR(texto,False)
print chavebr.chaveBR(texto,True)
