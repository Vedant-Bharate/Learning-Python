# File: HW Task 1
# Date: 01 February 2024
# By: Vedant Bharate
# Section: 018
# Team: 319
#
# ELECTRONIC SIGNATURE
# Vedant Bharate
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# The function calculates the final grade of the students.

# Open PatientData.txt for reading
data = open("PatientData.txt", "r")
# Open PatientsToMonitor.txt for writing
data_converted = open("PatientsToMonitor.txt", "w")
# Read lines from the input file
for line in data:
    patient_data = line.split(",")
    patient_id = patient_data[0]
    BPS = int(patient_data[1])
    BPD = int(patient_data[2])
    # Checking for negative values
    if BPS < 0 or BPD < 0:
        data_converted.write(f"{patient_id},Error\n")
    else:
# Categorizing blood pressure
        if BPS < 90 or BPD < 60:
            category = "Hypotension"
        elif 90 <= BPS < 120 and 60 <= BPD < 90:
            category = "Normal"
        else:
            category = "Hypertension"

        # WWriting converted data to file
        if category in ["Hypotension", "Hypertension"]:
            data_converted.write(f"{patient_id},{category}\n")
# Closing all files
data.close()
data_converted.close()
