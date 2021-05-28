# Binary files

Data that is inside our program (say in a variable) when written out
to the disk, needs to be converted into a format that can be stored on
disk. For example, a string like `noufal` can be stored as one byte
per character. Each byte would be one ascii code and we can save that
on the disk. But we can also store it using a different encoding than
ascii and then it would (maybe) take two bytes per letter. 

With binary files (e.g. images, audio etc.), The file will have a
specific format. e.g. https://docs.fileformat.com/audio/wav/ for wav
files. Note the header format. To be able to access this, we need to
read out the 44 byte header (into say a variable called `header`). If
we want pieces from that, we have to break down the header into
specific bytes and interpret that. 

For more details, refer to the wikipedia article on binary files at https://en.wikipedia.org/wiki/Binary_file

# Extra instructions for hangman. 
You will probably need the word list to run this program. You can get
that by running

              sudo apt-get install wamerican
