import sys
import filter_seq

def main():
    if len(sys.argv) < 2:
        print "Set a path to blast results file and output filename"
        return

    blast_results_file = sys.argv[1]
    output_filename = sys.argv[2]

    inp = open(blast_results_file, "r")
    outp = open(output_filename, "w")

    for line in inp.readlines():
        items = line.split()
        
        gi = items[0]
        seq = items[3]

        if filter_seq.filter(seq) == True:
            outp.write(">" + gi + "\n")
            outp.write(seq + "\n")

if __name__ == "__main__":
    main()
