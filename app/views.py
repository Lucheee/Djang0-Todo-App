from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

# Create your views here.


def home(request):
    todo_list = Todo.objects.all()
    return render(request, 'home.html', {'todo_list':todo_list})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

def completed(request, pk):
    todo_list = Todo.objects.get(pk=pk)
    todo_list.completed = True
    todo_list.save()
    return redirect('home')


def incomplete(request, pk):
    todo_list = Todo.objects.get(pk=pk)
    todo_list.completed = False
    todo_list.save()
    return redirect('home')




def update(request, pk):
	
		current_todo = Todo.objects.get(id=pk)
		form = TodoForm(request.POST or None, instance=current_todo)
		if form.is_valid():
			form.save()
			messages.success(request, "Todo Has Been Updated!")
			return redirect('home')
		return render(request, 'update.html', {'form':form})



def todo_lists(request, pk):
    
        todo_lists=Todo.objects.get(id=pk)
        return render(request, 'todo_lists.html', {'todo_lists':todo_lists})


def delete(request, pk):
   
        delete_it = Todo.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Todo deleted suceesfully")
        return redirect('home')
 



      



    
           
                
		
	

    







	





