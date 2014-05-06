# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AppDrfModel'
        db.create_table(u'app_drf_appdrfmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('appFlag', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'app_drf', ['AppDrfModel'])


    def backwards(self, orm):
        # Deleting model 'AppDrfModel'
        db.delete_table(u'app_drf_appdrfmodel')


    models = {
        u'app_drf.appdrfmodel': {
            'Meta': {'object_name': 'AppDrfModel'},
            'appFlag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['app_drf']