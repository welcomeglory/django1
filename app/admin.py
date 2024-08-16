from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'created_at')  # 리스트 뷰에서 표시할 필드
   search_fields = ('name', 'email')  # 검색 가능한 필드
   list_filter = ('created_at',)  # 필터링 가능한 필드
   ordering = ('-created_at',)  # 기본 정렬 순서

admin.site.register(Contact, ContactAdmin)
