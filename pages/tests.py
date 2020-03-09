import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'easternmarginmodelapp.settings'
django.setup()
from core_models.models import FeedstockProductSlateCombination,RefineryProcessUnit,RefinedProduct,CrudeFeedstock

fsps_objects = FeedstockProductSlateCombination.objects.all()

fsps_objects = FeedstockProductSlateCombination(refinery_processing_unit_id='ADU')


print(fsps_objects)
