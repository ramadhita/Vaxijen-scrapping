import re
import pandas as pd

if __name__=="__main__":
    with open('antigen_htl_ugm_10002.txt', 'r') as f: #change name file with yours xxx.txt
        file = f.read()

    file = re.sub(r'[\s]*', '', file)
    file = re.sub(r'[\n]*', '', file)

    #lookup for the sample text to know the format
    result = re.findall(r'YourSequence\:\>([a-z]+[_][0-9]?[a-z]+)([A-Z]+)OverallPredictionfortheProtectiveAntigen[=]([-]?[0-9]*[.][0-9]*)\(Probable([A-Z]+[-]?[A-Z]*)\)', file)

    df = pd.DataFrame(result, columns=['id','sequence','score','conclusion'])
    print(df)
    df.to_csv('antigen_htl_ugm_10002_results.csv',index=False) #change name file with yours xxx.csv