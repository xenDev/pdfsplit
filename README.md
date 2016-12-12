# pdfsplit
Since pdftk did not support easy way to generate multiple pdfs with ranges

Usage Examples
--------------
###Generates four pdfs with ranges 1-2, 3-5, 6-7, 8-endpage with given suffix
pdfsplit -i input.pdf -l 1,3,6,8 -s chapter  

###Split each page with 'page' as the suffix of the output filename
pdfsplit -i input.pdf  

