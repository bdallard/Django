from import_export import resources, fields
from .models import Client 

class ClientResources(resources.ModelResource):
    cclikpi = fields.Field(column_name='cclikpi', attribute="cclikpi")
    nom = fields.Field(column_name='nom', attribute="nom")
    prenom = fields.Field(column_name='prenom', attribute="prenom")
    message = fields.Field(column_name='message', attribute="message")

    class Meta: 
	model = Client 
	exclude = ('id') 
	skip_unchanged = True
	import_id_fields = ('cclikpi', 'nom', 'prenom', 'message',)
	fields =  ('cclikpi', 'nom', 'prenom', 'message',)


