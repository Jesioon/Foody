from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Part of a days

class Meal(models.Model):
    mealTime = models.CharField(max_length=20)

    def __str__(self):
        return self.mealTime

# Countries where this dish is popular

class WorldCuisine(models.Model):
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.country

class Recipe(models.Model):
    """Recipes information"""
    recipe_name = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)

    time_need = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(600)], default=0)
    portions = models.IntegerField(
        validators=[MinValueValidator(1)], default=1)

    likes = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    DEFAULT_KEY = 0
    day_key = models.ForeignKey(
        Meal, on_delete=models.CASCADE, default=DEFAULT_KEY)
    country_key = models.ForeignKey(
        WorldCuisine, on_delete=models.CASCADE, default=DEFAULT_KEY)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(blank=True, default='defaultRecipex640.jpg')

    EASY = 'ES'
    MEDIUM = 'MM'
    HARD = 'HR'
    LEVEL = [
        (EASY, 'Łatwe'),
        (MEDIUM, 'Średnie'),
        (HARD, 'Trudne'),
    ]
    level = models.CharField(
        max_length=2,
        choices=LEVEL,
        default='ES'
    )

    ingredients = models.TextField(max_length=400)
    recipe = models.TextField(max_length=1000)

    def __str__(self):
        return self.recipe_name
