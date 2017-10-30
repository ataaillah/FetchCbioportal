import numpy as np
def TakeAnElementInTabultatedLine(MY_LINE, MY_COL):

        #print(MY_LINE)
    My_line_splited = MY_LINE.split('\t')
        #print(My_line_splited)
    My_element="".join(My_line_splited[int(MY_COL) - 1:int(MY_COL)])
        #   print(My_element)

    My_element=MY_LINE
    return My_element

def takeAListOfElemenentIntabluatedLine(MY_LINE,MY_COL_LIST):
    if type(MY_COL_LIST) == list:
        if "\n" in MY_LINE:
            MY_LINE = MY_LINE[:-1]
            My_line_splited = np.array(MY_LINE.split('\t'))
            My_selected_columns = list(My_line_splited[MY_COL_LIST])
        else:
            My_line_splited = np.array(MY_LINE.split('\t'))
    #print('print(My_line_splited)')
    #print(My_line_splited)
    #print(len(My_line_splited))

            #My_line_splited=My_line_splited[My_col_list]
            My_selected_columns=list(My_line_splited[MY_COL_LIST])
    elif type(MY_COL_LIST)== str and MY_COL_LIST == "all":
        if "\n" in MY_LINE:
            MY_LINE=MY_LINE[:-1]
            My_line_splited = np.array(MY_LINE.split('\t'))
            My_selected_columns =list(My_line_splited)
        else:
            My_line_splited = np.array(MY_LINE.split('\t'))
            My_selected_columns = list(My_line_splited)

    return My_selected_columns

def MakeAllTabulatedElementofalineInAList(MY_LINE):
    My_line_splited = MY_LINE.split('\t')


    return My_line_splited

import urllib.request
def GetMutationData(CANCER_STUDY,GENE):
    "http: // www.cbioportal.org / webservice.do?cmd = getMutationData & case_set_id = gbm_tcga_all & genetic_profile_id = gbm_tcga_mutations & gene_list = EGFR + PTEN"
    Url = 'http://www.cbioportal.org/webservice.do?cmd=getMutationData&case_set_id=' + CANCER_STUDY + '_all&genetic_profile_id=' + CANCER_STUDY + '_mutations&gene_list=' + GENE
    req = urllib.request.Request(Url)
    resp = urllib.request.urlopen(req)
    List_of_mutation_data = resp.readlines()
    return List_of_mutation_data

