from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Recipe(models.Model):
    """Recipes information"""
    recipe_name = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    time_need = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(600)]) 
    # image = models.ImageField(upload_to='uploads/', height_field=440, width_field=800) #trzeba zmienić upload
    
    BREAKFAST = 'BR'
    DINNER = 'DN'
    SUPPER = 'SP'
    PART_OF_A_DAY = [
        (BREAKFAST, 'Śniadanie'),
        (DINNER, 'Obiad'),
        (SUPPER, 'Kolacja'),
    ]
    part_of_a_day = models.CharField(
        max_length = 2, 
        choices=PART_OF_A_DAY,
        default=BREAKFAST
    )

    ingredients = models.TextField(max_length=400)
    recipe = models.TextField(max_length=1000)


    likes = 0
    #poziom trudności, porcje

    def __str__(self):
        return self.recipe_name