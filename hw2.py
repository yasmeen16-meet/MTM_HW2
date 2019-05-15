

def inside_contest(faculty,file_name):

    file = open(file_name, 'r')
    students_already_voted = []
    programs_votes = {}
    first_program = ''
    for current_line in file:
        line_list = current_line.split()
        if line_list[0] == 'inside':
            if line_list[-1] == faculty and not line_list[2] in students_already_voted:
                students_already_voted.append(line_list[2])
                voted_program = line_list[3]
                if voted_program in programs_votes:
                    current_votes = int(programs_votes[voted_program])
                    programs_votes[voted_program] = current_votes+1
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
            first_program = program
    file.close()
    return first_program


first = inside_contest('CS', 'input.txt')
print(first)
