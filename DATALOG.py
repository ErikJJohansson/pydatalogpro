# AOI definitions are from PlantPAX V4.10.4

DATALOG_TEMPLATE = """Version
V14.0,THIS LINE CONTAINS VERSION INFORMATION. DO NOT REMOVE!!!
Group Name,Tag Name,Tag Type,Trigger Type,Interval Value,Interval Unit,Maximum updateRate Value,Maximum updateRate Unit,Deadband Mode,Deadband Value,HeartbeatRate Value,HeartbeatRate Unit,"""


DATALOG_DEFINITIONS = {
    'P_AInAdv': """\
GROUPNAME,SHORTCUTTAG.SrcQ,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_InpPV,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Dev,REAL,Periodic,1,Second,,,,,,
""",
    'P_AInDual': """\
GROUPNAME,SHORTCUTTAG.SrcQ,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_PVA,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_PVB,REAL,Periodic,1,Second,,,,,,
""",
    'P_AInMulti': """\
GROUPNAME,SHORTCUTTAG.SrcQ,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
""",
    'P_DIn': """\
GROUPNAME,SHORTCUTTAG.Sts,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Err,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_PV,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Sts,DINT,Periodic,1,Second,,,,,,
""",
    'P_PIDE': """\
GROUPNAME,SHORTCUTTAG.SrcQ,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_BypActive,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_IntlkTrip,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_NotRdy,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Oper,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Prog,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Sts,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_State,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_CVOut,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_PV,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_SP,REAL,Periodic,1,Second,,,,,,
""",
    'P_AOut': """\
GROUPNAME,SHORTCUTTAG.Sts_BypActive,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_IntlkTrip,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_NotRdy,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Oper,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Prog,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Sts,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_CVOut,REAL,Periodic,1,Second,,,,,,
""",
    'P_DOut': """\
GROUPNAME,SHORTCUTTAG.Sts_BypActive,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_IntlkTrip,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_FdbkOn,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Oper,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Prog,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Sts,DINT,Periodic,1,Second,,,,,,
""",
    'P_Motor': """\
GROUPNAME,SHORTCUTTAG.Sts_BypActive,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_IntlkTrip,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Oper,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Prog,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Sts,DINT,Periodic,1,Second,,,,,,
""",
    'P_ValveMO': """\
GROUPNAME,SHORTCUTTAG.Sts_BypActive,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_IntlkTrip,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Oper,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Prog,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Sts,DINT,Periodic,1,Second,,,,,,
""",
    'P_ValveSO': """\
GROUPNAME,SHORTCUTTAG.Sts_BypActive,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_IntlkTrip,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Oper,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Prog,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Sts,DINT,Periodic,1,Second,,,,,,
""",
    'P_VSD': """\
GROUPNAME,SHORTCUTTAG.Sts_BypActive,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_IntlkTrip,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Oper,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Sts_Prog,BOOL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Fault,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_LastFaultCode,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_Sts,DINT,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_InpDataLink,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_OutDataLink,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_SpeedFdbk,REAL,Periodic,1,Second,,,,,,
GROUPNAME,SHORTCUTTAG.Val_SpeedRef,REAL,Periodic,1,Second,,,,,,
""",



}

DATALOG_LIST = DATALOG_DEFINITIONS.keys()