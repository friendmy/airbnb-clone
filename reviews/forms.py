from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    accuracy = forms.IntegerField(max_value=5, min_value=1)
    communication = forms.IntegerField(max_value=5, min_value=1)
    cleanliness = forms.IntegerField(max_value=5, min_value=1)
    location = forms.IntegerField(max_value=5, min_value=1)
    value = forms.IntegerField(max_value=5, min_value=1)
    # check_in = forms.IntegerField(max_value=5, min_value=1)
    check_in = forms.ChoiceField(
        choices=(("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5))
    )

    class Meta:
        model = models.Review
        fields = (
            "accuracy",
            "communication",
            "cleanliness",
            "location",
            "value",
            "check_in",
            "review",
        )

    def save(self):
        review = super().save(commit=False)
        return review
