from django.contrib import admin
from .models import CommentModel, LikeModel, DisLikeModel

admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(DisLikeModel)
