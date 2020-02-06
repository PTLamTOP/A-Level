from django.contrib import admin
from .models import Request, Comment, Refusal, Approval, Denial


admin.site.register(Request)
admin.site.register(Comment)
admin.site.register(Refusal)
admin.site.register(Approval)
admin.site.register(Denial)
