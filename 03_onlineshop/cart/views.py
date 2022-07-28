from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST


from shop.models import Product
from .forms import AddProductForm
from .cart import Cart

@require_POST
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # 클라이언트 -> 서버로 데이터 전달 (클라이언트에서 받은 데이터는 form을 활용해 clean data로 사용 권장)
    # 유효성 검사, injection 전처리
    form = AddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], is_update=cd["is_update"])

        return redirect("cart:detail")

# 제품을 카트에서 제거
def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:detail")

def detail(request):
    cart = Cart(request)
    for product in cart:
        product["quantity_form"] = AddProductForm(initial={"quantity": product["quantity"], "is_update": True})
    return render(request, "cart/detail.html", {"cart": cart})
