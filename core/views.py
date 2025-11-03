from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import Time, Jogador
from .forms import TimeForm, JogadorForm

#Referente a time
def list_times(request):
    times = Time.objects.all()
    return render(request, 'core/list_times.html', {'times': times})

def add_time(request):
    form = TimeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_times')
    return render(request, 'core/form_time.html', {'form': form })

def edit_time(request, id):
    time = get_object_or_404(time, pk=id)
    form = TimeForm(request.POST or None, instance=time)
    if form.is_valid():
        form.save()
        return redirect('list_times')
    return render(request, 'core/form_time.html', {'form': form})

def delete_time(request, id):
    time = get_object_or_404(Time, pk=id)
    if request.method == 'POST':
        time.delete()
        return redirect('lista_times')
    return render(request, 'core/confirmar_exclusao.html', {'obj': time})

#Referente a jogadores

def list_jogadores(request):
    #referencia ao time
    jogadores = Jogador.objects.select_related('time').all()
    return render(request, 'core/list_jogadores.html', {'jogadores': jogadores})

def add_jogador(request):
    form = JogadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_jogadores')
    return render(request, 'core/form_jogador.html', {'form': form})

def edit_jogador(request, id):
    jogador = get_object_or_404(Jogador, pk=id)
    form = JogadorForm(request.POST or None, instance=jogador)
    if form.is_valid():
        form.save()
        return redirect('lista_jogadores')
    return render(request, 'core/form_jogador.html', {'form': form})

def delete_jogador(request, id):
    jogador = get_object_or_404(Jogador, pk=id)
    if request.method == 'POST':
        jogador.delete()
        return redirect('lista_jogadores')
    return render(request, 'core/confirmar_exclusao.html', {'obj': jogador})

