class StudentsDataException(Exception):
    def __init__(self, f_name='unknown', message='error'):
        Exception.__init__(self, message)
        self.f_name = f_name
        self.message = message

class BadLine(StudentsDataException):
    def __init__(self, f_name='unknown', message='contains bad line'):
        StudentsDataException.__init__(self, f_name, message)

class FileEmpty(StudentsDataException):
    def __init__(self, f_name='unknown', message='file is empty'):
        StudentsDataException.__init__(self, f_name, message)

def ask_f_name():
    return input('Enter filename: ')

def read_file(f_name):
    with open(f_name, 'r') as f:
        lines = f.readlines()
        if len(lines) == 0:
            raise FileEmpty
        l_list = [l.split() for l in lines]
        f_dict = {}
        for txt in l_list:
            if len(txt) != 3:
                raise BadLine
            name = txt[0] + ' ' + txt[1]
            grade = float(txt[2])
            if name in f_dict.keys():
                f_dict[name] += grade
            else:
                f_dict[name] = grade
    return f_dict

if __name__ == '__main__':
    f_name = ask_f_name()
    try:
        f_dict = read_file(f_name)
        f_list = sorted(f_dict.items(), key=lambda x: x[0])
        for d in f_list:
            print(d[0] + '\t' + str(d[1]))
    except FileNotFoundError as fn:
        print('File:', f_name, 'does not exist')
    except FileEmpty as fe:
        print('File:', f_name, ':', fe.message)
    except BadLine as bl:
        print('File:', f_name, ':', bl.message)
    except:
        print('Unexpected error')

