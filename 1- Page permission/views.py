from .decorators import allowed_editors

@allowed_editors(list_users=['admin','editor']) #allowed groups
def your_view(request):
  pass
