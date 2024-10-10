from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix d'achat unitaire
    resale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Prix de revente calculé
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)  # Unité de mesure (kg, g, l, ml, etc.)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)  # Coût par unité

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Coût total calculé

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Quantité de l'ingrédient dans la recette

    def __str__(self):
        return f"{self.quantity} {self.ingredient.unit} of {self.ingredient.name} in {self.recipe.name}"

class Invoice(models.Model):
    file = models.FileField(upload_to='invoices/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice {self.id} - {'Processed' if self.processed else 'Pending'}"

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

