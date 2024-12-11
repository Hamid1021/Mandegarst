from django.http import Http404
from django.shortcuts import render
from blog.models import Blog
from django.core.paginator import Paginator
from blog.utils import blog_paginator


def Blogs(request):
    # تعداد نتایج در هر صفحه برای نمایش تعداد اخبار در لیست اخبار
    results_per_page = 5
    # دریافت شماره صفحه : اطلاعات در هر صفحه به مقدار معینی نمایش داده می شود
    page = request.GET.get("p")
    # دریافت همه اخبار بر اساس وضعیت انتشار و ذخیره سازی آنها
    all_blogs: Blog = Blog.objects.get_active_blog()
    # تبدیل نتایج جستجو به صفحات مختلف یا پیج بندی آنها
    paginator = Paginator(all_blogs, results_per_page)
    # دریافت همه اخبار صفحه وارد شده مثلا 1
    all_blogs = paginator.get_page(page)
    # از ابزار ها لیست صفحات را به صورت لیست دریافت می کنیم
    page_numbers = blog_paginator(paginator, all_blogs)["page_numbers"]
    # از ابزار ها شماره صفحه جاری را به صورت یک عبارت دریافت می کنیم
    current_page = blog_paginator(paginator, all_blogs)["current_page"]
    # انتقال اطلاعات طبقه بندی شده به تمپلت
    context = {
        "object_list": all_blogs,
        "page_numbers": page_numbers,
        "current_page": current_page,
    }
    # رندر کردن و تبدیل اطلاعات دیتا بیس و اچ تی ام ال به اچ تی ام ال
    return render(request, "article-main.html", context)


def single_blog(request, pk, slug):
    # دریافت خبر با کلید واژه اختصاصی اسلاگ و ای دی خبر
    news: Blog = Blog.objects.get_blog(pk=pk, slug=slug)
    if news is None:
        # اگر خبر پیدا نشد صفحه 404 بر گردانده شود
        raise Http404()
    context = {
        "object": news,
    }
    return render(request, "article.html", context)

