from . import views

routes = [
    ('GET', '/api/v1/get_list/', views.get_list),
]
