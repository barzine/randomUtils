

useMart_HSG<-function(host){
    suppressPackageStartupMessages(library(biomaRt))
    useMart(host=host, 
            biomart='ENSEMBL_MART_ENSEMBL',
            dataset='hsapiens_gene_ensembl')
}


ens76<-useMart_HSG(host='aug2014.archive.ensembl.org')
ens78<-useMart_HSG(host='dec2014.archive.ensembl.org')
ens79<-useMart_HSG(host='mar2015.archive.ensembl.org')

AttList<-c('ensembl_gene_id',
           'gene_biotype')

getBM<-function(attributes,filters='ensembl_gene_id',values,mart){
      biomaRt::getBM(attributes=attributes,filters=filters,values=values,mart=mart)
      }



#TODO: fetch automatically the name of the attributes and the filters
#attributes[grep('ensembl_gene_id',attributes$name),]
