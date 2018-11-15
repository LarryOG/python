

def email_at_domain (domain, email):
    if email.count('@') != 1 or email[0] == '@' or email.split('@')[1] != domain:
        print('Email ', email, ' is not valid at ', domain)
    else:
        print('Email ',email, ' is valid at ', domain )


some_domain = input('Enter domain: ')
some_email = input('Enter email: ')
email_at_domain(some_domain,some_email)
