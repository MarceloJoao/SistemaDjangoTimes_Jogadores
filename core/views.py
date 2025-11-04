from django.shortcuts import render, redirect, get_object_or_404
from .models import Time, Jogador
from .forms import TimeForm, JogadorForm

# TIMES

def home(request):
    return render(request, 'home.html')
def lista_times(request):
    times = Time.objects.all()
    return render(request, 'lista_times.html', {'times': times})

def novo_time(request):
    form = TimeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_times')
    return render(request, 'form_time.html', {'form': form})

def editar_time(request, id):
    time = get_object_or_404(Time, pk=id)
    form = TimeForm(request.POST or None, instance=time)
    if form.is_valid():
        form.save()
        return redirect('lista_times')
    return render(request, 'form_time.html', {'form': form})

def deletar_time(request, id):
    time = get_object_or_404(Time, pk=id)
    if request.method == 'POST':
        time.delete()
        return redirect('lista_times')
    return render(request, 'confirmar_exclusao.html', {'obj': time})

# JOGADORES
def lista_jogadores(request):
    jogadores = Jogador.objects.select_related('time').all()
    return render(request, 'lista_jogadores.html', {'jogadores': jogadores})

def novo_jogador(request):
    form = JogadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_jogadores')
    return render(request, 'form_jogador.html', {'form': form})

def editar_jogador(request, id):
    jogador = get_object_or_404(Jogador, pk=id)
    form = JogadorForm(request.POST or None, instance=jogador)
    if form.is_valid():
        form.save()
        return redirect('lista_jogadores')
    return render(request, 'form_jogador.html', {'form': form})

def deletar_jogador(request, id):
    jogador = get_object_or_404(Jogador, pk=id)
    if request.method == 'POST':
        jogador.delete()
        return redirect('lista_jogadores')
    return render(request, 'confirmar_exclusao.html', {'obj': jogador})
