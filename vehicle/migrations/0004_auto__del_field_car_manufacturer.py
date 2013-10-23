# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Car.manufacturer'
        db.delete_column(u'vehicle_car', 'manufacturer_id')

        # Adding M2M table for field manufacturer on 'Car'
        m2m_table_name = db.shorten_name(u'vehicle_car_manufacturer')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('car', models.ForeignKey(orm[u'vehicle.car'], null=False)),
            ('manufacturer', models.ForeignKey(orm[u'production.manufacturer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['car_id', 'manufacturer_id'])


    def backwards(self, orm):
        # Adding field 'Car.manufacturer'
        db.add_column(u'vehicle_car', 'manufacturer',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=123, to=orm['production.Manufacturer']),
                      keep_default=False)

        # Removing M2M table for field manufacturer on 'Car'
        db.delete_table(db.shorten_name(u'vehicle_car_manufacturer'))


    models = {
        u'production.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'vehicle.car': {
            'Meta': {'object_name': 'Car'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['production.Manufacturer']", 'symmetrical': 'False'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2010'})
        }
    }

    complete_apps = ['vehicle']