def blog_paginator(paginator, page_obj):
    context = {}

    page_numbers = []

    for i in range(max(1, page_obj.number - 2), min(paginator.num_pages, page_obj.number + 2) + 1):
        page_numbers.append(i)

    if page_numbers[0] != 1:
        page_numbers.insert(0, 1)
        if paginator.num_pages != len(page_numbers):
            page_numbers.insert(1, "...")

    if page_numbers[-1] != paginator.num_pages:
        if paginator.num_pages != page_numbers[-1] + 1:
            page_numbers.append("...")
        page_numbers.append(paginator.num_pages)

    context["page_numbers"] = page_numbers
    context["current_page"] = page_obj.number
    # context["has_previous"] = page_obj.has_previous
    # context["has_next"] = page_obj.has_next
    return context
