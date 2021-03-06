from decimal import Decimal
from django.conf import settings

from shop.models import Product

class Cart(object):
    def __init__(self, request): # 초기화
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart


    def __len__(self):  #
        return sum(item["quantity"] for item in self.cart.values())

    def __iter__(self): # for 문 사용할 때 요소
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]

            yield item

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}

        if is_update:   # 제품 정보 수정
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True    # modified가 true가 아닐경우 업데이트가 되지 않음

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}

    def get_product_total(self):    # 장바구니 가격으 총 합
        return sum(item["price"] * item["quantity"] for item in self.cart.values())


