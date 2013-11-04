# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'onetoone_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'onetoone', ['Place'])

        # Adding model 'Restaurant'
        db.create_table(u'onetoone_restaurant', (
            ('place', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['onetoone.Place'], unique=True, primary_key=True)),
            ('serves_hot_dogs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('serves_pizza', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'onetoone', ['Restaurant'])

        # Adding model 'Waiter'
        db.create_table(u'onetoone_waiter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onetoone.Restaurant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'onetoone', ['Waiter'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'onetoone_place')

        # Deleting model 'Restaurant'
        db.delete_table(u'onetoone_restaurant')

        # Deleting model 'Waiter'
        db.delete_table(u'onetoone_waiter')


    models = {
        u'onetoone.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'onetoone.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'place': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['onetoone.Place']", 'unique': 'True', 'primary_key': 'True'}),
            'serves_hot_dogs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'serves_pizza': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'onetoone.waiter': {
            'Meta': {'object_name': 'Waiter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onetoone.Restaurant']"})
        }
    }

    complete_apps = ['onetoone']