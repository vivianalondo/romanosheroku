# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *
import math

# Create your views here.
def index(request):
	return render(request, 'index.html')


def convert(request):
	Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
	Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
	Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
	if request.method == 'POST':
		N=int(request.POST.get('textfield', None))
		u=N % 10
		d=int(math.floor(N/10))%10
		c=int(math.floor(N/100))
		if (N>=100):
			html = ("<H1> El número ",N," en romano es: ",Centena[c]+Decena[d]+Unidad[u],"</H1>")
			return HttpResponse(html)
		else:
			if (N>=10):
				html = ("<H1> El número ",N," en romano es: ",Decena[d]+Unidad[u],"</H1>")
				return HttpResponse(html)
			else:
				html = ("<H1> El número ",N," en romano es: ",Unidad[N],"</H1>")
				return HttpResponse(html)
	else:
		return render(request, 'index.html')

