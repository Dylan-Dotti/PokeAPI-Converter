import sys

def print_progress_bar(value, endvalue, label="Progress", same_line=True,bar_length=30):
        percent = float(value) / endvalue
        arrow = '=' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        sys.stdout.write("{0}{1}: [{2}] {3}/{4} ({5}%)".format(('\r' if same_line else ''), label, arrow + spaces, value, endvalue, int(round(percent * 100))))
        sys.stdout.flush()