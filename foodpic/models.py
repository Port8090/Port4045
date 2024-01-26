from django.db import models

class Image(models.Model):
    path = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now=True)
    detect_name = models.CharField()

class ResultImage(models.Model):
    image = models.ImageField(upload_to='result_images/')

    def __str__(self):
        return self.image.url

    @classmethod
    def create(cls, image_path):
        result_image = cls(image=image_path)
        result_image.save()
        return result_image


# class Nutrition(models.Model):
#     code = models.CharField(max_length = 10)
#     category1 = models.CharField(max_length = 10, null=True)
#     category2 = models.CharField(max_length = 10, null=True)
#     s_amount = models.FloatField()
#     kcal = models.FloatField()
#     water = models.FloatField()
#     protein = models.FloatField()
#     fat = models.FloatField()
#     carbohydrate = models.FloatField()
#     sugar = models.FloatField()
#     fiber = models.FloatField()
#     cal = models.FloatField()
#     fe = models.FloatField()
#     mg = models.FloatField()
#     phos = models.FloatField()
#     kal = models.FloatField()
#     sodium = models.FloatField()
#     zn = models.FloatField()
#     copper = models.FloatField()
#     mangan= models.FloatField()
#     selenm = models.FloatField()
#     retinol = models.FloatField()
#     betacarot = models.FloatField()
#     vitD3 = models.FloatField()
#     tocoph = models.FloatField()
#     tocotri = models.FloatField()
#     vitB1 = models.FloatField()
#     vitB2 = models.FloatField()
#     niacin = models.FloatField()
#     folic = models.FloatField()
#     vitB12 = models.FloatField()
#     vitC = models.FloatField()
#     amino = models.FloatField()
#     choles = models.FloatField()
#     transfat = models.FloatField()


