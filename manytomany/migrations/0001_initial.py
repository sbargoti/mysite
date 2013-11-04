# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publication'
        db.create_table(u'manytomany_publication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'manytomany', ['Publication'])

        # Adding model 'Article'
        db.create_table(u'manytomany_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'manytomany', ['Article'])

        # Adding M2M table for field publications on 'Article'
        m2m_table_name = db.shorten_name(u'manytomany_article_publications')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'manytomany.article'], null=False)),
            ('publication', models.ForeignKey(orm[u'manytomany.publication'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'publication_id'])


    def backwards(self, orm):
        # Deleting model 'Publication'
        db.delete_table(u'manytomany_publication')

        # Deleting model 'Article'
        db.delete_table(u'manytomany_article')

        # Removing M2M table for field publications on 'Article'
        db.delete_table(db.shorten_name(u'manytomany_article_publications'))


    models = {
        u'manytomany.article': {
            'Meta': {'ordering': "('headline',)", 'object_name': 'Article'},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['manytomany.Publication']", 'symmetrical': 'False'})
        },
        u'manytomany.publication': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Publication'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['manytomany']