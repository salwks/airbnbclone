from django.db import models


class House(models.Model):
    """Model Definition for House."""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, verbose_name="Pets Allowed?", help_text="Are pets allowed?"
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Unicode representation of House."""
        return self.name
