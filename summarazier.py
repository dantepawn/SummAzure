pip install pysummarization


from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


def topN(document, n ):
    '''print the n best phrases to summarize the text'''
    result_dict = auto_abstractor.summarize(document, abstractable_doc)
    
    if n > len(result_dict["summarize_result"]):
        n = len(result_dict["summarize_result"])
    indices = sorted(result_dict['scoring_data'],key = lambda x : x[1],reverse = True)[:n]
    for sent in indices :
        print(result_dict["summarize_result"][sent[0]])





# Object of automatic summarization.
auto_abstractor = AutoAbstractor()
# Set tokenizer.
auto_abstractor.tokenizable_doc = SimpleTokenizer()
# Set delimiter for making a list of sentence.
auto_abstractor.delimiter_list = [".", "\n"]
# Object of abstracting and filtering document.
abstractable_doc = TopNRankAbstractor()

document = "The exact quantities of goods exchanged—their prices, in other words—are determined by the values individuals attach to marginal units of these goods. With asingle buyer and seller, goods are exchanged as long as participants can agreeon an exchange ratio that leaves each better off than he was before. In a market with many buyers and sellers, the price reflects the valuations of the buyerleast  willing  to  buy  and  the  seller  least  willing  to  sell,  what  BöhmBawerk would call the “marginal pairs.” Regardless of the exact structure of the market, then, voluntary exchange takes place until the gains from trade are momentarily exhausted. Menger’s highly general explanation of price formation continues to form the core of Austrian microeconomics. Menger’s approach has been labeled “causalrealistic,” partly to emphasize  its  differences  with  the  mainstream,  neoclassical  approach.  Besides  itsfocus on causal relations, Menger’s analysis is realistic in the sense that hesought not to develop formal models of hypothetical economic relationships,but to explain the actual prices paid every day in real markets. The classicaleconomists had explained that prices are the result of supply and demand, butthey lacked a satisfactory theory of valuation to explain buyers’ willingnessto  pay  for  goods  and  services.  Rejecting  value  subjectivism,  the  classicaleconomists  tended  to  treat  demand  as  relatively  unimportant  and  concentrated on hypothetical “longrun” conditions, in which “objective” characteristics  of  goods—most  importantly,  their  costs  of  production would  determine  their  prices.  The  classical  economists  also  tended  to  group  factors  ofproduction  into  broad  categories—land,  labor,  and  capital—leaving  themunable to explain the prices of discrete, heterogeneous units of these factors.Menger realized that the actual prices paid for goods and services reflect notsome  objective,  “intrinsic”  characteristics,  but  rather  the  uses  to  which  discrete  units  of  goods  and  services  can  be  put,  as  perceived,  subjectively,  byindividual buyers and sellers. The Principleswas written as an introductory volume in a proposed multivolume  work.  Unfortunately,  those  later  volumes  were  never  written.Menger did not explicitly develop the concept of opportunity cost, he did notextend his analysis to explain the prices of the factors of production, and hedid  not  develop  a  theory  of  monetary  calculation." 

topN(document,2)


# Other examples
wiki_example = "The 2016 Atlantic hurricane season was the costliest, as well as the first above-average, Atlantic hurricane season in four years. It featured the highest number of deaths since the 2008 season and also yielded the highest number of named storm landfalls on the United States since that year. The season officially began on June 1 and concluded on November 30. The season s first cyclone, Alex, developed on January 12, while the final storm of the season, Otto, ultimately dissipated on November 26. A total of 16 tropical depressions were recorded, of which 15 further intensified into tropical storms. Of those 15, a total of seven strengthened into hurricanes, while four attained their peaks as major hurricanes. In late September and early October, Hurricane Matthew (pictured) wrought destruction throughout the Caribbean Sea and the Southeastern United States, resulting in $15.09 billion (2016 USD) in damage and 603 deaths; it remains the ninth-costliest hurricane on record in the Atlantic, as well as the tenth-costliest in the United States"
topN(wiki_example,1)

wiki2 ="Radiometric dating, radioactive dating or radioisotope dating is a techniqueused to date materials such as rocks or carbon, in which trace radioactive impurities were selectively incorporated when they were formed. The method compares the abundance of a naturally occurring radioactive isotope within the material to the abundance of its decay products, which form at a known constant rate of decay.[1] The use of radiometric dating was first published in 1907 by Bertram Boltwood[2] and is now the principal source of information about the absolute age of rocks and other geological features, including the age of fossilized life forms or the age of the Earth itself, and can also be used to date a wide range of natural and man-made materials."
topN(wiki2, 1)

#example
wiki3 = 'Microsoft Azure (formerly Windows Azure /ˈæʒər/) is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through Microsoft-managed data centers. It provides software as a service (SaaS), platform as a service (PaaS) andinfrastructure as a service (IaaS) and supports many different programminglanguages, tools and frameworks, including both Microsoft-specific and third-party software and systems.Azure was announced in October 2008,started with codename "Project Red Dog",[1] and released on February 1, 2010, as "Windows Azure" before being renamed "Microsoft Azure" on March 25, 2014'
topN(wiki3, 2)


#example
text = "The exact quantities of goods exchanged—their prices, in other words—are determined by the values individuals attach to marginal units of these goods. With a single buyer and seller, goods are exchanged as long as participants can a greeon an exchange ratiothat leaves each better off than he was before. In a market with many buyers and sellers, the price reflects the valuations of the buyerleast willing  to  buy  and  the  seller  least  willing  to  sell,  what  BöhmBawerk would call the “marginal pairs.” Regardless of the exact structure of the market, then, voluntary exchange takes place until the gains from trade are momentarily exhausted. Menger’s highly generalexplanation of price formation continues to form the core of Austrianmicroeconomics. Menger’s approach has been labeled “causalrealistic,”partly to emphasize  its  differences  with  the  mainstream,  neoclassical approach.  Besides  itsfocus on causal relations, Menger’s analysisis realistic in the sense that hesought not to develop formal modelsof hypothetical economic relationships,but to explain the actualprices paid every day in real markets. The classical economistshad explained that prices are the result of supply and demand,butthey lacked a satisfactory theory of valuation to explainbuyers’ willingness to  pay  for  goods  and  services.  Rejecting value  subjectivism,  the  classicaleconomists  tended  to  treat demand  as  relatively  unimportant  and  concentrated on hypothetical “longrun” conditions, in which “objective” characteristics  of  goods—mostimportantly,  their  costs  of  production would  determine  their  prices.The  classical  economists  also  tended  to  group  factors  ofproduction into  broad  categories—land,  labor,  and  capital—leaving  themunable to explain the prices of discrete, heterogeneous units of these factors.Mengerrealized that the actual prices paid for goods and services reflect notsomeobjective,  “intrinsic”  characteristics,  but  rather  the  uses  to  whichdiscrete  units  of  goods  and  services  can  be  put,  as  perceived,subjectively,  by individual buyers and sellers. The Principles was writtenas an introductory volume in a proposed multivolume  work.  Unfortunately,those  later  volumes  were  never  written.Menger did not explicitly developthe concept of opportunity cost, he did notextend his analysis to explain theprices of the factors of production, and hedid  not  develop  a  theory  of monetary  calculation." 
topN(text,4)
