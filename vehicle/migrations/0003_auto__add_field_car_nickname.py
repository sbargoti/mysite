# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Car.nickname'
        db.add_column(u'vehicle_car', 'nickname',
                      self.gf('django.db.models.fields.CharField')(default=123, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Car.nickname'
        db.delete_column(u'vehicle_car', 'nickname')


    models = {
        u'production.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'vehicle.car': {
            'Meta': {'object_name': 'Car'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['production.Manufacturer']"}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2010'})
        }
    }

    complete_apps = ['vehicle']