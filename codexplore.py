
from Seperategmail import emailProcess, printMsg

def main():
    emails = ['Elise33@gmail.com', 'Mallie.Grady0@gmail.com', 'Brionna.Donnelly14@hotmail.com', 'Sarina_Roberts@gmail.com', 'Wilbert_Conroy@yahoo.com']
    for email in emails:
        username, email_domain = emailProcess(email)
        printMsg(username, email_domain)

if __name__ == '__main__':
    main()