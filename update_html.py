import os

PATH_TEMPLATE = './templates'
STR_BASE = 'base.temp'


def update_html(str_target):
    path_base = os.path.join(PATH_TEMPLATE, STR_BASE)
    print(path_base)

    path_target = os.path.join(PATH_TEMPLATE, str_target)
    print(path_target)

    path_new = os.path.join('./', str_target.split('.')[0] + '.html')
    print(path_new)

    new_file = []

    with open(path_base, 'r') as file_base:
        for row_base in file_base:
            if '<title>JUNGTAEK KIM</title>' in row_base:
                if str_target == 'index.temp':
                    pass
                elif str_target == 'news.temp':
                    row_base = row_base.replace('JUNGTAEK KIM', 'NEWS | JUNGTAEK KIM')
                elif str_target == 'profile.temp':
                    row_base = row_base.replace('JUNGTAEK KIM', 'PROFILE | JUNGTAEK KIM')
                elif str_target == 'publications_categorized.temp':
                    row_base = row_base.replace('JUNGTAEK KIM', 'PUBLICATIONS | JUNGTAEK KIM')
                elif str_target == 'committees.temp':
                    row_base = row_base.replace('JUNGTAEK KIM', 'COMMITTEES | JUNGTAEK KIM')
                elif str_target == 'talks.temp':
                    row_base = row_base.replace('JUNGTAEK KIM', 'TALKS | JUNGTAEK KIM')
                elif str_target == 'archives.temp':
                    row_base = row_base.replace('JUNGTAEK KIM', 'ARCHIVES | JUNGTAEK KIM')
                else:
                    raise ValueError('Need to add a condition.')
                    
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
    update_html('news.temp')
    update_html('profile.temp')
    update_html('publications_categorized.temp')
    update_html('committees.temp')
    update_html('talks.temp')
    update_html('archives.temp')
