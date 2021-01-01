# from django.contrib.admin import SimpleListFilter
# from .models import Product

# class ProductDateFilter(SimpleListFilter):
#     """
#     This filter is being used in django admin panel in profile model.
#     """
#     title = 'Email Types'
#     parameter_name = 'user__email'

#     def lookups(self, request, model_admin):
#         return (
#             ('business', 'Business'),
#             ('non_business', 'non-business')
#         )

#     SOCIAL_EMAIL_REGEX = r"^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(?!hotmail|gmail|yahoo)(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"

#     def queryset(self, request, queryset):
#         if not self.value():
#             return queryset
#         if self.value().lower() == 'business':
#             return queryset.filter(user__email__regex=self.SOCIAL_EMAIL_REGEX)
#         elif self.value().lower() == 'non_business':
#             return queryset.filter().exclude(user__email__regex=self.SOCIAL_EMAIL_REGEX)