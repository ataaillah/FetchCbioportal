#!/usr/bin/env python




import sys
import cbioportal
import listtools


commande=sys.argv[1]

if commande=='getCancerStudies':
    List_of_cancer_studies = cbioportal.GetCancerStudies()
    List_of_cancer_studies = listtools.utf8decode(List_of_cancer_studies)
    print(List_of_cancer_studies)
    filout_cancer_studies = listtools.writeListInText(List_of_cancer_studies, 'cancer_studies.txt')



if commande =='getProfileData':

    GENES = sys.argv[2]
    print(GENES)
    CASE_SET_ID=sys.argv[3]
    GENETIC_PROFILE_ID = sys.argv[4]
    GENES_LIST = GENES.split('+')
    List_of_Profile_Data = cbioportal.GetProfileData(CASE_SET_ID, GENETIC_PROFILE_ID, GENES)
    List_of_Profile_Data = listtools.utf8decode(List_of_Profile_Data)
    listtools.writeListInText(List_of_Profile_Data, 'ProfileData.txt')

if commande == 'getMutationData.txt':
    GENES = sys.argv[3]
    print(GENES)
    GENETIC_PROFILE_ID = sys.argv[2]
    print(GENETIC_PROFILE_ID)
    list_of_mutation_data_gene = cbioportal.GetMutationData(GENETIC_PROFILE_ID, GENES)
    list_of_mutation_data_gene = listtools.utf8decode(list_of_mutation_data_gene)
    listtools.writeListInText(list_of_mutation_data_gene,  "ExtendedMutationData.txt")

if commande == 'getClinicalData':
    CASE_SET_ID = sys.argv[2]
    list_clinical_data = cbioportal.getClinicalData(CASE_SET_ID)
    list_clinical_data = listtools.utf8decode(list_clinical_data)
    listtools.writeListInText(list_clinical_data, 'ClinicalData.txt')

if commande == 'getTypesOfCancer':
    List_of_cancer_types = cbioportal.GetTypesOfCancer()
    List_of_cancer_types = listtools.utf8decode(List_of_cancer_types)
    filout_cancer_types = listtools.writeListInText(List_of_cancer_types, 'CancerTypes.txt')

if commande == 'getCaseLists':
    CANCER_STUDY = sys.argv[2]
    print(CANCER_STUDY)
    List_of_caselists = cbioportal.GetCaseListForCancerStudie(CANCER_STUDY)
    List_of_caselists=listtools.utf8decode(List_of_caselists)
    filout_caselist=listtools.writeListInText(List_of_caselists,'Caselists.txt')