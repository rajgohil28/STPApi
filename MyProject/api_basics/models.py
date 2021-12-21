from django.db import models
import pickle
import sklearn
# Create your models here.

class Articles(models.Model):
    ID = models.AutoField(primary_key=True)
    ph = models.FloatField(max_length=10)
    temp = models.FloatField(max_length=10)
    BOD = models.FloatField()
    COD = models.FloatField()
    TSS = models.FloatField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    DO = models.FloatField(max_length=10)
    watercons = models.FloatField(max_length=10)
    Alkalinity = models.FloatField(max_length=10)
    EBOD = models.FloatField()
    ETSS = models.FloatField()
    ENH = models.FloatField(max_length=10)
    ANO = models.FloatField(max_length=10)
    Eph = models.FloatField(max_length=10)
    FMLSS = models.FloatField()
    ADO = models.FloatField(max_length=10)
    ANH = models.FloatField(max_length=10)
    predicted_BOD = models.FloatField(max_length=10, default=0.00)

    def __str__(self):
        return self.title

    def predictBOD(self):
        model = pickle.load(open('api_basics/MLmodels/RegressionSTP_model.sav','rb'))
        self.predicted_BOD = model.predict([[self.ph,self.temp,self.ADO,self.ANO,self.FMLSS]])
        self.save()