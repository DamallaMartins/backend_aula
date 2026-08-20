from django.shortcuts import render
from .models import Aluno

def aluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno.html', {'alunos': alunos})

# Create your views here.
