# FetchCbioportal
-------------------------------------------------------------------------------------------------------------------------------
This script allows you to get data from cbioportal using the same query format as cbioportal's web API in a tab delimited .txt file in you current directory
-------------------------------------------------------------------------------------------------------------------------------

command line format: (options must be in the indicated order)
-------------------------------------------------------------
./FetchCbioportal.py  cmd options


Get All Types of Cancer :
------------------------
Query example: ./FetchCbioportal.py getTypesOfCancer
Query format: ./FetchCbioportal.py [cmd]
 	cmd = getTypesOfCancer

Get All Case Lists for a Specific Cancer Study :
----------------------------------------------
Query example: ./FetchCbioportal.py getCaseLists
Query format: ./FetchCbioportal.py [cmd]
    cmd = getCaseLists

to get profil data :
--------------------
Query example: ./FetchCbioportal.py getProfileData 'BRCA1+BRCA2' ov_tcga_all ov_tcga_linear_CNA
Query format: ./FetchCbioportal.py [cmd] [gene_list] [case_set_id] [genetic_profile_id]

    cmd=getProfileData (required)
    case_set_id= [case set ID] (required)
    genetic_profile_id= [one or more genetic profile IDs] (required). Multiple genetic profile IDs must be separated by comma (,) characters, or URL encoded spaces, e.g. +
    gene_list= [one or more genes, specified as HUGO Gene Symbols or Entrez Gene IDs] (required). Multiple genes must be separated by comma (,) characters, or URL encoded spaces, e.g. +

Get Extended Mutation Data :
---------------------------
Query example: ./FetchCbioportal.py getMutationData ov_tcga_mutations 'BRCA1+BRCA2'
Query format: ./FetchCbioportal.py [cmd] [genetic_profile_id] [gene_list]

    cmd = getMutationData
    genetic_profile_id = [one or more mutation profile IDs] (required). Multiple genetic profile IDs must be separated by comma (,) characters, or URL encoded spaces, e.g. +
    gene_list = [one or more genes, specified as HUGO Gene Symbols or Entrez Gene IDs] (required). Multiple genes must be separated by comma (,) characters, or URL encoded spaces, e.g. +


Get Clinical Data :
-------------------
Query example: ./FetchCbioportal.py getClinicalData ov_tcga_all
Query format: ./FetchCbioportal.py [cmd] [case_set_id]

    cmd = getClinicalData
    case_set_idv = [case set ID]




