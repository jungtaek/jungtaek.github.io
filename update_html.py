import os

PATH_TEMPLATE = './templates'
STR_BASE = 'base.temp'


def update_html(str_target):
    path_base = os.path.join(PATH_TEMPLATE, STR_BASE)
    print(path_base)

    path_target = os.path.join(PATH_TEMPLATE, str_target)
    print(path_target)

    path_new = os.path.join(PATH_TEMPLATE, str_target.split('.')[0] + '.html')
    print(path_new)

    new_file = []

    with open(path_base, 'r') as file_base:
        for row_base in file_base:
            new_file.append(row_base)

            if '<!-- START -->' in row_base:
                print(row_base)
                with open(path_target, 'r') as file_target:
                    for row_target in file_target:
                        new_file.append(row_target)

    print(f'len(new_file) = {len(new_file)}')

    with open(path_new, 'w') as file_new:
        for row_new in new_file:
            file_new.write(row_new)


if __name__ == '__main__':
    update_html('index.temp')
