import glob
import os
from natsort import natsorted

path = "/Users/shravanc/learning_pyt/fidelity/fidelity_2/generic/uploads/fidelity_1_f9960fe8-929a-11e9-87c9-1c36bb1a4426/texts"
machined_pages = natsorted(glob.glob(os.path.join(path, "*.txt")))
for file in machined_pages:
		print(file)
