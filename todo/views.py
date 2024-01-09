from django.shortcuts import redirect, render,HttpResponse
from todo.models import Task

# Create your views here.
def todo(request):
  
    context={'success':False}
        
    if request.method =="POST":
        #handle the form
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context={'success':True}
        
    return render(request,'index.html',context)


def tasks(request):
    allTasks=Task.objects.all()
    context={'tasks':allTasks}
    return render(request,'tasks.html',context)


def delete(request ,id):
     allTasks=Task.objects.get(id=id)
     allTasks.delete()
     return redirect('tasks')


def update(request,id):
    allTasks = Task.objects.get( id=id)
    if request.method =="POST":
     
        title=request.POST['title']
        desc=request.POST['desc']
        allTasks.taskTitle = title
        allTasks.taskDesc = desc
        allTasks.save()
        return redirect('/tasks', id=id)
    context={'title':allTasks.taskTitle,'desc':allTasks.taskDesc,'id':id}
    return render(request,'edit.html',context)

def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('searchInput', '')
       
        print("Performing search for:", search_query)
        return render(request, 'index.html', {'search_query': search_query})
    else:
        return render(request, 'index.html')

   
