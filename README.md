Overview:
	This repo contains the datasets from Payne et al. 2021 in xls format, as well as code used to
	visualize this data.
Data:
	The methods used to generate this data are described in Payne et al. 2021. Breifly, cultured cells are 
	fixed and treated with a Tn5 transposase, which inserts primers randomly into genomic DNA. These primed
	genomic reads are amplified in situ, and barcodes on the ligated primers are read out in situ using an
	ilumina style sequencing technique. Genomic DNA is then extracted and deep sequenced ex situ. The
	combination of spatially resolved barcode sequences and deep sequencing allows the user to map
	genomic reads to the three dimensional context of the nucleus.

	Payne A. C., Chiang Z. D., Reginato P. L., Mangiameli S. M., Murray E. M., Yao C., Markoulaki S.,
	Andrew S. E., Ajay S. L., Labade A. S., Jaenisch R., Church G. M., Boyden E. S., Buenrostro J. D. and
	Chen F., "In situ genome sequencing resolves DNA sequence and structure in intact biological samples,"
	Science 2021.

Folder structure:
	Payne_datasets contains the datasets published by Payne et al. More folders will be generated
	as the code for this project is written.

Installation:
	This code was run using PyCharm with the following packages: pandas, matplotlib, numpy, and seaborn.