import struct
import sys

def amplify(ipfile, opfile, amplification):
    # opens input and output files for reading and writing.
    i = open(ipfile, "rb") 
    o = open(opfile, "wb")
    
    header = i.read(44) # Wav files have a 44 byte header which we're simply reading out there https://docs.fileformat.com/audio/wav/
    o.write(header) # Write out the header into the output file

    sample = i.read(2) # Read and write the first sample. There's a bug here. We're not amplifying this sample. Try to fix it. 
    o.write(sample)

    while sample: # As long as we read a valid sample, repeat this loop
        sample = i.read(2)  # Read out a sample
        if sample: # If we read something (once we reach the end of the file, sample will be '' and the if won't execute.
            # Unpack the sample into a python object that we can use. More details about the struct module is there in the README.
            ip_data = struct.unpack('h', sample) 
            val = ip_data[0]
            # Alter the value and convert it into an integer
            val *= amplification
            val = int(val)
            # Convert it back into a file and write it out to the output file
            op_data = struct.pack('h', val)
            o.write(op_data)

    # Close files
    i.close()
    o.close()

def main():
    # sys.argv contains the command line arguments which were provided to the program. These. There's a basic introduction here https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    source = sys.argv[1] 
    target = sys.argv[2] 
    amplification = float(sys.argv[3])

    amplify(source, target, amplification)

main()

