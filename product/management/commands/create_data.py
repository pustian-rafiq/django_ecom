import requests
from django.core.management import BaseCommand
from django.utils.text import slugify
from product.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get('https://fakestoreapi.com/products').json()
        print('response',response)
        # for product in response:
        #     category, _ = Category.objects.get_or_create(
        #         title = product['category'],
        #         slug = slugify(product['category']),
        #         featured = True
        #     )
        #     Product.objects.create(
        #         category = category,
        #         title = product['title'],
        #         slug = slugify(product['title']),
        #         price = product['price'],
        #         thumbnail = product['image'],
        #         description = product['description'],

        #     )
        print('Product created')