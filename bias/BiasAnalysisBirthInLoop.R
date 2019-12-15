library(bigmemory)
data<-read.delim("~/Desktop/BigData_ProjectData/SPARCS-2017-birth-Bias.csv")
county_names<-unique(data$Hospital.County)
# screen the variables with 1 level for each county
flist<-c()
for (icount in county_names)
{
  subdata<-data[data$Hospital.County==icount,]
  for (iname in colnames(subdata))
  {
    if(nrow(unique(subdata[iname]))==1)
    {flist<-c(flist, iname)}#cat(icount, ",", iname,"1 level\n")}
  }
}
print(unique(flist))
bias<-c()
avg2male<-c()
for (iname in county_names)
{
  subdata<-data[data$Hospital.County==iname,]
  y<-subdata$Average.Charges
  gender<-as.factor(subdata$Gender)
  race<-as.factor(subdata$Race)
  #ethnity<-as.factor(subdata$Ethnicity)
  #admission<-as.factor(subdata$Type.of.Admission)
  disposition<-as.factor(subdata$Patient.Disposition)
  severity<-factor(subdata$APR.Severity.of.Illness.Description,order=TRUE,level=c("Minor", "Moderate", "Major", "Extreme"))
  #mortality<-factor(subdata$APR.Risk.of.Mortality,order=TRUE,level=c("Minor", "Moderate", "Major", "Extreme"))
  #emergency<-as.factor(subdata$Emergency.Department.Indicator)
  birthweight<-subdata$Birth.Weight
  fit1<-lm(y~race+gender+disposition+severity+birthweight)
  t1<-summary(aov(fit1))[[1]][["Pr(>F)"]]
  bias<-rbind(bias, c(iname, t1[1]<0.05, t1[2]<0.05))
  #cat(iname,",race bias:",t1[1]<0.05,"; gender bias:",t1[2]<0.05,".\n")
  # compute the gender bias
  if (is.element("M",subdata$Gender)){
    ratio<-cbind(iname,100)
    if(t1[2]>0.05){ratio<-cbind(ratio,0)}
    else{
      ratio<-cbind(ratio,round(100*mean(subdata[subdata$Gender=="F",]$Average.Charges)/mean(subdata[subdata$Gender=="M",]$Average.Charges),digits=2))}
  }
  else{
    ratio<-cbind(iname,0,0)
  }
  avg2male<-rbind(avg2male,ratio)
}
colnames(bias)<-c("County","RaceBias","GenderBias")
colnames(avg2male)<-c("County","Male","Female")

racelist<-c("Black/African American","Other Race","Multi-racial")
avg2white<-c()
# Multi-level comparison
for (iname in county_names)
{
  subdata<-data[data$Hospital.County==iname,]
  y<-subdata$Average.Charges
  gender<-as.factor(subdata$Gender)
  race<-as.factor(subdata$Race)
  #ethnity<-as.factor(subdata$Ethnicity)
  #admission<-as.factor(subdata$Type.of.Admission)
  disposition<-as.factor(subdata$Patient.Disposition)
  severity<-factor(subdata$APR.Severity.of.Illness.Description,order=TRUE,level=c("Minor", "Moderate", "Major", "Extreme"))
  #mortality<-factor(subdata$APR.Risk.of.Mortality,order=TRUE,level=c("Minor", "Moderate", "Major", "Extreme"))
  #emergency<-as.factor(subdata$Emergency.Department.Indicator)
  fit1<-lm(y~race+gender+disposition+severity)
  
  # compare the race difference
  tu<-TukeyHSD(aov(fit1),"race")
  ratio<-cbind(iname,100)
  for (icom in racelist){
    if(is.na(tu[[1]][,"p adj"][paste("White",icom,sep="-")]))
    {ratio<-cbind(ratio,0)}
    else{
      if(tu[[1]][,"p adj"][paste("White",icom,sep="-")]>0.05)
        {ratio<-cbind(ratio,100)}
      else
        {ratio<-cbind(ratio,round(100*mean(subdata[subdata$Race==icom,]$Average.Charges)/mean(subdata[subdata$Race=="White",]$Average.Charges),digits=2))}
    }
  }
  avg2white<-rbind(avg2white,ratio)
}  
colnames(avg2white)<-c("County","White",comlist)  
  
write.csv(bias,"~/Desktop/BigData_ProjectData/birth-Bias-anova.csv")
write.csv(avg2male,"~/Desktop/BigData_ProjectData/birth-avg2male-anova.csv")
write.csv(avg2white,"~/Desktop/BigData_ProjectData/birth-avg2white-tukey.csv")
