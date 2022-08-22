from django.core.mail import send_mail


adef send_email(data: dict) -> None:
    send_mail(
        subject=data['subject'],
        message=data['message'],
        from_email=data['from_email'],
        recipient_list=[data['to_email']],
        fail_silently=False,
    )
