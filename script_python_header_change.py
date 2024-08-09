from Bio import SeqIO

input_file = "./Streptophyta/Nymphae_caerulea.faa"  # Replace with your input FASTA file name
output_file = "output.fasta"  # Replace with your desired output FASTA file name

# Open the input FASTA file and create a new output FASTA file
with open(output_file, "w") as output_handle:
    for i, record in enumerate(SeqIO.parse(input_file, "fasta")):
        # Create a new header
        new_header = f"Nymphae_caerulea_{i + 1}"
        
        # Assign the new header to the record
        record.id = new_header
        record.description = ""
        
        # Write the modified record to the output file
        SeqIO.write(record, output_handle, "fasta")

print(f"Headers have been renamed and saved to {output_file}.")
