# -*- coding: utf-8 -*-
__author__ = 'Franklin'

# Tabela Cidades
Cidade.cep.requires = IS_NOT_EMPTY(error_message='Preencha o campo')
Cidade.nome.requires = IS_NOT_EMPTY(error_message='Preencha o campo')
Cidade.uf.requires = IS_IN_SET(UF, zero='Selecione uma UF')


# Tabela Alunos
Aluno.cidade.requires = IS_IN_DB(db,'cidades.id', '%(nome)s', zero='Selecione uma cidade')

# Tabela Professores
Professor.cidade.requires = IS_IN_DB(db, 'cidades.id', '%(nome)s', zero='Selecione uma cidade')

# Tabela Notas
Nota.aluno.requires = IS_IN_DB(db, 'alunos.id' , '%(nome)s', zero='Selecione um aluno')
Nota.professor.requires = IS_IN_DB(db  , 'professores.id' , '%(nome)s', zero='Selecione um professor')
Nota.disciplina.requires = IS_IN_DB(db , 'disciplinas.id', '%(nome)s', zero='Selecione uma disciplina')
Nota.unidade.requires = IS_IN_SET(UNIDADE, zero='Selecione uma unidade')

## Tabela Biblioteca
Biblioteca.arquivo.requires = IS_UPLOAD_FILENAME(extension='pdf')
Biblioteca.professor.requires = IS_IN_DB(db  , 'professores.id' , '%(nome)s' )
Biblioteca.disciplina.requires = IS_IN_DB(db  , 'disciplinas.id' , '%(nome)s' )

## Forum
Forum.mensagem.requires = IS_NOT_EMPTY(error_message='Nâo pode estar vazio')
Forum.disciplina.requires = IS_IN_DB(db, 'disciplinas.id', '%(nome)s')
IS_DATE(format='%d/%m/%Y')

##Comentarios
Comentario.mensagem.requires = IS_NOT_EMPTY()
Comentario.postagem.requires = IS_IN_DB(db , 'foruns.id' , '%(mensagem)s' )