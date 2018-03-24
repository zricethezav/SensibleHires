import argparse


def email_filename(employer):
    employer_formatted = employer.lower().replace(' ', '_').replace('-', '_')
    return '{}_email.txt'.format(employer_formatted)


def email(employer, name):
    with open('sample_email.txt', 'r') as f:
        contents = f.read()
        contents = contents.format(employer=employer, name=name)

    with open(email_filename(employer), 'w') as f:
        f.write(contents)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Email generator')
    parser.add_argument('employer', type=str, help='name of employer')
    parser.add_argument('name', type=str, help='your name')
    args = parser.parse_args()
    email(args.employer, args.name)