from django.db import models


class Nomenclature(models.Model):
    code_identifier = models.CharField(max_length=100)
    coding_system = models.CharField(max_length=100)
    coding_sys_cd = models.CharField(max_length=100)
    display = models.CharField(max_length=2000)
    popularity = models.IntegerField(default=0)
    isExclusive = models.BooleanField(default=False)
    attribute_string = models.CharField(max_length=5000, default='{}')
    class Meta:
        unique_together=(('code_identifier','coding_sys_cd'))

    def __str__(self):
        return u'({0}){1}[{2}{3}{4}]'.format(self.code_identifier, self.display, self.coding_system, self.attribute_string, self.isExclusive)
    
class Textmap(models.Model):
    free_text = models.CharField(max_length=1000)
    nomenclature = models.ForeignKey('Nomenclature')
    
    def __str__(self):
        return u'{0}->{1}'.format(self.free_text, self.nomenclature.code_identifier)
    

    
    
