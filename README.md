# FactoryTalk View SE PlantPAX DataLogPro Tag Generator

## Description

This project scans a PLC for instances of Plant PAX AOI's and generates tags for DataLogPro to be used with InfluxDB

## Motivation

Saving time and ensuring that all tags in the PLC are being stored historically.

## Connnecting to the PLC to generate the XML file

The tool requires a few command line arguments to work. a properly formatted command is shown below

```
pydatalogpro.py 10.10.17.10/4 [GroupName] [Device Shortcut]

```

10.10.17.10/4 is the PLC IP address and slot number of the PLC, without the slot number and just the IP address (like '10.10.17.10' it will default to slot 0)

The group name is the folder inside DataLogPro you want the tags to be stored in.

The device shortcut is the communications path set in the project (Typically /DATA::[PLC_SHORTCUT]). This can be found from the FactoryTalk Administration console. If this isn't entered the default is based on the PLC_NAME

## Output File

The generated CSV file will be stored in the same directory the pydatalogpro.py file is run. The name will have the PLC_Name at the beginning of it followed by "_DataLogProTags.csv"

The generated file must be imported into DataLogPro inside FactoryTalk View SE.

## Installation

Please ensure you have the python packages installed as specified in the requirements.txt file.

Navigate to the directory where you cloned the repo and run the command below

```
pip3 install -r requirements.txt

```

## Troubleshooting

Can you ping the PLC you are trying to read from? Ensure you have network connectivity to the PLC before running this script.

If you do not know how to ping, run the command below, it should be the same for Mac/Unix and Windows. Replace the IP address with the PLC you wish to ping

```
ping 10.10.17.10

```
If there are other issues related to importing the file please create an issue so I can fix it :)