from . import views

routes = [
    ('GET', '/api/v1/get_list/', views.get_list),
    ('GET', r'/api/v1/pages', views.get_page),
    ('GET', r'/api/v1/get_data/{id}/', views.get_data),
    ('POST', '/api/v1/set_data/', views.set_data),
    ('DELETE', r'/api/v1/delete/{id:\d+}/', views.delete_data),
    ('POST', '/api/v1/users/login/', views.login),
]
