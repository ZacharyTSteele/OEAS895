#! /usr/bin/env python

Usage = """
Taxonomy_cleanup.py - Version 1.0 - Emma Graves
Clean up taxonomy files so each assignment is in the correct rank column
Returns a Goodtaxa.csv file and a Flagtaxa.csv file with taxa that need to be corrected
Usage:
	Taxonomy_cleanup.py inputfile.csv
"""

# Import modules needed
import sys
import re
import pandas

# Print usage statement if input is not 3 variables
if len(sys.argv) < 2:
	print(Usage)
	
else:
	# Take in the input file
	Input = sys.argv[1]
	# Create the output files
	GoodOut = "Goodtaxa.csv"
	FlagOut = "Flagtaxa.csv"
	# Open the input file for reading and output files for writing
	Infile = open(Input, 'r')
	OutfileGood = open(GoodOut, 'w')
	OutfileFlag = open(FlagOut, 'w')	
	
	# Write the headerline for each output file
	Headerline = ", Kingdom, Clade, Phylum, Class, Subclass, Order, Family, Genus, Species"
	OutfileGood.write(Headerline + '\n')
	OutfileFlag.write(Headerline + '\n')
	
	# Make the list for good taxa
	goodtaxa = []
	
	# Start our line counter
	LineNumber = 0
	
	#Start Looping through each line
	for line in Infile:
		if LineNumber >= 1:
			line.split(",")
			 
			 # Pull out the sequence and assign it to the seq variable, since we need to save that data
			seq = line.split(',')[0]
			
			
			## Kingdom
			# Perform a regular expression search for words with the common kingdom suffix 'ota'
			searchking = '(\w+ota),'
			kingdom = re.search(searchking,line)
			# If loop to assign the kingdom found to the king variable, otherwise NA
			if kingdom != None:   
				#print(kingdom.group(1))
				king = kingdom.group(1)  
			else:
				king = 'NA'
				
				
			## Clade
			# Performing multiple regular expression searches for clades - these are common clades within the phytoplankton
			# data we use, but since we do not analyze based off of clade, these are not a necessary taxonomic rank
			searchclade = ',(\w+tista),'
			clade = re.search(searchclade,line)
			searchclade2 = ',(Sar),'
			clade2 = re.search(searchclade2,line)
			searchclade3 = ',(\w+plantae),'
			clade3 = re.search(searchclade3,line)
			searchclade4 = ',(Ochrophyta),'
			clade4 = re.search(searchclade4,line)
			searchclade5 = ',(Opisthokonta),'
			clade5 = re.search(searchclade5,line)
			searchclade6 = ',(Metazoa),'
			clade6 = re.search(searchclade6,line)
			# If/elif loops to find any of the above clades and assign them to the clad variable, otherwise NA
			if clade != None:   
				#print(clade.group(1))
				clad = clade.group(1)
			elif clade2 != None:   
				#print(clade2.group(1))
				clad = clade2.group(1)
			elif clade3 != None:   
				#print(clade3.group(1))
				clad = clade3.group(1)
			elif clade4 != None:   
				#print(clade4.group(1))
				clad = clade4.group(1)
			elif clade5 != None:   
				#print(clade5.group(1))
				clad = clade5.group(1)
			elif clade6 != None:   
				#print(clade6.group(1))
				clad = clade6.group(1)
			else:
				clad = 'NA'
			
			
			## Phylum
			# Performing multiple regular expression searches for phylum assignments. 
			searchphylum = ',(\w+phyta),'
			phylum = re.search(searchphylum,line)
			searchphylum2 = ',(\w+poda),'
			phylum2 = re.search(searchphylum2,line)
			searchphylum3 = ',(\w+usca),'
			phylum3 = re.search(searchphylum3,line)
			searchphylum4 = ',(Alveolata),'
			phylum4 = re.search(searchphylum4,line)
			searchphylum5 = ',(\w+myxa),'
			phylum5 = re.search(searchphylum5,line)
			searchphylum6 = ',(\w+atea),'
			phylum6 = re.search(searchphylum6,line)
			searchphylum7 = ',(\w+mycota),'
			phylum7 = re.search(searchphylum7,line)
			searchphylum8 = ',(\w+phora),'
			phylum8 = re.search(searchphylum8,line)
			# If/elif loops to find any of the above phylums and assign them to the phy variable, otherwise NA
			if phylum != None:
				#print(phylum.group(1))
				phy = phylum.group(1)
			elif phylum2 != None:
				#print(phylum2.group(1))
				phy = phylum2.group(1)
			elif phylum3 != None:
				#print(phylum3.group(1))
				phy = phylum3.group(1)
			# Specifically replacing Alveolata with Myzozoa - Alveolata is a more common name, Myzozoa is the scientific name
			# Databases typically use Alveolata, but should use Myzozoa
			elif phylum4 != None:
				#print(phylum4.group(1))
				phy = 'Myzozoa'
			elif phylum5 != None:
				#print(phylum5.group(1))
				phy = phylum5.group(1)
			elif phylum6 != None:
				#print(phylum6.group(1))
				phy = phylum6.group(1)
			elif phylum7 != None:
				#print(phylum7.group(1))
				phy = phylum7.group(1)
			elif phylum8 != None:
				#print(phylum8.group(1))
				phy = phylum8.group(1)
			else:
				phy = 'NA'
			
			
			## Class
			# Perform a regular expression search for words with the common class suffix 'phyceae'
			search_class = ',(\w+phyceae),'
			taxclass = re.search(search_class,line)
			# If loop to assign any class ranks to the cla variable, otherwise Flag at class since we use classes for analysis
			if taxclass != None:   
				#print(taxclass.group(1))
				cla = taxclass.group(1)  
			else: 
				cla = 'Flag: Failed at class'
			
			
			## Subclass
			# Perform a regular expression search for words with the common subclass suffix 'idae'
			search_subclass = ',(\w+idae)'
			subclass = re.search(search_subclass,line)
			# If loop to assign any subclass ranks to the subc variable, otherwise 'NA' because subclass is not a recognized
			# taxonomic rank and thus, some organisms do not have a subclass
			if subclass != None: 
				#print(subclass.group(1))
				subc = subclass.group(1)  
			else:
				subc = 'NA'
			
			
			## Order
			# Perform a regular expression search for words with the common subclass suffix 'ales'
			search_order = ',(\w+ales),'
			order = re.search(search_order,line)
			# If loop to assign any order ranks to the ord variable, otherwise Flag at order since we use orders for analysis
			if order != None:   
				#print(order.group(1))
				ord = order.group(1)  
			else: 
				ord = 'Flag: Failed at order'
			
			
			## Family
			# Perform a regular expression search for words with the common family suffix 'aceae'
			search_family = ',(\w+aceae),'
			family = re.search(search_family,line)
			# If loop to assign any family ranks to the fam variable, otherwise Flag at family since we use families for analysis
			if family != None:   
				#print(family.group(1))
				fam = family.group(1)  
			else: 
				fam = 'Flag: Failed at Family'
			
			
			## Genus and Species
			# Perform a regular expression search for a species assignment, which is usually two words (Genus species)
			search_species = ',([\w.\-\w]+) (\w+)'
			genspec = re.search(search_species,line)
			# If loop to assign any genus and species ranks to the gen and spec variables, otherwise Flag at genus and species,
			# since those are the most important classifications used to identify organisms
			if genspec != None:
				# Perform a regular expression search on the genus and species to search for unclassified organsisms (organisms 
				# classified only to the genus level)
				search_unclass = 'unclassified'
				unclass = re.search(search_unclass, line)
				if unclass != None:
					gen = genspec.group(2)
					spec = genspec.group(1)+' '+genspec.group(2)
				else:
					gen = genspec.group(1)
					spec = genspec.group(1)+' '+genspec.group(2)
			else:
				gen = 'Flag: failed at genus'
				spec = 'Flag: failed at species'
			
			# Append our list with the cleaned up taxonomy for each line/sequence
			Fixedline = seq+', '+king+', '+clad+', '+phy+', '+cla+', '+subc+', '+ord+', '+fam+', '+gen+', '+spec
			
			# Split the file into the good taxa and flagged taxa
			search_flag = 'Flag'
			flag = re.search(search_flag, Fixedline)
			# Excluse Metazoans from the flagged file, since we do not look at them anyways
			search_meta = 'Metazoa'
			meta = re.search(search_meta, Fixedline)
			if (flag != None) & (meta is None):
				OutfileFlag.write(Fixedline + ', ' + line )
			else:
				OutfileGood.write(Fixedline + '\n')
			
			
		LineNumber += 1
		
			
	# Close the output files
	OutfileFlag.close()
	OutfileGood.close()
			
			
				
				