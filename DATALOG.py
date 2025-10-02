# AOI definitions are from PlantPAX V4.10.4

DATALOG_DEFINITIONS = {
    'P_AIn': """\
        GROUPNAME,SHORTCUTTAG.SrcQ,DINT,Periodic,1,Second,,,,,,
        GROUPNAME,SHORTCUTTAG.Val,REAL,Periodic,1,Second,,,,,,
        GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
        GROUPNAME,SHORTCUTTAG.Val_InpPV,REAL,Periodic,1,Second,,,,,,
        GROUPNAME,SHORTCUTTAG.Val_Dev,REAL,Periodic,1,Second,,,,,,""",


}

DATALOG_LIST = DATALOG_DEFINITIONS.keys()