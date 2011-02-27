#!/bin/bash
output=$1
shift
if [ $# -gt 1 ]
then
	gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=$output -dBATCH $*
fi
