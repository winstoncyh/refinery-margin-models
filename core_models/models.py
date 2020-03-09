from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class CrudeFeedstock(models.Model):
    name = models.CharField(max_length=120)
    specific_gravity = models.DecimalField(blank=True,decimal_places=2,max_digits=15,null=True)
    sulphur_level = models.DecimalField(blank=True,decimal_places=2,max_digits=15,null=True)
    kquery_curve_string = models.TextField(null=True,blank=True)
    # product_slate = models.ManyToManyField('ProductSlate')

    def __str__(self):
        return self.name

class RefinedProductsWeightByMass(models.Model):
    weight = models.DecimalField(blank=True,decimal_places=6,max_digits=15,default=0)

    def __str__(self):
        return self.weight




class RefinedProduct(models.Model):
    name = models.CharField(max_length=120)
    specific_gravity = models.DecimalField(blank=True,decimal_places=2,max_digits=15,null=True)
    feedstock_indicator = models.BooleanField(default=False)
    percent_output_by_mass = models.DecimalField(blank=True,decimal_places=6,max_digits=12,null=True)
    kquery_curve_string = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.name


class RefineryProcessUnit(models.Model):
    name = models.CharField(max_length=120)
    unit_type_code = models.CharField(max_length=3,blank=True,null=True)
    country = models.ForeignKey('Country',on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self):
        return self.name

    # region RefineryProcessUnit codes
    # ADU
    # SRU
    # HSK
    # FCC
    # HCK
    # endregion


class FeedstockProductSlateCombination(models.Model):
    feedstockproductslate_name = models.CharField(max_length=120,blank=True)
    crude_feedstock = models.ForeignKey('CrudeFeedstock', on_delete=models.DO_NOTHING, blank=True, null=True)
    intermediate_feedstock_products = models.ManyToManyField(RefinedProduct,related_name='intermediate_feedstock_products',blank=True,null=True)
    products = models.ManyToManyField(RefinedProduct,blank=True)
    refinery_processing_unit = models.ForeignKey('RefineryProcessUnit',on_delete= models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        return self.feedstockproductslate_name

class Country(models.Model):
    country_name = models.CharField(max_length=120,blank=True,null=True)
    country_code = models.CharField(max_length=2,blank=True,null=True)
    country_region_name = models.ForeignKey('Region',on_delete=models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        return self.country_name

class Region(models.Model):
    region_name = models.CharField(max_length=120,blank=True,null=True)

    def __str__(self):
        return self.region_name

