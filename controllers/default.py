# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    mensagem = 'Sejam bem vindo, ao sistema de gestão escolar Sirius \n' \
               'Informção e tecnologia, aliados à sua gestão!'
    return dict(message=mensagem)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

"""
 Definindo as funções do objeto Disciplina.
"""

@auth.requires_login()
def insert_disciplina():
    form = crud.create(Disciplina)
    return dict(form=form)

@auth.requires_login()
def update_disciplina():
    id_disciplina = request.args(0, cast=int)
    form = crud.update(Disciplina, id_disciplina)
    return dict(form=form)

@auth.requires_login()
def view_disciplina():
    grid = SQLFORM.grid(Disciplina)
    return dict(grid=grid)

@auth.requires_login()
def delete_disciplina():
    id_disciplina = request.args(0, cast=int)
    db(Disciplina.id == id_disciplina).delete()
    response.flash = 'Apagado com sucesso'
    redirect(URL('view_disciplina'))
############################### Fim das funções do objeto disciplina####################################################

"""
 Definindo as funções do objeto Cidade.
"""

@auth.requires_login()
def insert_cidade():

    form = SQLFORM(Cidade)

    if form.process().accepted:
        response.flash = 'Gravado com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def update_cidade():
    id_cidade = request.args(0, cast=int)

    form = SQLFORM(Cidade, id_cidade, showid=False)
    if form.process().accepted:
        response.flash = 'Atualizado com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Registro pronto para ser atualizado'
    return dict(form=form)

@auth.requires_login()
def view_cidade():
    response.title += ' | Cidade' # Identifica o nome da aba da página
    cidades = db(Cidade.id > 0).select()

    return dict(cidades=cidades)

@auth.requires_login()
def delete_cidade():
    id_cidade = request.args(0, cast=int)
    db(Cidade.id == id_cidade).delete()
    response.flash = 'Apagado com sucesso'
    redirect(URL('view_cidade'))

############################### Fim das funções do objeto cidade########################################################
"""
 Definindo as funções do objeto Aluno.
"""

@auth.requires_login()
def insert_aluno():
    form = SQLFORM(Aluno)

    if form.process().accepted:
        response.flash = 'Inserido com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def update_aluno():
    id_aluno = request.args(0, cast=int)

    form = SQLFORM(Aluno, id_aluno, showid=False)
    if form.process().accepted:
        response.flash = 'Atualizado com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Registro pronto para ser atualizado'
    return dict(form=form)

@auth.requires_login()
def view_aluno():
    aluno = db(Aluno.id > 0).select()
    return dict(mensagem=aluno)

@auth.requires_login()
def delete_aluno():
    id_aluno = request.args(0, cast=int)
    db(Aluno.id == id_aluno).delete()
    response.flash = 'Apagado com sucesso'
    redirect(URL('view_aluno'))
############################### Fim das funções do objeto aluno#########################################################
"""
 Definindo as funções do objeto Professor.
"""

@auth.requires_login()
def insert_professor():
    form = SQLFORM(Professor)

    if form.process().accepted:
        response.flash = 'Inserido com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def update_professor():
    id_professor = request.args(0, cast=int)

    form = SQLFORM(Professor, id_professor, showid=False)
    if form.process().accepted:
        response.flash = 'Atualizado com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Registro pronto para ser atualizado'
    return dict(form=form)

@auth.requires_login()
def view_professor():
    professor = db(Professor.id > 0).select()
    return dict(mensagem=professor)

@auth.requires_login()
def delete_professor():
    id_professor = request.args(0, cast=int)
    db(Professor.id == id_professor).delete()
    response.flash = 'Apagado com sucesso'
    redirect(URL('view_professor'))
############################### Fim das funções do objeto professor#####################################################
"""
 Definindo as funções do objeto Nota.
"""
@auth.requires_membership('Professor')
def insert_nota():
    form = SQLFORM(Nota)

    if form.process().accepted:
        response.flash = 'Inserido com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def update_nota():
    id_nota = request.args(0, cast=int)

    form = SQLFORM(Nota, id_nota, showid=False)
    if form.process().accepted:
        response.flash = 'Atualizado com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Registro pronto para ser atualizado'
    return dict(form=form)

@auth.requires_login()
def view_nota():
    nota = db(Nota.id > 0).select()
    return dict(mensagem=nota)

@auth.requires_login()
def delete_nota():
    id_nota = request.args(0, cast=int)
    db(Nota.id == id_nota).delete()
    response.flash = 'Apagado com sucesso'
    redirect(URL('view_nota'))

############################### Fim das funções do objeto nota##########################################################
"""
 Definindo as funções do objeto Biblioteca.
"""

@auth.requires_login()
def insert_biblioteca():
    form = SQLFORM(Biblioteca)

    if form.process().accepted:
        response.flash = 'Inserido com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def update_biblioteca():
    id_biblioteca = request.args(0, cast=int)

    form = SQLFORM(Biblioteca, id_biblioteca, showid=False)
    if form.process().accepted:
        response.flash = 'Atualizado com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Registro pronto para ser atualizado'
    return dict(form=form)

@auth.requires_login()
def view_biblioteca():
    biblioteca = db(Biblioteca.id > 0).select()
    return dict(mensagem=biblioteca)

@auth.requires_login()
def delete_biblioteca():
    id_biblioteca = request.args(0, cast=int)
    db(Biblioteca.id == id_biblioteca).delete()
    response.flash = 'Apagado com sucesso'
    redirect(URL('view_biblioteca'))


############################### Fim das funções do objeto biblioteca####################################################
"""
 Definindo as funções do objeto Forum.
"""
@auth.requires_login()
def insert_forum():
    form = SQLFORM(Forum)

    if form.process().accepted:
        response.flash = 'Inserido com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def update_forum():
    id_forum = request.args(0, cast=int)

    form = SQLFORM(Forum, id_forum, showid=False)
    if form.process().accepted:
        response.flash = 'Atualizado com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Registro pronto para ser atualizado'
    return dict(form=form)

@auth.requires_login()
def view_forum():
    forum = db(Forum.id > 0).select()
    return dict(forum=forum)

@auth.requires_login()
def delete_forum():
    id_forum = request.args(0, cast=int)
    db(Forum.id == id_forum).delete()
    response.flash = 'Apagado com sucesso'
    redirect(URL('view_forum'))

############################### Fim das funções do objeto Forum#########################################################
"""
 Definindo as funções do objeto Comentario.
"""

@auth.requires_login()
def insert_comentario():
    form = SQLFORM(Comentario)

    if form.process().accepted:
        response.flash = 'Inserido com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form=form)

@auth.requires_login()
def update_comentario():
    id_comentario = request.args(0, cast=int)
    Comentario.postagem.default = id_comentario
    Comentario.postagem.writable = False
    Comentario.postagem.readable = True
    form = SQLFORM(Comentario, id_comentario, showid=False)
    if form.process().accepted:
        response.flash = 'Atualizado com sucesso'
    elif form.errors:
        response.flash = 'Erros no formulário'
    else:
        response.flash = 'Registro pronto para ser atualizado'
    return dict(form=form)

@auth.requires_login()
def view_comentario():
    comentario = db(Comentario.id > 0).select()
    return dict(comentario=comentario)

@auth.requires_login()
def delete_comentario():
    id_comentario = request.args(0, cast=int)
    db(Comentario.id == id_comentario).delete()
    response.flash = 'Apagado com sucesso'
    redirect(URL('view_comentario'))

############################### Fim das funções do objeto Comentario####################################################

