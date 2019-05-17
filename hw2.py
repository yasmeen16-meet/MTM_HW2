def data_contains(faculty_program_dict, program):
    for value in faculty_program_dict.values():
        if value == program:
            return True
    return False


def inside_contest(faculty, file_name):
    file = open(file_name, 'r')
    students_already_voted = []
    programs_votes = {}
    first = ''
    for current_line in file:
        line_list = current_line.split()
        if line_list[0] == 'inside':
            if line_list[-1] == faculty and not line_list[2] in students_already_voted:
                students_already_voted.append(line_list[2])
                voted_program = line_list[3]
                if voted_program in programs_votes:
                    current_votes = int(programs_votes[voted_program])
                    programs_votes[voted_program] = current_votes + 1
                else:
                    programs_votes[voted_program] = 1
        elif line_list[0] == 'staff':
            voted_program = line_list[2]
            if line_list[-1] == faculty:
                if voted_program in programs_votes:
                    programs_votes[voted_program] += 20
                else:
                    programs_votes[voted_program] = 20
    max_votes = 0
    for program, votes in programs_votes.items():
        if votes > max_votes:
            max_votes = votes
            first = program
    file.close()
    return first


# first = inside_contest('CS', 'input.txt')
# print(first)

# main()
file1 = open('input.txt', 'r')
faculty_program = {}
for line_current in file1:
    line = line_current.split()
    if line[0] == 'inside':
        faculty_current = line[-1]
        if faculty_current not in faculty_program:
            first_program = inside_contest(faculty_current, 'input.txt')
            # print(first_program)
            faculty_program[faculty_current] = first_program
file1.close()
# print(faculty_program)

file2 = open('input.txt', 'r')
forbidden_votes = []
for line_current in file2:
    line = line_current.split()
    # checking that the vote is legal, voting for a valid program
    if line[0] == 'techniovision':
        student_id = line[1]
        if not data_contains(faculty_program, line[2]):
            forbidden_votes.append(student_id)
        # elif student_id not in forbidden_votes:
        # call the function students_votes(...)

file2.close()
print(forbidden_votes)
