from django.db import models
from extensions.utils import jalali_converter_date


class PremiumCode(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="کد پریمیوم")
    expiry_date = models.DateField(verbose_name="تاریخ انقضا")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    def jexpiry_date(self):
        return jalali_converter_date(self.expiry_date)

    jexpiry_date.short_description = "بروز رسانی"

    class Meta:
        verbose_name = "کد پریمیوم"
        verbose_name_plural = "کدهای پریمیوم"

    def __str__(self):
        return self.code
