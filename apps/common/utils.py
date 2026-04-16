from django.utils.text import slugify


def generate_unique_slug(instance, value, slug_field_name="slug"):
    base_slug = slugify(value)
    slug = base_slug
    model_class = instance.__class__
    counter = 2

    while model_class.objects.filter(**{slug_field_name: slug}).exclude(pk=instance.pk).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug