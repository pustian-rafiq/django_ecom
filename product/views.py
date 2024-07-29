from django.views import generic
from django.http import JsonResponse
import json
import pandas as pd
#Nabil Moiun - youtube channel for this project

# Create your views here.
def json_to_csv(self):
    #open json file
    f = open('data.json')
    #read json file
    data = json.load(f)
    # print(data)
    data_list = [
        {
            'Transaction ID': 810,
            'Invoice Number': data['Invoices'][0]['InvoiceNumber'],
            'Invoice Date':  data['Invoices'][0]['InvoiceDate'],
            'Ship To Address - Line One': data['ShippingAddress']['Line1'],
            'Ship To Address - Line Two': data['ShippingAddress']['Line2'],
            'Ship To City': data['ShippingAddress']['City'],
            'Ship To State': data['ShippingAddress']['State'],
            'Ship To Zip code': data['ShippingAddress']['Postcode'],
            'Ship To Country': data['ShippingAddress']['Country'],
        },
        {
            'Transaction ID': 810,
            'InvoiceNumber': data['Invoices'][0]['InvoiceNumber'],
            'InvoiceDate':  data['Invoices'][0]['InvoiceDate'],
            'Ship To Address - Line One': data['ShippingAddress']['Line1'],
            'Ship To Address - Line Two': data['ShippingAddress']['Line2'],
            'Ship To City': data['ShippingAddress']['City'],
            'Ship To State': data['ShippingAddress']['State'],
            'Ship To Zip code': data['ShippingAddress']['Postcode'],
            'Ship To Country': data['ShippingAddress']['Country'],
        },
        
    ]
    df = pd.DataFrame(data_list)
    df.to_csv('inventory.csv')

    return JsonResponse(data)


class Home(generic.TemplateView):
    template_name = 'home.html'

class PrdocutDetail(generic.TemplateView):
    template_name = 'product/product-details.html'