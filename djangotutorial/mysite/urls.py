# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),  # ✅ 用字符串形式引入，不要直接导入模块对象
]
