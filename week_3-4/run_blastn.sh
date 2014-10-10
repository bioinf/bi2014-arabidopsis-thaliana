#!/bin/bash

if (( $# < 3 ))
then
    echo "Set query ESTs file, nucleotide genome db path and output filename"
    exit
fi

ests=$1
db_path=$2
out=$3
perc_identity=85

blastn -query $ests -db $db_path -perc_identity $perc_identity -out $out -outfmt "6 sseqid sstart send sseq"
