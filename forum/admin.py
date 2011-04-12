from django.contrib import admin
from forum.models import Forum, Thread, Post, Subscription

class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', '_parents_repr')
    list_filter = ('groups',)
    ordering = ['ordering', 'parent', 'title']
    prepopulated_fields = {"slug": ("title",)}

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['author','thread']

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'latest_post_time')
    list_filter = ('forum',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('_author', 'time', '_forum', 'thread')
    list_filter = ('thread__forum',)
    search_fields = ('author__email', 'body', 'thread__title', 'thread__forum__title')

    def _forum(self, obj):
        return obj.thread.forum
    
    def _author(self, obj):
        return obj.author.email

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
