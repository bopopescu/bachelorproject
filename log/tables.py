# example/app/tables.py
from models import Donor
from table import Table
from table.columns import Column
# from django.core.urlresolvers import reverse_lazy

class PersonTable(Table):
    firstName = Column(field='firstName')
    lastName = Column(field='lastName')
    createdDate = Column(field='createdDate')
    class Meta:
        model = Donor
        
        # ajax_source = reverse_lazy('donors')