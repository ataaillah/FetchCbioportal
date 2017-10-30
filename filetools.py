import numpy as np
import listtools
def getColumnOfFileInList(FILE_NAME ,COLUMN_LIST, NUM_TOP_LINES_OFF):
    # take the name of input file
    #print(FILE_NAME)
    #create the name of output file
    #output_file_name=input_file_name[:-4]+'_Extended_mutated_data'
    #open input file
    fillin_input_file=open(FILE_NAME,'r')
    # read input file and put each line in an element of a list
    lines_input_file=fillin_input_file.readlines() # le output est une liste de lignes: taille de la liste = nombre de
                                                # lignes de input_file_name
    fillin_input_file.close()
    #print(lines_input_file)
    lines_input_file=lines_input_file[NUM_TOP_LINES_OFF:]

    my_list=listtools.MakeListOfElementFromListOfTabulatedLines(lines_input_file,COLUMN_LIST)
    my_list=np.array(my_list)


    #print(gene_list)
    return my_list


def getAllLinesOfFileInList(FILE_NAME,TOP_LINES_TO_SKIP):
    input_file=open(FILE_NAME,'r')
    list_of_lines = input_file.readlines()  # le output est une liste de lignes: taille de la liste = nombre de
    # lignes de input_file_name
    input_file.close()
    list_of_lines=list_of_lines[TOP_LINES_TO_SKIP:]
    my_list=listtools.MakeAllTabulatedLinesElementInAList(list_of_lines)
    #print(my_list)
    my_list=np.array(my_list)
    return my_list
