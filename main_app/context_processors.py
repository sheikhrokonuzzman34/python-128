
from main_app.models import *


def category(request):
    g_category_list = Category.objects.all()
    
    context ={
        'g_category_list': g_category_list
    }
    return context