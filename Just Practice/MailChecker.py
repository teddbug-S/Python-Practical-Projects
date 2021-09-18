import webbrowser

trusted_websites = ['facebook.com', 'instagram.com', 'python.org', 'google.com', 'twitter.com', 'yahoo.com']

user_entry = input('Enter Email or website: ')

server_names = ['gmail', 'yahoo']


def checker(text):
    if '@' in text and text.endswith('.com'):
        server_name = text[slice(text.index('@')+1, text.index('.com'))]
        company_name = text[slice(0, text.index("@"))]
        if server_name in server_names:
            print(f'Server name: {server_name.capitalize()}')
            print(f'Sender name: {company_name.capitalize()}')
        else:
            print("Not from yahoo nor google.")
            print(f'Server name: {server_name.capitalize()}')
            print(f'Sender name: {company_name.capitalize()}')

    elif text.endswith('.com') or text.endswith('.org'):
        site = text.strip('www.').lower()
        if site in trusted_websites:
            print(f"{site} is a safe website, I'm opening it...")
            webbrowser.open_new_tab(site)
        else:
            print(f"I don't know much about this website but I'm opening it anyway {site}")
            webbrowser.open_new_tab(site)
    else:
        print('Please enter a valid email address or website.')


checker(user_entry)
