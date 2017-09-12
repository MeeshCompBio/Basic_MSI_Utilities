#This is to merge FPKM's from Cufflink output where all of your genes.FPKM.tracking files
  #are all in one location
  
#Set your working directory where all of your files are located
setwd("")

#Set all of the empty vars to populate
EXPRTable <- c()
#get a list of all the files in the current DIR
Files <- list.files(path = ".")
#Column names var even though we won't use it
CNAMES <- c()
#Go through each file
for (i in 1: length(Files)){
    #We need to make a dataframe to merge on the first iteration
        #So this one make a dataframe as assign gene names as row names
    if ( i == 1) {
        Temp <- read.delim(Files[i], sep = '\t', stringsAsFactors = FALSE)
        FPKM <- Temp[, which(colnames(Temp)=="FPKM")]
        #This is to split the file name into a real sample name
            #you might need to change the split var to reflect your file
        CTemp <- unlist(strsplit(Files[i], split='_gene', fixed=TRUE))[1]
        #add to calumn names var just in case
        CNAMES <- append(CNAMES, CTemp)
        #make an initial data frame
        EXPRTable <- as.data.frame(FPKM, row.names = Temp$tracking_id)
        colnames(EXPRTable) <- CTemp
    }
    else{
        Temp <- read.delim(Files[i], sep = '\t', stringsAsFactors = FALSE)
        FPKM <- as.data.frame(Temp[, which(colnames(Temp)=="FPKM")], row.names = Temp$tracking_id)
        CTemp <- unlist(strsplit(Files[i], split='_gene', fixed=TRUE))[1]
        colnames(FPKM) <- CTemp
        CNAMES <- append(CNAMES, CTemp)
        #merge our EXP table and new FPKM based off gene row names in each file
        EXPRTable <- merge(EXPRTable, FPKM, by="row.names",all.x=TRUE)
        #When merging then rownames get inserted as first column
            #reassign row names so we can merge in next iteration
        row.names(EXPRTable) <- EXPRTable$Row.names
        #remove the Row.names column that is in the first column position
        EXPRTable <- EXPRTable[,c(-1)]
        
    }    
}

#Capitalize all of the gene names for downstream analysis
row.names(EXPRTable) <- toupper(row.names(EXPRTable))

#Write the table our as a CSV
write.csv(EXPRTable, "YOURFILENAME.csv", quote = FALSE)
