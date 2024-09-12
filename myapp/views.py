from django.shortcuts import render, redirect, HttpResponse
from.models import Recipe
import os

def recipe(request):
    if request.method == "POST":
        image = request.FILES.get('recipe_image')
        name = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')
        if not name or not description:
            return HttpResponse('Recipe name and description are required.', status=400)
        Recipe.objects.create(recipe_name = name, recipe_description = description, recipe_image = image)
        return redirect('recipe')
    
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipe.html', context)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    recipe.delete()
    return redirect('recipe')

    
def search_recipe(request):
    search_query = request.GET.get('search', '')  # Use GET to retrieve search query

    if search_query:
        # If there is a search query, filter recipes
        recipes = Recipe.objects.filter(recipe_name__icontains=search_query)
    else:
        # If no search query, show all recipes
        recipes = Recipe.objects.all()

    context = {'recipes': recipes}
    return render(request, 'recipe.html', context)

def update_recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    if request.method == "POST":
        image = request.FILES.get('recipe_image')
        name = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')
        if not name or not description:
            return HttpResponse('Recipe name and description are required.', status=400)
        recipe.recipe_name = name
        recipe.recipe_description = description
        if image:
            recipe.recipe_image = image
        recipe.save()
        return redirect('recipe')
    context = {'recipe': recipe}
    return render(request, 'update_recipe.html', context)