from django.shortcuts import render
from . import api_cnpj

# Create your views here.
def index(request):
	return render(request, 'index.html')

def api(request):
	cnpj = request.GET.get('cnpj')
	api = api_cnpj.CNPJ(cnpj)
	api.consulta()
	if (api.demonstra == 'Por favor, verifique se o número digitado está correto'):
		resultado = {'nome': 'Por favor, verifique se o número digitado está correto'}
		
		contexto = {}
		contexto['resultado'] = resultado
		
		return render(request, 'index.html', contexto)
	elif (api.demonstra == 'Por favor, Insira um cnpj com 14 dígitos e sem . / ou -'):
		resultado = {'nome': 'Por favor, insira um cnpj com 14 dígitos e sem . / ou -'}

		contexto = {}
		contexto['resultado'] = resultado
		
		return render(request, 'index.html', contexto)
	else:
		resultado = api.demonstra

		contexto = {}
		contexto['resultado'] = resultado

		return render(request, 'form.html', contexto)