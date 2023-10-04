from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from manager.models import Task, Worker, Position, TaskType

admin.site.unregister(Group)
admin.site.register(TaskType)
admin.site.register(Position)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = (
        "name", "deadline", "priority", "is_completed", "task_type",
    )
    list_filter = ("priority", )


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )
