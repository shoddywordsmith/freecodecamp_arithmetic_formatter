def arithmetic_arranger(problems, show_answers=False):
    
    # import regular expressions for text processing
    import re  
    
    # lists to store numbers and problem lengths for later arranging
    tops = []
    mids = []
    bottoms = []
    lengths = []
    operators = []
    
    # setting counter for loop with number of total math problems
    probs_counter = 0
    
    # PART 1 - initiating loop to dissemble and store relevant values, do math for solutions
    for problem in problems :

        # check total number of math problems and return error if over 5
        probs_counter = probs_counter + 1
        if probs_counter > 5 :
            prob_error = 'Error: Too many problems.'
            return prob_error

        # verify that problems only contain numbers and return error if false
        elements = problem.rsplit()
        if re.search('[a-z]+', elements[0]) != None or re.search('[a-z]+', elements[2]) != None:
            num_error = 'Error: Numbers must only contain digits.'
            return num_error

        # find and extract numbers from string
        numbers = re.findall(r'\d+', problem)
        first_num = numbers[0]
        second_num = numbers[1]

        # identify operator, define solution, append solution to list AS INT, return error if operator is invalid
        if ' + ' in problem :
            solution = int(first_num) + int(second_num)
            bottoms.append(solution)
            operator = '+'
            operators.append(operator)
        elif ' - ' in problem :
            solution = int(first_num) - int(second_num)
            bottoms.append(solution)
            operator = '-'
            operators.append(operator)
        else : 
            op_error = "Error: Operator must be '+' or '-'."
            return op_error

        # establish max number length (4 digits) and break if invalid
        if len(first_num) > 4 or len(second_num) > 4 :
            len_error = 'Error: Numbers cannot be more than four digits.'
            return len_error

        # append numbers to respective lists AS INT
        tops.append(int(first_num))
        mids.append(int(second_num))
        
        # establish horizontal length of each problem, must equal (length of the longest operand + 2)
        i = probs_counter - 1
        if len(str(tops[i])) >= len(str(mids[i])):
            bigger_num = len(str(tops[i]))
        else :
            bigger_num = len(str(mids[i]))
        
        problem_length = bigger_num + 2
        lengths.append(int(problem_length))
        # does the above have to be defined as INT?
    
    # PART 2, taking stored values and arranging them correctly
    
    # there must be 4 spaces between problems, assign to STR variable
    spaces = '   '
    
    # establish lists for each line's contents
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    
    # set counter for while loop to iterate through the number of math problems
    i = 0
    
    while i < probs_counter:
        
        # set spacing for top number, combine it with 4 spaces, append to line 1 list
        num = "{:{align}{width}}"
        line1_value = num.format(tops[i], align='>', width=int(lengths[i]))
        line1_arr_value = ' '.join([line1_value, spaces])
        line1.append(line1_arr_value)
        
        line2_value = num.format(mids[i], align='>', width=int(lengths[i]-2))
        line2_arr_value = ' '.join([operators[i], line2_value, spaces])
        line2.append(line2_arr_value)
        
        line3_arr_value = ' '.join(['-' * lengths[i], spaces])
        line3.append(line3_arr_value)
                                
        line4_value = num.format(bottoms[i], align='>', width=int(lengths[i]))
        line4_arr_value = ' '.join([line4_value, spaces])
        line4.append(line4_arr_value)
                                
        i = i + 1                       
    

    stripped_first_line = line1[i-1]
    stripped_first_line = stripped_first_line[:-4]
    line1.pop()
    line1.append(stripped_first_line)
    
    stripped_second_line = line2[i-1]
    stripped_second_line = stripped_second_line[:-4]
    line2.pop()
    line2.append(stripped_second_line)
    
    stripped_third_line = line3[i-1]
    stripped_third_line = stripped_third_line[:-4]
    line3.pop()
    line3.append(stripped_third_line)
    
    stripped_fourth_line = line4[i-1]
    stripped_fourth_line = stripped_fourth_line[:-4]
    line4.pop()
    line4.append(stripped_fourth_line)

    
    # concatenate all string lists into single strings
    line1_final = ''.join(line1)        
    line2_final = ''.join(line2)
    line3_final = ''.join(line3)
    line4_final = ''.join(line4)
    
    if show_answers == True :
        #arranged_problems = ' '.join([line1 + "\r\n" + line2 + "\r\n" + line3 + "\r\n" + line4])
        
        
        
        arranged_problems = (f"{line1_final}\n"
                             f"{line2_final}\n"
                             f"{line3_final}\n"
                             f"{line4_final}\n")
        #arranged_problems = [line1]
        #arranged_problems.append(line2)
        #arranged_problems.append(line3)
        #arranged_problems.append(line4)
    else : 
        arranged_problems = (f"{line1_final}\n"
                             f"{line2_final}\n"
                             f"{line3_final}\n")
    
    return arranged_problems
