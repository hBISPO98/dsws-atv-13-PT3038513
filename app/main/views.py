from flask import render_template, redirect, url_for, session, current_app, request, flash
from . import main
from .forms import NameForm  # Ajuste o nome do formulário se necessário
from .. import db
from ..models import User
from ..email import send_simple_message

# Rota principal
@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # Procura se o utilizador já existe na base de dados
        user = User.query.filter_by(username=form.name.data).first()

        if user is None:
            # Cria o novo utilizador e guarda no banco de dados
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False

            # Dispara a notificação por e-mail (usando o try-except do email.py)
            # Passa o e-mail do formulário, o assunto limpo e o nome do novo utilizador
            send_simple_message(
                to=form.email.data,
                subject="Novo Utilizador Cadastrado",
                newUser=form.name.data
            )
        else:
            session['known'] = True

        session['name'] = form.name.data
        return redirect(url_for('main.index'))

    # Procura todos os utilizadores para exibir na tabela da página principal
    users = User.query.all()

    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False),
                           users=users)

# Rota de exclusão de usuário
@main.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    username_deleted = user.username
    db.session.delete(user)
    db.session.commit()
    # Adição 'f' antes das aspas para a variável funcionar dentro da string
    flash(f'Usuário "{username_deleted}" excluído com sucesso!', 'success')
    return redirect(url_for('main.index'))

# Rota de edição de usuário
@main.route('/edit/<int:id>', methods=['POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    new_name = request.form.get('username')
    if new_name:
        user.username = new_name
        db.session.commit()
        flash(f'Usuário "{new_name}" atualizado com sucesso!', 'success')
    return redirect(url_for('main.index'))