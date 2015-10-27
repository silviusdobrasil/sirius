# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    return dict(message=T('Welcome to web2py!'))


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

def contato():
    response.subtitle += " -> Contato"
    form = SQLFORM.factory(
        Field('nome', requires=IS_NOT_EMPTY(), label='Nome'),
        Field('email', requires=IS_EMAIL()),
        Field('mensagem', 'text', requires=IS_NOT_EMPTY(), label='Mesagem')
        )
    if form.process().accepted:
        mail.send(
            to=['protonfranklin@gmail.com'],
            subject='Novo email de %s' %form.vars.nome,
            reply_to=form.vars.email,
            message=form.vars.mensagem,
            )
        session.flash = 'Mensagem enviada'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Ops, algo errado no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form = form)

def inserir_cidade():
    response.subtitle += " -> Inserir cidades"
    form = crud.create(Cidade)
    return dict(form=form)


# Será necessário criar um grupo chamado professor para acessar a rotina.
@auth.requires_membership('professor')
def inserir_notas():
    response.subtitle += " -> Inserir notas"
    form = crud.create(Notas)
    return dict(form=form)

@auth.requires_membership('professor')
def novo_arquivo():
    response.subtitle += " -> Enviar arquivos"
    form = crud.create(Biblioteca)
    return dict(form=form)

@auth.requires_login()
def nova_mensagem():
    form = crud.create(Forum)
    return dict(form=form)

def forum():
    response.subtitle += " -> Fórum"
    posts = db(Forum.id>0).select() 
    return dict(posts=posts)

@auth.requires_login()
def ver_mensagem():
    id_mensagem = request.args(0, cast = int)
    mensagem = db(db.forum.id == id_mensagem).select().first()

    Comentarios.postagem.default = id_mensagem
    Comentarios.postagem.writable = Comentarios.postagem.readable = False
    form = crud.create(Comentarios)
    coments = db(Comentarios.postagem == id_mensagem).select()
    return dict(mensagem=mensagem, form=form, coments=coments)
    
@auth.requires_login()
def notas():
    response.subtitle += " -> Notas"
    if request.post_vars.busca:
        print request.post_vars
        #notas = db(Notas.)
    else:
        notas = db(Notas.id > 0).select()
    return dict(notas=notas)

def ver_notas():
    response.subtitle += " -> Consultar notas"
    id_nota = request.args(0, cast=int)
    total_notas = db(Notas.id > id_nota).count()

    try:
        pag = int(request.vars.pagina)
        if pag <= 0:
            redirect(URL('ver_notas', args=request.args, vars={'pagina':1}))
        if total_notas % 5 == 0:
            red = total_notas / 5
            if pag > red:
                redirect(URL('ver_notas', args=request.args, vars={'pagina': red}))
        else:
            red = total_notas / 5 + 1
            if pag > red:
                redirect(URL('ver_notas', args=request.args, vars={'pagina': red}))

    except TypeError:
        redirect(URL('ver_notas', args=request.args, vars={'pagina':1}))

    inicio = (pag - 1) * 5
    fim = pag * 5
    notas = db(Notas.id > id_nota).select(limitby=(inicio,fim))

    return dict(notas=notas, total_notas=total_notas)

def biblioteca():
    response.subtitle += " -> Biblioteca"
    arquivos = db(Biblioteca.id > 0).select()
    return dict(arquivos=arquivos)