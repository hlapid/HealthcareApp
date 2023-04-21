# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:20:14 2020

@author: hadas
"""
from Initialization.serverInitiation import *
import pandas as pd

class DataQueries:
    def __init__(self,dbName):
        # self.cursor = connect2server()
        self.cursor, self.con = connect2serverDB(database=dbName)
        self.df_patientData = pd.DataFrame()
        self.df_PatientAdmissions = pd.DataFrame()

    # A)
    # A query of all patients's data for a specific staff user
    # select David Simantov's patients using 'where' and 'inner join'
    # of tables staffpatients and patients
    # output the patient's first name, last name, address and phone number
    # save output to csv and return the dataframe output
    def queryUserPatientData(self,staffID):
        self.cursor.execute(f"SELECT \
                            t1.*\
                            FROM patients t1\
                            INNER JOIN staffpatients t2\
                            ON t1.PatientID = t2.patientID \
                            WHERE t2.staffID = {staffID}")
        # res = self.con.commit()
        res = self.cursor.fetchall()
        self.df_patientData = pd.DataFrame(res,columns=["ID","firstName","lastName","phone","address"])
        self.df_patientData.to_csv(f"DR_{staffID}_patients.csv", sep=',',index=False)
        return self.df_patientData
    # B)
    # similarly, get all data points of a questionnaire table of specific doctor's patients

    # C)
    # get all patient's data (first name, last name, address, phone)
    # from patients that were addmitted to hospitalizations between the dates 1.11.2019 and 31.12.2019
    def queryPatientDataByDate(self,addmitionDate0,addmitionDate1):
        self.cursor.execute(f"SELECT \
                            t2.admissionDate,\
                            t1.*\
                            FROM patients t1\
                            INNER JOIN admissions t2\
                            ON t1.patientID = t2.patientID \
                            WHERE t2.admissionDate >= '{addmitionDate0:s}' \
                            AND t2.admissionDate <= '{addmitionDate1:s}'")
        res2 = self.cursor.fetchall()
        self.df_PatientAdmissions = pd.DataFrame(res2,columns = ["admission date","patient ID","First Name","Last Name","phone","address"])
        self.df_PatientAdmissions.to_csv('SelectedAdmissionDates.csv', sep=',',index=False)
        return self.df_PatientAdmissions
def main():
    q = DataQueries("emr")
    q.queryUserPatientData('477046263')
    q.queryPatientDataByDate('2019-11-01','2019-12-31')
if __name__=="__main__":
    main()