from django.urls import path # импортируем path для создания путей к нашему приложению
from . import views # импортируем views нашего приложения

urlpatterns = [     
    path('', views.index, name='index'), # по пустому пути импортируем функцию index из нашего view и даём ей имя 'index'    
    path('about/', views.about, name='about'),# по пути about/ вызываем функцию about из veiws
]  