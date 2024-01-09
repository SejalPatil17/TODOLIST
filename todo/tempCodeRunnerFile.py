def update(request,id):
    allTasks = Task.objects.get( id=id)
    if request.method =="POST":
     
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        allTasks=Task(taskTitle=title,taskDesc=desc)
        allTasks.save()
    context={'title':allTasks.taskTitle,'desc':allTasks.taskDesc,'id':id}
    return redirect(request,'edit.html',context)