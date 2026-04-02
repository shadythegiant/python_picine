from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    if any(item.lower() in ingredients_lower for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
