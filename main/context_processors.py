from django.utils.safestring import mark_safe
from .models import TypePage, Page


# def base_list_type_page(request):
#     categories = {}
#     for catagory in TypePage.objects.all():
#         categories[catagory.name] = mark_safe(catagory.name)
#     return {'categories': categories}
#
#
# def base_list_page(request):
#     pages = {}
#     for page in Page.objects.all():
#         pages[page.title_m] = mark_safe(page.title_m)
#     return {'pages': pages}
#
#
# def base_name_page(request):
#     names = {}
#     for name in Page.objects.all():
#         names[name.url_page] = mark_safe(name.url_page)
#     return {'names': names}
#
#
# def base_urls_page(request):
#     urls = {}
#     for url in Page.objects.all():
#         urls[url.url_page] = mark_safe(url.url_page)
#     return {'urls': urls}

# def get_categories(request):
#     categories = {}
#     for category in TypePage.objects.all():
#         categories[category.id] = {
#           "name": mark_safe(category.name),
#           "pages": [],
#         }
#     for page in Page.objects.values("url_page", "title_m", "categories_id"):
#         if page["categories_id"]:
#            categories[page["categories_id"]]["pages"].append({
#                'url': mark_safe(page["url_page"]),
#                'title': mark_safe(page["title_m"]),
#             })
#     return {'categories': categories}