r"""

\begin_inset Graphics
	filename C:/Users/Itai/source/repos/data-processing/hw2/plots/H/n2/h1.png
	width 25text%

\end_inset


\begin_inset Graphics
	filename C:/Users/Itai/source/repos/data-processing/hw2/plots/H/n2/h2.png
	width 25text%

\end_inset


\begin_inset Graphics
	filename C:/Users/Itai/source/repos/data-processing/hw2/plots/H/n2/h3.png
	width 25text%

\end_inset


\begin_inset Graphics
	filename C:/Users/Itai/source/repos/data-processing/hw2/plots/H/n2/h4.png
	width 25text%

\end_inset


"""

directory = "hw2/plots/H/n6"

import os
import pyperclip

directory = os.path.abspath(directory)

latex = r""
newline = r"""\begin_inset Newline newline
\end_inset

"""
count = 0
for fname in os.listdir(directory):
    fpath = os.path.join(directory, fname)
    
    if os.path.isfile(fpath):
        latex += rf"""\begin_inset Graphics
	filename {fpath}
	width 25text%

\end_inset

"""
    count += 1
    if count == 4:
        count = 0
        latex += newline

latex = latex.replace(r"/mnt/c",r"C:")
print(latex)

pyperclip.copy(latex)


