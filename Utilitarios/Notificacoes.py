from pushbullet import PushBullet


def EnviarNotificacao(token, titulo, texto):
    pb = PushBullet(token)
    push = pb.push_note(titulo, texto)
