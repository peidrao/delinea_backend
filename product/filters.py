from rest_framework.filters import BaseFilterBackend


class ProductTitleFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        title = request.query_params.get(
            'title', None,
        )
        if not title:
            return queryset.all()
        else:
            try:
                return queryset.filter(title=title).order_by('id')
            except Exception:
                return queryset.none()


class ProductPriceFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        price = request.query_params.get(
            'price', None,
        )

        if not price:
            return queryset.all()
        else:
            try:
                return queryset.filter(price=price).order_by('id')
            except Exception:
                return queryset.none()
