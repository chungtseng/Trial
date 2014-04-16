print( ''' Hello! I am a SNP Summarizer.
I will read your snps.vcf file and summarize the SNPs present.''')
valid_file = False
while not valid_file:
	user_file = raw_input('Enter your filename:')
	snp_data = open('/home/ycz/snps.vcf','r')
        valid_file = True
    	#except IOError:
        #	print('\nUnable to locate and open file. Re-enter correct file name.\n')
header_found = False
for line in snp_data:
    if '#CHROM' in line and 'REF' in line and 'ALT' in line:
        header_found = True
        snp_dict = {}
        snp_dict['A > C'] = 0
        snp_dict['A > G'] = 0
        snp_dict['A > T'] = 0
        snp_dict['C > A'] = 0
        snp_dict['C > G'] = 0
        snp_dict['C > T'] = 0
        snp_dict['G > A'] = 0
        snp_dict['G > C'] = 0
        snp_dict['G > T'] = 0
        snp_dict['T > A'] = 0
        snp_dict['T > C'] = 0
        snp_dict['T > G'] = 0
        for num,line in enumerate(snp_data):
            linex = line.split('\t')
            for ind in xrange(len(linex)):
                     if linex[ind] in ['A','T','C','G']:
                         snp_dict[linex[ind] +' '+ '>' +' '+ linex[ind+1][0]] += 1
			 break
            #except:
             #   print('Invalid SNP found. Unable to add to calculations. Review files.')
              #  print('Error encountered on line number: ' + str(num))
               # print('Tried to add: ' + linex[ind] + ' > ' + linex[ind+1])
snp_data.close()
if header_found:
    print("Required fields of 'CHROM', 'REF', and 'ALT' could not be found.\nPlease check if that file is properly formatted and try again or quit.")
    total_snp = sum(snp_dict.values())
    with open('/home/ycz/SNP_summary.txt','w+') as out_put:
        for snp in sorted(snp_dict):
            out_put.write(snp + '\t' + str(snp_dict[snp]) + '\t' + str(float(snp_dict[snp])/float(total_snp)) + '\n')
    print("\nComplete. Output file is named 'SNP_summary.txt'")
            
