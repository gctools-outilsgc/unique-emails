
'''
File containing old one-use code that can likely be re-used.
'''


#From one file

def email_clean_up(lst_of_emails):
    '''
    There's some values stored in the email field of the databases that aren't actual emails and this sorts them out. 
    They're sorted into normal, admin, and weird. It tells you how many are weird, how many are admin, and returns the normal emails 

    @param lst_of_emails is a list of full emails and separates them into normal, admin, and weird. 
    '''
    
    normal_emails = []
    weird_emails = [] #In case you want to see the weird ones
    
    admin = 0
    
    for x in lst_of_emails:
        for y in x:
            z = y.split("@")
            if len(z) == 2:
                normal_emails.append(z[1])
            else:
                if not y.contains("admin"):
                    admin += 1
                else:
                    weird_emails.append(y)

    print("num weird:" , len(weird_emails))
    print("num admin:" , admin)

    return normal_emails



#The rest is from another file, clumped into separate functions to be a little more useful

import pandas as pd
import re


def get_ends(df):
    '''
    Creates a list of email endings

    @param df is a dataframe containing a column titled emails
    '''
    ends = []

    for email in df["emails"]:
        try:
            email = email.split("@")[1]
            ends.append(email)
        except:
            print("Excluding:", email)

    return ends

def email_endings_counts(ends):
    '''
    Displays each distinct email ending within the given list and how many repetitions there are. Returns a dictionary containing this information

    @ends is a list of email endings
    '''

    #create a dictionary with counts of each ending
    dic = {}
    for email in ends:
        try:
            dic[email] += 1
        except:
            dic[email] = 1

    #print(dic)
    return (dic)


def sort_emails(dic):
    '''
    Displays how many emails endings in a dictionary are government, educational, or other. Further determines of the government emails, are they federal, provincial, or municipal
    each distinct email ending within the given list and how many repetitions there are and returns a dictionary containing this information

    @param dic is a dictionary of email endings and counts of their repetition
    '''

    #Not exhaustive! Adjusted as new data is used to sort them
    edu_pattern = re.compile( r'^u[a-z]+\.ca$|alumni|[a-z]+\.u[a-z]+\.ca|sait.ca|humber.ca|^ccnb\.ca$|sfu\.ca|laval.ca|grenfell.mun.ca|hec.ca|rmc.ca|\D\*smu\.ca|nscc.ca|laurentian.ca|myseneca.ca|[\D]*concordia\.ca$|msvu|mun.ca|[\D]+\.edu$|\D+yorku\D+|(my)*laurier.ca$|trentu|polymtl|\D+mcgill\D+|[\D]*carleton.ca$|^guelph.ca$|ryerson|algonquinlive|georgebrown|queensu.ca|acadiau.ca|myumanitoba.ca|lakeheadu.ca|mcmaster.ca|student')

    gov_pattern = re.compile(r'^\D*\.\D\D\.ca$|(\D)+\.gc\.ca$|tofino.ca|canada\.ca$|princegeorge\.ca|middlesex.ca|snb.ca|lincoln\.ca|nfb\.ca|sarnia\.ca|peelregion\.ca|cmhc\.ca|townofbeausejour\.com|gnb\.ca|^ontario\.ca$|elections\.ca|calgary\.ca|[\D]*\.quebec|ncc-ccn.ca|agco.ca|^greatersudbury.ca$|ehealthsask|winnipeg.ca|york.ca|toronto.ca|canadacouncil|markham|novascotia|thunderbay')

    fed_pattern = re.compile(r'[\D]+\.gc\.ca$|canada\.ca$|nfb\.ca|cmhc\.ca|elections\.ca|ncc-ccn.ca|canadacouncil')

    prov_pattern = re.compile(r'(gov|gouv|nlhc|cdpdj|frq|edu|nwhu|cegep-heritage)\.(qc|mb|nl|sk|ab|bc|nu|nt|yk|pe|on).ca$|snb.ca|gnb\.ca|^ontario\.ca$|agco.ca|ehealthsask|.*.gouv.qc.ca$')

    mun_pattern = re.compile(r'^\D*\.[qc|mb|nl|sk|ab|bc|nu|nt|yk|pe|on].ca$|tofino.ca|princegeorge\.ca|middlesex.ca|brazeau|lincoln\.ca|sarnia\.ca|peelregion\.ca|townofbeausejour\.com|calgary\.ca|[\D]*\.quebec|^greatersudbury.ca$|winnipeg.ca|york.ca|toronto.ca|markham|novascotia|thunderbay|villemontlaurier|ville|torontopolice')

    edu = 0
    govc = 0
    oth = 0 #gmail.com, hotmail, ... 

    fed = 0
    prov = 0
    mun = 0

    for end in dic:
        if edu_pattern.match(end):
            edu += dic[end]
        elif gov_pattern.match(end):
            govc += dic[end]
            if fed_pattern.match(end):
                fed += dic[end]
            elif prov_pattern.match(end):
                prov += dic[end]
            elif mun_pattern.match(end):
                mun += dic[end]
            else:
                print("Misc", end)
        else:
            oth += dic[end]

    print("num edu emails:", edu)
    print("num govc emails:", govc)
    print("num oth emails:", oth)

    print("num fed emails:", fed)
    print("num prov emails:", prov)
    print("num muni emails:", mun)
    
