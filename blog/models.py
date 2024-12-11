from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Q
from django.shortcuts import reverse

from django.utils import timezone
from extensions.utils import (
    get_filename_ext, jalali_converter, jalali_get_day, jalali_get_month,
    jalali_get_year
)
from account.models import USER


def upload_to_blog_image(instance, filename):
    return f"blog/Images/{filename}"


def upload_to_blog_video(instance, filename):
    return f"blog/Videos/{filename}"


def upload_to_file_library(instance, filename):
    return f"blog/Videos/{filename}"


class FolderLibraryManager(models.Manager):
    def get_active_folder(self):
        return self.get_queryset().filter(is_delete=False)

    def get_active_folder_no_parent(self):
        return self.get_active_folder().filter(parent=None)


class FolderLibrary(models.Model):
    parent = models.ForeignKey(
        'self', on_delete=models.DO_NOTHING, verbose_name="پوشه والد", null=True, blank=True,
        related_name='parent_children',
    )
    title = models.CharField(
        verbose_name="عنوان پوشه", blank=True, null=True, default="",
        max_length=255,
    )
    author = models.ForeignKey(
        USER, models.DO_NOTHING, "folder_author", verbose_name="کاربر ثبت کننده", null=True
    )
    created = models.DateTimeField(
        verbose_name="تاریخ ذخیره", editable=False, default=timezone.now
    )
    modified = models.DateTimeField(verbose_name="تاریخ بروزرسانی", default=timezone.now)
    is_delete = models.BooleanField(
        verbose_name="حذف شده", blank=False, null=False, default=False
    )

    objects = FolderLibraryManager()

    def get_absolute_url(self):
        return reverse("admin_panel:all_filles_in_folder", kwargs={"pk": self.pk})

    def get_children(self):
        return FolderLibrary.objects.filter(parent=self, is_delete=False, )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(FolderLibrary, self).save(*args, **kwargs)

    def jmodified(self):
        return jalali_converter(self.modified)

    jmodified.short_description = "بروز رسانی"

    def __str__(self):
        name = self.title
        if name is None:
            return self.author.get_full_name() if self.author is not None else 'بدون عنوان'
        return name

    class Meta:
        verbose_name = "پوشه"
        verbose_name_plural = "پوشه ها"
        db_table = 'folder_tbl'
        ordering = ['title', 'created', 'modified', 'pk']


class FilesLibraryManager(models.Manager):
    def get_active_files(self):
        return self.get_queryset().filter(save_type="P", is_delete=False)

    def get_deleted_files(self):
        return self.get_queryset().filter(
            # Q(folder__isnull=True) |
            Q(is_delete=True)
        )


class FilesLibrary(models.Model):
    file_type_choice = (
        ("N", "پیش نویس"), ("P", "منتشر شده")
    )
    folder = models.ForeignKey(
        FolderLibrary, on_delete=models.SET_NULL, verbose_name="پوشه", blank=True, null=True,
    )
    title = models.CharField(
        verbose_name="عنوان فایل", blank=True, null=True, default="",
        max_length=255,
    )
    file = models.FileField(
        verbose_name="آدرس محل ذخیره سازی", null=True, blank=True,
        default="", upload_to=upload_to_file_library,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'MOV', 'avi', 'mp4', 'webm', 'mkv', 'png', 'jpg', 'jpeg', 'gif', 'ts', 'pdf',
                    'bmp'],
                message="پسوند فایل های مجاز bmp MOV avi mp4 webm mkv png jpg jpeg gif ts pdf می باشد")
        ],
        help_text="پسوند فایل های مجاز bmp MOV avi mp4 webm mkv png jpg jpeg gif ts pdf می باشد",
        max_length=2500
    )
    save_type = models.CharField(
        verbose_name="وضعیت انتشار", blank=False,
        null=False, default="P", choices=file_type_choice, max_length=1
    )
    author = models.ForeignKey(
        USER, models.DO_NOTHING, "file_author", verbose_name="کاربر ثبت کننده", null=True
    )
    created = models.DateTimeField(
        verbose_name="تاریخ ذخیره", editable=False, default=timezone.now
    )
    modified = models.DateTimeField(verbose_name="تاریخ بروزرسانی", default=timezone.now)
    is_delete = models.BooleanField(
        verbose_name="حذف شده", blank=False, null=False, default=False
    )
    objects = FilesLibraryManager()

    def file_ext(self):
        ext = str(get_filename_ext(self.file.path)[1])
        return ext

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(FilesLibrary, self).save(*args, **kwargs)

    def jmodified(self):
        return jalali_converter(self.modified)

    jmodified.short_description = "بروز رسانی"

    def __str__(self):
        name = self.title
        if name is None:
            return self.author.get_full_name() if self.author is not None else 'بدون عنوان'
        return name

    class Meta:
        verbose_name = "فایل"
        verbose_name_plural = "کتاب خانه فایل ها"
        db_table = 'files_tbl'
        ordering = ['title', 'created', 'modified', 'pk']


class BlogManager(models.Manager):
    def get_fast_blog(self):
        blog = self.get_active_blog().filter(
            is_fast_blog=True)
        return blog

    def get_static_blog(self, count):
        blog = self.get_active_blog().filter(
            is_static_blog=True, static_blog_rank__isnull=False).order_by(
            'static_blog_rank')[:count]
        return blog

    def get_active_blog_with_query(self, query):
        blog = self.get_active_blog().filter(
            Q(title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(text__icontains=query) |
            Q(tags__icontains=query)
        ).distinct()
        if blog.count() != 0:
            return blog
        return []

    def get_blog(self, pk, slug):
        blog = self.get_active_blog().filter(pk=pk, slug=slug)
        if blog is not []:
            return blog.first()
        return None

    def get_last_tags(self, count):
        all_active_blog = self.get_active_blog()
        tag_list = []
        for item in all_active_blog:
            for j in item.get_tags():
                if j != "":
                    tag_list.append(j)
        return list(set(tag_list))[:count]

    def get_keyword(self):
        return ", ".join(self.keyword.split("+"))

    def get_active_blog(self):
        return self.get_queryset().filter(save_type="P", is_delete=False)

    def get_most_visit_blog(self, count):
        return self.get_active_blog().order_by("-visit").distinct()[:count]

    def get_last_active_blog(self, count):
        return self.get_active_blog().order_by("-modified").distinct()[:count]


# مدل ذخیره‌سازی اخبار
class Blog(models.Model):
    blog_type_choice = (
        ("N", "پیش نویس"), ("P", "منتشر شده")
    )
    title = models.CharField(
        verbose_name="عنوان مقاله", blank=False, null=False, default="", unique=True,
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name="عنوان مقاله در نوار آدرس", blank=False, null=False, default="", unique=True,
        max_length=255,  # allow_unicode=True
    )
    blog_photo = models.ImageField(
        verbose_name="تصویر اصلی مقاله", null=True, blank=True,
        default="", upload_to=upload_to_blog_image
    )
    short_description = models.CharField(
        verbose_name="توضیح کوتاه", blank=True, null=True, default="",
        max_length=500, help_text="محدودیت عبارت 500 کاراکتر می باشد"
    )
    text = models.TextField(
        verbose_name="متن مقاله", blank=False, null=False, default="",
    )
    save_type = models.CharField(
        verbose_name="وضعیت انتشار", blank=False,
        null=False, default="N", choices=blog_type_choice, max_length=1
    )
    author = models.ForeignKey(
        USER, models.DO_NOTHING, "blog_author", verbose_name="ثبت کننده خبر", null=True
    )
    created = models.DateTimeField(
        verbose_name="تاریخ ذخیره", editable=False, default=timezone.now
    )
    modified = models.DateTimeField(verbose_name="تاریخ بروزرسانی", default=timezone.now)
    is_delete = models.BooleanField(
        verbose_name="حذف شده", blank=False, null=False, default=False
    )
    objects = BlogManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def jmodified(self):
        return jalali_converter(self.modified)

    jmodified.short_description = "بروز رسانی"

    def jcreated(self):
        return jalali_converter(self.created)

    jcreated.short_description = "ایجاد"

    def jcreated_day(self):
        return jalali_get_day(self.modified)

    def jcreated_month(self):
        return jalali_get_month(self.modified)

    def jcreated_year(self):
        return jalali_get_year(self.modified)

    def get_absolute_url(self):
        return reverse("Blog:single_blog", kwargs={"pk": self.pk, "slug": self.slug})

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        db_table = 'blog_tbl'
        ordering = ["pk"]
