from django.contrib import admin

# Register your models here.
from .models import FeedstockProductSlateCombination,RefineryProcessUnit,CrudeFeedstock,RefinedProduct,Region,Country
admin.site.register(CrudeFeedstock)
admin.site.register(FeedstockProductSlateCombination)
admin.site.register(RefineryProcessUnit)
admin.site.register(RefinedProduct)
admin.site.register(Country)
admin.site.register(Region)
# To reset migrations, delete everything in the migrations folder and delete the sqlite database and rerun makemigrations and migrate
