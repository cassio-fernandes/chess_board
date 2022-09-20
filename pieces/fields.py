from rest_framework import serializers


class CustomChoiceField(serializers.ChoiceField):
    def __init__(self, choices, **kwargs):
        self.choices = choices
        kwargs['choices'] = [(c.value, c.label) for c in choices]

        super(CustomChoiceField, self).__init__(**kwargs)

    def to_representation(self, key):
        return self.choices[key]

    def to_internal_value(self, data):
        try:
            return data
        except KeyError:
            self.fail('invalid_choice', input=data)
