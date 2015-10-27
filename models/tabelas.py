# -*- coding: utf-8 -*-
from datetime import datetime

UF = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR',
      'PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO']

UNIDADE = ['I','II','III','IV']

Cidade = db.define_table('cidades',
	Field('cep', 'string', label = 'Cep'),
	Field('nome', 'string', label = 'Nome'),
	Field('uf', 'string', requires=IS_IN_SET(UF) , length=2, label = 'Uf'),
	auth.signature
)

Notas = db.define_table('notas',
	Field('nota', 'float', default = 0, label = 'Nota'),
	Field('aluno', 'reference auth_user', notnull = True, label = 'Aluno'),
	Field('professor', 'reference auth_user', ondelete = "NO ACTION", label = 'Professor'),
	)

Biblioteca = db.define_table('biblioteca',
	Field('arquivo', 'upload', notnull = True, label = 'Arquivo'),
	Field('professor', 'reference auth_user', ondelete = 'NO ACTION', label = 'Professor'),
	Field('titulo', 'string', notnull = True, label = 'Título'),
	)

Forum = db.define_table('forum',
	Field('titulo', 'string', notnull = True, label = 'Título'),
	Field('mensagem', 'text', notnull = True, label = 'Mensagem'),
	auth.signature
	)

Comentarios = db.define_table('comentarios',
	Field('mensagem', 'text', notnull = True, label = 'Mensagem'),
	Field('postagem', 'reference forum', label = 'Postagem'),
	auth.signature
	)