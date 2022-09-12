from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

def home(self, name):
    return HttpResponse(f'Hola soy {name}')

def homepage(self):
    lista = [1,2,3,4,5,6,7,8,9,10]
    data = {'nombre':'Hernán','apellido':'Luna','lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    #planilla = loader.get_template('cursos.html')
    curso = Curso(nombre="UX/UI" , camada="12345")
    curso.save()
    
    documento = f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse(documento)
    