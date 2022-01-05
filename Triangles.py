from math import *
a=input('entrer une première valeur:')
b=input('entrer une deuxième valeur:')
c=input('entrer une troisième valeur:')

if a<=b<=c:
    print('Arrangement ok de valeurs!')
if a+b>=c:
    print('Un triangle existe avec ces valeurs!')
if pow(float(a),2)+pow(float(b),2)==pow(float(c),2):
    print('On a affaire à un triangle rectangle')
if a==b==c:
    print('On a affaire à un triangle équilatéral')
if a==b or a==c or b==c:
    print('On a affaire à un triangle isocèle')
if (-float(a)**2+float(b)**2+float(c)**2/2*float(b)*float(c))>=0 and (float(a)**2-float(b)**2+float(c)**2/2*float(a)*float(c))>=0 and (-float(a)**2+float(b)**2-float(c)**2/2*float(a)*float(b))>=0:
    print('Les angles sont aigus')
      

