from Exceptions.exceptions import ValidationError

class Validator:
    @staticmethod
    def player_validator(player):
        errors = ""
        if len(player.nume) == 0:
            errors += 'nume must not be empty\n'

        if len(player.tara) == 0:
            errors += 'tara must not be empty\n'

        if player.nr_meciuri <= 0:
            errors += 'nr_meciuri must be a positive integer\n'

        if player.nr_victorii <= 0:
            errors += 'nr_victorii must be a positive integer\n'

        if player.nr_puncte <= 0:
            errors += 'nr_puncte must be a positive integer\n'

        if player.nr_victorii > player.nr_meciuri:
            errors += 'nr_victorii must be less than nr_meciuri'

        if len(errors) > 0:
            raise ValidationError(errors)
