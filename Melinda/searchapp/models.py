from django.db import models

class Nomenclature(models.Model):
    code_identifier = models.CharField(max_length=100)
    coding_system = models.CharField(max_length=100)
    display = models.CharField(max_length=2000)
    popularity = models.IntegerField(default=0)
    
    def __str__(self):
        return u'({0}){1}[{2}]'.format(self.code_identifier, self.display, self.coding_system)
    
class Textmap(models.Model):
    free_text = models.CharField(max_length=1000)
    nomenclature = models.ForeignKey('Nomenclature')
    
    def __str__(self):
        return u'{0}->{1}'.format(self.free_text, self.nomenclature.code_identifier)
