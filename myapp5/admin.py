from django.contrib import admin
from .models import Category, Product


@admin.action(description="Сбросить количество в ноль") 
def reset_quantity(modeladmin, request, queryset): 
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin): # класс для отображения изменений только в админке (сама модель не меняется)
    """Список продуктов"""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity'] # настраиваем сортировку в списках админки как нам нужно
    list_filter = ['date_added', 'price'] # настраиваем параметры фильтрации
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity] # подключаем функцию сброса кол-ва товаров через зарезервированную переменную actions

    """Отдельный продукт"""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [       # fieldsets не дружит с переменной fields, поэтому можно использовать только что-то одно
        ( 
            None, 
            { 
                'classes': ['wide'], 
                'fields': ['name'], 
            }, 
        ), 
        ( 
            'Подробности', 
            { 
                'classes': ['collapse'], 
                'description': 'Категория товара и его подробное описание', 
                'fields': ['category', 'description'], 
            }, 
        ), 
        ( 
            'Бухгалтерия', 
            { 
                'fields': ['price', 'quantity'], 
            }
        ), 
        (
            'Рейтинг и прочее', 
            { 
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей', 
                'fields': ['rating', 'date_added'], 
            } 
        ), 
]




admin.site.register(Category)
admin.site.register(Product, ProductAdmin) # регистрируем ProductAdmin рядом с той моделью, которую хотим видеть в админке
