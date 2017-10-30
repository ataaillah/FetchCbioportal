import texttools
def utf8decode(LIST):
    for i in range(len(LIST)):
        LIST[i]=LIST[i].decode('utf-8')
    return LIST

def writeListInText(LIST,FILE_NAME):
    filout = open(FILE_NAME, "w")

    for i in LIST:
        if type(i) == str:
            if '\n' in i:
                filout.write(i)
            else:
                filout.write(i+'\n')
        elif type(i) == list:
            if '\n' in '\t'.join(i):
                filout.write('\t'.join(i))
            else:
                filout.write('\t'.join(i)+'\n')
        if type(i)== int:
            filout.write(str(i) + '\n')

    filout.close()






def MakeListOfElementFromListOfTabulatedLines(MY_LIST_OF_TABULATED_LINES, COLUMN_LIST):
    #print(MY_LIST_OF_TABULATED_LINES)
    My_list_of_elements = []
    for LINE in MY_LIST_OF_TABULATED_LINES:  # mettre la colonne donnee en argument dans un liste
        #print('print(MY_LIST_OF_TABULATED_LINES)')
        #print(MY_LIST_OF_TABULATED_LINES)
        #print(len(MY_LIST_OF_TABULATED_LINES))
        My_element=texttools.takeAListOfElemenentIntabluatedLine(LINE, COLUMN_LIST)
        My_list_of_elements.append(My_element)
    return My_list_of_elements

def MakeAllTabulatedLinesElementInAList(MY_LIST_OF_TABULATED_LINES):

    # print(MY_LIST_OF_TABULATED_LINES)
    My_list_of_lists = []
    for LINE in MY_LIST_OF_TABULATED_LINES:  # mettre la colonne donnee en argument dans un liste
        # print('print(MY_LIST_OF_TABULATED_LINES)')
        # print(MY_LIST_OF_TABULATED_LINES)
        # print(len(MY_LIST_OF_TABULATED_LINES))

        My_list = LINE.split('\t')
        #print(My_list)
        My_list_of_lists.append(My_list)
        #print(len(My_list_of_lists))

    return My_list_of_lists


def concatenateListElement(LIST,SYMBOL):
    gene_string = ''
    for Element in LIST:
        gene_string = gene_string + Element + SYMBOL
    gene_string=gene_string[:-1]
    return gene_string


def AppendSideBySideTwoLists(MY_LIST_1, MY_LIST_2, INTERCALAR):
    # intercalar: ":" or "-" etc
    My_combined_list=[]
    for i in range(len(MY_LIST_1)):
        My_combined_list.append(MY_LIST_1[i] + INTERCALAR + MY_LIST_2[i])
    return  My_combined_list