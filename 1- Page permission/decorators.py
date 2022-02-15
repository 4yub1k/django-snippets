def allowed_editors(list_users):
    def decorator(func): #it can be of any name.
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in list_users:
                return func(request,*args,**kwargs)
            else:
                return HttpResponse("not allowed", status=405)
            return func(request,*args,**kwargs)
        return wrapper_func
    return decorator
