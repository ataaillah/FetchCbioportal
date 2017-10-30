import urllib.request
def GetTypesOfCancer():
    """Retrieves a list of all the clinical types of cancer stored on the server
        OUTPUT:
        A tab-delimited file with two columns:
        type_of_cancer_id: a unique text identifier used to identify the type of cancer. For example, "gbm" identifies Glioblastoma multiforme.
        name: short name of the type of cancer.

    """
    Url = 'http://www.cbioportal.org/webservice.do?cmd=getTypesOfCancer'
    req = urllib.request.Request(Url)
    resp = urllib.request.urlopen(req)
    List_of_cancer_types = resp.readlines()

    return List_of_cancer_types


def GetCancerStudies():
    """Retrieves meta-data regarding cancer studies stored on the server.
        OUTPUT:
        A tab-delimited file with three columns:
        cancer_study_id: a unique ID that should be used to identify the cancer study in subsequent interface calls.
        name: short name of the cancer study.
        description: short description of the cancer study.

    """
    Url = 'http://www.cbioportal.org/webservice.do?cmd=getCancerStudies'
    req = urllib.request.Request(Url)
    resp = urllib.request.urlopen(req)
    List_of_cancer_studies = resp.readlines()

    return List_of_cancer_studies

def GetGeneticProfileForCancerStudie(CANCER_STUDY):
    """
    Retrieves meta-data regarding all genetic profiles, e.g. mutation or copy number profiles, stored about a specific cancer study.

    OUTPUT:
    A tab-delimited file with six columns:

    genetic_profile_id: a unique ID used to identify the genetic profile ID in subsequent interface calls. This is a human readable ID. For example, "gbm_mutations" identifies the TCGA GBM mutation genetic profile.
    genetic_profile_name: short profile name.
    genetic_profile_description: short profile description.
    cancer_study_id: cancer study ID tied to this genetic profile. Will match the input cancer_study_id.
    genetic_alteration_type: indicates the profile type. Will be one of:
        MUTATION
        MUTATION_EXTENDED
        COPY_NUMBER_ALTERATION
        MRNA_EXPRESSION
        METHYLATION
    show_profile_in_analysis_tab: a boolean flag used for internal purposes (you can safely ignore it).
    """

    Url = 'http://www.cbioportal.org/webservice.do?cmd=getGeneticProfiles&cancer_study_id='+CANCER_STUDY
    req = urllib.request.Request(Url)
    resp = urllib.request.urlopen(req)
    List_of_genetic_profile = resp.readlines()
    return List_of_genetic_profile

def GetCaseListForCancerStudie(CANCER_STUDY):
    """
    Retrieves meta-data regarding all case lists stored about a specific cancer study.
    For example, a within a particular study, only some cases may have sequence data,
    and another subset of cases may have been sequenced and treated with a specific
    therapeutic protocol. Multiple case lists may be associated with each cancer study,
    and this method enables you to retrieve meta-data regarding all of these case lists.
    OUTPUT
    A tab-delimited file with five columns:

    case_list_id: a unique ID used to identify the case list ID in subsequent interface calls. This is a human readable ID. For example, "gbm_all" identifies all cases profiles in the TCGA GBM study.
    case_list_name: short name for the case list.
    case_list_description: short description of the case list.
    cancer_study_id: cancer study ID tied to this genetic profile. Will match the input cancer_study_id.
    case_ids: space delimited list of all case IDs that make up this case list.

    """
    Url = 'http://www.cbioportal.org/webservice.do?cmd=getCaseLists&cancer_study_id='+CANCER_STUDY
    req = urllib.request.Request(Url)
    resp = urllib.request.urlopen(req)
    List_of_caselists = resp.readlines()
    return List_of_caselists


def GetProfileData(CASE_SET_ID, GENETIC_PROFILE_ID,GENE): # ! je peux donner une liste ou iterer plusieur fois sur une liste
    """

    Retrieves genomic profile data for one or more genes.

    COMMANDE ARGUMENTS:
    #CASE_SET_ID='gbm_tcga_all'
    #GENETIC_PROFILE_ID='gbm_tcga_mutations'#
    #GENE='BRCA1' # it may be several genes: 'BRCA1+BRCA2+TP53'

    OUTPUT:
Response Format 1

When requesting one or multiple genes and a single genetic profile ID (see above), you will receive a tab-delimited matrix with the following columns:

    GENE_ID: Entrez Gene ID
    COMMON: HUGO Gene Symbol
    Columns 3 - N: Data for each case

Response Format 2

When requesting a single gene and multiple genetic profile IDs (see above), you will receive a tab-delimited matrix with the following columns:

    GENETIC_PROFILE_ID: The Genetic Profile ID.
    ALTERATION_TYPE: The Genetic Alteration Type, e.g. MUTATION, MUTATION_EXTENDED, COPY_NUMBER_ALTERATION, or MRNA_EXPRESSION.
    GENE_ID: Entrez Gene ID.
    COMMON: HUGO Gene Symbol.
    Columns 5 - N: Data for each case.

    """
    print("print(CASE_SET_ID)")
    print(CASE_SET_ID)
    print("print(GENETIC_PROFILE_ID)")
    print(GENETIC_PROFILE_ID)
    print("print(GENE)")
    print(GENE)

    Url = 'http://www.cbioportal.org/webservice.do?cmd=getProfileData&case_set_id='+CASE_SET_ID+'&genetic_profile_id='+GENETIC_PROFILE_ID+'&gene_list='+GENE
    'http://www.cbioportal.org/webservice.do?cmd=getProfileData&case_set_id=gbm_tcga_all&genetic_profile_id=gbm_tcga_mutations,gbm_tcga_gistic&gene_list=EGFR'
    req = urllib.request.Request(Url)
    resp = urllib.request.urlopen(req)
    List_of_Profile_Data = resp.readlines()

    return List_of_Profile_Data

def GetMutationData(GENETIC_PROFILE_ID,GENE):
    "http: // www.cbioportal.org / webservice.do?cmd = getMutationData & case_set_id = gbm_tcga_all & genetic_profile_id = gbm_tcga_mutations & gene_list = EGFR + PTEN"
    Url = 'http://www.cbioportal.org/webservice.do?cmd=getMutationData&genetic_profile_id=' + GENETIC_PROFILE_ID +'&gene_list=' + GENE
    req = urllib.request.Request(Url)
    resp = urllib.request.urlopen(req)
    List_of_mutation_data = resp.readlines()
    return List_of_mutation_data


def getClinicalData(CASE_SET_ID):

    Url = 'http://www.cbioportal.org/webservice.do?cmd=getClinicalData&case_set_id='+CASE_SET_ID
    req = urllib.request.Request(Url)
    resp = urllib.request.urlopen(req)
    List_of_mutation_data = resp.readlines()
    return List_of_mutation_data