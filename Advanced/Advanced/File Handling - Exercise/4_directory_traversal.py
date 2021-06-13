import os


def extract_files():

    _, _, files = next(os.walk(input()))
    return files


def get_report_info(files):

    raw_report = {}
    for file in files:
        _, extension = os.path.splitext(file)
        if extension not in raw_report:
            raw_report[extension] = []
        raw_report[extension].append(file)
    return raw_report


def get_and_sort_report(report_info):

    sorted_report_info = dict(sorted(report_info.items()))
    report = ''
    for extension, files in sorted_report_info.items():
        report += f'{extension}\n'
        sorted_files = sorted(files)
        for file in sorted_files:
            report += f'- - - {file}\n'
    return report[:-1]


def save_report_on_desktop(report):
    ### Works for Windows and Linux ###

    with open(os.path.join(os.path.expanduser('~'), 'Desktop', 'report.txt'), 'w') as file:
        file.write(report)


def start_program():

    files = extract_files()
    report_info = get_report_info(files)
    report = get_and_sort_report(report_info)
    save_report_on_desktop(report)


start_program()
