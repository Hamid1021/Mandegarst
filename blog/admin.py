from django.contrib import admin

from blog.models import Blog, FilesLibrary, FolderLibrary

from django import forms
from ckeditor.widgets import CKEditorWidget

from django.contrib import messages


# "parent","title","author","created","modified","is_delete",
class FolderLibraryAdmin(admin.ModelAdmin):
    list_display = ['__str__', "title", "parent", 'author', 'jmodified', 'is_delete', ]
    list_filter = ['is_delete']
    readonly_fields = ['author', 'modified', 'jmodified', ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        super(FolderLibraryAdmin, self).save_model(request, obj, form, change)

    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)

    def delete_model(self, request, obj):
        obj.update(is_delete=True)


admin.site.register(FolderLibrary, FolderLibraryAdmin)


# 'folder', 'title','file','save_type','author','created','modified','is_delete','jmodified',
class FilesLibraryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'file', 'folder', 'save_type', 'author', 'jmodified', 'is_delete', ]
    list_filter = ['save_type', 'is_delete']
    readonly_fields = ['author', 'modified', 'jmodified', ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        super(FilesLibraryAdmin, self).save_model(request, obj, form, change)

    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)

    def delete_model(self, request, obj):
        obj.update(is_delete=True)


admin.site.register(FilesLibrary, FilesLibraryAdmin)


@admin.action(description="تغییر موارد انتخاب شده به حذف نشده", permissions=["change"])
def make_as_undelete_blog(modeladmin, request, queryset):
    queryset.update(is_delete=False)
    modeladmin.message_user(
        request,
        "موارد انتخاب شده به حالت حذف نشده تغییر کردند",
        messages.SUCCESS,
    )


@admin.action(description="تغییر موارد انتخاب شده به انتشار یافته", permissions=["change"])
def make_published(modeladmin, request, queryset):
    queryset.update(save_type="P")
    modeladmin.message_user(
        request,
        "موارد انتخاب شده به حالت انتشار یافته تغییر یافت",
        messages.SUCCESS,
    )


@admin.action(description="تغییر موارد انتخاب شده به پیش نویس", permissions=["change"])
def make_not_published(modeladmin, request, queryset):
    queryset.update(save_type="N")
    modeladmin.message_user(
        request,
        "موارد انتخاب شده به حالت پیش نویس تغییر یافت",
        messages.SUCCESS,
    )


class BlogAppAdminAdminForm(forms.ModelForm):
    keyword = forms.CharField(
        label="کلمات کلیدی", widget=forms.Textarea(
            attrs={
                "rows": 2, "placeholder": "کلمات را وارد نموده و با علامت + آن ها را از هم دیگر جدا نمایید",
                "style": "width:50%;"
            }
        ), required=False
    )
    text = forms.CharField(
        label="متن خبر", widget=CKEditorWidget(), required=True
    )
    short_description = forms.CharField(
        label="توضیح کوتاه", widget=CKEditorWidget(), required=True
    )
    class Meta:
        model = Blog
        fields = '__all__'


# "title","slug","blog_photo","short_description","text",
# "blog_type","author","created","modified","is_delete",
class BlogAppAdmin(admin.ModelAdmin):
    actions = [
        make_as_undelete_blog, make_published, make_not_published,
    ]
    form = BlogAppAdminAdminForm
    list_display = [
        'title', "jcreated", "jmodified", "save_type", "is_delete",
    ]
    search_fields = ["title", "slug", "short_description", "text", ]
    list_filter = [
        "is_delete",  "save_type",
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ["created", 'author', "is_delete"]

    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)

    def delete_model(self, request, obj):
        obj.update(is_delete=True)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        return super(BlogAppAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = ['author', 'created',]
        else:
            self.readonly_fields = ['author', 'created', "save_type"]
        return request.user.is_superuser or (obj and obj.author == request.user.id)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        if user.is_superuser:
            return qs
        else:
            return qs.filter(author=user)


admin.site.register(Blog, BlogAppAdmin)
