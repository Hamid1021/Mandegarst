from django.db import models


def game_photo_path(instance, filename):
    return f'game_photos/{instance.game_name}/{filename}'

def game_photo_path(instance, filename):
    return f'game_photos/{instance.game_name}/{filename}'


class GameManager(models.Manager):
    def get_highest_rate(self):
        return self.order_by('-rate_score')[:5]
    def get_latest_games(self):
        return self.order_by('-id')[:8]


class Game(models.Model):
    GAME_STATUS_CHOICES = [
        ('p', 'انتشار یافته'),
        ('d', 'پیش نویس'),
    ]
    
    game_name = models.CharField(max_length=255, null=False, blank=False, default="", verbose_name="نام بازی")
    game_genre = models.CharField(max_length=255, null=False, blank=False, default="", verbose_name="ژانر بازی")
    rate_score = models.FloatField(null=True, blank=True, default=0.0, verbose_name="امتیاز")
    photo = models.ImageField(upload_to=game_photo_path, null=True, blank=True, default="", verbose_name="عکس")
    game_description = models.TextField(null=True, blank=True, default="", verbose_name="توضیحات بازی")
    text_link_win = models.URLField(null=True, blank=True, default="", verbose_name="لینک برای ویندوز")
    text_link_ios = models.URLField(null=True, blank=True, default="", verbose_name="لینک برای iOS")
    text_link_android = models.URLField(null=True, blank=True, default="", verbose_name="لینک برای اندروید")
    publish_status = models.CharField(max_length=1, choices=GAME_STATUS_CHOICES, default='D', verbose_name="وضعیت انتشار")
    is_deleted = models.BooleanField(default=False, verbose_name="حذف شده")
    
    objects = GameManager()
    
    class Meta:
        verbose_name = "بازی"
        verbose_name_plural = "بازی ها"
        ordering = ['pk']

    def __str__(self):
        return self.game_name


class BannerManager(models.Manager):
    def get_first_top_banner(self):
        return self.filter(position='t').first()

    def get_first_mid_banner(self):
        return self.filter(position='m').first()

    def get_first_bottom_banner(self):
        return self.filter(position='b').first()


class Banner(models.Model):
    BANNER_STATUS_CHOICES = [
        ('a', 'فعال'),
        ('i', 'غیرفعال'),
    ]
    BANNER_POSITION_CHOICES = [
        ('t', 'بالا'),
        ('m', 'وسط'),
        ('b', 'پایین'),
    ]
    position = models.CharField(max_length=1, verbose_name="موقعیت", choices=BANNER_POSITION_CHOICES)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, verbose_name="بازی")
    status = models.CharField(max_length=1, choices=BANNER_STATUS_CHOICES, default='a', verbose_name="وضعیت")

    objects = BannerManager()

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنرها"

    def __str__(self):
        return f"{self.game.game_name} - {self.position}"
