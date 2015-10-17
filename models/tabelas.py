__author__ = 'Franklin'

# -*- coding: utf-8 -*-

from datetime import datetime

UF = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR',
      'PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO']

UNIDADE = ['I','II','III','IV']

"""
    IDENTIFICAÇÃO DA TABELA DE DISCIPLINAS
"""
Disciplina = db.define_table('disciplinas',
    Field('nome', 'string', length=50, notnull=True, label='Nome'),
    Field('ch', 'integer', notnull=True, label='Carga horária'),
    auth.signature
)


"""
    IDENTIFICAÇÃO DA TABELA DE CIDADES
"""
Cidade = db.define_table('cidades',
    Field('cep', 'string', length=8, label='Cep'),
    Field('nome', 'string', length=50, label='Nome'),
    Field('uf', 'string', length=2, label='Uf'),
    auth.signature
)# FIM DA TABELA CIDADE

"""
 IDENTIFICAÇÃO DA TABELA DE ALUNOS
"""
Aluno = db.define_table('alunos',
    Field('nome', 'string', notnull=True, label='Nome'),
    Field('cidade', 'reference cidades', ondelete='NO ACTION', notnull=True, label='Cidade'),
    Field('endereco', 'string', notnull=True, label='Endereço'),
    Field('numero', 'string', notnull=True, label='Número'),
    Field('data_nasc','date', notnull=True, label='Data nascimento'),
    Field('tel', 'string', notnull=True, label='Telefone'),
    Field('email', 'string', notnull=True, label='Email'),
    auth.signature
)# FIM DA TABELA ALUNO

"""
 IDENTIFICAÇÃO DA TABELA DE PROFESSORES
"""
Professor = db.define_table('professores',
    Field('nome', 'string', notnull=True, label='Nome'),
    Field('cidade', 'reference cidades', ondelete='NO ACTION', notnull=True, label='Cidade'),
    Field('endereco', 'string', notnull=True, label='Endereço'),
    Field('numero', 'string', notnull=True, label='Número'),
    Field('data_nasc','date', notnull=True, label='Data nascimento'),
    Field('tel', 'string', notnull=True, label='Telefone'),
    Field('email', 'string', notnull=True, label='Email'),
    auth.signature
)# FIM DA TABELA PROFESSOR

"""
 IDENTIFICAÇÃO DA TABELA DE NOTAS
"""
Nota = db.define_table('notas',
    Field('aluno' , 'reference alunos' , notnull=True , label="Aluno"),
    Field('professor' , 'reference professores' ,ondelete='NO ACTION', label="Professor"),
    Field('disciplina' , 'reference disciplinas' ,ondelete='NO ACTION',label="Disciplina"),
    Field('unidade', 'string', notnull=True, label='Unidade'),
    Field('nota' , 'float' , default=0.00, label="Nota"),
    auth.signature
)# FIM DA TABELA NOTAS

"""
 IDENTIFICAÇÃO DA TABELA BIBLIOTECA
"""
Biblioteca = db.define_table('bibliotecas',
    Field('arquivo' , 'upload' , notnull=True , label="Arquivo"),
    Field('disciplina' , 'reference disciplinas' , ondelete='NO ACTION' ,  label="Disciplina"),
    Field('professor' , 'reference professores' , ondelete='NO ACTION' ,  label="Professor"),
    auth.signature
)# FIM DA TABELA BIBLIOTECA

"""
 IDENTIFICAÇÃO DA TABELA FORUM
"""
Forum = db.define_table('foruns',
    Field('titulo' , 'string' , notnull=True , label="Titulo"),
    Field('disciplina' , 'reference disciplinas' , ondelete='NO ACTION' ,  label="Disciplina"),
    Field('mensagem' , 'text' , notnull=True , label="Mensagem"),
    auth.signature
)# FIM DA TABELA FORUM

"""
 IDENTIFICAÇÃO DA TABELA COMENTARIO
"""
Comentario = db.define_table('comentarios',
    Field('postagem' , 'reference foruns' , notnull=True ,ondelete='NO ACTION', label="Postagem" ),
    Field('mensagem' , 'text' , notnull=True , label="Mensagem") ,
    auth.signature
)# FIM DA TABELA COMENTARIO