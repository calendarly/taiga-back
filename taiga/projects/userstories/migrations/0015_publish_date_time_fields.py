# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



class Migration(migrations.Migration):

     dependencies = [ 
         ('userstories', '0014_auto_20160928_0540'),
     ]   

     operations = [ 
         migrations.AddField(
             model_name='userstory',
             name='publish_date',
             field=models.TextField(blank=True, null=True, verbose_name='publish date'),
         ),

         migrations.AddField(
             model_name='userstory',
             name='publish_time',
             field=models.TextField(blank=True, null=True, verbose_name='publish time'),
         ),
     ]   
