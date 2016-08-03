

class SchoolScraper(object):
    def __init__(self):
        self.school_file='SchoolList'

    def get_schools(self):
        school_list =[]
        with open(self.school_file, 'r')as f:
            for line in f:
                line_formatted = ' '.join(line.split())
                schoolID, _, school_name = line_formatted.partition(" ")
                school_list.append({
                    'id':schoolID,
                    'name': school_name

                })
        return school_list