from django.core.exceptions import ValidationError


def image_validation(self, max_size=1000*1024):
    image_size = self.file.size
    if image_size > max_size:
        raise ValidationError(f'You image should be less then {max_size}b.')


def file_size_validator(self,max_size=1000*1024):
    file_size = self.file.size
    if file_size > max_size:
        raise ValidationError(f"Your file size should be less then {max_size}b.")

# def vault_validation(value):
#     file_count =  .objects.filter(vault_id=self.vault_id)
#     if file_count > value:
#         raise ValidationError(
#             (f'You vault only can store {value} files')
#         )