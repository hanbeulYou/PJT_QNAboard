from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

"""
인자를 두 개를 보냈으므로, url에서도 인자 두 개를 모두 사용해야 한다.

(인자를 받는 순서가 중요하므로 이름은 자유롭게 설정해도 된다)

path('reply_delete/<int:p_id>/<int:r_id>', views.comment_delete, name="comment_delete"),
<a href="{% url 'comment_delete' post.id r.id%}">삭제</a>
"""

# 저기 지금 article의 pk는 int:pk로 이름은 'pk'로 설정해뒀잖아
# 이미 받았다기 보다는 이름이 달라서
# 그 url에 int:pk 이 부분이 인자 이름인데 그게 views에서 이름이 같아야하는듯